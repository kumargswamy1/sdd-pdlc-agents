# Testing Standards

This document defines testing conventions and best practices for unit testing across frontend and backend applications.

## Overview

Unit testing is the foundation of quality assurance. Each unit test should:
- Test a single piece of functionality in isolation
- Use mocks to isolate from dependencies
- Execute quickly (milliseconds)
- Be deterministic and repeatable
- Have clear, descriptive names

**Note:** Unit testing focuses on isolated component/module testing. End-to-end and functional/BDD testing are separate concerns and handled by a dedicated functional testing agent.

---

## Frontend Unit Testing Standards

### Test Framework Selection

Choose based on your frontend technology:

| Technology | Framework | Package | Command |
|------------|-----------|---------|---------|
| React | Jest | `jest` | `npm test` |
| React | Vitest | `vitest` | `npm run test` |
| Vue 3 | Vitest | `vitest` | `npm run test` |
| Vue 2 | Jest | `jest` | `npm test` |
| Angular | Jasmine/Karma | `@angular/core` | `ng test` |
| Flutter | Flutter test | builtin | `flutter test` |
| Svelte | Vitest | `vitest` | `npm run test` |
| Next.js | Jest | `jest` | `npm test` |

### Test File Organization

```
frontend/
├── src/
│   ├── components/
│   ├── hooks/
│   ├── services/
│   ├── utils/
│   └── state/
├── test/
│   └── unit/
│       ├── components/          # Component unit tests
│       ├── hooks/               # Custom hook tests
│       ├── services/            # Service/API client tests
│       ├── utils/               # Utility function tests
│       ├── state/               # State management tests
│       ├── __mocks__/           # Mock data and fixtures
│       └── __fixtures__/        # Test fixtures
└── jest.config.js (or vitest.config.ts)
```

### Test File Naming Convention

```
ComponentName.test.js         # Jest
ComponentName.spec.js         # Jasmine
useCustomHook.test.js         # Hook test
apiClient.test.js             # Service test
validators.test.js            # Utility test
userStore.test.js             # State management test
```

### Component Unit Test Template

```javascript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm';

describe('LoginForm Component', () => {
  describe('Rendering', () => {
    it('should render login form with email and password fields', () => {
      render(<LoginForm />);
      
      expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
      expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
      expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
    });

    it('should render error message when provided', () => {
      const errorMsg = 'Invalid credentials';
      render(<LoginForm error={errorMsg} />);
      
      expect(screen.getByText(errorMsg)).toBeInTheDocument();
    });
  });

  describe('User Interactions', () => {
    it('should update email input on change', async () => {
      const user = userEvent.setup();
      render(<LoginForm />);
      
      const emailInput = screen.getByLabelText(/email/i);
      await user.type(emailInput, 'test@example.com');
      
      expect(emailInput.value).toBe('test@example.com');
    });

    it('should call onSubmit with email and password on form submit', async () => {
      const user = userEvent.setup();
      const handleSubmit = jest.fn();
      render(<LoginForm onSubmit={handleSubmit} />);
      
      await user.type(screen.getByLabelText(/email/i), 'test@example.com');
      await user.type(screen.getByLabelText(/password/i), 'password123');
      await user.click(screen.getByRole('button', { name: /login/i }));
      
      expect(handleSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123'
      });
    });
  });

  describe('Validation', () => {
    it('should show error for invalid email format', async () => {
      const user = userEvent.setup();
      render(<LoginForm />);
      
      const emailInput = screen.getByLabelText(/email/i);
      await user.type(emailInput, 'invalid-email');
      await user.click(screen.getByRole('button', { name: /login/i }));
      
      expect(screen.getByText(/invalid email format/i)).toBeInTheDocument();
    });

    it('should disable submit button when password is too short', () => {
      render(<LoginForm minPasswordLength={8} />);
      
      const emailInput = screen.getByLabelText(/email/i);
      const passwordInput = screen.getByLabelText(/password/i);
      const submitButton = screen.getByRole('button', { name: /login/i });
      
      expect(submitButton).not.toBeDisabled();
      
      fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
      fireEvent.change(passwordInput, { target: { value: 'short' } });
      
      expect(submitButton).toBeDisabled();
    });
  });

  describe('Async Behavior', () => {
    it('should show loading state while submitting', async () => {
      const user = userEvent.setup();
      const handleSubmit = jest.fn(() => new Promise(resolve => 
        setTimeout(() => resolve({ success: true }), 100)
      ));
      
      render(<LoginForm onSubmit={handleSubmit} />);
      
      await user.type(screen.getByLabelText(/email/i), 'test@example.com');
      await user.type(screen.getByLabelText(/password/i), 'password123');
      
      const submitButton = screen.getByRole('button', { name: /login/i });
      await user.click(submitButton);
      
      expect(screen.getByText(/logging in/i)).toBeInTheDocument();
      
      await waitFor(() => {
        expect(screen.queryByText(/logging in/i)).not.toBeInTheDocument();
      });
    });
  });
});
```

