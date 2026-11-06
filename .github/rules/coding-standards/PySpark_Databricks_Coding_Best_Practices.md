# PySpark and Databricks Coding Best Practices

## 1. Naming and SQL Style
- Name DataFrames descriptively using `snake_case`, typically with a `_df` suffix where helpful.
- Use lowercase, underscore-separated column names without spaces or special characters.
- Use uppercase SQL keywords and consistent formatting for Spark SQL.
- Name notebooks, modules, and files according to the task they perform.

## 2. Data Loading
- Define schemas explicitly for CSV, JSON, and other weakly typed sources.
- Prefer columnar formats such as Parquet or Delta for analytical workloads.
- Validate source schema, required columns, nullability, and data types at ingestion.
- Parameterize input and output locations instead of hardcoding paths.
- Use approved cloud storage locations and access patterns rather than workspace-local assumptions.

## 3. DataFrame API
- Prefer DataFrames and Spark SQL over RDDs unless an RDD is technically justified.
- Break complex transformations into named intermediate steps.
- Select required columns early and filter as close to the source as possible.
- Avoid Python UDFs when built-in Spark functions can express the logic.
- Avoid `collect()` for large datasets. Use controlled sampling such as `show()`, `take(n)`, or bounded aggregations.
- Do not convert large Spark DataFrames to pandas on the driver.

## 4. Joins and Shuffles
- Treat joins, `groupBy`, `distinct`, repartitioning, and wide aggregations as potentially expensive shuffle operations.
- Broadcast only datasets that safely fit within executor memory and meet platform thresholds.
- Handle skewed join keys explicitly when they cause uneven partitions.
- Verify join cardinality and duplicate behavior before and after joins.
- Use appropriate partition keys and avoid excessive tiny partitions.

## 5. Caching and Persistence
- Cache or persist only DataFrames that are reused and expensive to recompute.
- Choose the storage level intentionally.
- Materialize the cache when required and call `unpersist()` after use.
- Do not cache every intermediate DataFrame.

## 6. Partitioning and File Management
- Partition large output datasets by frequently filtered, reasonably distributed columns.
- Avoid high-cardinality partition columns that create many small directories.
- Manage small-file proliferation through optimized writes and compaction.
- Use Delta Lake capabilities when ACID transactions, reliable updates, or schema evolution are required.

## 7. Notebook Design
- Organize notebooks with clear markdown sections such as configuration, loading, validation, transformation, and output.
- Keep notebooks focused on orchestration or exploration rather than embedding large reusable libraries.
- Move reusable business logic into testable Python modules or packages.
- Use notebook parameters or job parameters for environment-specific inputs.
- Store notebooks and supporting code in Git-integrated repositories.
- Avoid oversized notebooks and hidden state dependencies between cells.

## 8. Testing and Data Quality
- Unit-test transformation functions with small deterministic datasets.
- Add integration tests for source and sink contracts.
- Validate row counts, schemas, uniqueness, ranges, null handling, and business rules.
- Test empty datasets, late-arriving records, duplicate data, malformed rows, and schema changes.
- Use approved data-quality frameworks when rules require operational monitoring.

## 9. Performance
- Inspect physical plans for significant workloads.
- Configure cluster size and autoscaling based on data volume and workload characteristics.
- Prefer built-in optimized operations supported by Catalyst and Tungsten.
- Avoid unnecessary actions, repeated scans, and recomputation.
- Measure before tuning Spark configuration values.

## 10. Security
- Apply least-privilege access to notebooks, jobs, clusters, tables, and storage.
- Use managed identities, service principals, or approved workload identities.
- Store secrets in an approved secret store or Databricks secret scope.
- Encrypt data at rest and in transit.
- Avoid exposing sensitive data in notebook output, logs, or exception messages.
- Use governed catalogs, table permissions, and audit logging where available.

## 11. Operational Readiness
- Emit structured logs and job metrics.
- Capture run identifiers, source versions, output versions, and processing timestamps.
- Make jobs idempotent or define safe retry and checkpoint behavior.
- Configure alerts, timeouts, retry policies, and failure handling.
- Document backfill, recovery, and rollback procedures.

## Review Checklist
- Explicit schema and data contracts are present.
- No unbounded driver collection is used.
- Join, shuffle, partition, and cache choices are justified.
- Reusable logic is modular and tested.
- Paths, clusters, and parameters are configurable.
- Secrets and sensitive data are handled securely.

---
Source basis: `Coding_Standard_V1.0.docx`, PySpark & Databricks Best Practices and Databricks Specific Security Reviews sections.
