# Course overview
1. PostgreSQL
    - about PostgreSQL:
        - PostgreSQL is an open source object-relational database system that uses & extends SQL, combining it with many features to safely store & scale complicated data workloads
        - most advanced open source database
        - designed for extensibility & customization
        - has been actively developed for 20+ years
        - ANSI/ISO compliant SQL support
        - the support for JSON also makes PostgreSQL an excellent database solution for scaling NoSQL workloads

    - history - released in 1987
    
    - major features:
        - portable
            - written in ANSI C
            - supports Windows, Linux, Mac OS/X and major Unix platforms
        - reliable
            - ACID compliant
            - supports transactions & save points
            - uses transaction logging (WAL)
        - scalable
            - uses multi version concurrency control (MVCC)
            - supports table partitioning
            - full support for table-space
            - supports parallel sequential scans
        - secure
            - host-based access control
            - object-level permissions & row-level security
            - supports logging
            - SSL connections
        - recovery/availability
            - replication (asynchronous, synchronous, logical)
            - supports hot-backup & PITR (point-in-time restore/recovery)
        - advanced features
            - supports stored procedures, stored functions, triggers, unlogged tables, & materialized views
            - procedural languages (PL/PGSQL, Perl, Python, etc.)
            - SQL/JSON path expressions
            - Foreign data wrappers (allows for addition of extra feature to the database)
            - additional functionality like PostGIS
    
    - database limits:
        - max. database size: unlimited
        - max. table size: 32TB
        - max. row size: 1.6TB
        - max. field size: 1GB
        - max. rows per table: unlimited
        - max columns per table: 250-1600, depending on column types
        - max. indexes per table: unlimited
    
    - common object names:
        - table/index (industry term) -> relation (PostgreSQL term)
        - row (industry term) -> tuple (PostgreSQL term)
        - column (industry term) -> attribute (PostgreSQL term)
        - data block (industry term) -> page (when block is on disk, PostgreSQL term, data stored in the table, each one is 8kb)
        - page (industry term) -> buffer (when block is on memory, PostgreSQL term, data stored in the table, each one is 8kb)
    
    - installation of PostgreSQL:
        - OS user & permissions:
            - PostgreSQL Server runs as a daemon (Linux/Unix) or service (Windows)
            - PostgreSQL Server requires superuser access
            - All processes & data files must be owned by a user in the OS
            - During the PostgreSQL installation, a locked user will be created on Linux, and on Windows, a password is required
            - On SELinux systems, SELinux must be set to permissive mode
            - the user account (for this tutorial):
                - it's advised to run PostgreSQL Server under a separate user account
                - this account should own the data directory that's managed by the server
                - the user-add or add-user command can be used to add users
                - the user account named PostgreSQL is used throughout this tutorial

        - Installation options (4 methods):
            - wizard installer (interactive method & easy download, but it's only supported on Windows & Mac)
            - RPM installer (preferred installation method on Linux, requires access to an enterprise rpm repository, dependencies have to be resolved manually)
            - YUM installer (attempts to install package & dependencies)
            - using the source code

        - Installation of PostgreSQL server
        - Setting environment variables

2. Database design
3. SQL queries
4. Indexing
5. Transactions
6. Performance tuning
7. Advanced topics:
    - Replication
    - Partitioning
    - Working with PostgreSQL in cloud environments