### Hook Unit Test Template

```javascript
import { renderHook, act, waitFor } from '@testing-library/react';
import { useFormValidation } from './useFormValidation';

describe('useFormValidation Hook', () => {
  it('should initialize with empty form data', () => {
    const { result } = renderHook(() => useFormValidation({
      email: '',
      password: ''
    }));

    expect(result.current.formData).toEqual({ email: '', password: '' });
    expect(result.current.errors).toEqual({});
  });

  it('should update form data on field change', () => {
    const { result } = renderHook(() => useFormValidation({
      email: '',
      password: ''
    }));

    act(() => {
      result.current.handleChange('email', 'test@example.com');
    });

    expect(result.current.formData.email).toBe('test@example.com');
  });

  it('should validate email format', () => {
    const { result } = renderHook(() => useFormValidation(
      { email: '', password: '' },
      {
        email: (value) => {
          if (!value.includes('@')) return 'Invalid email';
          return null;
        }
      }
    ));

    act(() => {
      result.current.handleChange('email', 'invalid');
      result.current.validate();
    });

    expect(result.current.errors.email).toBe('Invalid email');
  });

  it('should reset form data', () => {
    const { result } = renderHook(() => useFormValidation({
      email: '',
      password: ''
    }));

    act(() => {
      result.current.handleChange('email', 'test@example.com');
      result.current.handleChange('password', 'pass123');
      result.current.reset();
    });

    expect(result.current.formData).toEqual({ email: '', password: '' });
    expect(result.current.errors).toEqual({});
  });
});
```

### Service/API Test Template

```javascript
import axios from 'axios';
import { UserApiClient } from './userApiClient';

jest.mock('axios');

describe('UserApiClient', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('getUser', () => {
    it('should fetch user data successfully', async () => {
      const mockUser = { id: 1, name: 'John Doe', email: 'john@example.com' };
      axios.get.mockResolvedValue({ data: mockUser });

      const client = new UserApiClient();
      const result = await client.getUser(1);

      expect(result).toEqual(mockUser);
      expect(axios.get).toHaveBeenCalledWith('/api/users/1');
    });

    it('should handle API errors gracefully', async () => {
      const error = new Error('Network error');
      axios.get.mockRejectedValue(error);

      const client = new UserApiClient();
      
      await expect(client.getUser(1)).rejects.toThrow('Network error');
    });

    it('should return null for 404 response', async () => {
      axios.get.mockRejectedValue({
        response: { status: 404 }
      });

      const client = new UserApiClient();
      const result = await client.getUser(999);

      expect(result).toBeNull();
    });
  });

  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const newUser = { name: 'Jane Doe', email: 'jane@example.com' };
      const createdUser = { id: 2, ...newUser };
      axios.post.mockResolvedValue({ data: createdUser });

      const client = new UserApiClient();
      const result = await client.createUser(newUser);

      expect(result).toEqual(createdUser);
      expect(axios.post).toHaveBeenCalledWith('/api/users', newUser);
    });

    it('should validate required fields before posting', async () => {
      const client = new UserApiClient();
      
      await expect(client.createUser({ name: 'John' })).rejects.toThrow('Email is required');
      expect(axios.post).not.toHaveBeenCalled();
    });
  });
});
```

### Mocking Best Practices

```javascript
// Mock axios
jest.mock('axios');

// Mock a module
jest.mock('../services/authService', () => ({
  login: jest.fn(),
  logout: jest.fn()
}));

// Partial mock (preserve other exports)
jest.mock('../utils/helpers', () => ({
  ...jest.requireActual('../utils/helpers'),
  someFunction: jest.fn()
}));

// Mock with implementation
jest.mock('../api/client', () => ({
  get: jest.fn((url) => Promise.resolve({ data: [] }))
}));

// Reset between tests
beforeEach(() => {
  jest.clearAllMocks();
});

// Verify mocks were called
expect(mockFn).toHaveBeenCalled();
expect(mockFn).toHaveBeenCalledWith(arg1, arg2);
expect(mockFn).toHaveBeenCalledTimes(1);
```

