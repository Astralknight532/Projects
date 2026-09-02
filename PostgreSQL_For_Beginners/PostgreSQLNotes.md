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
                - download the .zip file from the PostgreSQL website (postgresql.org), extract the compressed installer, run the .exe installer as admin, & use the install wizard
            - RPM installer (preferred installation method on Linux, requires access to an enterprise rpm repository, dependencies have to be resolved manually)
            - YUM installer (attempts to install package & dependencies)
            - using the source code
            - main login set by me: postgres, postgresroot

        - Installation of PostgreSQL server
        - Setting environment variables

2. Database design
    - system architecture
    - architecture summary
        - PostgreSQL Server uses processes instead of threads
        - the postmaster process is also called a supervisor process
        - the postmaster processes are responsible for starting all other processes
        - utility processes carry their own background work
        - each user session has its own backend process
        - postmasters work as listeners (listening for new connections)

    - memory architecture
        - at the very top level is the postmaster
        - the shared memory contains the shared buffers (all transactions on the database happen here), the WAL buffers (WAL - write add logs, all transaction logs are kept here), & the process array
        - other components:
            - bgwriter
            - stats collector
            - autovacuum
            - archive
            - checkpointer
            - walwriter (syncs the data after COMMIT statements - shared buffers are lost if the server goes down, but WAL buffers aren't)
            - logger
            - logical rep
        - storage components:
            - data files
            - WAL segments
            - archived WAL
            - error log files
    
    - utility processes
        - background writer is responsible for writing "dirty" (new or modified) shared buffers to the disk
        - checkpointer process automatically performs a checkpoint (every 5 minutes) based on config parameters
        - WAL writer flushes the WAL to the disk
        - autovacuum launcher starts autovacuum workers as needed
        - autovacuum workers recover free space for reuse
        - logging routes log messages to syslog, eventlog, or log files
        - archiver archives the WAL files
        - stats collector collects usage statistics by relation & block
    
    - postmaster is a master process called postgres that listens for only 1 port, and it's responsible for receiving client requests
        - client sends connection request to the database server -> the postmaster receives the request and then sends it to the shared memory for processing
    
    - user backend process
        - the postmaster process spawns a new process for each connection request
        - authentication with IP address, username, and password
        - authorization to verify permissions
        - communication is done using semaphores & shared memory
        - postmaster -> postgres (work memory - some memory is allocated for the postgres process to run queries) -> shared memory
    
    - respond to client
        - once the user backend process called postgres is created, the postgres process waits for SQL queries (which are transmitted using plaintext)
        - the client/user communicates only with the postgres process
    
    - disk read buffering
        - the Postgres Server buffer cache reduces OS reads
        - read the block once and then examine it many times in the cache
        - the shared buffer contained inside the shared memory is used by multiple users to query the database
    
    - disk write buffering
        - blocks are written to the disk only when needed
        - this can be done to also make room for new blocks
        - this is done at checkpoint time
        - users write to the shared buffer (which is inside the shared memory), then the shared buffer makes a write to both the checkpoint & the database directly, and then the checkpoint writes to the database directly

    - background write scan
        - background writer scan attempts to ensure an adequate supply of clean buffers
        - the backend writes "dirty" buffers as needed
        - users write data to the shared buffer (which is inside shared memory) and then bgwriter writes the "dirty" buffers to the database as needed with the scan ensuring there are enough clean buffers
    
    - write ahead logging (WAL)
        - the backend writes data to the WAL buffer
        - WAL buffers are flushed periodically, either on commit or when the buffers are full
        - users access the WAL buffers in the shared memory and the WAL buffers write to the transaction log on the database/server
    
    - WAL archiving
        - archiver spawns a task to copy away pg_wal log files when full
        - users access the WAL buffers in the shared memory, the WAL buffers write to the transaction log, and then the archive command copies the pg_wal log files

    - connection request-response
    - disk read & write buffering
    - BG writer cleaning scan
    - commit & checkpoint
    - statement processing
    - physical DB architecture
    - data directory layout

3. SQL queries
4. Indexing
5. Transactions
6. Performance tuning
7. Advanced topics:
    - Replication
    - Partitioning
    - Working with PostgreSQL in cloud environments