---

## Backend Unit Testing Standards

### Test Framework Selection

| Technology | Framework | Package | Command |
|------------|-----------|---------|---------|
| Python | pytest | `pytest` | `pytest` |
| Python | unittest | builtin | `python -m unittest` |
| Node.js | Jest | `jest` | `npm test` |
| Node.js | Mocha | `mocha` | `npm test` |
| Java | JUnit 5 | `junit-jupiter` | `mvn test` |
| Java | TestNG | `testng` | `mvn test` |
| Go | testing | builtin | `go test ./...` |
| C# | xUnit | `xunit` | `dotnet test` |

### Test File Organization

```
backend/
├── src/
│   ├── services/
│   ├── controllers/
│   ├── models/
│   ├── middleware/
│   ├── utils/
│   └── config/
├── test/
│   └── unit/
│       ├── services/            # Service/business logic tests
│       ├── controllers/         # API endpoint tests
│       ├── models/              # Database model tests
│       ├── middleware/          # Middleware tests
│       ├── utils/               # Utility function tests
│       ├── fixtures/            # Test data fixtures
│       └── conftest.py          # Pytest configuration (Python)
└── pytest.ini or jest.config.js
```

### Test File Naming Convention

```
test_user_service.py           # pytest
UserServiceTest.java           # JUnit
user.controller.spec.js        # Jest
```

### Python Unit Test Template (pytest)

```python
import pytest
from datetime import datetime
from unittest.mock import Mock, patch, MagicMock
from services.user_service import UserService
from models.user import User

class TestUserService:
    @pytest.fixture
    def mock_db(self):
        """Fixture for mocking database"""
        db = Mock()
        yield db
        db.close()

    @pytest.fixture
    def user_service(self, mock_db):
        """Fixture for UserService with mocked database"""
        return UserService(db=mock_db)

    def test_create_user_with_valid_data(self, user_service, mock_db):
        """Test creating a user with valid data"""
        user_data = {
            'email': 'test@example.com',
            'name': 'John Doe',
            'password': 'secure_password'
        }
        
        mock_user = User(id=1, **user_data)
        mock_db.add.return_value = mock_user
        
        result = user_service.create_user(user_data)
        
        assert result.email == 'test@example.com'
        assert result.name == 'John Doe'
        mock_db.add.assert_called_once()

    def test_create_user_validates_email(self, user_service):
        """Test that email validation occurs before user creation"""
        user_data = {
            'email': 'invalid-email',
            'name': 'John Doe',
            'password': 'secure_password'
        }
        
        with pytest.raises(ValueError, match='Invalid email format'):
            user_service.create_user(user_data)

    def test_create_user_requires_email(self, user_service):
        """Test that email is required"""
        user_data = {
            'name': 'John Doe',
            'password': 'secure_password'
        }
        
        with pytest.raises(ValueError, match='Email is required'):
            user_service.create_user(user_data)

    def test_get_user_by_id(self, user_service, mock_db):
        """Test retrieving user by ID"""
        mock_user = User(id=1, email='test@example.com', name='John Doe')
        mock_db.query.return_value.filter_by.return_value.first.return_value = mock_user
        
        result = user_service.get_user(1)
        
        assert result.id == 1
        assert result.email == 'test@example.com'
        mock_db.query.assert_called_once()

    def test_get_user_returns_none_when_not_found(self, user_service, mock_db):
        """Test that None is returned when user not found"""
        mock_db.query.return_value.filter_by.return_value.first.return_value = None
        
        result = user_service.get_user(999)
        
        assert result is None

    def test_delete_user(self, user_service, mock_db):
        """Test deleting a user"""
        mock_db.delete.return_value = True
        
        result = user_service.delete_user(1)
        
        assert result is True
        mock_db.delete.assert_called_once()

    @patch('services.user_service.send_email')
    def test_create_user_sends_confirmation_email(self, mock_send_email, user_service):
        """Test that confirmation email is sent after user creation"""
        user_data = {
            'email': 'test@example.com',
            'name': 'John Doe',
            'password': 'secure_password'
        }
        
        user_service.create_user(user_data)
        
        mock_send_email.assert_called_once_with(
            'test@example.com',
            subject='Welcome',
            template='welcome'
        )
```

### JavaScript/Node.js Unit Test Template (Jest)

```javascript
const UserService = require('../services/userService');
const UserRepository = require('../repositories/userRepository');
const EmailService = require('../services/emailService');

jest.mock('../repositories/userRepository');
jest.mock('../services/emailService');

describe('UserService', () => {
  let userService;

  beforeEach(() => {
    jest.clearAllMocks();
    userService = new UserService(
      new UserRepository(),
      new EmailService()
    );
  });

  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const userData = {
        email: 'test@example.com',
        name: 'John Doe',
        password: 'secure_password'
      };
      const expectedUser = { id: 1, ...userData };

      UserRepository.prototype.create.mockResolvedValue(expectedUser);

      const result = await userService.createUser(userData);

      expect(result).toEqual(expectedUser);
      expect(UserRepository.prototype.create).toHaveBeenCalledWith(userData);
    });

    it('should validate email format', async () => {
      const userData = {
        email: 'invalid-email',
        name: 'John Doe',
        password: 'secure_password'
      };

      await expect(userService.createUser(userData))
        .rejects.toThrow('Invalid email format');
      
      expect(UserRepository.prototype.create).not.toHaveBeenCalled();
    });

    it('should require email', async () => {
      const userData = {
        name: 'John Doe',
        password: 'secure_password'
      };

      await expect(userService.createUser(userData))
        .rejects.toThrow('Email is required');
    });

    it('should send confirmation email after creation', async () => {
      const userData = {
        email: 'test@example.com',
        name: 'John Doe',
        password: 'secure_password'
      };
      const expectedUser = { id: 1, ...userData };

      UserRepository.prototype.create.mockResolvedValue(expectedUser);

      await userService.createUser(userData);

      expect(EmailService.prototype.sendWelcomeEmail)
        .toHaveBeenCalledWith(expectedUser);
    });
  });

  describe('getUser', () => {
    it('should retrieve user by ID', async () => {
      const expectedUser = { id: 1, email: 'test@example.com', name: 'John Doe' };
      UserRepository.prototype.findById.mockResolvedValue(expectedUser);

      const result = await userService.getUser(1);

      expect(result).toEqual(expectedUser);
      expect(UserRepository.prototype.findById).toHaveBeenCalledWith(1);
    });

    it('should return null when user not found', async () => {
      UserRepository.prototype.findById.mockResolvedValue(null);

      const result = await userService.getUser(999);

      expect(result).toBeNull();
    });
  });

  describe('deleteUser', () => {
    it('should delete user successfully', async () => {
      UserRepository.prototype.delete.mockResolvedValue(true);

      const result = await userService.deleteUser(1);

      expect(result).toBe(true);
      expect(UserRepository.prototype.delete).toHaveBeenCalledWith(1);
    });
  });
});
```

### Java Unit Test Template (JUnit 5)

```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import com.example.services.UserService;
import com.example.repositories.UserRepository;
import com.example.services.EmailService;
import com.example.models.User;

@DisplayName("UserService Tests")
class UserServiceTest {
    
    private UserService userService;
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private EmailService emailService;
    
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        userService = new UserService(userRepository, emailService);
    }
    
    @Test
    @DisplayName("Should create user with valid data")
    void testCreateUserWithValidData() {
        // Arrange
        UserCreateRequest request = new UserCreateRequest(
            "test@example.com",
            "John Doe",
            "secure_password"
        );
        User expectedUser = new User(1L, "test@example.com", "John Doe");
        when(userRepository.save(any(User.class))).thenReturn(expectedUser);
        
        // Act
        User result = userService.createUser(request);
        
        // Assert
        assertNotNull(result);
        assertEquals("test@example.com", result.getEmail());
        assertEquals("John Doe", result.getName());
        verify(userRepository, times(1)).save(any(User.class));
        verify(emailService, times(1)).sendWelcomeEmail(expectedUser);
    }
    
    @Test
    @DisplayName("Should validate email format before creation")
    void testCreateUserValidatesEmail() {
        // Arrange
        UserCreateRequest request = new UserCreateRequest(
            "invalid-email",
            "John Doe",
            "secure_password"
        );
        
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> 
            userService.createUser(request),
            "Should throw exception for invalid email"
        );
        verify(userRepository, never()).save(any());
    }
    
    @Test
    @DisplayName("Should require email field")
    void testCreateUserRequiresEmail() {
        // Arrange
        UserCreateRequest request = new UserCreateRequest(null, "John Doe", "secure_password");
        
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> 
            userService.createUser(request),
            "Email is required"
        );
    }
    
    @Test
    @DisplayName("Should retrieve user by ID")
    void testGetUserById() {
        // Arrange
        User expectedUser = new User(1L, "test@example.com", "John Doe");
        when(userRepository.findById(1L)).thenReturn(java.util.Optional.of(expectedUser));
        
        // Act
        User result = userService.getUser(1L);
        
        // Assert
        assertNotNull(result);
        assertEquals(1L, result.getId());
        verify(userRepository, times(1)).findById(1L);
    }
    
    @Test
    @DisplayName("Should return empty when user not found")
    void testGetUserNotFound() {
        // Arrange
        when(userRepository.findById(999L)).thenReturn(java.util.Optional.empty());
        
        // Act
        User result = userService.getUser(999L);
        
        // Assert
        assertNull(result);
    }
}
```

### Test Database Setup

For tests that require database interactions, use:

**Python (pytest):**
```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def test_db():
    """Create in-memory SQLite database for tests"""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    engine.dispose()
```

**Node.js (Jest):**
```javascript
const sqlite3 = require('sqlite3');

beforeAll(() => {
  db = new sqlite3.Database(':memory:');
  // Create test tables
});

afterEach(() => {
  // Clear test data
});

afterAll(() => {
  db.close();
});
```

---

## Common Testing Patterns

### Testing Async Operations

**Frontend (React):**
```javascript
it('should handle async operation', async () => {
  const { result } = renderHook(() => useAsync(fetchData));
  
  await waitFor(() => {
    expect(result.current.data).toBeDefined();
  });
});
```

**Backend (Python):**
```python
@pytest.mark.asyncio
async def test_async_operation():
    result = await async_function()
    assert result is not None
```

### Testing Error Scenarios

**Frontend:**
```javascript
it('should display error message', async () => {
  mockFetch.mockRejectedValue(new Error('API Error'));
  render(<MyComponent />);
  
  await waitFor(() => {
    expect(screen.getByText(/error/i)).toBeInTheDocument();
  });
});
```

**Backend (Python):**
```python
def test_handles_database_error(self, mock_db):
    mock_db.query.side_effect = DatabaseError('Connection failed')
    
    with pytest.raises(DatabaseError):
        service.get_user(1)
```

### Testing State Transitions

**Frontend (Redux/Vuex):**
```javascript
it('should transition through loading states', () => {
  const initialState = { loading: false, data: null };
  const action = fetchData();
  
  const state1 = reducer(initialState, { type: 'FETCH_START' });
  expect(state1.loading).toBe(true);
  
  const state2 = reducer(state1, { type: 'FETCH_SUCCESS', payload: data });
  expect(state2.loading).toBe(false);
  expect(state2.data).toEqual(data);
});
```

---

## Coverage Targets

| Layer | Coverage Target | Priority |
|-------|-----------------|----------|
| Business Logic | 80%+ | CRITICAL |
| Validation | 90%+ | CRITICAL |
| API Endpoints | 75%+ | HIGH |
| UI Components | 70%+ | HIGH |
| Utilities | 85%+ | HIGH |
| Error Handling | 80%+ | HIGH |

**Note:** Coverage percentage is a metric, not a goal. Focus on meaningful test cases over line coverage numbers.

---

## Test Execution

### Running Tests

**Frontend:**
```bash
npm test                    # Run all tests
npm test -- --watch       # Watch mode
npm test -- --coverage    # With coverage report
```

**Backend (Python):**
```bash
pytest                     # Run all tests
pytest -v                 # Verbose output
pytest --cov             # With coverage
pytest -k test_user      # Run specific tests
```

**Backend (JavaScript):**
```bash
npm test                  # Run all tests
npm test -- --watch     # Watch mode
npm test -- --coverage  # With coverage
```

### Continuous Integration

All unit tests must:
- Run automatically on pull requests
- Pass before merge to main/master
- Have coverage reports in CI logs
- Fail fast on first error (fail-fast mode)

---

## Anti-Patterns to Avoid

❌ **Testing implementation details** - Test behavior, not how it works  
❌ **Coupling tests to UI structure** - Use semantic queries, not selectors  
❌ **Making real API/DB calls** - Always mock external dependencies  
❌ **Creating fragile tests** - Use flexible assertions, not brittle comparisons  
❌ **Writing giant monolithic tests** - One concern per test  
❌ **Skipping edge cases** - Test nulls, empty values, boundaries  
❌ **Non-deterministic tests** - Avoid timeouts, use explicit waits  
❌ **Duplicated test setup** - Use fixtures and helpers  
❌ **Ignoring test maintenance** - Refactor tests like production code  

---

## Related Documentation

- [Quality Tester Agent](../.github/agents/tester.agent.md)
- [Frontend Standards](./frontend-context.md)
- [Backend Standards](./backend-context.md)
- [Project Context](./project-context.md)
