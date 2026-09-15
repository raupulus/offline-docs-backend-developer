---
title: Release 17.11
source_url: https://www.postgresql.org/docs/17/release-17-11.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: release-17.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3440
---

## Release 17.11

Release date:

2026-08-13

This release contains a variety of fixes from 17.10. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.11

A dump/restore is not required for those running 17.X.

However, the first three security entries below describe configuration adjustments and data cleanups that you may need to make after updating.

Also, if you use `contrib/btree_gist` or `contrib/ltree`, you may need to reindex indexes made with those extensions; see the relevant entries below.

Also, if you are upgrading from a version earlier than 17.6, see [Release 17.6](#release-17-6).

## Changes

- Restrict logical decoding output plugins to the set specified by a new server parameter `output_plugin_libraries` (Jacob Champion) [](https://postgr.es/c/01992176e) [](https://postgr.es/c/4fcccea97)

  Previously, a replication user could select any loadable library for logical decoding, allowing exploits of various sorts. To allow locking this down without breaking setups that worked before, introduce a whitelist of allowed output plugins.

  By default, only the output plugins shipped as part of PostgreSQL (`pgoutput` and `test_decoding`) are included in `output_plugin_libraries`. Installations that rely on other output plugins must add them after updating the server, for example

      output_plugin_libraries = 'pgoutput, test_decoding, my_trusted_decoder'

  Additionally, `pg_upgrade --check` will fail if the `output_plugin_libraries` parameter on the new cluster does not permit the plugins of logical replication slots on the old cluster, when migrating from versions 17 and later. Make necessary additions to the new cluster's setting before performing pg_upgrade.

  The PostgreSQL Project thanks Vladimir Tokarev and Yu Kunpeng for reporting this problem. (CVE-2026-6471)

- Fix `contrib/pgcrypto`'s PGP encryption to detect unsupported ciphers (Daniel Gustafsson) [](https://postgr.es/c/b05cfc693) [](https://postgr.es/c/7eed42aa8)

  Previously, if OpenSSL rejected the requested cipher (for example, because it is running in FIPS mode, or the legacy provider hasn't been loaded), pgcrypto failed to notice the failure and simply XOR'd the non-encrypted block with the plaintext, rendering the “encryption” trivially breakable. This will typically occur with deprecated or non-FIPS cipher algorithms (cipher-algo=blowfish/bf, twofish, cast5, or 3des).

  By default, pgcrypto will now fail to decrypt any messages that were affected in this way. To allow retrieval of such data, a new option `ignore-cipher-failure` has been added to `pgp_pub_decrypt()` and `pgp_sym_decrypt()`. Setting `ignore-cipher-failure=1` will restore their previous behavior, allowing the faulty encryption wrapper to be stripped off:

      pgp_sym_decrypt(encrypted_column, any key, 'ignore-cipher-failure=1')

  Once the affected messages are identified and stripped of their wrappers, they can then be re-encrypted with a modern algorithm. It is important however that the behavior of OpenSSL be the same as it was when the faulty messages were created: if the set of unsupported algorithms is not the same, this approach will not work. See the documentation for `ignore-cipher-failure`.

  The PostgreSQL Project thanks Shishir Sharma for reporting this problem. (CVE-2026-14663)

- Fix psql to skip in-line data following a scripted `COPY ... FROM STDIN` command, even if the `COPY` fails before sending `PGRES_COPY_IN` (Tom Lane) [](https://postgr.es/c/46fa1f6f3) [](https://postgr.es/c/dca6627de)

  Previously, if a `COPY` command failed at startup (for instance, because the target table doesn't exist) psql would not realize that and would proceed to read the following in-line data as SQL commands. In the best case that's wrong and in the worst case it's a SQL-injection hazard. Teach psql to recognize syntactically-valid `COPY ... FROM STDIN` commands and to skip data on its own authority if the server doesn't respond with `PGRES_COPY_IN`.

  While this fix is unlikely to affect any production SQL scripts, test scripts might intentionally exercise failing `COPY ... FROM STDIN` commands. Those will need to gain a `\.` data terminator line after each such command.

  The PostgreSQL Project thanks Alexander Lakhin for reporting this problem. (CVE-2026-6464)

- Cross-check the output row type of a portal running `EXECUTE` or `FETCH` (Robert Haas) [](https://postgr.es/c/60887d348)

  `EXECUTE` and `FETCH` use two portals: an outer one for the statement itself, and an inner one running the query being executed on its behalf. It was previously possible to make the declared row types of the two portals diverge, leading to server memory disclosure and arbitrary code execution.

  The PostgreSQL Project thanks Ben Morris (in collaboration with Claude and Anthropic Research) and Peter Geoghegan for reporting this problem. (CVE-2026-16239)

- Fix buffer overrun with long time zone abbreviation in `to_char()` (Tom Lane) [](https://postgr.es/c/12a620686)

  This can easily crash the server, and exploits leading to arbitrary code execution have been reported.

  The PostgreSQL Project thanks Hcamael, Amjad Shahzad, Tan Zhen of AntAISecurityLab, Tomer Fichman, Zheng Yu, Amy Burnett (OpenAI Codex Security), Rick de Jager, Heewon Song, Sylvie Mayer, Aleksander Alekseev, and Hillai Ben Sasson for reporting this problem. (CVE-2026-14669)

- Fix buffer overrun in regexp match/split functions (Masahiko Sawada) [](https://postgr.es/c/e91dcfcca)

  If passed invalidly-encoded data, these functions could write past the end of their conversion buffer.

  The PostgreSQL Project thanks Francesco Verardi for reporting this problem. (CVE-2026-14664)

- Harden the `ascii()` function against invalid input (Michael Paquier) [](https://postgr.es/c/849da8210)

  By supplying invalidly-encoded input, this function could be coaxed to read and return a few bytes of data that it shouldn't. In assert-enabled builds, its assertions could be triggered too.

  The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-18024)

- Make `scalarineqsel()` check that a constant it expects to be of type `tid` actually is (Tom Lane) [](https://postgr.es/c/0ebf896f4)

  This expectation will hold for all the built-in operators that use this estimator, but a maliciously-constructed operator could violate it, leading to a crash or server memory disclosure.

  The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-14668)

- Harden `tsvector` and `tsquery` code against overly long values (both individual lexemes and total vector/query length) (Tom Lane) [](https://postgr.es/c/fe0b5bd6d) [](https://postgr.es/c/8e87bd473)

  The documented limits were not enforced in all code paths.

  The PostgreSQL Project thanks Yuhang Wu, Zhenpeng Lin, Zheng Yu, and Hcamael for reporting these problems. (CVE-2026-14662)

- Fix various places that mistakenly assumed they would not have to deal with more than `FUNC_MAX_ARGS` function arguments (Tom Lane) [](https://postgr.es/c/797e3cc4c) [](https://postgr.es/c/8a40f4b09)

  Notably, the server's actual limit on the number of arguments to an aggregate function is `FUNC_MAX_ARGS - 1`, but the parser failed to enforce that, creating hazards downstream.

  The PostgreSQL Project thanks Zheng Yu, ylwangtju, and Masahiko Sawada for reporting these problems. (CVE-2026-14679)

- Reject calls from SQL to functions that take or return type `internal` (Tom Lane) [](https://postgr.es/c/eb9e55297) [](https://postgr.es/c/83d0a083f)

  The existing defenses against doing this have been shown to be insufficient, so add more explicit checks.

  The PostgreSQL Project thanks Amy Burnett (OpenAI Codex Security) for reporting this problem. (CVE-2026-14680)

- Preserve the ownership of extended statistics objects when they are rebuilt by `ALTER TABLE` (Masahiko Sawada) [](https://postgr.es/c/75a03c569)

  Previously, the role running `ALTER TABLE` gained ownership of such objects, but that seems inappropriate.

  The PostgreSQL Project thanks Noah Misch for reporting this problem. (CVE-2026-6469)

- When deparsing an `EXTRACT()` function call, quote the field name if needed (Nathan Bossart) [](https://postgr.es/c/5981fe370)

  The parser accepts any string literal as a field name in `EXTRACT()`, deferring validation to execution. If the call is stored and deparsed (for example during pg_dump), the string body was regurgitated verbatim, allowing SQL injection.

  The PostgreSQL Project thanks Ben Morris (in collaboration with Claude and Anthropic Research) for reporting this problem. (CVE-2026-15741)

- Check for `USAGE` privilege on data types in places that formerly failed to check that (Nathan Bossart) [](https://postgr.es/c/fd6d3e7e9) [](https://postgr.es/c/671359605) [](https://postgr.es/c/d1c8aa0b0)

  `CREATE TYPE AS RANGE` did not check, nor did `ALTER TABLE OF`, nor did commands that create stored expressions. These omissions allowed roles without `USAGE` privilege to nonetheless create objects depending on the type, possibly blocking the type's owner from changing the type later.

  The PostgreSQL Project thanks Jingzhou Fu for reporting this problem. (CVE-2026-6470)

- Invalidate role-dependent cached plans after role changes (Ilya Staroverov, Shinya Kato, Nathan Bossart) [](https://postgr.es/c/1974acf23)

  Role membership, role attribute, and database ownership changes may impact the expected behavior of row-level security policies, but previously we'd continue to use cached plans that were made according to the old state of affairs.

  The PostgreSQL Project thanks Ilya Staroverov and Shinya Kato for reporting this problem. (CVE-2026-14666)

- Reject GSSEncRequest after direct SSL connection (Michael Paquier) [](https://postgr.es/c/067a64d40)

  After establishing a TLS-encrypted connection, the server would still accept a request for GSSAPI encryption. If that succeeded, the connection would proceed using TLS encryption, but it would look like a GSS connection to the `pg_hba` rules. Thus, a `pg_hba` policy intending to disallow TLS would not be enforced correctly.

  The PostgreSQL Project thanks p4p3r for reporting this problem. (CVE-2026-14681)

- Make mock SCRAM authentication secrets more plausible (Nathan Bossart) [](https://postgr.es/c/dec60e8ad)

  If a SCRAM login is attempted against a role that doesn't exist or doesn't have a SCRAM secret, we generate a mock secret and carry out the authentication handshake anyway, to avoid revealing these facts to an attacker. But the mock secret was made with a fixed iteration count, which in itself can be an observable response discrepancy. Use the configuration setting `scram_iterations` instead, to make the mock secret look more like the installation's real secrets.

  The PostgreSQL Project thanks Radim Marek for reporting this problem. (CVE-2026-14672)

- Fix out-of-bounds writes in ecpg applications caused by invalid `bytea` data received from the server (Michael Paquier) [](https://postgr.es/c/c3c830272)

  ecpg assumed without checking that any `bytea` value must begin with `\x`. A broken or malicious server might send a string shorter than 2 bytes, resulting in memory clobber in the application.

  The PostgreSQL Project thanks ylwangtju for reporting this problem. (CVE-2026-16241)

- Do not do backquote expansion on the argument of psql's `\unrestrict` command (Nathan Bossart) [](https://postgr.es/c/0bfac9e1f)

  This oversight in the fix for CVE-2025-8714 allows a malicious server to inject shell commands into plain-text dump output that will be run at restore time on the machine running psql, the exact scenario that CVE-2025-8714 intended to prevent.

  The PostgreSQL Project thanks Lucas Velgus, Filip Janus, and Daniel Bakker for reporting this problem. (CVE-2026-18408)

- Remove pg_dump's assumption that pg_proc.protrftypes cannot have more than `FUNC_MAX_ARGS` entries (Tom Lane) [](https://postgr.es/c/c2b16f5d4)

  Since there could be entries for both input and output arguments, it's feasible for this array's length to exceed `FUNC_MAX_ARGS` (which constrains only input arguments). Even if that were not so, pg_dump cannot assume that the server was built with the same value of `FUNC_MAX_ARGS` that it has. An overrun would lead to a memory clobber inside pg_dump.

  The PostgreSQL Project thanks Masahiko Sawada for reporting this problem. (CVE-2026-19385)

- Harden PL/Perl against “tied” Perl arrays and hashes (Tom Lane) [](https://postgr.es/c/2d78c34f8)

  A tied object that doesn't behave like a regular one could lead to memory overwrite, or to constructing a corrupt result array (which would likely cause problems later).

  The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-14670)

- Fix integer overflows in memory-allocation calculations in PL/Perl and PL/Tcl (Heikki Linnakangas) [](https://postgr.es/c/b56cc7deb)

  This is the same type of problem as CVE-2026-6473, just in a different part of the code, and is fixed in the same way.

  The PostgreSQL Project thanks the Tulya Project (Team Dhiutsa, Bitecope Technologies Private Ltd) for reporting this problem. (CVE-2026-14677)

- Ensure that `contrib/amcheck` functions restrict `search_path` before executing index expressions (Noah Misch) [](https://postgr.es/c/e41c72aff)

  Because amcheck will run such index expressions as the owner of their tables, a caller could potentially hijack `search_path`-dependent functions to run arbitrary code as the table owner. By default this is not a vulnerability because only superusers are allowed to call amcheck functions; but if that privilege was granted out, it created a larger hazard than the documentation suggests.

  The PostgreSQL Project thanks Yuelin Wang and Jacob Brazeal for reporting this problem. (CVE-2026-14673)

- Fix integer overflows in `contrib/fuzzystrmatch`'s `levenshtein()` and `levenshtein_less_equal()` functions (Nathan Bossart) [](https://postgr.es/c/c4d51b627)

  Passing large cost values to these functions could cause integer overflows, thereby producing nonsensical results, and even causing out-of-bounds writes in some cases.

  The PostgreSQL Project thanks Ben Morris (in collaboration with Claude and Anthropic Research) for reporting this problem. (CVE-2026-15742)

- Fix datatype error in `contrib/pg_trgm`'s GiST picksplit function (Heikki Linnakangas) [](https://postgr.es/c/1af08af69)

  This mistake resulted in reading past the end of the buffer, typically causing bad split decisions; but a crash could ensue if you're very unlucky.

  The PostgreSQL Project thanks Mehmet D. Ince for reporting this problem. (CVE-2026-14678)

- Remove the plan cache in `contrib/refint` (Ayush Tiwari) [](https://postgr.es/c/66a5146dc)

  This caching behavior has several serious bugs, notably that `check_foreign_key()` embeds the new key values in its cascade-UPDATE queries, so a cached plan reuses the originally-needed values rather than the key values that should be used. The simplest solution is to remove it.

  The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-14671)

- Fix mis-handling of asynchronous reads when rescanning an asynchronous Append plan node (Alexander Korotkov, Gleb Kashkin, Etsuro Fujita) [](https://postgr.es/c/3704870b2)

  When an upper plan node rescans an Append before having read the entire Append output, we need to discard any in-flight requests sent to external servers (by `postgres_fdw` for example). This was not done correctly in cases where a subplan has parameter changes or is discarded by partition pruning in the next scan. The outcome could be incorrect query results, an infinite loop, or an assertion failure.

- Fix error in partition pruning for RANGE-partitioned tables (David Rowley) [](https://postgr.es/c/31f2acde5)

  In some cases the DEFAULT partition would be skipped when it should not be, which could lead to rows missing from query results.

- Fix planner's nullability and strictness checks for `value IN (array)` expressions (Ayush Tiwari) [](https://postgr.es/c/26d6b7dc9)

  These checks should only succeed if the array operand is known to be non-empty, but that consideration was missed, allowing optimizations to be applied that should not be. This could result in wrong query answers if the array actually was empty.

- Fix incorrect join removal logic (Matheus Alcantara, Richard Guo) [](https://postgr.es/c/cdcec567d) [](https://postgr.es/c/b308eb366)

  In edge cases, it was possible for a constant output value coming from within the nullable side of an outer join to not be replaced by NULL when it should be.

- Add missed checks for hashability of equality comparisons on container datatypes (arrays, composites, ranges) (Andrei Lepikhov, Tom Lane) [](https://postgr.es/c/19152e3c2)

  The planner must verify hashability of the container's component type(s) before deciding it can use a hash-based plan type. This step was missed in some places, leading to “could not identify a hash function” failures at execution.

- Fix mis-optimization of `COUNT` window functions that have an `EXCLUDE` clause or lack `ORDER BY` (Chengpeng Yan, David Rowley) [](https://postgr.es/c/be63b285e)

  These window functions were treated as monotonic when they should not be, allowing wrong answers to be computed.

- Fix `ALTER COLUMN ... DROP EXPRESSION` to work when there are multiple levels of partitions (Alberto Piai) [](https://postgr.es/c/18006c1bd)

- Fix attaching partitions of indexes that are exclusion constraints (Japin Li) [](https://postgr.es/c/1d6c654c8)

  Notably, this oversight broke dump/restore of partitioned exclusion constraints.

- Disallow renaming a rule to `_RETURN` (Tom Lane) [](https://postgr.es/c/e99fb3262)

  That name is reserved for a view's `ON SELECT` rule, but `ALTER RULE` allowed renaming other rules to `_RETURN`, causing trouble later.

- Fix missing lock release for role membership grants in `DROP OWNED BY` (Jeff Davis) [](https://postgr.es/c/25e54cec7)

  This oversight resulted in a warning message, followed by retaining a lock on the membership grant until the end of the transaction.

- Fix failure of `EXPLAIN` when deparsing `SQL/JSON` aggregates (Richard Guo) [](https://postgr.es/c/dcda1f07d)

  Some plan structures resulted in “invalid JsonConstructorExpr underlying node type” errors.

- Fix use of `REINDEX CONCURRENTLY` with a deferred uniqueness constraint (Nitin Motiani) [](https://postgr.es/c/28269fed6)

  The transient index copy created during `REINDEX CONCURRENTLY` was incorrectly marked as enforcing immediate uniqueness, causing spurious reports of constraint violation.

- Fix matching of localized month/day names in `to_date()` (Heikki Linnakangas) [](https://postgr.es/c/8acfaa12a)

  The matching logic misbehaved in cases where case-folding changes the byte length of the string.

- Fix incorrect NFC recomposition for Hangul U+11A7 (TBASE) (Diego Frias, Michael Paquier) [](https://postgr.es/c/0c9cbbfb5)

  This character was treated as a valid T syllable, which it is not, and hence silently swallowed during normalization.

- Avoid possible truncation of output lexemes in case-insensitive `synonym` dictionaries (Jeff Davis) [](https://postgr.es/c/3805641cb)

  If folding to lower case increased the byte length of a lexeme, it was incorrectly truncated to its original byte length when emitted.

- Defend against truncated UTF-8 characters in case-conversion logic (Jeff Davis) [](https://postgr.es/c/5e78ebca5)

- Fix typo in `hash_record_extended()` (Man Zeng) [](https://postgr.es/c/203e238bb)

  The code failed to initialize the second isnull argument passed to FunctionCallInvoke(). This is harmless for existing in-core extended hash support functions, which will not examine that value. However, extension-provided hash functions could be affected if they inspect `PG_ARGISNULL(1)`.

- Fix `pg_get_publication_tables()` to not fail if a publishable table is dropped concurrently (Bharath Rupireddy) [](https://postgr.es/c/dcbc96685)

- Prevent `satisfies_hash_partition()` from crashing with `VARIADIC NULL` (Robert Haas) [](https://postgr.es/c/52af6fef4)

- Report invalid-weight errors more cleanly and consistently in `tsvector_filter()` and allied functions (Ewan Young) [](https://postgr.es/c/0626fbfeb)

  In particular, report weight characters that are not printable ASCII in octal form (`\nnn`), as `charout()` would render them. This avoids possibly producing an invalidly-encoded error message.

- Fix mishandling of namespace nodes in `xpath()` (Michael Paquier) [](https://postgr.es/c/6c08cbb7a) [](https://postgr.es/c/940916549)

  This fix avoids an unexpected “could not copy node” error.

- Fix `jsonpath`'s `.decimal` method to not throw a hard error for incorrect precision or scale (Ewan Young) [](https://postgr.es/c/ab35b8d25) [](https://postgr.es/c/c768637d6)

  Silent mode should suppress these errors, but failed to.

- Fix NULL-pointer crash when `IS JSON` or similar constructs have an argument that is of string category but lacks a cast to type `text` (Ayush Tiwari) [](https://postgr.es/c/d0acd2535)

  There are no such data types in core PostgreSQL, but the problem is reachable with some extension types.

- Ensure that `SQL/JSON` `ON EMPTY / ON ERROR DEFAULT` values are coerced to the correct typmod (Ewan Young) [](https://postgr.es/c/71cd10cd2)

  For example, the declared precision and scale of a `numeric` target column were not applied to the default value.

- Avoid machine-dependent behavior when dividing the smallest possible `money` value by -1 (Andrey Rachitskiy) [](https://postgr.es/c/1416f304d)

- Fix crash after out-of-memory failure partway through creation of a cache entry for a text search dictionary (Tom Lane) [](https://postgr.es/c/634a8dcb8)

- Fix memory-safety bugs in processing of incorrect ispell/hunspell dictionary files (Andrey Rachitskiy) [](https://postgr.es/c/5fdea3aa3)

- Prevent access to other sessions' temporary tables (Jim Jones, Daniil Davydov, Alexander Korotkov) [](https://postgr.es/c/4dfae59a1) [](https://postgr.es/c/4e49f68b7)

  Some code paths failed to prevent this, leading to silently wrong (inconsistent) results.

- Fix the order in which autovacuum processes databases (Rustam Khamidullin) [](https://postgr.es/c/288d4e83f)

  It was unintentionally processing databases from lowest to highest score, when it should be doing the reverse.

- Fix memory leak in parallel vacuum worker processes (Baji Shaik) [](https://postgr.es/c/8ad414831)

  Progress reports from a parallel worker leaked about 1kB per report, with the waste accumulating for the life of the worker process.

- Honor query cancel and vacuum delay during GIN index posting-tree cleanup (Paul Kim, Alexander Korotkov) [](https://postgr.es/c/ba5e46329)

  The posting tree for a common value can be large, so that this missed check could allow vacuum to run for a long time before noticing an interrupt.

- Fix possible mis-decoding of index tuples during GiST and SP-GiST index-only scans (Peter Geoghegan) [](https://postgr.es/c/355faed5a)

  This error could lead to emitting corrupted data from an index-only scan plan. The only affected core opclass is GiST's range_ops, and it could only fail if the range column were not the first index column.

- Ensure that the new last block of a bulk-extended table is added to its free space map promptly (Jingtang Zhang) [](https://postgr.es/c/768ae083e)

  An off-by-one error caused the last block of a multi-block table extension to not be marked as free in the map. This would eventually get corrected by vacuum, but meanwhile the space wouldn't be used.

- Avoid possible double-free or infinite error recovery loop in resource cleanup during transaction abort (Tom Lane) [](https://postgr.es/c/011eedcdc)

- When creating directories, tolerate concurrent creation of the same directory (Andrew Dunstan, Tom Lane) [](https://postgr.es/c/f0a831ef3)

- Prevent creation of dangling object dependencies by acquiring a shared lock on any object being depended on (Bertrand Drouvot) [](https://postgr.es/c/3a9909eda) [](https://postgr.es/c/c1588f92a)

  The shared lock will conflict with any attempt to drop the depended-on object, eliminating the race condition that formerly existed. For example, if one session drops a schema (that appears empty to it) concurrently with some other session creating a function in that schema, previously both transactions could commit, leaving an invalid function definition behind. Now, one transaction or the other will fail.

- Fix race condition in conflict detection for `SERIALIZABLE` isolation mode (Peter Geoghegan) [](https://postgr.es/c/8434c9385)

  A conflict could be missed when examining an initially-empty btree index, allowing failure of serializability due to improperly allowing conflicting transactions to commit.

- Fix race condition in ProcSignalBarrier code (Masahiko Sawada) [](https://postgr.es/c/a651b8a89)

  This error could result in processes getting stuck, typically after reporting “still waiting for backend with PID \<nnnn\> to accept ProcSignalBarrier”.

- Fix race conditions when a set of processes that belong to the same lock group exit at the same time (Vlad Lesin) [](https://postgr.es/c/d489c4439) [](https://postgr.es/c/e14b4ea4a)

  These errors could lead to PANIC aborts, with messages such as “latch already owned”. The issue does not normally arise in regular parallel query, since the leader won't exit before seeing its workers finish; but some extensions reach the problem.

- Fix WAL logging of operations that clear bits in tables' visibility maps (Melanie Plageman, Andres Freund) [](https://postgr.es/c/7edec8b57) [](https://postgr.es/c/c0d9864f5) [](https://postgr.es/c/067213430)

  Such VM changes were missed by the WAL summarizer, potentially leading to incorrect incremental backups. We also failed to log full-page images of such VM pages when needed, potentially allowing torn page writes to go uncorrected. This could lead to misbehavior later, such as wrong results from index-only scans.

- Prevent WAL summarizer process from getting stuck at a timeline switch (Robert Haas) [](https://postgr.es/c/499d9eabb) [](https://postgr.es/c/d28cdf46e)

- Fix race with timeline selection in logical decoding during standby promotion (Bertrand Drouvot) [](https://postgr.es/c/16b89ff04) [](https://postgr.es/c/ab5334d8b)

  Logical decoding being performed on the standby could fail with a “requested WAL segment has already been removed” error. A repeat attempt would succeed, so there was no permanent problem but there was an availability hazard.

- Avoid exposing a WAL receiver's full connection string during timeline jumps (Chao Li) [](https://postgr.es/c/c89499a79)

  The pg_stat_wal_receiver view should show a sanitized version of the connection string, without sensitive data. But it transiently showed the full string when we re-use an existing WAL receiver.

- Use run-time checks, not just Asserts, to verify the correct number of columns in tuples received during logical replication (Varik Matevosyan) [](https://postgr.es/c/15f4e3d0c)

  A malicious or buggy publisher could send inconsistent numbers of columns. While we could not find a scenario in which this would have serious ill effects, extra caution seems warranted.

- Clean up quoting of string parameters within constructed replication commands (Tom Lane) [](https://postgr.es/c/14810cc0d)

  Various places that generate replication commands were not being adequately careful about quoting replication slot names and other parameters that need to be inserted into those commands. This could result in unexpected syntax errors in those commands. In principle, a crafted replication slot name could result in SQL injection; but such a scenario seems very unlikely to occur in practice, since replication operations can only be invoked by highly-privileged users and there is no reason for them to use a slot name coming from an untrustworthy source.

- Fix logical decoding of empty prepared transactions (Masahiko Sawada) [](https://postgr.es/c/8c4519c71)

  A prepared transaction that did not cause any decodable updates could result in sending `COMMIT/ROLLBACK PREPARED` to the output plugin with no preceding `PREPARE`. For the built-in subscriber this breaks replication, and other plugins will probably not like it either.

- Fix corruption of unlogged sequences after standby promotion (Fujii Masao) [](https://postgr.es/c/a1ed6a9a0)

  Previously, if an unlogged sequence was created on the primary and replicated to a standby, accessing the sequence after promoting the standby could fail with “bad magic number in sequence” or related errors.

- Fix cascading standby reconnect failure after archive fallback (Marco Nenciarini) [](https://postgr.es/c/2cf28d1b9)

  A cascading standby could fail to reconnect to its upstream standby with “requested starting point ... is ahead of the WAL flush position” after falling back to archive recovery.

- Do not try to clear pg_database.dathasloginevt locally on a standby server (Ayush Tiwari) [](https://postgr.es/c/4a375527a)

  Event trigger cleanup tried to perform that action on standby servers as well as the primary. That can't work on a standby, and there's no need anyway since replay of the primary's database change will soon fix it.

- Avoid race condition while dropping obsolete replication slots (Xuneng Zhou) [](https://postgr.es/c/ea834d747)

  An incorrect unlock and log message could occur if another session immediately re-used the dropped slot's shared-memory entry.

- Avoid race condition while dropping ephemeral replication slots (Zhijie Hou) [](https://postgr.es/c/080d61f07)

  The slot-releasing code performed some additional updates to the replication slot's shared-memory entry after releasing the slot. This is unsafe since another session could immediately re-use the dropped slot's shared-memory entry. Skip those updates in the case of an ephemeral slot.

- Fix stale progress reports during logical replication table synchronization (Shinya Kato) [](https://postgr.es/c/f2acab534)

  Previously, the pg_stat_progress_copy view in the subscriber would continue to show the initial `COPY` operation as active even after the data copy had finished. The stale entry remained visible until synchronization caught up with the publisher.

- Clear base backup progress on backup failure (Chao Li) [](https://postgr.es/c/e2ea6bfed) [](https://postgr.es/c/a240e8cd2)

  Previously the pg_stat_progress_basebackup view would continue to show a stale progress entry after a failure, until the replication client disconnected. pg_basebackup normally disconnects immediately, but other clients might not.

- Fix possible PANIC due to concurrent drop of pgstats entries when `track_functions` is enabled (Sami Imseih, Michael Paquier) [](https://postgr.es/c/2e0c61aed) [](https://postgr.es/c/39e649d44) [](https://postgr.es/c/afb076b29)

- Clean up broken local pgstats entry after failing to obtain space for the corresponding shared hashtable entry (Niall Newman) [](https://postgr.es/c/fc9283b21)

  Failure to do this led to a null-pointer dereference the next time the local entry was used.

- In PL/Perl, avoid NULL pointer dereference crash when working with an invalid `PostgreSQL::InServer::ARRAY` object (Xing Guo) [](https://postgr.es/c/d424d06ed)

- In PL/Python, properly check for errors when working with sequence and mapping objects (Richard Guo) [](https://postgr.es/c/3dc59c173)

  Previously, a broken object or an unhandled exception could result in a NULL pointer dereference crash.

- In libpq, always drain all pending bytes from the SSL or GSS decryption buffer during `pqReadData()` (Jacob Champion) [](https://postgr.es/c/c162810a5) [](https://postgr.es/c/177a2a2e3) [](https://postgr.es/c/0958c3ea4) [](https://postgr.es/c/bab0a2db7)

  This avoids edge cases where libpq or its calling application waits for more data to arrive on the socket, but actually all the data has already arrived.

- Allow libpq to accept ParameterDescription messages exceeding 30000 bytes (Ning Sun) [](https://postgr.es/c/e4183c667)

  Previously, this message type was not among those that libpq's validity heuristics believed could be long. The limit resulted in failure for prepared queries having more than 7498 parameters, which is unlikely but supported.

- Reject multiple descriptor header items in ecpg's `GET/SET DESCRIPTOR` statements (Masashi Kamura) [](https://postgr.es/c/fe8c0a762)

  Previously the grammar allowed this syntax, but broken C code was generated. Adjust the grammar and the documentation to allow only one header item.

- Make line widths match in psql's expanded aligned output format (Pavel Stehule) [](https://postgr.es/c/efd885d05)

  When the table's data rows are narrower than the record header lines, widen the data rows to match the headers, avoiding unsightly output.

- Fix psql's privilege check for showing database size in `\l+` (Christoph Berg) [](https://postgr.es/c/41949c6f3)

  The underlying server function permits users who have `pg_read_all_stats` privileges to see the sizes of all databases, even if they lack `CONNECT` privilege. But psql was unaware of that provision and would not call the function unless the user has `CONNECT` privilege.

- Fix psql's tab completion for `\df` to consider procedures too (Erik Wienhold) [](https://postgr.es/c/355a4fcf9)

- Fix thread-safety bug in pgbench (Fujii Masao) [](https://postgr.es/c/52b3e7001)

  When pgbench runs with multiple threads and the `--verbose-errors` option, different threads could attempt to use the same buffer to construct error messages, leading to corrupted log output.

- In pg_combinebackup, prevent infinite loop if the source file is shorter than expected (Peter Eisentraut) [](https://postgr.es/c/090ce6934)

- Fix cleanup of publisher-side objects after errors in pg_createsubscriber (Nisha Moond) [](https://postgr.es/c/c03784a21)

  When pg_createsubscriber fails after creating logical replication objects, it should remove the publication and replication slot that it created on the publisher. Some error cases failed to do so.

- Use the source cluster's group-read file permissions for pg_recvlogical output files (Fujii Masao) [](https://postgr.es/c/ddd12d1a5)

  pg_recvlogical was documented to behave this way, but it never actually enabled group-read.

- In `contrib/amcheck`, handle short-header varlena datums correctly (Andrey Borodin) [](https://postgr.es/c/8abb8a155)

  This error could result in doing excess work while verifying a btree index, but seems not to have had any worse consequences.

- In `contrib/btree_gist`, fix `NaN` handling in the `float4` and `float8` opclasses (Bill Kim, Tom Lane) [](https://postgr.es/c/d215d2cc2)

  Comparisons, as well as the GiST penalty and distance functions, did not account for `NaN` and would give the wrong answer when handed one. It is recommended to reindex `btree_gist` indexes on float columns after installing this update, if there is any possibility that there are `NaN` entries in those columns.

- In `contrib/btree_gist`, fix searches using a not-equal operator (Ayush Tiwari) [](https://postgr.es/c/86992769e)

  For variable-length data types, the code for scanning non-leaf index pages applied the wrong comparison function, leading to wrong results and potentially crashes.

- Fix unguarded recursion and loops in `contrib/hstore_plperl`, `contrib/jsonb_plperl`, and `contrib/jsonb_plpython` (Aleksander Alekseev) [](https://postgr.es/c/3df0b7755) [](https://postgr.es/c/4efef9d18)

  Prevent stack overflow when dealing with deeply nested `jsonb` values, and allow interruption of the infinite loop caused when attempting to dereference circular chains of Perl object references.

- Fix missed release of statistics catcache entry in `contrib/intarray` (Man Zeng) [](https://postgr.es/c/94b57ab54)

  This oversight led to warnings like “resource was not closed: cache pg_statistic”.

- In `contrib/ltree`, fix integer overflow in comparisons (Ayush Tiwari) [](https://postgr.es/c/c391c00d9)

  `ltree` values containing more than about 14,653 labels resulted in wrong comparison answers due to overflow. If a btree index contains such values, it is probably corrupt and should be reindexed after installing this update.

- In `contrib/pgcrypto`, avoid double-free crash after encountering an error while using an OSSLCipher object (Yuelin Wang) [](https://postgr.es/c/2aa6be6e6)

- Fix array overrun in `contrib/pg_surgery`'s `heap_force_kill` and `heap_force_freeze` functions (Michael Paquier) [](https://postgr.es/c/0bcf19c9e)

  Attempting to change a TID whose offset number equals MaxHeapTuplesPerPage wrote one byte past the end of the allocated array, potentially crashing the server.

- In `contrib/pg_surgery`, avoid infinite loop with TID arrays having more than 64K elements (Andrey Rachitskiy) [](https://postgr.es/c/1b6c99d96)

- Avoid NULL-pointer dereference in `contrib/refint`'s `check_foreign_key()` (Ayush Tiwari) [](https://postgr.es/c/6b4de201e)

  In the on-update-cascade case, a null value of a referenced column led to a crash. This is an oversight in the fix for CVE-2026-6637, but the code that was there before that wasn't really right either.

- Fix `contrib/seg` to print segments with `~` certainty indicators correctly (Ewan Young) [](https://postgr.es/c/bcbbd070d)

  Due to a typo, `seg_out()` did not print a `~` certainty indicator attached to a segment's upper boundary. Worse, if the lower boundary had `~` while the upper boundary had no indicator, the upper boundary was not printed at all, incorrectly converting the value into an open interval.

- Fix crash with namespace nodes in `contrib/xml2`'s `xpath_nodeset()` function (Andrey Chernyy, Michael Paquier) [](https://postgr.es/c/4a49ab289)

- Support building PostgreSQL with OpenSSL 4 (Daniel Gustafsson) [](https://postgr.es/c/8bcabfcce)

- Update time zone data files to tzdata release 2026c (Tom Lane) [](https://postgr.es/c/669438aed)

  Alberta (America/Edmonton) will be on year-round UTC-06 (effectively, permanent DST) beginning in November 2026. This release assumes that their TZ abbreviation will be `CST` from that time forward. That seems likely to change, but it's unclear what new abbreviation will be used.

  Morocco (Africa/Casablanca) will move to permanent UTC+00, without daylight saving time transitions, on 2026-09-20.

## Release 17.10

Release date:

2026-05-14

This release contains a variety of fixes from 17.9. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.10

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.6, see [Release 17.6](#release-17-6).

## Changes

- Prevent unbounded recursion while processing startup packets (Michael Paquier) [](https://postgr.es/c/32a4ce55c) [](https://postgr.es/c/6dffaeb8e)

  A malicious client could crash the connected backend by alternating rejected SSL and GSS encryption requests indefinitely.

  The PostgreSQL Project thanks Calif.io (in collaboration with Claude and Anthropic Research) for reporting this problem. (CVE-2026-6479)

- Fix assorted integer overflows in memory-allocation calculations (Tom Lane, Nathan Bossart, Heikki Linnakangas) [](https://postgr.es/c/fe2720c45) [](https://postgr.es/c/01b5ef7df) [](https://postgr.es/c/e3a2bea41) [](https://postgr.es/c/26dd3cac2) [](https://postgr.es/c/87357a606) [](https://postgr.es/c/3c41f5534) [](https://postgr.es/c/ebcfa7867) [](https://postgr.es/c/00e243e67) [](https://postgr.es/c/e5babf754) [](https://postgr.es/c/8e909812d)

  Various places were incautious about the possibility of integer overflow in calculations of how much memory to allocate. Overflow would lead to allocating a too-small buffer which the caller would then write past the end of. This would at least trigger server crashes, and probably could be exploited for arbitrary code execution. In many but by no means all cases, the hazard exists only in 32-bit builds.

  The PostgreSQL Project thanks Xint Code, Bruce Dang, Sven Klemm, and Pavel Kohout for reporting these problems. (CVE-2026-6473)

- Properly quote subscription names in pg_createsubscriber (Nathan Bossart) [](https://postgr.es/c/d7de7fa84)

  The given subscription name was inserted into SQL commands without quoting, so that SQL injection could be achieved in the (perhaps unlikely) case that the subscription name comes from an untrusted source.

  The PostgreSQL Project thanks Yu Kunpeng for reporting this problem. (CVE-2026-6476)

- Properly quote object names in logical replication origin checks (Pavel Kohout) [](https://postgr.es/c/f0f59b658)

  `ALTER SUBSCRIPTION ... REFRESH PUBLICATION` interpolated schema and relation names into SQL commands without quoting them, allowing execution of arbitrary SQL on the publisher.

  The PostgreSQL Project thanks Pavel Kohout for reporting this problem. (CVE-2026-6638)

- Reject over-length options in `ts_headline()` (Michael Paquier) [](https://postgr.es/c/3ed3dbbf4)

  The `StartSel`, `StopSel` and `FragmentDelimiter` strings must not exceed 32Kb in length, but this was not checked for. An over-length value would typically crash the server.

  The PostgreSQL Project thanks Xint Code for reporting this problem. (CVE-2026-6473)

- Guard against malicious time zone names in `timeofday()` and `pg_strftime()` (Tom Lane) [](https://postgr.es/c/4197c880c) [](https://postgr.es/c/a386d14fe)

  A crafted time zone setting could pass `%` sequences to `snprintf()`, potentially causing crashes or disclosure of server memory. Another path to similar results was to overflow the limited-size output buffer used by `pg_strftime()`.

  The PostgreSQL Project thanks Xint Code for reporting this problem. (CVE-2026-6474)

- When creating a multirange type, ensure the user has `CREATE` privilege on the schema specified for the multirange type (Jelte Fennema-Nio) [](https://postgr.es/c/c27ba08cd)

  The multirange type can be put into a different schema than its parent range type, but we neglected to apply the required privilege check when doing so.

  The PostgreSQL Project thanks Jelte Fennema-Nio for reporting this problem. (CVE-2026-6472)

- Use timing-safe string comparisons in authentication code (Michael Paquier) [](https://postgr.es/c/c4e7435b3) [](https://postgr.es/c/8e34acfda)

  Use `timingsafe_bcmp()` instead of `memcmp()` or `strcmp()` when checking passwords, hashes, etc. It is not known whether the data dependency of those functions is usefully exploitable in any of these places, but in the interests of safety, replace them.

  The PostgreSQL Project thanks Joe Conway for reporting this problem. (CVE-2026-6478)

- Mark `PQfn()` as unsafe, and avoid using it within libpq (Nathan Bossart) [](https://postgr.es/c/d88c7be15)

  For a non-integral result type, `PQfn()` is not passed the size of the output buffer, so it cannot check that the data returned by the server will fit. A malicious server could therefore overwrite client memory. This is unfixable without an API change, so mark the function as deprecated. Internally to libpq, use a variant version that can apply the missing check.

  The PostgreSQL Project thanks Yu Kunpeng and Martin Heistermann for reporting this problem. (CVE-2026-6477)

- Prevent path traversal in pg_basebackup and pg_rewind (Michael Paquier) [](https://postgr.es/c/8f881e188)

  These applications failed to validate output file paths read from their input, so that a malicious source could overwrite any file writable by these applications. Constrain where data can be written by rejecting paths that are absolute or contain parent-directory references.

  The PostgreSQL Project thanks XlabAI Team of Tencent Xuanwu Lab and Valery Gubanov for reporting this problem. (CVE-2026-6475)

- Guard against field overflow within `contrib/intarray`'s `query_int` type and `contrib/ltree`'s `ltxtquery` type (Tom Lane) [](https://postgr.es/c/c4d04cc48) [](https://postgr.es/c/2b429d887)

  Parsing of these query structures did not check for overflow of 16-bit fields, so that construction of an invalid query tree was possible. This can crash the server when executing the query.

  The PostgreSQL Project thanks Xint Code for reporting this problem. (CVE-2026-6473)

- Guard against overly long values of `contrib/ltree`'s `lquery` type (Michael Paquier) [](https://postgr.es/c/8c3426110)

  Values with more than 64K items caused internal overflows, potentially resulting in stack smashes or wrong answers.

  The PostgreSQL Project thanks Vergissmeinnicht, A1ex, and Jihe Wang for reporting this problem. (CVE-2026-6473)

- Prevent SQL injection and buffer overruns in `contrib/spi` (Nathan Bossart) [](https://postgr.es/c/2dc64ef28)

  `check_foreign_key()` was insufficiently careful about quoting key values, and also used fixed-length buffers for constructing queries. While this module is only meant as example code, it still shouldn't contain such dangerous errors.

  The PostgreSQL Project thanks Nikolay Samokhvalov for reporting this problem. (CVE-2026-6637)

- Check for nondeterministic collations before assuming that an equality condition on a collatable type implies uniqueness (Richard Guo) [](https://postgr.es/c/d0e73bb18) [](https://postgr.es/c/13226050e)

  Numerous planner optimizations assume that, for example, at most one table row can satisfy `WHERE x = 'abc'` if there is a unique index on `x`. However this conclusion is unsafe in general if the index and the `WHERE` clause have different collations attached. It is safe when both collations are deterministic, because that property essentially requires that equality of two strings means bitwise equality. But nondeterministic collations don't act that way, so that optimizing on the assumption of unique matches can give wrong query answers if either the `WHERE` clause or the index has a nondeterministic collation.

- Fix incomplete removal of relation references in `RestrictInfo` structs during join removal (Tom Lane) [](https://postgr.es/c/766d40286) [](https://postgr.es/c/53cb4ec1d)

  This oversight has been shown to result in planner failures such as unexpected “FULL JOIN is only supported with merge-joinable or hash-joinable join conditions” errors. It may also have caused failure to consider valid plans in other cases.

- Fix incorrect handling of `NEW` generated columns in rule actions and rule qualifications (Richard Guo, Dean Rasheed) [](https://postgr.es/c/9d6208939)

  Previously, such column references would produce NULL in `INSERT` cases, or be equivalent to the `OLD` value in `UPDATE` cases.

- Fix spurious “generated columns are not supported in COPY FROM WHERE conditions” errors (Tom Lane) [](https://postgr.es/c/681a91d29)

  Use of a system column in a `COPY FROM WHERE` condition could sometimes incorrectly report this error.

- Correctly report a serialization failure when `MERGE` encounters a concurrently-updated tuple in repeatable-read or serializable mode (Tender Wang) [](https://postgr.es/c/2dcac93c0)

  Previously, such cases behaved the same as in lower isolation levels.

- Fix `CREATE TABLE ... LIKE ... INCLUDING STATISTICS` for cases where the source table has dropped column(s) (Julien Tachoires) [](https://postgr.es/c/a0104b447)

  In such cases, extended statistics objects could be copied incorrectly, or the command could give an incorrect error.

- Allow `ALTER INDEX ... ATTACH PARTITION` to mark the parent index valid if appropriate (Sami Imseih) [](https://postgr.es/c/becf6d269)

  There are edge cases in which a partitioned index might remain marked as invalid even when all its leaf indexes are valid. This change provides a mechanism whereby a user can correct such a situation without resorting to manual catalog updates.

- Fix `ALTER FOREIGN DATA WRAPPER` to not drop the wrapper object's dependency on its handler function (Jeff Davis) [](https://postgr.es/c/876fa84a2)

- Disallow making a composite type be a member of itself via a multirange (Heikki Linnakangas) [](https://postgr.es/c/54343f6f9)

  We already forbade such cases when the intermediate type is a domain, array, composite type, or range; but multiranges were overlooked.

- Fix datum-image comparisons to be insensitive to sign-extension variations (David Rowley) [](https://postgr.es/c/d29808e35)

  This fixes some situations that previously led to “could not find memoization table entry” errors or wrong query results.

- Fix incorrect logic for hashed `IN`/`NOT IN` with non-strict equality operator (Chengpeng Yan) [](https://postgr.es/c/3fda3e12f)

  The previous coding could crash or give wrong answers. All built-in data types have strict equality operators, so that this issue could only arise with an extension data type.

- Truncate overly-long locale-specific numeric symbols in `to_char()` (Tom Lane) [](https://postgr.es/c/c97a28618)

  If a locale specified a currency symbol, thousands separator, or decimal or sign symbol more than 8 bytes long, a buffer overrun was possible. No such locales exist in the real world, and it's impractical for an unprivileged attacker to install a malicious locale definition underneath a Postgres server; but for safety's sake check for overlength symbols and truncate if needed.

- Prevent buffer overruns when parsing an affix file for an `Ispell` dictionary (Tom Lane) [](https://postgr.es/c/ea5f0d176) [](https://postgr.es/c/a5426dbf8)

  A corrupt or malicious affix file could crash the server. This is not considered a security issue because text search configuration files are presumed trustworthy, but it still seems worth fixing.

- Guard against integer overflow in calculations of frame start and end positions for window aggregates (Richard Guo) [](https://postgr.es/c/f8736f8bc)

  Very large user-specified offsets (close to INT64_MAX) could result in errors or incorrect query results.

- Fix `array_agg_array_combine()` to combine the arrays' null bitmaps correctly (Dmytro Astapov) [](https://postgr.es/c/d6c9432cb)

  This mistake resulted in sometimes-incorrect output from parallelized `array_agg(anyarray)` calculations.

- Retry `sync_file_range()` if it returns error code `EINTR` (DaeMyung Kang) [](https://postgr.es/c/5499be332)

- Fix incorrect behavior of `pg_stat_reset_single_table_counters()` on a shared catalog (Chao Li) [](https://postgr.es/c/a4fefb3e0)

  Such cases had a side-effect of resetting the current database's `stat_reset_timestamp`, which was unintended.

- Update activity statistics when a parallel apply worker is idle (Zhijie Hou) [](https://postgr.es/c/88d7fdcc9)

  Previously, statistics from a recently-completed transaction might go unreported for long intervals, particularly if the workload is light.

- Fix “no relation entry for relid 0” failure while estimating array lengths in set operations (Tender Wang) [](https://postgr.es/c/93ed18720)

- Fix buffer overread when `pglz_decompress()` receives corrupt input (Andrew Dunstan) [](https://postgr.es/c/c05c3baf1)

  It was possible to read a few bytes past the end of the input, which in very unlucky cases might cause a crash.

- Fix incremental JSON parser's handling of numeric tokens that cross input buffer boundaries (Andrew Dunstan) [](https://postgr.es/c/2e373785e)

  It was possible to accept an incorrectly-formatted number, leading to failures later.

- Prevent bloating relation visibility maps during restore of an incremental backup (Robert Haas) [](https://postgr.es/c/076bc57fa)

  Restore could append many blocks of zeroes to a visibility map, due to incorrect computation of the expected file length. This does not result in data corruption, but it could waste a substantial amount of disk space.

- Use C collation, not the database's default collation, in catalog cache lookups on text columns (Jeff Davis) [](https://postgr.es/c/9dda30dd3)

  This avoids failures in edge cases such as physical replication startup, where there is no identified database so that a default collation cannot be determined.

- Prevent stuck slotsync worker processes from blocking promotion of a standby server (Nisha Moond, Ajin Cherian) [](https://postgr.es/c/15910b1c3) [](https://postgr.es/c/586f4266f) [](https://postgr.es/c/4bed04d39)

  A worker process that was vainly waiting for a response from the primary would delay promotion for an unreasonable amount of time.

- Fix excessive log output from idle slotsync worker processes (Zhijie Hou) [](https://postgr.es/c/91741b7cb)

- Ensure that tuplestore data structures are internally consistent even after an error (Tom Lane) [](https://postgr.es/c/1f5b6a5e5)

  The code was previously careless about this, which is fine most of the time but is problematic for the tuplestore backing a `WITH HOLD` cursor. In v15 and before this leads to easily-reproducible crashes; later branches are not known to be vulnerable, but it seems best to preserve consistency in all.

- Fix premature NULL lag reporting in pg_stat_replication (Shinya Kato) [](https://postgr.es/c/fdce5de55)

  The lag columns frequently read as NULL even while replication activity was happening.

- Avoid rare flush failure when working with non-WAL-logged GiST indexes (Tomas Vondra) [](https://postgr.es/c/6ef36bb35)

  A non-logged GiST index could nonetheless sometimes produce “xlog flush request \<n/nnnn\> is not satisfied” errors, due to incorrect selection of a “fake LSN” to represent an insertion point.

- Fix underestimate of required size of DSA page maps for odd-size segments (Paul Bunn) [](https://postgr.es/c/2543b9ea9)

  This miscalculation led to out-of-bounds accesses and hence server crashes.

- Fix indexing of oldest-multixact arrays in shared memory (Yura Sokolov) [](https://postgr.es/c/dcd9c06a4) [](https://postgr.es/c/969576dab)

  This mistake could cause a prepared-but-not-yet-committed transaction's row locks to appear invisible to other sessions, or other visibility issues for the results of such a transaction. With a very small max_connections setting, memory stomps were also possible.

- Fix possible server crash when processing extended statistics on expressions of extension data types (Michael Paquier) [](https://postgr.es/c/530b6b02f)

  NULL pointer dereferences were possible if the data type's typanalyze function does not compute any useful statistics. No in-core typanalyze function behaves that way, but extensions could.

- Fix minor memory leaks in ICU-based string processing (Jeff Davis) [](https://postgr.es/c/4761f2eee)

- If the startup process fails, properly shut down other child processes before exiting the postmaster (Ayush Tiwari) [](https://postgr.es/c/e381843cf)

  The handling of this situation relied on a long-obsolete assumption that no other postmaster children exist while the startup process is running, so that immediate postmaster exit is acceptable. Orphaned children would eventually notice the postmaster's death and exit on their own, but a cleaner shutdown procedure is desirable.

- Fix race condition between WAL replay of checkpoints and multixact ID creations (Heikki Linnakangas) [](https://postgr.es/c/1ca385032)

  A standby server following WAL from a primary of an older minor version could get into a crash-and-restart loop complaining about “could not access status of transaction”.

- Prevent indefinite wait in shutdown of a walsender process (Anthonin Bonnefoy) [](https://postgr.es/c/bbbc0888b) [](https://postgr.es/c/8ee536c89)

  At shutdown of a cluster that is publishing logical replication data, the walsender waits for all pending WAL to be written out. But it did not correctly request that to happen, so that in some cases this could become an indefinite wait.

- Ensure that changes to tables' free space maps are persisted during recovery (Alexey Makhmutov) [](https://postgr.es/c/1cf010f21)

  Previously, while WAL replay did update the free space map while replaying operations that should change it, the map page buffer did not get marked dirty if checksums are enabled, so that the changes might never get written out. On a standby server, over time this would result in a map wildly at variance with the table's actual contents. While the map is only used as a hint, this condition could cause significant performance degradation for some period of time after the standby server is promoted to be active, until most of the map has been repaired by updates.

- Fix crashes in some ecpg functions when called without any established connection (Shruthi Gowda) [](https://postgr.es/c/5d67549d9)

- Fix assorted bugs in backup decompression and tar-parsing code (Andrew Dunstan, Tom Lane, Chao Li) [](https://postgr.es/c/f1298a4c2) [](https://postgr.es/c/8b198b093) [](https://postgr.es/c/2640c5ba7)

  The decompression and tar-file reading code used in pg_basebackup and pg_verifybackup mishandled tar-file padding data, could corrupt LZ4-compressed data in edge cases, failed to check for some unusual error conditions, failed to exit after compression/decompression errors (leading to cascading error reports), and leaked memory.

- In pg_dumpall, don't skip role `GRANT`s with dangling grantor OIDs (Tom Lane) [](https://postgr.es/c/1cd783d20)

  Instead, handle such cases by emitting `GRANT` without any `GRANTED BY` clause, as we did before v16. This avoids losing the grant in foreseeable cases, since pre-v16 servers didn't prevent dropping the grantor role. Continue to emit a warning about the missing grantor, but only if the source server is v16 or later.

- In pg_upgrade, take care to use the correct protocol version when connecting to older source servers (Jacob Champion) [](https://postgr.es/c/ad7fc3f1f)

  This could be problematic when attempting to upgrade from a pre-2018 server.

- In `contrib/basic_archive`, allow the archive directory to be missing at startup (Nathan Bossart) [](https://postgr.es/c/f510577de)

  Previously, the setting of `basic_archive.archive_directory` was rejected if it didn't point to an existing directory. This is undesirable because archiving will be stuck indefinitely, even if the directory appears later.

- Fix `contrib/ltree` to cope when case-folding changes a string's byte length (Jeff Davis) [](https://postgr.es/c/d1bd9a7dc)

  Previously, `lquery` patterns specifying case-insensitive matching might fail to match labels they should match.

- In `contrib/pg_stat_statements`, don't leak memory if an error occurs while parsing the `pgss_query_texts.stat` file (Heikki Linnakangas) [](https://postgr.es/c/351e59f34)

- In `contrib/postgres_fdw`, avoid crash due to premature cleanup of a failed connection (Etsuro Fujita) [](https://postgr.es/c/af8f9248f)

  If a remote connection fails abort cleanup, we can't use it any longer. But delay closing the connection object until end of transaction, because there might still be references to it within data structures such as open cursors.

- Update time zone data files to tzdata release 2026b (Tom Lane) [](https://postgr.es/c/4c0eab6f0)

  British Columbia (America/Vancouver) will be on year-round UTC-07 (effectively, permanent DST) beginning in November 2026. This release assumes that their TZ abbreviation will be `MST` from that time forward. That seems likely to change, but it's unclear what new abbreviation will be used. Also a historical correction for Moldova: they have followed EU DST transition times since 2022.

## Release 17.9

Release date:

2026-02-26

This release contains a small number of fixes from 17.8. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.9

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.6, see [Release 17.6](#release-17-6).

## Changes

- Fix failure after replaying a multixid truncation record from WAL that was generated by an older minor version (Heikki Linnakangas) [](https://postgr.es/c/4a36c89f1)

  Erroneous logic for coping with the way that previous versions handled multixid wraparound led to replay failure, with messages like “could not access status of transaction”. A typical scenario in which this could occur is a standby server of the latest minor version consuming WAL from a primary server of an older version.

- Avoid incorrect complaint of invalid encoding when `substring()` is applied to “toasted” data (Noah Misch) [](https://postgr.es/c/5d5232bc3) [](https://postgr.es/c/50d361f62) [](https://postgr.es/c/8e73530f1)

  The fix for CVE-2026-2006 was too aggressive and could raise an error about an incomplete character in cases that are actually valid.

- Fix computation of the set of potentially-nulling outer joins for the output of a `LATERAL UNION ALL` subquery (Richard Guo) [](https://postgr.es/c/bcaf1b510)

  This error could lead to skipping `NOT NULL` tests in the mistaken belief that they were unnecessary, resulting in wrong query output.

- Fix `pg_stat_get_backend_wait_event()` and `pg_stat_get_backend_wait_event_type()` to report values for auxiliary processes (Heikki Linnakangas) [](https://postgr.es/c/842473337)

  Previously these functions returned NULL for auxiliary processes, but that's inconsistent with the pg_stat_activity view.

- Fix casting a composite-type variable to a domain type when returning its value from a PL/pgSQL function (Tom Lane) [](https://postgr.es/c/dfd850980)

  If the variable's value is NULL, a “cache lookup failed for type 0” error resulted.

- Fix potential null pointer dereference in `contrib/hstore`'s binary input function (Michael Paquier) [](https://postgr.es/c/0dfbe42da)

  `hstore`'s receive function crashed on input containing duplicate keys. `hstore` values generated by Postgres would never contain duplicate keys, so this mistake has gone unnoticed. The crash could be provoked by malicious or corrupted data.

## Release 17.8

Release date:

2026-02-12

This release contains a variety of fixes from 17.7. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.8

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.6, see [Release 17.6](#release-17-6).

## Changes

- Guard against unexpected dimensions of `oidvector`/`int2vector` (Tom Lane) [](https://postgr.es/c/3d160401b)

  These data types are expected to be 1-dimensional arrays containing no nulls, but there are cast pathways that permit violating those expectations. Add checks to some functions that were depending on those expectations without verifying them, and could misbehave in consequence.

  The PostgreSQL Project thanks Altan Birler for reporting this problem. (CVE-2026-2003)

- Harden selectivity estimators against being attached to operators that accept unexpected data types (Tom Lane) [](https://postgr.es/c/bbf5bcf58) [](https://postgr.es/c/dd3ad2a4d) [](https://postgr.es/c/dbb09fd8e)

  `contrib/intarray` contained a selectivity estimation function that could be abused for arbitrary code execution, because it did not check that its input was of the expected data type. Third-party extensions should check for similar hazards and add defenses using the technique intarray now uses. Since such extension fixes will take time, we now require superuser privilege to attach a non-built-in selectivity estimator to an operator.

  The PostgreSQL Project thanks Daniel Firer, as part of zeroday.cloud, for reporting this problem. (CVE-2026-2004)

- Fix buffer overrun in `contrib/pgcrypto`'s PGP decryption functions (Michael Paquier) [](https://postgr.es/c/7a7d9693c)

  Decrypting a crafted message with an overlength session key caused a buffer overrun, with consequences as bad as arbitrary code execution.

  The PostgreSQL Project thanks Team Xint Code, as part of zeroday.cloud, for reporting this problem. (CVE-2026-2005)

- Fix inadequate validation of multibyte character lengths (Thomas Munro, Noah Misch) [](https://postgr.es/c/838248b1b) [](https://postgr.es/c/7a522039f) [](https://postgr.es/c/319e8a644) [](https://postgr.es/c/10ebc4bd6) [](https://postgr.es/c/dc072a09a) [](https://postgr.es/c/955433ebd)

  Assorted bugs allowed an attacker able to issue crafted SQL to overrun string buffers, with consequences as bad as arbitrary code execution. After these fixes, applications may observe “invalid byte sequence for encoding” errors when string functions process invalid text that has been stored in the database.

  The PostgreSQL Project thanks Paul Gerste and Moritz Sanft, as part of zeroday.cloud, for reporting this problem. (CVE-2026-2006)

- Don't allow CTE references in sub-selects to determine semantic levels of aggregate functions (Tom Lane) [](https://postgr.es/c/075a763e2)

  This change undoes a change made two minor releases ago, instead throwing an error if a sub-select references a CTE that's below the semantic level that standard SQL rules would assign to the aggregate based on contained column references and aggregates. The attempted fix turned out to cause problems of its own, and it's unclear what to do instead. Since sub-selects within aggregates are disallowed altogether by the SQL standard, treating such cases as errors seems sufficient.

- Fix trigger transition table capture for `MERGE` in CTE queries (Dean Rasheed) [](https://postgr.es/c/c5fc17dda)

  When executing a data-modifying CTE query containing both a `MERGE` and another DML operation on a table with statement-level `AFTER` triggers, the transition tables passed to the triggers would not include the rows affected by the `MERGE`, only those affected by the other operation(s).

- Fix failure when all children of a partitioned target table of an update or delete have been pruned (Amit Langote) [](https://postgr.es/c/933f67fb6)

  In such cases, the executor could report “could not find junk ctid column” errors, even though nothing needs to be done.

- Avoid possible planner failure when a query contains duplicate window function calls (Meng Zhang, David Rowley) [](https://postgr.es/c/cae812741)

  Confusion over de-duplication of such calls could result in errors like “WindowFunc with winref 2 assigned to WindowAgg with winref 1”.

- Allow indexscans on partial hash indexes even when the index's predicate implies the truth of the WHERE clause (Tom Lane) [](https://postgr.es/c/e79b27662)

  Normally we drop a WHERE clause that is implied by the predicate, since it's pointless to test it; it must hold for every index entry. However that can prevent creation of an indexscan plan if the index is one that requires a WHERE clause on the leading index key, as hash indexes do. Don't drop implied clauses when considering such an index.

- Do not emit WAL for unlogged BRIN indexes (Kirill Reshke) [](https://postgr.es/c/4b6d096a0)

  One seldom-taken code path incorrectly emitted a WAL record relating to a BRIN index even if the index was marked unlogged. Crash recovery would then fail to replay that record, complaining that the file already exists.

- Prevent truncation of CLOG that is still needed by unread `NOTIFY` messages (Joel Jacobson, Heikki Linnakangas) [](https://postgr.es/c/d02c03ddc) [](https://postgr.es/c/c2682810a) [](https://postgr.es/c/d80d5f099)

  This fix prevents “could not access status of transaction” errors when a backend is slow to absorb `NOTIFY` messages.

- Escalate errors occurring during `NOTIFY` message processing to FATAL, i.e. close the connection (Heikki Linnakangas) [](https://postgr.es/c/b821c9292)

  Formerly, if a backend got an error while absorbing a `NOTIFY` message, it would advance past that message, report the error to the client, and move on. That behavior was fraught with problems though. One big concern is that the client has no good way to know that a notification was lost, and certainly no way to know what was in it. Depending on the application logic, missing a notification could cause the application to get stuck waiting, for example. Also, any remaining messages would not get processed until someone sent a new `NOTIFY`.

  Also, if the connection is idle at the time of receiving a `NOTIFY` signal, any ERROR would be escalated to FATAL anyway, due to unrelated concerns. Therefore, we've chosen to make that happen in all cases, for consistency and to provide a clear signal to the application that it might have missed some notifications.

- Fix erroneous counting of updates in `EXPLAIN ANALYZE MERGE` with a concurrent update (Dean Rasheed) [](https://postgr.es/c/d6c415c4b)

  This situation led to an incorrect count of “skipped” tuples in `EXPLAIN`'s output, or to an assertion failure in an assert-enabled build.

- Fix bug in following update chain when locking a tuple (Jasper Smit) [](https://postgr.es/c/bb87d7fef)

  This code path neglected to check the xmin of the first new tuple in the update chain, making it possible to lock an unrelated tuple if the original updater aborted and the space was immediately reclaimed by `VACUUM` and then re-used. That could cause unexpected transaction delays or deadlocks. Errors associated with having identified the wrong tuple have also been observed.

- Fix issues around in-place catalog updates (Noah Misch) [](https://postgr.es/c/0f69bedde) [](https://postgr.es/c/d3e5d8950) [](https://postgr.es/c/bcb784e7d)

  Send a nontransactional invalidation message for an in-place update, since such an update will survive transaction rollback. Also ensure that the update is WAL-logged before other sessions can see it. These fixes primarily prevent scenarios in which relations' frozen-XID attributes become inconsistent, possibly allowing premature CLOG truncation and subsequent “could not access status of transaction” errors.

- Fix incorrect handling of incremental backups of large tables (Robert Haas, Oleg Tkachenko) [](https://postgr.es/c/ad569b54a)

  If a table exceeding 1GB (or in general, the installation's segment size) is truncated by `VACUUM` between the base backup and the incremental backup, pg_combinebackup could fail with an error about “truncation block length in excess of segment size”. This prevented restoring the incremental backup.

- Fix potential backend process crash at process exit due to trying to release a lock in an already-unmapped shared memory segment (Rahila Syed) [](https://postgr.es/c/4071fe900)

- Guard against incorrect truncation of the multixact log after a crash (Heikki Linnakangas) [](https://postgr.es/c/d3ad4cef6)

- Fix possibly mis-encoded result of `pg_stat_get_backend_activity()` (Chao Li) [](https://postgr.es/c/52b27f585)

  The shared-memory buffer holding a session's activity string can end with an incomplete multibyte character. Readers are supposed to truncate off any such incomplete character, but this function failed to do so.

- Guard against recursive memory context logging (Fujii Masao) [](https://postgr.es/c/699293d27)

  A constant flow of signals requesting memory context logging could cause recursive execution of the logging code, which in theory could lead to stack overflow.

- Fix memory context usage when reinitializing a parallel execution context (Jakub Wartak, Jeevan Chalke) [](https://postgr.es/c/1d0fc2499)

  This error could result in a crash due to a subsidiary data structure having a shorter lifespan than the parallel context. The problem is not known to be reachable using only core PostgreSQL, but we have reports of trouble in extensions.

- Set next multixid's offset when creating a new multixid, to remove the wait loop that was needed in corner cases (Andrey Borodin) [](https://postgr.es/c/8ba61bc06) [](https://postgr.es/c/cad40cec2)

  The previous logic could get stuck waiting for an update that would never occur.

- Avoid rewriting data-modifying CTEs more than once (Bernice Southey, Dean Rasheed) [](https://postgr.es/c/c09096503)

  Formerly, when updating an auto-updatable view or a relation with rules, if the original query had any data-modifying CTEs, the rewriter would rewrite those CTEs multiple times due to recursion. This was inefficient and could produce false errors if a CTE included an update of an always-generated column.

- Allow retrying initialization of a DSM registry entry (Nathan Bossart) [](https://postgr.es/c/2fc5c5062)

  If we fail partway through initialization of a dynamic shared memory entry, allow the next attempt to use that entry to retry initialization. Previously the entry was left in a permanently-failed state.

- Fail recovery if WAL does not exist back to the redo point indicated by the checkpoint record (Nitin Jadhav) [](https://postgr.es/c/f5927da4f)

  Add an explicit check for this before starting recovery, so that no harm is done and a useful error message is provided. Previously, recovery might crash or corrupt the database in this situation.

- Avoid scribbling on the source query tree during `ALTER PUBLICATION` (Sunil S) [](https://postgr.es/c/bb08ac7ac)

  This error had the visible effect that an event trigger fired for the query would see only the first `publish` option, even if several had been specified. If such a query were set up as a prepared statement, re-executions would misbehave too.

- Pass connection options specified in `CREATE SUBSCRIPTION ... CONNECTION` to the publisher's walsender (Fujii Masao) [](https://postgr.es/c/7a990e801)

  Before this fix, the `options` connection option (if any) was ignored, thus for example preventing setting custom server parameter values in the walsender session. It was intended for that to work, and it did work before refactoring in PostgreSQL version 15 broke it, so restore the previous behavior.

- Prevent invalidation of newly created or newly synced replication slots (Zhijie Hou) [](https://postgr.es/c/3243c0177) [](https://postgr.es/c/9649f1adf) [](https://postgr.es/c/3510ebeb0)

  A race condition with a concurrent checkpoint could allow WAL to be removed that is needed by the replication slot, causing the slot to immediately get marked invalid.

- Fix race condition in computing a replication slot's required xmin (Zhijie Hou) [](https://postgr.es/c/123b851ab)

  This could lead to the error “cannot build an initial slot snapshot as oldest safe xid follows snapshot's xmin”.

- During initial synchronization of a logical replication subscription, commit the addition of a pg_replication_origin entry before starting to copy data (Zhijie Hou) [](https://postgr.es/c/e063ccc72)

  Previously, if the copy step failed, the new pg_replication_origin entry would be lost due to transaction rollback. This led to inconsistent state in shared memory.

- Don't advance logical replication progress after a parallel worker apply failure (Zhijie Hou) [](https://postgr.es/c/0ed8f1afb)

  The previous behavior allowed transactions to be lost by a subscriber.

- Fix logical replication slotsync worker processes to handle LOCK_TIMEOUT signals correctly (Zhijie Hou) [](https://postgr.es/c/f2818868a)

  Previously, timeout signals were effectively ignored.

- Fix possible failure with “unexpected data beyond EOF” during restart of a streaming replica server (Anthonin Bonnefoy) [](https://postgr.es/c/c3770181c)

- Fix error reporting for SQL/JSON path type mismatches (Jian He) [](https://postgr.es/c/b5511fed5)

  The code could produce a “cache lookup failed for type 0” error instead of the intended complaint about the path expression not being of the right type.

- Fix erroneous tracking of column position when parsing partition range bounds (myzhen) [](https://postgr.es/c/84b787ae6)

  This could, for example, lead to the wrong column name being cited in error messages about casting partition bound values to the column's data type.

- Fix assorted minor errors in error messages (Man Zeng, Tianchen Zhang) [](https://postgr.es/c/67ad4387b) [](https://postgr.es/c/263af458e) [](https://postgr.es/c/5995135f1) [](https://postgr.es/c/05ef2371a) [](https://postgr.es/c/5449fd261)

  For example, an error report about mismatched timeline number in a backup manifest showed the starting timeline number where it meant to show the ending timeline number.

- Fix failure to perform function inlining when doing JIT compilation with LLVM version 17 or later (Anthonin Bonnefoy) [](https://postgr.es/c/d0bb0e5b3)

- Adjust our JIT code to work with LLVM 21 (Holger Hoffstätte) [](https://postgr.es/c/60215eae7)

  The previous coding failed to compile on aarch64 machines.

- Add new server parameter [???](#guc-file-extend-method) to control use of `posix_fallocate()` (Thomas Munro) [](https://postgr.es/c/4dac22aa1)

  PostgreSQL version 16 and later will use `posix_fallocate()`, if the platform provides it, to extend relation files. However, this has been reported to interact poorly with some file systems: BTRFS compression is disabled by the use of `posix_fallocate()`, and XFS could produce spurious `ENOSPC` errors in older Linux kernel versions. To provide a workaround, introduce this new server parameter. Setting `file_extend_method` to `write_zeros` will cause the server to return to the old method of extending files by writing blocks of zeroes.

- Honor `open()`'s `O_CLOEXEC` flag on Windows (Bryan Green, Thomas Munro) [](https://postgr.es/c/f24af0e04) [](https://postgr.es/c/045185913) [](https://postgr.es/c/b3c8119e2)

  Make this flag work like it does on POSIX platforms, so that we don't leak file handles into child processes such as `COPY TO/FROM PROGRAM`. While that leakage hasn't caused many problems, it seems undesirable.

- Fix failure to parse long options on the server command line in Solaris executables built with meson (Tom Lane) [](https://postgr.es/c/59c2f7efa)

- Support process title changes on GNU/Hurd (Michael Banck) [](https://postgr.es/c/d66a922f9)

- Avoid pg_dump assertion failure in binary-upgrade mode (Vignesh C) [](https://postgr.es/c/1cdc07ad5)

  Failure to handle subscription-relation objects in the object sorting code triggered an assertion, though there were no serious ill effects in production builds.

- Fix incorrect error handling in pgbench with multiple `\syncpipeline` commands in pipeline mode (Yugo Nagata) [](https://postgr.es/c/5bc251b28)

  If multiple `\syncpipeline` commands are encountered after a query error, pgbench would report “failed to exit pipeline mode”, or get an assertion failure in an assert-enabled build.

- Make pg_resetwal print the updated value when changing OldestXID (Heikki Linnakangas) [](https://postgr.es/c/f2e0ca0af)

  It already did that for every other variable it can change.

- Make pg_resetwal allow setting next multixact xid to 0 or next multixact offset to UINT32_MAX (Maxim Orlov) [](https://postgr.es/c/cb2ef0e92)

  These are valid values, so rejecting them was incorrect. In the worst case, if a pg_upgrade is attempted when exactly at the point of multixact wraparound, the upgrade would fail.

- In `contrib/amcheck`, use the correct snapshot for btree index parent checks (Mihail Nikalayeu) [](https://postgr.es/c/ce2f575b7) [](https://postgr.es/c/e1a327dc4)

  The previous coding caused spurious errors when examining indexes created with `CREATE INDEX CONCURRENTLY`.

- Fix `contrib/amcheck` to handle “half-dead” btree index pages correctly (Heikki Linnakangas) [](https://postgr.es/c/e8ae59445)

  `amcheck` expected such a page to have a parent downlink, but it does not, leading to a false error report about “mismatch between parent key and child high key”.

- Fix `contrib/amcheck` to handle incomplete btree root page splits correctly (Heikki Linnakangas) [](https://postgr.es/c/5a2d1df00)

  `amcheck` could report a false error about “block is not true root”.

- Fix edge-case integer overflow in `contrib/intarray`'s selectivity estimator for `@@` (Chao Li) [](https://postgr.es/c/a5f2dc421)

  This could cause poor selectivity estimates to be produced for cases involving the maximum integer value.

- Fix multibyte-encoding issue in `contrib/ltree` (Jeff Davis) [](https://postgr.es/c/b8cfe9dc2)

  The previous coding could pass an incomplete multibyte character to `lower()`, probably resulting in incorrect behavior.

- Update time zone data files to tzdata release 2025c (Tom Lane) [](https://postgr.es/c/f87c0b84e)

  The only change is in historical data for pre-1976 timestamps in Baja California.

## Release 17.7

Release date:

2025-11-13

This release contains a variety of fixes from 17.6. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.7

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.6, see [Release 17.6](#release-17-6).

## Changes

- Check for `CREATE` privileges on the schema in `CREATE STATISTICS` (Jelte Fennema-Nio) [](https://postgr.es/c/e2fb3dfa8)

  This omission allowed table owners to create statistics in any schema, potentially leading to unexpected naming conflicts.

  The PostgreSQL Project thanks Jelte Fennema-Nio for reporting this problem. (CVE-2025-12817)

- Avoid integer overflow in allocation-size calculations within libpq (Jacob Champion) [](https://postgr.es/c/f5999f018)

  Several places in libpq were not sufficiently careful about computing the required size of a memory allocation. Sufficiently large inputs could cause integer overflow, resulting in an undersized buffer, which would then lead to writing past the end of the buffer.

  The PostgreSQL Project thanks Aleksey Solovev of Positive Technologies for reporting this problem. (CVE-2025-12818)

- Prevent “unrecognized node type” errors when a SQL/JSON function such as `JSON_VALUE` has a `DEFAULT` clause containing a `COLLATE` expression (Jian He) [](https://postgr.es/c/09f86a42f) [](https://postgr.es/c/1e6dfdaa0)

- Correctly treat JSON constructor expressions, such as `JSON_OBJECT()`, as non-strict (Tender Wang, Richard Guo) [](https://postgr.es/c/d719e2ecb)

  In some cases these expressions can yield a non-null result despite having one or more null inputs, making them non-strict. The planner incorrectly classified them as strict and could perform incorrect query transformations as a result.

- Further fix processing of character classes within `SIMILAR TO` regular expressions (Laurenz Albe) [](https://postgr.es/c/e09adb5b9)

  The previous fix for translating `SIMILAR TO` pattern matching expressions to POSIX-style regular expressions broke a corner case that formerly worked: if there is an escape character right after the opening bracket and then a closing bracket right after the escape sequence (for example `[\w]`), the closing bracket was no longer seen as terminating the character class.

- Fix parsing of aggregate functions whose arguments contain a sub-select with a `FROM` reference to a CTE outside the aggregate function (Tom Lane) [](https://postgr.es/c/e830896c1)

  Such a CTE reference must act like a outer-level column reference when determining the aggregate's semantic level; but it was not being accounted for, leading to obscure planner or executor errors.

- Fix “no relation entry for relid” errors in corner cases while estimating SubPlan costs (Richard Guo) [](https://postgr.es/c/f34202f51)

- Avoid unlikely use-after-free in planner's expansion of partitioned tables (Bernd Reiß) [](https://postgr.es/c/ed394c4bd)

  There was a hazard only when the last live partition was concurrently dropped.

- Remove faulty assertion in btree index cleanup (Peter Geoghegan) [](https://postgr.es/c/ae15cebc2)

- Fix possible infinite loop in GIN index scans with multiple scan conditions (Tom Lane) [](https://postgr.es/c/456c6a05d)

  GIN can handle scan conditions that can reject non-matching entries but are not useful for searching for relevant entries, for example a `tsquery` clause like `!term`. But such a condition must not be first in the array of scan conditions. The code failed to ensure that in all cases, with the result that a query having a mix of such conditions with normal conditions might work or not depending on the order in which the conditions were given in the query.

- Ensure that GIN index scans can be canceled (Tom Lane) [](https://postgr.es/c/d17abaea8)

  Some code paths were capable of running for a long time without checking for interrupts.

- Ensure that BRIN autosummarization provides a snapshot for index expressions that need one (Álvaro Herrera) [](https://postgr.es/c/f4b68b033) [](https://postgr.es/c/3b5007347)

  Previously, autosummarization would fail for such indexes, and then leave placeholder index tuples behind, causing the index to bloat over time.

- Fix integer-overflow hazard in BRIN index scans when the table contains close to 2<sup>32</sup> pages (Sunil S) [](https://postgr.es/c/c4f5a59ab)

  This oversight could result in an infinite loop or scanning of unneeded table pages.

- Fix incorrect zero-extension of stored values in JIT-generated tuple deforming code (David Rowley) [](https://postgr.es/c/10945148e)

  When not using JIT, the equivalent code does sign-extension not zero-extension, leading to a different Datum representation of small integer data types. This inconsistency was masked in most cases, but it is known to lead to “could not find memoization table entry” errors when using Memoize plan nodes, and there might be other symptoms.

- Fix incorrect logic for caching result-relation information for triggers (David Rowley, Amit Langote) [](https://postgr.es/c/0d3074615)

  In cases where partitions' column sets aren't physically identical to their parent partitioned tables' column sets, this oversight could lead to crashes.

- Add missing EvalPlanQual rechecks for TID Scan and TID Range Scan plan nodes (Sophie Alpert, David Rowley) [](https://postgr.es/c/0fb06e893) [](https://postgr.es/c/3d939a9b1)

  This omission led to possibly not rechecking a condition on ctid during concurrent-update situations, causing the update's behavior to vary depending on which plan type had been selected.

- Fix EvalPlanQual handling of foreign or custom joins that do not have an alternative local-join plan prepared for EPQ (Masahiko Sawada, Etsuro Fujita) [](https://postgr.es/c/2bb84ea7e)

  In such cases the foreign or custom access method should be invoked normally, but that did not happen, typically leading to a crash.

- Avoid duplicating hash partition constraints during `DETACH CONCURRENTLY` (Haiyang Li) [](https://postgr.es/c/ea06f97ee)

  `ALTER TABLE DETACH PARTITION CONCURRENTLY` was written to add a copy of the partitioning constraint to the now-detached partition. This was misguided, partially because non-concurrent `DETACH` doesn't do that, but mostly because in the case of hash partitioning the constraint expression contains references to the parent table's OID. That causes problems during dump/restore, or if the parent table is dropped after `DETACH`. In v19 and later, we'll no longer create any such copied constraints at all. In released branches, to minimize the risk of unforeseen consequences, only skip adding a copied constraint if it is for hash partitioning.

- Disallow generated columns in partition keys (Jian He, Ashutosh Bapat) [](https://postgr.es/c/0b44f2443)

  This was already not allowed, but the check missed some cases, such as where the column reference is implicit in a whole-row reference.

- Disallow generated columns in `COPY ... FROM ... WHERE` clauses (Peter Eisentraut, Jian He) [](https://postgr.es/c/07f787e57)

  Previously, incorrect behavior or an obscure error message resulted from attempting to reference such a column, since generated columns have not yet been computed at the point where `WHERE` filtering is done.

- Avoid potential use-after-free in parallel vacuum (Kevin Oommen Anish) [](https://postgr.es/c/3549ffb6a)

  This bug seems to have no consequences in standard builds, but it's theoretically a hazard.

- Fix visibility checking for statistics objects in `pg_temp` (Noah Misch) [](https://postgr.es/c/6778fbca6)

  A statistics object located in a temporary schema cannot be named without schema qualification, but `pg_statistics_obj_is_visible()` missed that memo and could return “true” regardless. In turn, functions such as `pg_describe_object()` could fail to schema-qualify the object's name as expected.

- Fix `pg_event_trigger_dropped_objects()`'s reporting of temporary status (Antoine Violin, Tom Lane) [](https://postgr.es/c/c0c8ee23c) [](https://postgr.es/c/a220e40d1)

  If a dropped column default, trigger, or RLS policy belongs to a temporary table, report it with `is_temporary` true.

- Fix memory leakage in hashed subplans (Haiyang Li) [](https://postgr.es/c/862980f92)

  Any memory consumed by the hash functions used for hashing tuples constituted a query-lifespan memory leak. One way that could happen is if the values being hashed require de-toasting.

- Avoid leaking SMgrRelation objects in the startup process (Jingtang Zhang) [](https://postgr.es/c/e2dd7b2ac)

  In a long-running standby server, the hashtable holding these objects could bloat substantially, because there was no mechanism for freeing no-longer-interesting entries.

- Fix minor memory leak during WAL replay of database creation (Nathan Bossart) [](https://postgr.es/c/f9993ac64)

- Fix corruption of the shared statistics table after out-of-memory failures (Mikhail Kot) [](https://postgr.es/c/3e6dfcfb0)

  Previously, an out-of-memory failure partway through creating a new hash table entry left a broken entry behind, potentially causing errors in other sessions later.

- Fix concurrent update issue in `MERGE` (Yugo Nagata) [](https://postgr.es/c/6195afbe5)

  When executing a `MERGE UPDATE` action, if there is more than one concurrent update of the target row, the lock-and-retry code would sometimes incorrectly identify the latest version of the target tuple, leading to incorrect results.

- Add missing replica identity checks in `MERGE` and `INSERT ... ON CONFLICT DO UPDATE` (Zhijie Hou) [](https://postgr.es/c/76f45be93) [](https://postgr.es/c/0b934d399) [](https://postgr.es/c/57dfb64ec)

  If `MERGE` may require update or delete actions, and the target table publishes updates or deletes, insist that it have a `REPLICA IDENTITY` defined. Failing to require this can silently break replication. Likewise, `INSERT` with an `UPDATE` option must require `REPLICA IDENTITY` if the target table publishes either inserts or updates.

- Avoid deadlock during `DROP SUBSCRIPTION` when publisher is on the same server as subscriber (Dilip Kumar) [](https://postgr.es/c/288a817bc)

- Fix incorrect reporting of replication lag in pg_stat_replication view (Fujii Masao) [](https://postgr.es/c/62d5ee75b)

  If any standby server's replay LSN stopped advancing, the write_lag and flush_lag columns would eventually stop updating.

- Avoid duplicative log messages about invalid `primary_slot_name` settings (Fujii Masao) [](https://postgr.es/c/1db2870bb)

- Avoid failures when `synchronized_standby_slots` references nonexistent replication slots (Shlok Kyal) [](https://postgr.es/c/0024f5a10)

- Remove the unfinished slot state file after failing to write a replication slot's state to disk (Michael Paquier) [](https://postgr.es/c/42348839d)

  Previously, a failure such as out-of-disk-space resulted in leaving a temporary `state.tmp` file behind. That's problematic because it would block all subsequent attempts to write the state, requiring manual intervention to clean up.

- Fix mishandling of lock timeout signals in parallel apply workers for logical replication (Hayato Kuroda) [](https://postgr.es/c/2f6e1a490)

  The same signal number was being used for both worker shutdown and lock timeout, leading to confusion.

- Avoid unwanted WAL receiver shutdown when switching from streaming to archive WAL source (Xuneng Zhou) [](https://postgr.es/c/e7340b484)

  During a timeline change, a standby server's WAL receiver should remain alive, waiting for a new WAL streaming start point. Instead it was repeatedly shutting down and immediately getting restarted, which could confuse status monitoring code.

- Avoid failures in logical replication due to chance collisions of file numbers between regular and temporary tables (Vignesh C) [](https://postgr.es/c/dcdc95cb4)

  This low-probability problem manifested as transient errors like “unexpected duplicate for tablespace \<X\>, relfilenode \<Y\>”. `contrib/autoprewarm` was also affected. A side-effect of the fix is that the SQL function `pg_filenode_relation()` will now ignore temporary tables.

- Fix use-after-free issue in the relation synchronization cache maintained by the pgoutput logical decoding plugin (Vignesh C, Masahiko Sawada) [](https://postgr.es/c/a61592253)

  An error during logical decoding could result in crashes in subsequent logical decoding attempts in the same session. The case is only reachable when pgoutput is invoked via SQL functions.

- Avoid unnecessary invalidation of logical replication slots (Bertrand Drouvot) [](https://postgr.es/c/f3fb6bc9f)

- Avoid assertion failure when trying to release a replication slot in single-user mode (Hayato Kuroda) [](https://postgr.es/c/07a302387)

- Fix incorrect printing of messages about failures in checking whether the user has Windows administrator privilege (Bryan Green) [](https://postgr.es/c/4c53519e1)

  This code would have crashed or at least printed garbage. No such cases have been reported though, indicating that failure of these system calls is extremely rare.

- Avoid startup failure on macOS and BSD platforms when there is a collision with a pre-existing semaphore set (Tom Lane) [](https://postgr.es/c/ab92f0e7f)

  If the pre-existing set has fewer semaphores than we asked for, these platforms return `EINVAL` not `EEXIST` as our code expected, resulting in failure to start the database.

- Avoid crash when attempting to test PostgreSQL with certain libsanitizer options (Emmanuel Sibi, Jacob Champion) [](https://postgr.es/c/a9515f294)

- Fix false memory-context-checking warnings in debug builds on 64-bit Windows (David Rowley) [](https://postgr.es/c/bd6f986c9)

- Correctly handle `GROUP BY DISTINCT` in PL/pgSQL assignment statements (Tom Lane) [](https://postgr.es/c/3fc9aa5b0)

  The parser failed to record the `DISTINCT` option in this context, so that the command would act as if it were plain `GROUP BY`.

- Avoid leaking memory when handling a SQL error within PL/Python (Tom Lane) [](https://postgr.es/c/fbc41a145)

  This fixes a session-lifespan memory leak introduced in our previous minor releases.

- Fix libpq's trace output of characters with the high bit set (Ran Benita) [](https://postgr.es/c/0fedb3a27)

  On platforms where `char` is considered signed, the output included unsightly `\xffffff` decoration.

- Fix libpq's handling of socket-related errors on Windows within its GSSAPI logic (Ning Wu, Tom Lane) [](https://postgr.es/c/1c4671f7b)

  The code for encrypting/decrypting transmitted data using GSSAPI did not correctly recognize error conditions on the connection socket, since Windows reports those differently than other platforms. This led to failure to make such connections on Windows.

- Fix dumping of non-inherited not-null constraints on inherited table columns (Dilip Kumar) [](https://postgr.es/c/c945b06d5)

  pg_dump failed to preserve such constraints when dumping from a pre-v18 server.

- In pg_dump, dump security labels on subscriptions and event triggers (Jian He, Fujii Masao) [](https://postgr.es/c/968141898)

  Labels on these types of objects were previously missed.

- Fix pg_dump's sorting of default ACLs and foreign key constraints (Kirill Reshke, Álvaro Herrera) [](https://postgr.es/c/e8d22095e) [](https://postgr.es/c/49a09c6c5) [](https://postgr.es/c/7419c99a2)

  Ensure consistent ordering of these database object types, as was already done for other object types.

- In pg_dump, label comments for separately-dumped domain constraints with the proper dependency (Noah Misch) [](https://postgr.es/c/e127764b6)

  This error could lead to parallel pg_restore attempting to create the comment before the constraint itself has been restored.

- In pg_restore, skip comments and security labels for publications and subscriptions that are not being restored (Jian He, Fujii Masao) [](https://postgr.es/c/f7f9c5d65) [](https://postgr.es/c/dc8aa2f58)

  Do not emit `COMMENT` or `SECURITY LABEL` commands for these objects when `--no-publications` or `--no-subscriptions` is specified.

- Fix assorted errors in the data compression logic in pg_dump and pg_restore (Daniel Gustafsson, Tom Lane) [](https://postgr.es/c/92268b35d) [](https://postgr.es/c/bf18e9bd7) [](https://postgr.es/c/2efca1633)

  Error checking was missing or incorrect in several places, and there were also portability issues that would manifest on big-endian hardware. These problems had been missed because this code is only used to read compressed TOC files within directory-format dumps. pg_dump never produces such a dump; the case can be reached only by manually compressing the TOC file after the fact, which is a supported thing to do but very uncommon.

- Fix pgbench to error out cleanly if a `COPY` operation is started (Anthonin Bonnefoy) [](https://postgr.es/c/de6de069d)

  pgbench doesn't intend to support this case, but previously it went into an infinite loop.

- Fix pgbench's reporting of multiple errors (Yugo Nagata) [](https://postgr.es/c/a912118c6)

  In cases where two successive `PQgetResult` calls both fail, pgbench might report the wrong error message.

- In pgbench, fix faulty assertion about errors in pipeline mode (Yugo Nagata) [](https://postgr.es/c/f39d9164b)

- Fix per-file memory leakage in pg_combinebackup (Tom Lane) [](https://postgr.es/c/4eb6992af)

- Ensure that `contrib/pg_buffercache` functions can be canceled (Satyanarayana Narlapuram, Yuhang Qiu) [](https://postgr.es/c/b6090ed96)

  Some code paths were capable of running for a long time without checking for interrupts.

- Fix `contrib/pg_prewarm`'s privilege checks for indexes (Ayush Vatsa, Nathan Bossart) [](https://postgr.es/c/a0551bc57) [](https://postgr.es/c/d4e8c37cc)

  `pg_prewarm()` requires `SELECT` privilege on relations to be prewarmed. However, since indexes have no SQL privileges of their own, this resulted in non-superusers being unable to prewarm indexes. Instead, check for `SELECT` privilege on the index's table.

- Make `contrib/pgstattuple` more robust about empty or invalid index pages (Nitin Motiani) [](https://postgr.es/c/036decbba)

  Count all-zero pages as free space, and ignore pages that are invalid according to a check of the page's special-space size. The code for btree indexes already counted all-zero pages as free, but the hash and gist code would error out, which has been found to be much less user-friendly. Similarly, make all three cases agree on ignoring corrupted pages rather than throwing errors.

- Harden our read and write barrier macros to satisfy Clang (Thomas Munro) [](https://postgr.es/c/03d9140cb)

  We supposed that `__atomic_thread_fence()` is a sufficient barrier to prevent the C compiler from re-ordering memory accesses around it, but it appears that that's not true for Clang, allowing it to generate incorrect code for at least RISC-V, MIPS, and LoongArch machines. Add explicit compiler barriers to fix that.

- Fix building with LLVM version 21 and later (Holger Hoffstätte) [](https://postgr.es/c/755f01ad7)

- When building with meson, apply the same special optimization flags for `numeric.c` and `checksum.c` as the makefile build does (Nathan Bossart, Jeff Davis) [](https://postgr.es/c/15f9eeef6) [](https://postgr.es/c/e25453a36)

  Use `-ftree-vectorize` for both files, as well as `-funroll-loops` for `checksum.c`, to match what the makefiles have long done.

- Fix PGXS build infrastructure to support building NLS `po` files for extensions (Ryo Matsumura) [](https://postgr.es/c/a8933194e)

## Release 17.6

Release date:

2025-08-14

This release contains a variety of fixes from 17.5. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.6

A dump/restore is not required for those running 17.X.

However, if you have any BRIN `numeric_minmax_multi_ops` indexes, it is advisable to reindex them after updating. See the fourth changelog entry below.

Also, if you are upgrading from a version earlier than 17.5, see [Release 17.5](#release-17-5).

## Changes

- Tighten security checks in planner estimation functions (Dean Rasheed) [](https://postgr.es/c/a85eddab2)

  The fix for CVE-2017-7484, plus followup fixes, intended to prevent leaky functions from being applied to statistics data for columns that the calling user does not have permission to read. Two gaps in that protection have been found. One gap applies to partitioning and inheritance hierarchies where RLS policies on the tables should restrict access to statistics data, but did not.

  The other gap applies to cases where the query accesses a table via a view, and the view owner has permissions to read the underlying table but the calling user does not have permissions on the view. The view owner's permissions satisfied the security checks, and the leaky function would get applied to the underlying table's statistics before we check the calling user's permissions on the view. This has been fixed by making security checks on views occur at the start of planning. That might cause permissions failures to occur earlier than before.

  The PostgreSQL Project thanks Dean Rasheed for reporting this problem. (CVE-2025-8713)

- Prevent pg_dump scripts from being used to attack the user running the restore (Nathan Bossart) [](https://postgr.es/c/575f54d4c)

  Since dump/restore operations typically involve running SQL commands as superuser, the target database installation must trust the source server. However, it does not follow that the operating system user who executes psql to perform the restore should have to trust the source server. The risk here is that an attacker who has gained superuser-level control over the source server might be able to cause it to emit text that would be interpreted as psql meta-commands. That would provide shell-level access to the restoring user's own account, independently of access to the target database.

  To provide a positive guarantee that this can't happen, extend psql with a `\restrict` command that prevents execution of further meta-commands, and teach pg_dump to issue that before any data coming from the source server.

  The PostgreSQL Project thanks Martin Rakhmanov, Matthieu Denais, and RyotaK for reporting this problem. (CVE-2025-8714)

- Convert newlines to spaces in names included in comments in pg_dump output (Noah Misch) [](https://postgr.es/c/9b92f115b)

  Object names containing newlines offered the ability to inject arbitrary SQL commands into the output script. (Without the preceding fix, injection of psql meta-commands would also be possible this way.) CVE-2012-0868 fixed this class of problem at the time, but later work reintroduced several cases.

  The PostgreSQL Project thanks Noah Misch for reporting this problem. (CVE-2025-8715)

- Fix incorrect distance calculation in BRIN `numeric_minmax_multi_ops` support function (Peter Eisentraut, Tom Lane) [](https://postgr.es/c/0b0d3c19b)

  The results were sometimes wrong on 64-bit platforms, and wildly wrong on 32-bit platforms. This did not produce obvious failures because the logic is only used to choose how to merge values into ranges; at worst the index would become inefficient and bloated. Nonetheless it's recommended to reindex any BRIN indexes that use the `numeric_minmax_multi_ops` operator class.

- Avoid regression in the size of XML input that we will accept (Michael Paquier, Erik Wienhold) [](https://postgr.es/c/fd4ad33fe) [](https://postgr.es/c/7571e0f6e)

  Our workaround for a bug in early 2.13.x releases of libxml2 made use of a code path that rejects text chunks exceeding 10MB, whereas the previous coding did not. Those early releases are presumably extinct in the wild by now, so revert to the previous coding.

- Fix `MERGE` problems with concurrent updates (Dean Rasheed) [](https://postgr.es/c/91ad1bdef)

  If a `MERGE` inside a CTE attempts an update or delete on a table with `BEFORE ROW` triggers, and a concurrent `UPDATE` or `DELETE` changes the target row, the `MERGE` command would fail (crashing in the case of an update action, and potentially executing the wrong action in the case of a delete action).

- Fix `MERGE` into a plain-inheritance parent table (Dean Rasheed) [](https://postgr.es/c/ab52f6b5b)

  Insertions into such a target table could crash or produce incorrect query results due to failing to handle `WITH CHECK OPTION` and `RETURNING` actions.

- Allow tables with statement-level triggers to become partitions or inheritance children (Etsuro Fujita) [](https://postgr.es/c/e028ce911)

  We do not allow partitions or inheritance child tables to have row-level triggers with transition tables, because an operation on the whole inheritance tree would need to maintain a separate transition table for each such child table. But that problem does not apply for statement-level triggers, because only the parent's statement-level triggers will be fired. The code that checks whether an existing table can become a partition or inheritance child nonetheless rejected both kinds of trigger.

- Disallow collecting transition tuples from child foreign tables (Etsuro Fujita) [](https://postgr.es/c/9048a83c7)

  We do not support triggers with transition tables on foreign tables. However, the case of a partition or inheritance child that is a foreign table was overlooked. If the parent has such a trigger, incorrect transition tuples were collected from the foreign child. Instead throw an error, reporting that the case is not supported.

- Allow resetting unknown custom parameters with reserved prefixes (Nathan Bossart) [](https://postgr.es/c/39ff05636)

  Previously, if a parameter setting had been stored using `ALTER DATABASE/ROLE/SYSTEM`, the stored setting could not be removed if the parameter was unknown but had a reserved prefix. This case could arise if an extension used to have a parameter, but that parameter had been removed in an upgrade.

- Fix a potential deadlock during `ALTER SUBSCRIPTION ... DROP PUBLICATION` (Ajin Cherian) [](https://postgr.es/c/8c298324a)

  Ensure that server processes acquire catalog locks in a consistent order during replication origin drops.

- Shorten the race condition window for creating indexes with conflicting names (Tom Lane) [](https://postgr.es/c/fdd826922)

  When choosing an auto-generated name for an index, avoid conflicting with not-yet-committed pg_class rows as well as fully-valid ones. This avoids possibly choosing the same name as some concurrent `CREATE INDEX` did, when that command is still in process of filling its index, or is done but is part of a not-yet-committed transaction. There's still a window for trouble, but it's only as long as the time needed to validate a new index's parameters and insert its pg_class row.

- Prevent usage of incorrect `VACUUM` options in some cases where multiple tables are vacuumed in a single command (Nathan Bossart, Michael Paquier) [](https://postgr.es/c/2e0b5d252)

  The `TRUNCATE` and `INDEX_CLEANUP` options of one table could be applied to others.

- Ensure that the table's free-space map is updated in a timely way when vacuuming a table that has no indexes (Masahiko Sawada) [](https://postgr.es/c/792238c8b)

  A previous optimization caused FSM vacuuming to sometimes be skipped for such tables.

- Fix processing of character classes within `SIMILAR TO` regular expressions (Laurenz Albe) [](https://postgr.es/c/e3ffc3e91) [](https://postgr.es/c/a3c6d92f3)

  The code that translates `SIMILAR TO` pattern matching expressions to POSIX-style regular expressions did not consider that square brackets can be nested. For example, in a pattern like `[[:alpha:]%_]`, the code treated the `%` and `_` characters as metacharacters when they should be literals.

- When deparsing queries, always add parentheses around the expression in `FETCH FIRST expression ROWS WITH TIES` clauses (Heikki Linnakangas) [](https://postgr.es/c/54c05292b) [](https://postgr.es/c/a4da7b0cf)

  This avoids some cases where the deparsed result wasn't syntactically valid.

- Limit the checkpointer process's fsync request queue size (Alexander Korotkov, Xuneng Zhou) [](https://postgr.es/c/13559de95) [](https://postgr.es/c/605890034)

  With very large `shared_buffers` settings, it was possible for the checkpointer to attempt to allocate more than 1GB for fsync requests, leading to failure and an infinite loop. Clamp the queue size to prevent this scenario.

- Avoid infinite wait in logical decoding when reading a partially-written WAL record (Vignesh C) [](https://postgr.es/c/c9f4e7520)

  If the server crashes after writing the first part of a WAL record that would span multiple pages, subsequent logical decoding of the WAL stream would wait for data to arrive on the next WAL page. That might never happen if the server is now idle.

- Fix inconsistent spelling of LWLock names for `MultiXactOffsetSLRU` and `MultiXactMemberSLRU` (Bertrand Drouvot) [](https://postgr.es/c/b3abec0ad)

  This resulted in different wait-event names being displayed in pg_wait_events and pg_stat_activity, potentially breaking monitoring queries that join those views.

- Fix inconsistent quoting of role names in ACL strings (Tom Lane) [](https://postgr.es/c/50959f96e)

  The previous quoting rule was locale-sensitive, which could lead to portability problems when transferring `aclitem` values across installations. (pg_dump does not do that, but other tools might.) To ensure consistency, always quote non-ASCII characters in `aclitem` output; but to preserve backward compatibility, never require that they be quoted during `aclitem` input.

- Reject equal signs (`=`) in the names of relation options and foreign-data options (Tom Lane) [](https://postgr.es/c/d4046125d)

  There's no evident use-case for option names like this, and allowing them creates ambiguity in the stored representation.

- Fix potentially-incorrect decompression of LZ4-compressed archive data (Mikhail Gribkov) [](https://postgr.es/c/074003431)

  This error seems to manifest only with not-very-compressible input data, which may explain why it escaped detection.

- Avoid a rare scenario where a btree index scan could mark the wrong index entries as dead (Peter Geoghegan) [](https://postgr.es/c/40aa5ddea)

- Avoid re-distributing cache invalidation messages from other transactions during logical replication (vignesh C) [](https://postgr.es/c/45c357e0e)

  Our previous round of minor releases included a bug fix to ensure that replication receiver processes would respond to cross-process cache invalidation messages, preventing them from using stale catalog data while performing replication updates. However, the fix unintentionally made them also redistribute those messages again, leading to an exponential increase in the number of invalidation messages, which would often end in a memory allocation failure. Fix by not redistributing received messages.

- Avoid unexpected server shutdown when replication slot synchronization is misconfigured (Fujii Masao) [](https://postgr.es/c/f71fa981c)

  The postmaster process would report an error (and then stop) if `sync_replication_slots` was set to `true` while `wal_level` was less than `logical`. The desired behavior is just that slot synchronization should be disabled, so reduce this error message's level to avoid postmaster shutdown.

- Avoid premature removal of old WAL during checkpoints (Vitaly Davydov) [](https://postgr.es/c/2090edc6f)

  If a replication slot's restart point is advanced while a checkpoint is in progress, no-longer-needed WAL segments could get removed too soon, leading to recovery failure if the database crashes immediately afterwards. Fix by keeping them for one additional checkpoint cycle.

- Never move a replication slot's confirmed-flush position backwards (Shveta Malik) [](https://postgr.es/c/7318f241d)

  In some cases a replication client could acknowledge an LSN that's past what it has stored persistently, and then perhaps send an older LSN after a restart. We consider this not-a-bug so long as the client did not have anything it needed to do for the WAL between the two points. However, we should not re-send that WAL for fear of data duplication, so make sure we always believe the latest confirmed LSN for a given slot.

- Prevent excessive delays before launching new logical replication workers (Tom Lane) [](https://postgr.es/c/9f33300e6)

  In some cases the logical replication launcher could sleep considerably longer than the configured `wal_retrieve_retry_interval` before launching a new worker.

- Fix use-after-free during logical replication of `INSERT ... ON CONFLICT` (Ethan Mertz, Michael Paquier) [](https://postgr.es/c/9e0b4b1ab)

  This could result in incorrect progress reporting, or with very bad luck it could result in a crash of the WAL sender process.

- Allow waiting for a transaction on a standby server to be interrupted (Kevin K Biju) [](https://postgr.es/c/24c5ad5be)

  Creation of a replication slot on a standby server may require waiting for some active transaction(s) to finish on the primary and then be replayed on the standby. Since that could be an indefinite wait, it's desirable to allow the operation to be cancelled, but there was no check for query cancel in the loop.

- Do not let cascading logical WAL senders try to send data that's beyond what has been replayed on their standby server (Alexey Makhmutov) [](https://postgr.es/c/87be749c7)

  This avoids a situation where such WAL senders could get stuck at standby server shutdown, waiting for replay work that will not happen because the server's startup process is already shut down.

- Fix per-relation memory leakage in autovacuum (Tom Lane) [](https://postgr.es/c/cd3064f98)

- Fix session-lifespan memory leaks in `XMLSERIALIZE(... INDENT)` (Dmitry Kovalenko, Tom Lane) [](https://postgr.es/c/95cf1a181) [](https://postgr.es/c/20bae0690)

- Fix possible crash after out-of-memory when allocating large chunks with the “bump” allocator (Tom Lane) [](https://postgr.es/c/a05cf22e0)

- Fix some places that might try to fetch toasted fields of system catalogs without any snapshot (Nathan Bossart) [](https://postgr.es/c/fe8ea7a2a)

  This could result in an assertion failure or “cannot fetch toast data without an active snapshot” error.

- Avoid assertion failure during cross-table constraint updates (Tom Lane, Jian He) [](https://postgr.es/c/bbfcbc4cd) [](https://postgr.es/c/6d4395b40)

- Remove faulty assertion that a command tag must have been determined by the end of `PortalRunMulti()` (Álvaro Herrera) [](https://postgr.es/c/0c466f5e0)

  This failed in edge cases such as an empty prepared statement.

- Fix assertion failure in `XMLTABLE` parsing (Richard Guo) [](https://postgr.es/c/2f48b4f07)

- Restore the ability to run PL/pgSQL expressions in parallel (Dipesh Dhameliya) [](https://postgr.es/c/a553a2289)

  PL/pgSQL's notion of an “expression” is very broad, encompassing any SQL `SELECT` query that returns a single column and no more than one row. So there are cases, for example evaluation of an aggregate function, where the query involves significant work and it'd be useful to run it with parallel workers. This used to be possible, but a previous bug fix unintentionally disabled it.

- Fix edge-case resource leaks in PL/Python error reporting (Tom Lane) [](https://postgr.es/c/7559a16e2) [](https://postgr.es/c/6f724fcf8)

  An out-of-memory failure while reporting an error from Python could result in failure to drop reference counts on Python objects, leading to session-lifespan memory leakage.

- Fix libpq's `PQcancelCreate()` function for the case where the server's address was specified using `hostaddr` (Sergei Kornilov) [](https://postgr.es/c/445bd37b1)

  libpq would crash if the resulting cancel object was actually used.

- Fix libpq's `PQport()` function to never return NULL unless the passed connection is NULL (Daniele Varrazzo) [](https://postgr.es/c/3f10d2b66)

  This is the documented behavior, but recent libpq versions would return NULL in some cases where the user had not provided a port specification. Revert to our historical behavior of returning an empty string in such cases. (v18 and later will return the compiled-in default port number, typically `"5432"`, instead.)

- Avoid failure when GSSAPI authentication requires packets larger than 16kB (Jacob Champion, Tom Lane) [](https://postgr.es/c/8b0aa7a6b)

  Larger authentication packets are needed for Active Directory users who belong to many AD groups. This limitation manifested in connection failures with unintelligible error messages, typically “GSSAPI context establishment error: The routine must be called again to complete its function: Unknown error”.

- Fix timing-dependent failures in SSL and GSSAPI data transmission (Tom Lane) [](https://postgr.es/c/30e0d9ee9)

  When using SSL or GSSAPI encryption in non-blocking mode, libpq sometimes failed with “SSL error: bad length” or “GSSAPI caller failed to retransmit all data needing to be retried”.

- Avoid null-pointer dereference during connection lookup in ecpg applications (Aleksander Alekseev) [](https://postgr.es/c/2805e1c1e)

  The case could occur only if the application has some connections that are named and some that are not.

- Improve psql's tab completion for `COPY` and `\copy` options (Atsushi Torikoshi) [](https://postgr.es/c/c1c6169eb)

  The same completions were offered for both `COPY FROM` and `COPY TO`, although some options are only valid for one case or the other. Distinguish these cases to provide more accurate suggestions.

- Avoid assertion failure in pgbench when multiple pipeline sync messages are received (Fujii Masao) [](https://postgr.es/c/398e07162)

- Fix duplicate transaction replay when initializing a subscription with pg_createsubscriber (Shlok Kyal) [](https://postgr.es/c/967309116)

  It was possible for the last transaction processed during subscriber recovery to be sent again once normal replication begins.

- Ensure that pg_dump dumps comments on not-null constraints on domain types (Jian He, Álvaro Herrera) [](https://postgr.es/c/6b755d8d7)

- Ensure that pg_dump dumps comments on domain constraints in a valid order (Jian He) [](https://postgr.es/c/d07bc7c2b)

  In some cases the comment command could appear before creation of the constraint.

- Ensure stable sort ordering in pg_dump for all types of database objects (Noah Misch, Andreas Karlsson) [](https://postgr.es/c/1ca1889ea) [](https://postgr.es/c/5dd4957b2) [](https://postgr.es/c/28e7252e4)

  pg_dump sorts objects by their logical names before performing dependency-driven reordering. This sort did not account for the full unique key identifying certain object types such as rules and constraints, and thus it could produce dissimilar sort orders for logically-identical databases. That made it difficult to compare databases by diff'ing pg_dump output, so improve the logic to ensure stable sort ordering in all cases.

- Fix incorrect parsing of object types in pg_dump filter files (Fujii Masao) [](https://postgr.es/c/7dafc4a41)

  Treat keywords as extending to the next whitespace, rather than stopping at the first non-alphanumeric character as before. This makes no difference for valid keywords, but it allows some error cases to be recognized properly. For example, `table-data` will now be rejected, whereas previously it was misinterpreted as `table`.

- pg_restore failed to restore large objects (BLOBs) from directory-format dumps made by pg_dump versions before PostgreSQL v12 (Pavel Stehule) [](https://postgr.es/c/839802792)

- In pg_upgrade, check for inconsistent inherited not-null constraints (Ali Akbar) [](https://postgr.es/c/b8b2e6052) [](https://postgr.es/c/bcb8d47cd) [](https://postgr.es/c/930e1faec)

  PostgreSQL versions before 18 allow an inherited column not-null constraint to be dropped. However, this results in a schema that cannot be restored, leading to failure in pg_upgrade. Detect such cases during pg_upgrade's preflight checks to allow users to fix them before initiating the upgrade.

- Don't require that the target installation have `max_slot_wal_keep_size` set to its default during pg_upgrade (Dilip Kumar) [](https://postgr.es/c/24f6c1bd4)

- Avoid assertion failure if `track_commit_timestamp` is enabled during initdb (Hayato Kuroda, Andy Fan) [](https://postgr.es/c/ae20c105f)

- Fix pg_waldump to show information about dropped statistics in `PREPARE TRANSACTION` WAL records (Daniil Davydov) [](https://postgr.es/c/11efaaffa)

- Avoid possible leak of the open connection during `contrib/dblink` connection establishment (Tom Lane) [](https://postgr.es/c/e20b3256a)

  In the rare scenario where we hit out-of-memory while inserting the new connection object into dblink's hashtable, the open connection would be leaked until end of session, leaving an idle session sitting on the remote server.

- Make `contrib/pg_prewarm` cope with very large `shared_buffers` settings (Daria Shanina) [](https://postgr.es/c/e4b8f925a)

  Autoprewarm failed with a memory allocation error if `shared_buffers` was larger than about 50 million buffers (400GB).

- Prevent assertion failure in `contrib/pg_prewarm` (Masahiro Ikeda) [](https://postgr.es/c/b64c585fd)

  Applying `pg_prewarm()` to a relation lacking storage (such as a view) caused an assertion failure, although there was no ill effect in non-assert builds. Add an error check to reject that case.

- In `contrib/pg_stat_statements`, avoid leaving gaps in the set of parameter numbers used in a normalized query (Sami Imseih) [](https://postgr.es/c/290e8ab32)

- Fix memory leakage in `contrib/postgres_fdw`'s DirectModify methods (Tom Lane) [](https://postgr.es/c/9339c85af)

  The PGresult holding the results of the remote modify command would be leaked for the rest of the session if the query fails between invocations of the DirectModify methods, which could happen when there's `RETURNING` data to process.

- Ensure that directories listed in configure's `--with-includes` and `--with-libraries` options are searched before system-supplied directories (Tom Lane) [](https://postgr.es/c/a644f5fc6)

  A common reason for using these options is to allow a user-built version of some library to override the system-supplied version. However, that failed to work in some environments because of careless ordering of switches in the commands issued by the makefiles.

- Fix configure's checks for `__cpuid()` and `__cpuidex()` (Lukas Fittl, Michael Paquier) [](https://postgr.es/c/8de56323c)

  configure failed to detect these Windows-specific functions, so that they would not be used, leading to slower-than-necessary CRC computations since the availability of hardware instructions could not be verified. The practical impact of this error was limited, because production builds for Windows typically do not use the Autoconf toolchain.

- Fix build failure with `--with-pam` option on Solaris-based platforms (Tom Lane) [](https://postgr.es/c/635a85627)

  Solaris is inconsistent with other Unix platforms about the API for PAM authentication. This manifested as an “inconsistent pointer” compiler warning, which we never did anything about. But as of GCC 14 it's an error not warning by default, so fix it.

- Make our code portable to GNU Hurd (Michael Banck, Christoph Berg, Samuel Thibault) [](https://postgr.es/c/0991249d7) [](https://postgr.es/c/29c54ea7b)

  Fix assumptions about `IOV_MAX` and `O_RDONLY` that don't hold on Hurd.

- Make our usage of `memset_s()` conform strictly to the C11 standard (Tom Lane) [](https://postgr.es/c/5355a2400)

  This avoids compile failures on some platforms.

- Silence compatibility warning when using Meson to build with MSVC (Peter Eisentraut) [](https://postgr.es/c/2499c3490)

- Prevent uninitialized-value compiler warnings in JSONB comparison code (Tom Lane) [](https://postgr.es/c/5a2139a90)

- Avoid deprecation warnings when building with libxml2 2.14 and later (Michael Paquier) [](https://postgr.es/c/c911e7802)

- Avoid problems when compiling `pg_locale.h` under C++ (John Naylor) [](https://postgr.es/c/21ae8fc5f)

  PostgreSQL header files generally need to be wrapped in `extern "C" { ... }` in order to be included in extensions written in C++. This failed for `pg_locale.h` because of its use of libicu headers, but we can work around that by suppressing C++-only declarations in those headers. C++ extensions that want to use libicu's C++ APIs can do so by including the libicu headers ahead of `pg_locale.h`.

## Release 17.5

Release date:

2025-05-08

This release contains a variety of fixes from 17.4. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.5

A dump/restore is not required for those running 17.X.

However, if you have any self-referential foreign key constraints on partitioned tables, it may be necessary to recreate those constraints to ensure that they are being enforced correctly. See the second changelog entry below.

Also, if you have any BRIN bloom indexes, it may be advisable to reindex them after updating. See the third changelog entry below.

Also, if you are upgrading from a version earlier than 17.1, see [Release 17.1](#release-17-1).

## Changes

- Avoid one-byte buffer overread when examining invalidly-encoded strings that are claimed to be in GB18030 encoding (Noah Misch, Andres Freund) [](https://postgr.es/c/ec5f89e8a) [](https://postgr.es/c/617d34908)

  While unlikely, a SIGSEGV crash could occur if an incomplete multibyte character appeared at the end of memory. This was possible both in the server and in libpq-using applications. (CVE-2025-4207)

- Handle self-referential foreign keys on partitioned tables correctly (Álvaro Herrera) [](https://postgr.es/c/f51ae3187)

  Creating or attaching partitions failed to make the required catalog entries for a foreign-key constraint, if the table referenced by the constraint was the same partitioned table. This resulted in failure to enforce the constraint fully.

  To fix this, you should drop and recreate any self-referential foreign keys on partitioned tables, if partitions have been created or attached since the constraint was created. Bear in mind that violating rows might already be present, in which case recreating the constraint will fail, and you'll need to fix up those rows before trying again.

- Avoid data loss when merging compressed BRIN summaries in `brin_bloom_union()` (Tomas Vondra) [](https://postgr.es/c/cb0ad70b8)

  The code failed to account for decompression results not being identical to the input objects, which would result in failure to add some of the data to the merged summary, leading to missed rows in index searches.

  This mistake was present back to v14 where BRIN bloom indexes were introduced, but this code path was only rarely reached then. It's substantially more likely to be hit in v17 because parallel index builds now use the code.

- Fix unexpected “attribute has wrong type” errors in `UPDATE`, `DELETE`, and `MERGE` queries that use whole-row table references to views or functions in `FROM` (Tom Lane) [](https://postgr.es/c/ca0830e5a)

- Fix `MERGE` into a partitioned table with `DO NOTHING` actions (Tender Wang) [](https://postgr.es/c/25303678a)

  Some cases failed with “unknown action in MERGE WHEN clause” errors.

- Prevent failure in `INSERT` commands when the table has a `GENERATED` column of a domain data type and the domain's constraints disallow null values (Jian He) [](https://postgr.es/c/3c39c000c)

  Constraint failure was reported even if the generation expression produced a perfectly okay result.

- Correctly process references to outer CTE names that appear within a `WITH` clause attached to an `INSERT`/`UPDATE`/`DELETE`/`MERGE` command that's inside `WITH` (Tom Lane) [](https://postgr.es/c/5e7be43f4)

  The parser failed to detect disallowed recursion cases, nor did it account for such references when sorting CTEs into a usable order.

- Fix misprocessing of casts within the keys of JSON constructor expressions (Amit Langote) [](https://postgr.es/c/8b2392ae3)

- Don't try to parallelize `array_agg()` when the argument is of an anonymous record type (Richard Guo, Tom Lane) [](https://postgr.es/c/43847dd5e)

  The protocol for communicating with parallel workers doesn't support identifying the concrete record type that a worker is returning.

- Fix `ARRAY(subquery)` and `ARRAY[expression, ...]` constructs to produce sane results when the input is of type `int2vector` or `oidvector` (Tom Lane) [](https://postgr.es/c/c826cd1b1)

  This patch restores the behavior that existed before PostgreSQL 9.5: the result is of type `int2vector[]` or `oidvector[]`.

- Fix possible erroneous reports of invalid affixes while parsing Ispell dictionaries (Jacob Brazeal) [](https://postgr.es/c/99c01aadf)

- Fix `ALTER TABLE ADD COLUMN` to correctly handle the case of a domain type that has a default (Jian He, Tom Lane, Tender Wang) [](https://postgr.es/c/d6dd2a02b) [](https://postgr.es/c/0941aadcd)

  If a domain type has a default, adding a column of that type (without any explicit `DEFAULT` clause) failed to install the domain's default value in existing rows, instead leaving the new column null.

- Repair misbehavior when there are duplicate column names in a foreign key constraint's `ON DELETE SET DEFAULT` or `SET NULL` action (Tom Lane) [](https://postgr.es/c/5e6e97fbf)

- Improve the error message for disallowed attempts to alter the properties of a foreign key constraint (Álvaro Herrera) [](https://postgr.es/c/4e026be5f)

- Avoid error when resetting the relhassubclass flag of a temporary table that's marked `ON COMMIT DELETE ROWS` (Noah Misch) [](https://postgr.es/c/d0a049987)

- Add missing deparsing of the `INDENT` option of `XMLSERIALIZE()` (Jim Jones) [](https://postgr.es/c/2e0f93d7c) [](https://postgr.es/c/310907aaf)

  Previously, views or rules using `XMLSERIALIZE(... INDENT)` were dumped without the `INDENT` clause, causing incorrect results after restore.

- Avoid premature evaluation of the arguments of an aggregate function that has both `FILTER` and `ORDER BY` (or `DISTINCT`) options (David Rowley) [](https://postgr.es/c/065ce49a1)

  If there is `ORDER BY` or `DISTINCT`, we consider pre-sorting the aggregate input values rather than doing the sort within the Agg plan node. But this is problematic if the aggregate inputs include expressions that could fail (for example, a division where some of the input divisors could be zero) and there is a `FILTER` clause that's meant to prevent such failures. Pre-sorting would push the expression evaluations to before the `FILTER` test, allowing the failures to happen anyway. Avoid this by not pre-sorting if there's a `FILTER` and the input expressions are anything more complex than a simple Var or Const.

- Fix erroneous deductions from column `NOT NULL` constraints in the presence of outer joins (Richard Guo) [](https://postgr.es/c/bc5a08af3)

  In some cases the planner would discard an `IS NOT NULL` query condition, even though the condition applies after an outer join and thus is not redundant.

- Avoid incorrect optimizations based on `IS [NOT] NULL` tests that are applied to composite values (Bruce Momjian) [](https://postgr.es/c/b8b1e87b7)

- Fix planner's failure to identify more than one hashable ScalarArrayOpExpr subexpression within a top-level expression (David Geier) [](https://postgr.es/c/5672a8399)

  This resulted in unnecessarily-inefficient execution of any additional subexpressions that could have been processed with a hash table (that is, `IN`, `NOT IN`, or `= ANY` clauses with all-constant right-hand sides).

- Fix incorrect table size estimate with low fill factor (Tomas Vondra) [](https://postgr.es/c/587b6aa3f)

  When the planner estimates the number of rows in a never-yet-analyzed table, it uses the table's fillfactor setting in the estimation, but it neglected to clamp the result to at least one row per page. A low fillfactor could thus result in an unreasonably small estimate.

- Disable “skip fetch” optimization in bitmap heap scan (Matthias van de Meent) [](https://postgr.es/c/78cb2466f)

  It turns out that this optimization can result in returning dead tuples when a concurrent vacuum marks a page all-visible.

- Fix performance issues in GIN index search startup when there are many search keys (Tom Lane, Vinod Sridharan) [](https://postgr.es/c/9094eb25b) [](https://postgr.es/c/8c153fcfa)

  An indexable clause with many keys (for example, `jsonbcol ?| array[...]` with tens of thousands of array elements) took O(N<sup>2</sup>) time to start up, and was uncancelable for that interval too.

- Detect missing support procedures in a BRIN index operator class, and report an error instead of crashing (Álvaro Herrera) [](https://postgr.es/c/ade976f8b)

- Respond to interrupts (such as query cancel) while waiting for asynchronous subplans of an Append plan node (Heikki Linnakangas) [](https://postgr.es/c/e731e9d5e)

  Previously, nothing would happen until one of the subplans becomes ready.

- Report the I/O statistics of active WAL senders more frequently (Bertrand Drouvot) [](https://postgr.es/c/5cbbe70a9)

  Previously, the pg_stat_io view failed to accumulate I/O performed by a WAL sender until that process exited. Now such I/O will be reported after at most one second's delay.

- Fix race condition in handling of `synchronous_standby_names` immediately after startup (Melnikov Maksim, Michael Paquier) [](https://postgr.es/c/3339847cc)

  For a short period after system startup, backends might fail to wait for synchronous commit even though `synchronous_standby_names` is enabled.

- Cope with possible intra-query changes of `io_combine_limit` (Thomas Munro) [](https://postgr.es/c/e27346807)

- Avoid infinite loop if `scram_iterations` is set to `INT_MAX` (Kevin K Biju) [](https://postgr.es/c/34fbfe1f5)

- Avoid possible crashes due to double transformation of `json_array()`'s subquery (Tom Lane) [](https://postgr.es/c/717e8a1e5)

- Fix `pg_strtof()` to not crash with null endptr (Alexander Lakhin, Tom Lane) [](https://postgr.es/c/d69c78108)

- Fix crash after out-of-memory in certain GUC assignments (Daniel Gustafsson) [](https://postgr.es/c/8afec4ef6)

- Avoid crash when a Snowball stemmer encounters an out-of-memory condition (Maksim Korotkov) [](https://postgr.es/c/7edd2cbc5)

- Fix over-enthusiastic freeing of SpecialJoinInfo structs during planning (Richard Guo) [](https://postgr.es/c/727bc6ac3)

  This led to crashes during planning if partitionwise joining is enabled.

- Disallow copying of invalidated replication slots (Shlok Kyal) [](https://postgr.es/c/a4309e85f)

  This prevents trouble when the invalid slot points to WAL that's already been removed.

- Disallow restoring logical replication slots on standby servers that are not in hot-standby mode (Masahiko Sawada) [](https://postgr.es/c/174952ece)

  This prevents a scenario where the slot could remain valid after promotion even if `wal_level` is too low.

- Prevent over-advancement of catalog xmin in “fast forward” mode of logical decoding (Zhijie Hou) [](https://postgr.es/c/36148b22e)

  This mistake could allow deleted catalog entries to be vacuumed away even though they were still potentially needed by the WAL-reading process.

- Avoid data loss when DDL operations that don't take a strong lock affect tables that are being logically replicated (Shlok Kyal, Hayato Kuroda) [](https://postgr.es/c/cadaf0ac4) [](https://postgr.es/c/d96206f25)

  The catalog changes caused by the DDL command were not reflected into WAL-decoding processes, allowing them to decode subsequent changes using stale catalog data, probably resulting in data corruption.

- Prevent incorrect reset of replication origin when an apply worker encounters an error but the error is caught and does not result in worker exit (Hayato Kuroda) [](https://postgr.es/c/05676d87e)

  This mistake could allow duplicate data to be applied.

- Fix crash in logical replication if the subscriber's partitioned table has a BRIN index (Tom Lane) [](https://postgr.es/c/788baa9a2)

- Avoid duplicate snapshot creation in logical replication index lookups (Heikki Linnakangas) [](https://postgr.es/c/c1dd3a944) [](https://postgr.es/c/f1ef111a0)

- Improve detection of mixed-origin subscriptions (Hou Zhijie, Shlok Kyal) [](https://postgr.es/c/0ae1245e0)

  Subscription creation gives a warning if a subscribed-to table is also being followed through other publications, since that could cause duplicate data to be received. This change improves that logic to also detect cases where a partition parent or child table is the one being followed through another publication.

- Fix wrong checkpoint details in error message about incorrect recovery timeline choice (David Steele) [](https://postgr.es/c/29cce279b)

  If the requested recovery timeline is not reachable, the reported checkpoint and timeline should be the values read from the backup_label, if there is one. This message previously reported values from the control file, which is correct when recovering from the control file without a backup_label, but not when there is a backup_label.

- Fix order of operations in `smgropen()` (Andres Freund) [](https://postgr.es/c/ee578921b)

  Ensure that the SMgrRelation object is fully initialized before calling the smgr_open callback, so that it can be cleaned up properly if the callback fails.

- Remove incorrect assertion in `pgstat_report_stat()` (Michael Paquier) [](https://postgr.es/c/4b6331e0f)

- Fix overly-strict assertion in `gistFindCorrectParent()` (Heikki Linnakangas) [](https://postgr.es/c/6526d0794)

- Avoid assertion failure in parallel vacuum when `maintenance_work_mem` has a very small value (Masahiko Sawada) [](https://postgr.es/c/a38dce3c4)

- Fix rare assertion failure in standby servers when the primary is restarted (Heikki Linnakangas) [](https://postgr.es/c/302ce5bd9)

- In PL/pgSQL, avoid “unexpected plan node type” error when a scrollable cursor is defined on a simple `SELECT expression` query (Andrei Lepikhov) [](https://postgr.es/c/1353b1161)

- Don't try to drop individual index partitions in pg_dump's `--clean` mode (Jian He) [](https://postgr.es/c/3424c1075)

  The server rejects such `DROP` commands. That has no real consequences, since the partitions will go away anyway in the subsequent `DROP`s of either their parent tables or their partitioned index. However, the error reported for the attempted drop causes problems when restoring in `--single-transaction` mode.

- In pg_dumpall, avoid emitting invalid role `GRANT` commands if pg_auth_members contains invalid role OIDs (Tom Lane) [](https://postgr.es/c/16eff4261)

  Instead, print a warning and skip the entry. This copes better with catalog corruption that has been seen to occur in back branches as a result of race conditions between `GRANT` and `DROP ROLE`.

- In pg_amcheck and pg_upgrade, use the correct function to free allocations made by libpq (Michael Paquier, Ranier Vilela) [](https://postgr.es/c/ee78823ff) [](https://postgr.es/c/0851b6573) [](https://postgr.es/c/f903d4da9)

  These oversights could result in crashes in certain Windows build configurations, such as a debug build of libpq used by a non-debug build of the calling application.

- Fix reindexdb's scheduling of parallel reindex operations (Alexander Korotkov) [](https://postgr.es/c/09ef2f8df)

  The original coding failed to achieve the expected amount of parallelism.

- Avoid crashing with corrupt input data in `contrib/pageinspect`'s `heap_page_items()` (Dmitry Kovalenko) [](https://postgr.es/c/ecb8e5641)

- Prevent assertion failure in `contrib/pg_freespacemap`'s `pg_freespacemap()` (Tender Wang) [](https://postgr.es/c/51d038da8)

  Applying `pg_freespacemap()` to a relation lacking storage (such as a view) caused an assertion failure, although there was no ill effect in non-assert builds. Add an error check to reject that case.

- In `contrib/postgres_fdw`, avoid pulling up restriction conditions from subqueries (Alexander Pyhalov) [](https://postgr.es/c/729fe699e)

  This fix prevents rare cases of “unexpected expression in subquery output” errors.

- Fix build failure when an old version of `libpq_fe.h` is present in system include directories (Tom Lane) [](https://postgr.es/c/f186f90e5)

- Fix build failure on macOS 15.4 (Tom Lane, Peter Eisentraut) [](https://postgr.es/c/915e88968)

  This macOS update broke our configuration probe for `strchrnul()`.

- Fix valgrind labeling of per-buffer data of read streams (Thomas Munro) [](https://postgr.es/c/57dca6faa)

  This affects no core code in released versions of PostgreSQL, but an extension using the per-buffer data feature might have encountered spurious failures when being tested under valgrind.

- Avoid valgrind complaints about string hashing code (John Naylor) [](https://postgr.es/c/fde7c0164)

- Update time zone data files to tzdata release 2025b for DST law changes in Chile, plus historical corrections for Iran (Tom Lane) [](https://postgr.es/c/5d5970b9f)

  There is a new time zone America/Coyhaique for Chile's Aysén Region, to account for it changing to UTC-03 year-round and thus diverging from America/Santiago.

## Release 17.4

Release date:

2025-02-20

This release contains a few fixes from 17.3. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.4

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.1, see [Release 17.1](#release-17-1).

## Changes

- Improve behavior of libpq's quoting functions (Andres Freund, Tom Lane) [](https://postgr.es/c/a92db3d02) [](https://postgr.es/c/3abe6e04c) [](https://postgr.es/c/3977bd298)

  The changes made for CVE-2025-1094 had one serious oversight: `PQescapeLiteral()` and `PQescapeIdentifier()` failed to honor their string length parameter, instead always reading to the input string's trailing null. This resulted in including unwanted text in the output, if the caller intended to truncate the string via the length parameter. With very bad luck it could cause a crash due to reading off the end of memory.

  In addition, modify all these quoting functions so that when invalid encoding is detected, an invalid sequence is substituted for just the first byte of the presumed character, not all of it. This reduces the risk of problems if a calling application performs additional processing on the quoted string.

- Fix small memory leak in pg_createsubscriber (Ranier Vilela) [](https://postgr.es/c/ff6d9cfcb)

- Fix meson build system to correctly detect availability of the `bsd_auth.h` system header (Nazir Bilal Yavuz) [](https://postgr.es/c/c9a1d2135)

## Release 17.3

Release date:

2025-02-13

This release contains a variety of fixes from 17.2. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.3

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.1, see [Release 17.1](#release-17-1).

## Changes

- Harden `PQescapeString` and allied functions against invalidly-encoded input strings (Andres Freund, Noah Misch) [](https://postgr.es/c/43a77239d) [](https://postgr.es/c/7d43ca6fe) [](https://postgr.es/c/61ad93cdd) [](https://postgr.es/c/02d4d87ac) [](https://postgr.es/c/05abb0f83) [](https://postgr.es/c/85c1fcc65)

  Data-quoting functions supplied by libpq now fully check the encoding validity of their input. If invalid characters are detected, they report an error if possible. For the ones that lack an error return convention, the output string is adjusted to ensure that the server will report invalid encoding and no intervening processing will be fooled by bytes that might happen to match single quote, backslash, etc.

  The purpose of this change is to guard against SQL-injection attacks that are possible if one of these functions is used to quote crafted input. There is no hazard when the resulting string is sent directly to a PostgreSQL server (which would check its encoding anyway), but there is a risk when it is passed through psql or other client-side code. Historically such code has not carefully vetted encoding, and in many cases it's not clear what it should do if it did detect such a problem.

  This fix is effective only if the data-quoting function, the server, and any intermediate processing agree on the character encoding that's being used. Applications that insert untrusted input into SQL commands should take special care to ensure that that's true.

  Applications and drivers that quote untrusted input without using these libpq functions may be at risk of similar problems. They should first confirm the data is valid in the encoding expected by the server.

  The PostgreSQL Project thanks Stephen Fewer for reporting this problem. (CVE-2025-1094)

- Restore auto-truncation of database and user names appearing in connection requests (Nathan Bossart) [](https://postgr.es/c/d09fbf645)

  This reverts a v17 change that proved to cause trouble for some users. Over-length names should be truncated in an encoding-aware fashion, but for now just return to the former behavior of blind truncation at `NAMEDATALEN-1` bytes.

- Exclude parallel workers from connection privilege checks and limits (Tom Lane) [](https://postgr.es/c/15b4c46c3)

  Do not check `datallowconn`, `rolcanlogin`, and `ACL_CONNECT` privileges when starting a parallel worker, instead assuming that it's enough for the leader process to have passed similar checks originally. This avoids, for example, unexpected failures of parallelized queries when the leader is running as a role that lacks login privilege. In the same vein, enforce `ReservedConnections`, `datconnlimit`, and `rolconnlimit` limits only against regular backends, and count only regular backends while checking if the limits were already reached. Those limits are meant to prevent excessive consumption of process slots for regular backends --- but parallel workers and other special processes have their own pools of process slots with their own limit checks.

- Drop “Lock” suffix from LWLock wait event names (Bertrand Drouvot) [](https://postgr.es/c/5ffbbcfa1)

  Refactoring unintentionally caused the pg_stat_activity view to show lock-related wait event names with a “Lock” suffix, which among other things broke joining it to pg_wait_events.

- Fix possible failure to return all matching tuples for a btree index scan with a ScalarArrayOp (`= ANY`) condition (Peter Geoghegan) [](https://postgr.es/c/9e85b20da)

- Fix possible re-use of stale results in window aggregates (David Rowley) [](https://postgr.es/c/9d5ce4f1a)

  A window aggregate with a “run condition” optimization and a pass-by-reference result type might incorrectly return the result from the previous partition instead of performing a fresh calculation.

- Keep `TransactionXmin` in sync with `MyProc->xmin` (Heikki Linnakangas) [](https://postgr.es/c/7cfdb4d1e)

  This oversight could permit a process to try to access data that had already been vacuumed away. One known consequence is transient “could not access status of transaction” errors.

- Fix race condition that could cause failure to add a newly-inserted catalog entry to a catalog cache list (Heikki Linnakangas) [](https://postgr.es/c/96e61b279)

  This could result, for example, in failure to use a newly-created function within an existing session.

- Prevent possible catalog corruption when a system catalog is vacuumed concurrently with an update (Noah Misch) [](https://postgr.es/c/1587f7b9f) [](https://postgr.es/c/f4af4515b)

- Fix data corruption when relation truncation fails (Thomas Munro) [](https://postgr.es/c/0350b876b) [](https://postgr.es/c/66aaabe7a) [](https://postgr.es/c/45aef9f6b)

  The filesystem calls needed to perform relation truncation could fail, leaving inconsistent state on disk (for example, effectively reviving deleted data). We can't really prevent that, but we can recover by dint of making such failures into PANICs, so that consistency is restored by replaying from WAL up to just before the attempted truncation. This isn't a hugely desirable behavior, but such failures are rare enough that it seems an acceptable solution.

- Prevent checkpoints from starting during relation truncation (Robert Haas) [](https://postgr.es/c/d4ffbf47b)

  This avoids a race condition wherein the modified file might not get fsync'd before completing the checkpoint, creating a risk of data corruption if the operating system crashes soon after.

- Avoid possibly losing an update of pg_database.datfrozenxid when `VACUUM` runs concurrently with a `REASSIGN OWNED` that changes that database's owner (Kirill Reshke) [](https://postgr.es/c/fa6131377)

- Fix incorrect tg_updatedcols values passed to `AFTER UPDATE` triggers (Tom Lane) [](https://postgr.es/c/2b72fed2d)

  In some cases the tg_updatedcols bitmap could describe the set of columns updated by an earlier command in the same transaction, fooling the trigger into doing the wrong thing.

  Also, prevent memory bloat caused by making too many copies of the tg_updatedcols bitmap.

- Fix detach of a partition that has its own foreign-key constraint referencing a partitioned table (Amul Sul) [](https://postgr.es/c/2f30847d1)

  In common cases, foreign keys are defined on a partitioned table's top level; but if instead one is defined on a partition and references a partitioned table, and the referencing partition is detached, the relevant pg_constraint entries were updated incorrectly. This led to errors like “could not find ON INSERT check triggers of foreign key constraint”.

- Fix `pg_get_constraintdef`'s support for `NOT NULL` constraints on domains (Álvaro Herrera) [](https://postgr.es/c/6e793582b)

- Fix mis-processing of `to_timestamp`'s `FFn` format codes (Tom Lane) [](https://postgr.es/c/765f76d8c)

  An integer format code immediately preceding `FFn` would consume all available digits, leaving none for `FFn`.

- When deparsing a `PASSING` clause in a SQL/JSON query function, ensure that variable names are double-quoted when necessary (Dean Rasheed) [](https://postgr.es/c/d037cc2af)

- When deparsing an `XMLTABLE()` expression, ensure that XML namespace names are double-quoted when necessary (Dean Rasheed) [](https://postgr.es/c/61b12135f)

- Include the `ldapscheme` option in `pg_hba_file_rules()` output (Laurenz Albe) [](https://postgr.es/c/8ed9bf0a3) [](https://postgr.es/c/dc24c9ad5)

- Fix planning of pre-sorted `UNION` operations for cases where the input column datatypes don't all match (David Rowley) [](https://postgr.es/c/5db9367e5)

  This error could lead to sorting data with the wrong sort operator, with consequences ranging from no visible problem to core dumps.

- Don't merge `UNION` operations if their column collations aren't consistent (Tom Lane) [](https://postgr.es/c/c1ebef3c1)

  Previously we ignored collations when deciding if it's safe to merge `UNION` steps into a single N-way `UNION` operation. This was arguably valid before the introduction of nondeterministic collations, but it's not anymore, since the collation in use can affect the definition of uniqueness.

- Prevent “wrong varnullingrels” planner errors after pulling up a subquery that's underneath an outer join (Tom Lane) [](https://postgr.es/c/72822a99d) [](https://postgr.es/c/78883cd90)

- Ignore nulling-relation marker bits when looking up statistics (Richard Guo) [](https://postgr.es/c/297b280ab)

  This oversight could lead to failure to use relevant statistics about expressions, or to “corrupt MVNDistinct entry” errors.

- Fix missed expression processing for partition pruning steps (Tom Lane) [](https://postgr.es/c/0671a71e0)

  This oversight could lead to “unrecognized node type” errors, and perhaps other problems, in queries accessing partitioned tables.

- Give the slotsync worker process its own process slot (Tom Lane, Hou Zhijie) [](https://postgr.es/c/14141bbbc)

  This was overlooked in the addition of the slotsync worker, with the result that its process slot effectively came out of the pool meant for regular backend processes. This could result in failure to launch the worker, or to subsequent failures of connection requests that should have succeeded according to the configured settings, if the number of regular backend processes approached `max_connections`.

- Allow dshash tables to grow past 1GB (Matthias van de Meent) [](https://postgr.es/c/18452b70a)

  This avoids errors like “invalid DSA memory alloc request size”. The case can occur for example in transactions that process several million tables.

- Avoid possible integer overflow in `bringetbitmap()` (James Hunter, Evgeniy Gorbanyov) [](https://postgr.es/c/e027ee990)

  Since the result is only used for statistical purposes, the effects of this error were mostly cosmetic.

- Correct miscalculation of SLRU bank numbers (Yura Sokolov) [](https://postgr.es/c/ffd9b8134)

  This error led to using a smaller number of banks than intended, causing more contention but no functional misbehavior.

- Ensure that an already-set process latch doesn't prevent the postmaster from noticing socket events (Thomas Munro) [](https://postgr.es/c/44f400fbc)

  An extremely heavy workload of backends launching workers and workers exiting could prevent the postmaster from responding to incoming client connections in a timely fashion.

- Prevent streaming standby servers from looping infinitely when reading a WAL record that crosses pages (Kyotaro Horiguchi, Alexander Kukushkin) [](https://postgr.es/c/e6767c0ed)

  This would happen when the record's continuation is on a page that needs to be read from a different WAL source.

- Fix unintended promotion of FATAL errors to PANIC during early process startup (Noah Misch) [](https://postgr.es/c/4bd9de3f4)

  This fixes some unlikely cases that would result in “PANIC: proc_exit() called in child process”.

- Fix cases where an operator family member operator or support procedure could become a dangling reference (Tom Lane) [](https://postgr.es/c/ec7b89cc5) [](https://postgr.es/c/5b44a317a)

  In some cases a data type could be dropped while references to its OID still remain in pg_amop or pg_amproc. While that caused no immediate issues, an attempt to drop the owning operator family would fail, and pg_dump would produce bogus output when dumping the operator family. This fix causes creation and modification of operator families/classes to add needed dependency entries so that dropping a data type will also drop any dependent operator family elements. That does not help vulnerable pre-existing operator families, though, so a band-aid has also been added to `DROP OPERATOR FAMILY` to prevent failure when dropping a family that has dangling members.

- Fix multiple memory leaks in logical decoding output (Vignesh C, Masahiko Sawada, Boyu Yang) [](https://postgr.es/c/836435424) [](https://postgr.es/c/bbe68c13a) [](https://postgr.es/c/afe9b0d9f)

- Fix small memory leak when updating the `application_name` or `cluster_name` settings (Tofig Aliev) [](https://postgr.es/c/9add1bbfa)

- Avoid crash when a background process tries to check a new value of `synchronized_standby_slots` (Álvaro Herrera) [](https://postgr.es/c/9abdc1841)

- Avoid integer overflow while testing `wal_skip_threshold` condition (Tom Lane) [](https://postgr.es/c/1e25cdb21)

  A transaction that created a very large relation could mistakenly decide to ensure durability by copying the relation into WAL instead of fsync'ing it, thereby negating the point of `wal_skip_threshold`. (This only matters when `wal_level` is set to `minimal`, else a WAL copy is required anyway.)

- Fix unsafe order of operations during cache lookups (Noah Misch) [](https://postgr.es/c/718af10da)

  The only known consequence was a usually-harmless “you don't own a lock of type ExclusiveLock” warning during `GRANT TABLESPACE`.

- Avoid potential use-after-free in parallel vacuum (Vallimaharajan G, John Naylor) [](https://postgr.es/c/83ce20d67)

  This bug seems to have no consequences in standard builds, but it's theoretically a hazard.

- Fix possible “failed to resolve name” failures when using JIT on older ARM platforms (Thomas Munro) [](https://postgr.es/c/8a9a51518)

  This could occur as a consequence of inconsistency about the default setting of `-moutline-atomics` between gcc and clang. At least Debian and Ubuntu are known to ship gcc and clang compilers that target armv8-a but differ on the use of outline atomics by default.

- Fix assertion failure in `WITH RECURSIVE ... UNION` queries (David Rowley) [](https://postgr.es/c/7b8d45d27)

- Avoid assertion failure in rule deparsing if a set operation leaf query contains set operations (Man Zeng, Tom Lane) [](https://postgr.es/c/fea81aee8)

- Avoid edge-case assertion failure in parallel query startup (Tom Lane) [](https://postgr.es/c/556f7b7bc)

- Fix assertion failure at shutdown when writing out the statistics file (Michael Paquier) [](https://postgr.es/c/dc5f90541)

- Avoid valgrind complaints about string hashing code (John Naylor) [](https://postgr.es/c/6555fe197)

- In `NULLIF()`, avoid passing a read-write expanded object pointer to the data type's equality function (Tom Lane) [](https://postgr.es/c/97be02ad0)

  The equality function could modify or delete the object if it's given a read-write pointer, which would be bad if we decide to return it as the `NULLIF()` result. There is probably no problem with any built-in equality function, but it's easy to demonstrate a failure with one coded in PL/pgSQL.

- Ensure that expression preprocessing is applied to a default null value in `INSERT` (Tom Lane) [](https://postgr.es/c/6e41e9e5e)

  If the target column is of a domain type, the planner must insert a coerce-to-domain step not just a null constant, and this expression missed going through some required processing steps. There is no known consequence with domains based on core data types, but in theory an error could occur with domains based on extension types.

- Avoid data loss when starting a bulk write on a relation fork that already contains data (Matthias van de Meent) [](https://postgr.es/c/969583553)

  Any pre-existing data was overwritten with zeroes. This is not an issue for core PostgreSQL, which never does that. Some extensions would like to, however.

- Avoid crash if a server process tried to iterate over a shared radix tree that it didn't create (Masahiko Sawada) [](https://postgr.es/c/9af2b3435)

  There is no code in core PostgreSQL that does this, but an extension might wish to.

- Repair memory leaks in PL/Python (Mat Arye, Tom Lane) [](https://postgr.es/c/e98df02df)

  Repeated use of `PLyPlan.execute` or `plpy.cursor` resulted in memory leakage for the duration of the calling PL/Python function.

- Fix PL/Tcl to compile with Tcl 9 (Peter Eisentraut) [](https://postgr.es/c/f979197eb)

- In the ecpg preprocessor, fix possible misprocessing of cursors that reference out-of-scope variables (Tom Lane) [](https://postgr.es/c/a963abd54)

- In ecpg, fix compile-time warnings about unsupported use of `COPY ... FROM STDIN` (Ryo Kanbayashi) [](https://postgr.es/c/ba2dbedd5)

  Previously, the intended warning was not issued due to a typo.

- Fix psql to safely handle file path names that are encoded in SJIS (Tom Lane) [](https://postgr.es/c/0b713b94b)

  Some two-byte characters in SJIS have a second byte that is equal to ASCII backslash (`\`). These characters were corrupted by path name normalization, preventing access to files whose names include such characters.

- Add psql tab completion for `COPY (MERGE INTO)` (Jian He) [](https://postgr.es/c/4527b9e26)

- Fix use of wrong version of `pqsignal()` in pgbench and psql (Fujii Masao, Tom Lane) [](https://postgr.es/c/a0dfeae0d)

  This error could lead to misbehavior when using the `-T` option in pgbench or the `\watch` command in psql, due to interrupted system calls not being resumed as expected.

- Fix misexecution of some nested `\if` constructs in pgbench (Michail Nikolaev) [](https://postgr.es/c/ff9dc96f3)

  An `\if` command appearing within a false (not-being-executed) `\if` branch was incorrectly treated the same as `\elif`.

- In pgbench, fix possible misdisplay of progress messages during table initialization (Yushi Ogiwara, Tatsuo Ishii, Fujii Masao) [](https://postgr.es/c/adb103fca) [](https://postgr.es/c/e35d396ec)

- Make pg_controldata more robust against corrupted `pg_control` files (Ilyasov Ian, Anton Voloshin) [](https://postgr.es/c/1b8a9533f)

  Since pg_controldata will attempt to print the contents of `pg_control` even if the CRC check fails, it must take care not to misbehave for invalid field values. This patch fixes some issues triggered by invalid timestamps and apparently-negative WAL segment sizes.

- Fix possible crash in pg_dump with identity sequences attached to tables that are extension members (Tom Lane) [](https://postgr.es/c/ad950ea98)

- Fix memory leak in pg_restore with zstd-compressed data (Tom Lane) [](https://postgr.es/c/04b860198)

  The leak was per-decompression-operation, so would be most noticeable with a dump containing many tables or large objects.

- Fix pg_basebackup to correctly handle `pg_wal.tar` files exceeding 2GB on Windows (Davinder Singh, Thomas Munro) [](https://postgr.es/c/faee3185a) [](https://postgr.es/c/af109e339)

- Use SQL-standard function bodies in the declarations of `contrib/earthdistance`'s SQL-language functions (Tom Lane, Ronan Dunklau) [](https://postgr.es/c/3652de36e)

  This change allows their references to `contrib/cube` to be resolved during extension creation, reducing the risk of search-path-based failures and possible attacks.

  In particular, this restores their usability in contexts like generated columns, for which PostgreSQL v17 restricts the search path on security grounds. We have received reports of databases failing to be upgraded to v17 because of that. This patch has been included in v16 to provide a workaround: updating the `earthdistance` extension to this version beforehand should allow an upgrade to succeed.

- Detect version mismatch between `contrib/pageinspect`'s SQL declarations and the underlying shared library (Tomas Vondra) [](https://postgr.es/c/3668c1d50)

  Previously, such a mismatch could result in a crash while calling `brin_page_items()`. Instead throw an error recommending updating the extension.

- When trying to cancel a remote query in `contrib/postgres_fdw`, re-issue the cancel request a few times if it didn't seem to do anything (Tom Lane) [](https://postgr.es/c/89962bfef)

  This fixes a race condition where we might try to cancel a just-sent query before the remote server has started to process it, so that the initial cancel request is ignored.

- Update configuration probes that determine the compiler switches needed to access ARM CRC instructions (Tom Lane) [](https://postgr.es/c/e266a0ed6)

  On ARM platforms where the baseline CPU target lacks CRC instructions, we need to supply a `-march` switch to persuade the compiler to compile such instructions. Recent versions of gcc reject the value we were trying, leading to silently falling back to software CRC.

- Fix meson build system to support old OpenSSL libraries on Windows (Darek Slusarczyk) [](https://postgr.es/c/0951d4ee4)

  Add support for the legacy library names `ssleay32` and `libeay32`.

- In Windows builds using meson, ensure all libcommon and libpgport functions are exported (Vladlen Popolitov, Heikki Linnakangas) [](https://postgr.es/c/c80acbc6f) [](https://postgr.es/c/d8b0c6411)

  This fixes “unresolved external symbol” build errors for extensions.

- Fix meson configuration process to correctly detect OSSP's `uuid.h` header file under MSVC (Andrew Dunstan) [](https://postgr.es/c/7c655a04a)

- When building with meson, install `pgevent` in \<pkglibdir\> not \<bindir\> (Peter Eisentraut) [](https://postgr.es/c/e00c1e249)

  This matches the behavior of the make-based build system and the old MSVC build system.

- When building with meson, install `sepgsql.sql` under `share/contrib/` not `share/extension/` (Peter Eisentraut) [](https://postgr.es/c/24c5b73eb)

  This matches what the make-based build system does.

- Update time zone data files to tzdata release 2025a for DST law changes in Paraguay, plus historical corrections for the Philippines (Tom Lane) [](https://postgr.es/c/e292ba333)

## Release 17.2

Release date:

2024-11-21

This release contains a few fixes from 17.1. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.2

A dump/restore is not required for those running 17.X.

However, if you are upgrading from a version earlier than 17.1, see [Release 17.1](#release-17-1).

## Changes

- Repair ABI break for extensions that work with struct ResultRelInfo (Tom Lane) [](https://postgr.es/c/6bfacd368)

  Last week's minor releases unintentionally broke binary compatibility with timescaledb and several other extensions. Restore the affected structure to its previous size, so that such extensions need not be rebuilt.

- Restore functionality of `ALTER {ROLE|DATABASE} SET role` (Tom Lane, Noah Misch) [](https://postgr.es/c/1c05004a8)

  The fix for CVE-2024-10978 accidentally caused settings for `role` to not be applied if they come from non-interactive sources, including previous `ALTER {ROLE|DATABASE}` commands and the `PGOPTIONS` environment variable.

- Fix cases where a logical replication slot's restart_lsn could go backwards (Masahiko Sawada) [](https://postgr.es/c/568e78a65)

  Previously, restarting logical replication could sometimes cause the slot's restart point to be recomputed as an older value than had previously been advertised in pg_replication_slots. This is bad, since for example WAL files might have been removed on the basis of the later restart_lsn value, in which case replication would fail to restart.

- Avoid deleting still-needed WAL files during pg_rewind (Polina Bungina, Alexander Kukushkin) [](https://postgr.es/c/cb844d66b)

  Previously, in unlucky cases, it was possible for pg_rewind to remove important WAL files from the rewound demoted primary. In particular this happens if those files have been marked for archival (i.e., their `.ready` files were created) but not yet archived. Then the newly promoted node no longer has such files because of them having been recycled, but likely they are needed for recovery in the demoted node. If pg_rewind removes them, recovery is not possible anymore.

- Fix race conditions associated with dropping shared statistics entries (Kyotaro Horiguchi, Michael Paquier) [](https://postgr.es/c/1d6a03ea4)

  These bugs could lead to loss of statistics data, assertion failures, or “can only drop stats once” errors.

- Count index scans in `contrib/bloom` indexes in the statistics views, such as the pg_stat_user_indexes.idx_scan counter (Masahiro Ikeda) [](https://postgr.es/c/7af6d1306)

- Fix crash when checking to see if an index's opclass options have changed (Alexander Korotkov) [](https://postgr.es/c/a6fa869cf)

  Some forms of `ALTER TABLE` would fail if the table has an index with non-default operator class options.

- Avoid assertion failure caused by disconnected NFA sub-graphs in regular expression parsing (Tom Lane) [](https://postgr.es/c/5f28e6ba7)

  This bug does not appear to have any visible consequences in non-assert builds.

## Release 17.1

Release date:

2024-11-14

This release contains a variety of fixes from 17.0. For information about new features in major release 17, see [Release 17](#release-17).

## Migration to Version 17.1

A dump/restore is not required for those running 17.X.

However, if you have ever detached a partition from a partitioned table that has a foreign-key reference to another partitioned table, and not dropped the former partition, then you may have catalog and/or data corruption to repair, as detailed in the fifth changelog entry below.

Also, in the uncommon case that a database's `LC_CTYPE` setting is `C` while its `LC_COLLATE` setting is some other locale, indexes on textual columns should be reindexed, as described in the sixth changelog entry below.

## Changes

- Ensure cached plans are marked as dependent on the calling role when RLS applies to a non-top-level table reference (Nathan Bossart) [](https://postgr.es/c/edcda9bb4)

  If a CTE, subquery, sublink, security invoker view, or coercion projection in a query references a table with row-level security policies, we neglected to mark the resulting plan as potentially dependent on which role is executing it. This could lead to later query executions in the same session using the wrong plan, and then returning or hiding rows that should have been hidden or returned instead.

  The PostgreSQL Project thanks Wolfgang Walther for reporting this problem. (CVE-2024-10976)

- Make libpq discard error messages received during SSL or GSS protocol negotiation (Jacob Champion) [](https://postgr.es/c/a5cc4c667)

  An error message received before encryption negotiation is completed might have been injected by a man-in-the-middle, rather than being real server output. Reporting it opens the door to various security hazards; for example, the message might spoof a query result that a careless user could mistake for correct output. The best answer seems to be to discard such data and rely only on libpq's own report of the connection failure.

  The PostgreSQL Project thanks Jacob Champion for reporting this problem. (CVE-2024-10977)

- Fix unintended interactions between `SET SESSION AUTHORIZATION` and `SET ROLE` (Tom Lane) [](https://postgr.es/c/cd82afdda) [](https://postgr.es/c/f4f5d27d8)

  The SQL standard mandates that `SET SESSION AUTHORIZATION` have a side-effect of doing `SET ROLE NONE`. Our implementation of that was flawed, creating more interaction between the two settings than intended. Notably, rolling back a transaction that had done `SET SESSION AUTHORIZATION` would revert `ROLE` to `NONE` even if that had not been the previous state, so that the effective user ID might now be different from what it had been before the transaction. Transiently setting `session_authorization` in a function `SET` clause had a similar effect. A related bug was that if a parallel worker inspected `current_setting('role')`, it saw `none` even when it should see something else.

  The PostgreSQL Project thanks Tom Lane for reporting this problem. (CVE-2024-10978)

- Prevent trusted PL/Perl code from changing environment variables (Andrew Dunstan, Noah Misch) [](https://postgr.es/c/3ebcfa54d) [](https://postgr.es/c/4cd4f3b97) [](https://postgr.es/c/8d19f3fea)

  The ability to manipulate process environment variables such as `PATH` gives an attacker opportunities to execute arbitrary code. Therefore, “trusted” PLs must not offer the ability to do that. To fix `plperl`, replace `%ENV` with a tied hash that rejects any modification attempt with a warning. Untrusted `plperlu` retains the ability to change the environment.

  The PostgreSQL Project thanks Coby Abrams for reporting this problem. (CVE-2024-10979)

- Fix updates of catalog state for foreign-key constraints when attaching or detaching table partitions (Jehan-Guillaume de Rorthais, Tender Wang, Álvaro Herrera) [](https://postgr.es/c/5914a22f6) [](https://postgr.es/c/936ab6de9)

  If the referenced table is partitioned, then different catalog entries are needed for a referencing table that is stand-alone versus one that is a partition. `ATTACH/DETACH PARTITION` commands failed to perform this conversion correctly. In particular, after `DETACH` the now stand-alone table would be missing foreign-key enforcement triggers, which could result in the table later containing rows that fail the foreign-key constraint. A subsequent re-`ATTACH` could fail with surprising errors, too.

  The way to fix this is to do `ALTER TABLE DROP CONSTRAINT` on the now stand-alone table for each faulty constraint, and then re-add the constraint. If re-adding the constraint fails, then some erroneous data has crept in. You will need to manually re-establish consistency between the referencing and referenced tables, then re-add the constraint.

  This query can be used to identify broken constraints and construct the commands needed to recreate them:

      SELECT conrelid::pg_catalog.regclass AS "constrained table",
             conname AS constraint,
             confrelid::pg_catalog.regclass AS "references",
             pg_catalog.format('ALTER TABLE %s DROP CONSTRAINT %I;',
                               conrelid::pg_catalog.regclass, conname) AS "drop",
             pg_catalog.format('ALTER TABLE %s ADD CONSTRAINT %I %s;',
                               conrelid::pg_catalog.regclass, conname,
                               pg_catalog.pg_get_constraintdef(oid)) AS "add"
      FROM pg_catalog.pg_constraint c
      WHERE contype = 'f' AND conparentid = 0 AND
         (SELECT count(*) FROM pg_catalog.pg_constraint c2
          WHERE c2.conparentid = c.oid) <>
         ((SELECT count(*) FROM pg_catalog.pg_inherits i
          WHERE (i.inhparent = c.conrelid OR i.inhparent = c.confrelid) AND
            EXISTS (SELECT 1 FROM pg_catalog.pg_partitioned_table
                    WHERE partrelid = i.inhparent)) +
          CASE WHEN pg_catalog.pg_partition_root(conrelid) = confrelid THEN
                    (SELECT count(*) FROM pg_catalog.pg_partition_tree(confrelid)
                      WHERE level = 1)
               ELSE 0 END);

  Since it is possible that one or more of the `ADD CONSTRAINT` steps will fail, you should save the query's output in a file and then attempt to perform each step.

- Fix test for `C` locale when `LC_COLLATE` is different from `LC_CTYPE` (Jeff Davis) [](https://postgr.es/c/8148e7124)

  When using `libc` as the default collation provider, the test to see if `C` locale is in use for collation accidentally checked `LC_CTYPE` not `LC_COLLATE`. This has no impact in the typical case where those settings are the same, nor if both are not `C` (nor its alias `POSIX`). However, if `LC_CTYPE` is `C` while `LC_COLLATE` is some other locale, wrong query answers could ensue, and corruption of indexes on strings was possible. Users of databases with such settings should reindex affected indexes after installing this update. The converse case with `LC_COLLATE` being `C` while `LC_CTYPE` is some other locale would cause performance degradation, but no actual errors.

- Don't use partitionwise joins or grouping if the query's collation for the key column doesn't match the partition key's collation (Jian He, Webbo Han) [](https://postgr.es/c/a0cdfc889) [](https://postgr.es/c/b6484ca95)

  Such plans could produce incorrect results.

- Avoid planner failure after converting an `IS NULL` test on a `NOT NULL` column to constant `FALSE` (Richard Guo) [](https://postgr.es/c/78b1c553b)

  This bug typically led to errors such as “variable not found in subplan target lists”.

- Avoid possible planner crash while inlining a SQL function whose arguments contain certain array-related constructs (Tom Lane, Nathan Bossart) [](https://postgr.es/c/a3c4a91f1)

- Fix possible wrong answers or “wrong varnullingrels” planner errors for `MERGE ... WHEN NOT MATCHED BY SOURCE` actions (Dean Rasheed) [](https://postgr.es/c/d7d297f84) [](https://postgr.es/c/34ae54af9)

- Fix possible “could not find pathkey item to sort” error when the output of a `UNION ALL` member query needs to be sorted, and the sort column is an expression (Andrei Lepikhov, Tom Lane) [](https://postgr.es/c/54889ea64)

- Fix edge case in B-tree ScalarArrayOp index scans (Peter Geoghegan) [](https://postgr.es/c/c177726ae)

  When a scrollable cursor with a plan of this kind was backed up to its starting point and then run forward again, wrong answers were possible.

- Fix assertion failure or confusing error message for `COPY (query) TO ...`, when the \<query\> is rewritten by a `DO INSTEAD NOTIFY` rule (Tender Wang, Tom Lane) [](https://postgr.es/c/3685ad618)

- Fix validation of `COPY`'s `FORCE_NOT_NULL` and `FORCE_NULL` options (Joel Jacobson) [](https://postgr.es/c/c06a4746b)

  Some incorrect usages are now rejected as they should be.

- Fix server crash when a `json_objectagg()` call contains a volatile function (Amit Langote) [](https://postgr.es/c/7148cb3e3)

- Fix detection of skewed data during parallel hash join (Thomas Munro) [](https://postgr.es/c/4ac5d33a8)

  After repartitioning the inner side of a hash join because one partition has accumulated too many tuples, we check to see if all the partition's tuples went into the same child partition, which suggests that they all have the same hash value and further repartitioning cannot improve matters. This check malfunctioned in some cases, allowing repeated futile repartitioning which would eventually end in a resource-exhaustion error.

- Avoid crash when `ALTER DATABASE SET` is used to set a server parameter that requires search-path-based lookup, such as `default_text_search_config` (Jeff Davis) [](https://postgr.es/c/2fe4167bc)

- Avoid repeated lookups of opclasses and collations while creating a new index on a partitioned table (Tom Lane) [](https://postgr.es/c/fee8cb947)

  This was problematic mainly because some of the lookups would be done with a restricted `search_path`, leading to unexpected failures if the `CREATE INDEX` command referenced objects outside `pg_catalog`.

  This fix also prevents comments on the parent partitioned index from being copied to child indexes.

- Add missing dependency from a partitioned table to a non-built-in access method specified in `CREATE TABLE ... USING` (Michael Paquier) [](https://postgr.es/c/bb584e831)

  Dropping the access method should be blocked when a table exists that depends on it, but it was not, allowing subsequent odd behavior. Note that this fix only prevents problems for partitioned tables created after this update.

- Disallow locale names containing non-ASCII characters (Thomas Munro) [](https://postgr.es/c/9c7acc333)

  This is only an issue on Windows, as such locale names are not used elsewhere. They are problematic because it's quite unclear what encoding such names are represented in (since the locale itself defines the encoding to use). In recent PostgreSQL releases, an abort in the Windows runtime library could occur because of confusion about that.

  Anyone who encounters the new error message should either create a new duplicated locale with an ASCII-only name using Windows Locale Builder, or consider using BCP 47-compliant locale names like `tr-TR`.

- Fix race condition in committing a serializable transaction (Heikki Linnakangas) [](https://postgr.es/c/234f6d09e)

  Mis-processing of a recently committed transaction could lead to an assertion failure or a “could not access status of transaction” error.

- Fix race condition in `COMMIT PREPARED` that resulted in orphaned 2PC files (wuchengwen) [](https://postgr.es/c/f250cb29d)

  A concurrent `PREPARE TRANSACTION` could cause `COMMIT PREPARED` to not remove the on-disk two-phase state file for the completed transaction. There was no immediate ill effect, but a subsequent crash-and-recovery could fail with “could not access status of transaction”, requiring manual removal of the orphaned file to restore service.

- Avoid invalid memory accesses after skipping an invalid toast index during `VACUUM FULL` (Tender Wang) [](https://postgr.es/c/1532599a8)

  A list tracking yet-to-be-rebuilt indexes was not properly updated in this code path, risking assertion failures or crashes later on.

- Fix ways in which an “in place” catalog update could be lost (Noah Misch) [](https://postgr.es/c/fd27b878c) [](https://postgr.es/c/3b7a689e1) [](https://postgr.es/c/da99df15c) [](https://postgr.es/c/e11907682) [](https://postgr.es/c/9aef6f19a) [](https://postgr.es/c/0bcb9d079) [](https://postgr.es/c/54bc22fbf)

  Normal row updates write a new version of the row to preserve rollback-ability of the transaction. However, certain system catalog updates are intentionally non-transactional and are done with an in-place update of the row. These patches fix race conditions that could cause the effects of an in-place update to be lost. As an example, it was possible to forget having set pg_class.relhasindex to true, preventing updates of the new index and thus causing index corruption.

- Reset catalog caches at end of recovery (Noah Misch) [](https://postgr.es/c/a4668c99f)

  This prevents scenarios wherein an in-place catalog update could be lost due to using stale data from a catalog cache.

- Avoid using parallel query while holding off interrupts (Francesco Degrassi, Noah Misch, Tom Lane) [](https://postgr.es/c/2370582ab) [](https://postgr.es/c/943b65358)

  This situation cannot arise normally, but it can be reached with test scenarios such as using a SQL-language function as B-tree support (which would be far too slow for production usage). If it did occur it would result in an indefinite wait.

- Ignore not-yet-defined Portals in the pg_cursors view (Tom Lane) [](https://postgr.es/c/3daeb539a)

  It is possible for user-defined code that inspects this view to be called while a new cursor is being set up, and if that happens a null pointer dereference would ensue. Avoid the problem by defining the view to exclude incompletely-set-up cursors.

- Avoid “unexpected table_index_fetch_tuple call during logical decoding” error while decoding a transaction involving insertion of a column default value (Takeshi Ideriha, Hou Zhijie) [](https://postgr.es/c/918107759) [](https://postgr.es/c/c4b8a916f)

- Reduce memory consumption of logical decoding (Masahiko Sawada) [](https://postgr.es/c/eef9cc4dc)

  Use a smaller default block size to store tuple data received during logical replication. This reduces memory wastage, which has been reported to be severe while processing long-running transactions, even leading to out-of-memory failures.

- Fix behavior of stable functions called from a `CALL` statement's argument list, when the `CALL` is within a PL/pgSQL `EXCEPTION` block (Tom Lane) [](https://postgr.es/c/b5eef7539)

  As with a similar fix in our previous quarterly releases, this case allowed such functions to be passed the wrong snapshot, causing them to see stale values of rows modified since the start of the outer transaction.

- Parse libpq's `keepalives` connection option in the same way as other integer-valued options (Yuto Sasaki) [](https://postgr.es/c/c7a201053)

  The coding used here rejected trailing whitespace in the option value, unlike other cases. This turns out to be problematic in ecpg's usage, for example.

- In ecpglib, fix out-of-bounds read when parsing incorrect datetime input (Bruce Momjian, Pavel Nekrasov) [](https://postgr.es/c/2c37cb26f)

  It was possible to try to read the location just before the start of a constant array. Real-world consequences seem minimal, though.

- Fix psql's describe commands to again work with pre-9.4 servers (Tom Lane) [](https://postgr.es/c/923a71584)

  Commands involving display of an ACL (permissions) column failed with very old PostgreSQL servers, due to use of a function not present in those versions.

- Avoid hanging if an interval less than 1ms is specified in psql's `\watch` command (Andrey Borodin, Michael Paquier) [](https://postgr.es/c/8a6170860)

  Instead, treat this the same as an interval of zero (no wait between executions).

- Fix failure to find replication password in `~/.pgpass` (Tom Lane) [](https://postgr.es/c/e2a912909)

  pg_basebackup and pg_receivewal failed to match an entry in `~/.pgpass` that had `replication` in the database name field, if no `-d` or `--dbname` switch was supplied. This resulted in an unexpected prompt for password.

- In pg_combinebackup, throw an error if an incremental backup file is present in a directory that is supposed to contain a full backup (Robert Haas) [](https://postgr.es/c/e36711442)

- In pg_combinebackup, don't construct filenames containing double slashes (Robert Haas) [](https://postgr.es/c/0d635b615)

  This caused no functional problems, but the duplicate slashes were visible in error messages, which could create confusion.

- Avoid trying to reindex temporary tables and indexes in vacuumdb and in parallel reindexdb (VaibhaveS, Michael Paquier, Fujii Masao, Nathan Bossart) [](https://postgr.es/c/85cb21df6) [](https://postgr.es/c/77f154681) [](https://postgr.es/c/5bd26e652)

  Reindexing other sessions' temporary tables cannot work, but the check to skip them was missing in some code paths, leading to unwanted failures.

- Fix incorrect LLVM-generated code on ARM64 platforms (Thomas Munro, Anthonin Bonnefoy) [](https://postgr.es/c/b7467ab71)

  When using JIT compilation on ARM platforms, the generated code could not support relocation distances exceeding 32 bits, allowing unlucky placement of generated code to cause server crashes on large-memory systems.

- Fix a few places that assumed that process start time (represented as a `time_t`) will fit into a `long` value (Max Johnson, Nathan Bossart) [](https://postgr.es/c/a356d23fd)

  On platforms where `long` is 32 bits (notably Windows), this coding would fail after Y2038. Most of the failures appear only cosmetic, but notably `pg_ctl start` would hang.

- Update time zone data files to tzdata release 2024b (Tom Lane) [](https://postgr.es/c/cad65907e) [](https://postgr.es/c/6283ff201)

  This tzdata release changes the old System-V-compatibility zone names to duplicate the corresponding geographic zones; for example `PST8PDT` is now an alias for `America/Los_Angeles`. The main visible consequence is that for timestamps before the introduction of standardized time zones, the zone is considered to represent local mean solar time for the named location. For example, in `PST8PDT`, `timestamptz` input such as `1801-01-01 00:00` would previously have been rendered as `1801-01-01 00:00:00-08`, but now it is rendered as `1801-01-01 00:00:00-07:52:58`.

  Also, historical corrections for Mexico, Mongolia, and Portugal. Notably, `Asia/Choibalsan` is now an alias for `Asia/Ulaanbaatar` rather than being a separate zone, mainly because the differences between those zones were found to be based on untrustworthy data.

## Release 17

Release date:

2024-09-26

## Overview

PostgreSQL 17 contains many new features and enhancements, including:

- New memory management system for `VACUUM`, which reduces memory consumption and can improve overall vacuuming performance.

- New SQL/JSON capabilities, including constructors, identity functions, and the [`JSON_TABLE()`](#functions-sqljson-table) function, which converts JSON data into a table representation.

- Various query performance improvements, including for sequential reads using streaming I/O, write throughput under high concurrency, and searches over multiple values in a [btree](#btree) index.

- Logical replication enhancements, including:

  - Failover control

  - [pg_createsubscriber](#app-pgcreatesubscriber), a utility that creates logical replicas from physical standbys

  - [pg_upgrade](#pgupgrade) now preserves logical replication slots on publishers and full subscription state on subscribers. This will allow upgrades to future major versions to continue logical replication without requiring copy to resynchronize.

- New client-side connection option, [`sslnegotiation=direct`](#libpq-connect-sslnegotiation), that performs a direct TLS handshake to avoid a round-trip negotiation.

- [pg_basebackup](#app-pgbasebackup) now supports incremental backup.

- [`COPY`](#sql-copy) adds a new option, `ON_ERROR ignore`, that allows a copy operation to continue in the event of an error.

The above items and other new features of PostgreSQL 17 are explained in more detail in the sections below.

## Migration to Version 17

A dump/restore using [???](#app-pg-dumpall) or use of [???](#pgupgrade) or logical replication is required for those wishing to migrate data from any previous release. See [???](#upgrading) for general information on migrating to new major releases.

Version 17 contains a number of changes that may affect compatibility with previous releases. Observe the following incompatibilities:

- Change functions to use a safe [???](#guc-search-path) during maintenance operations (Jeff Davis) [](https://postgr.es/c/2af07e2f7) [](https://postgr.es/c/b4da732fd64)

  This prevents maintenance operations (`ANALYZE`, `CLUSTER`, `CREATE INDEX`, `CREATE MATERIALIZED VIEW`, `REFRESH MATERIALIZED VIEW`, `REINDEX`, or `VACUUM`) from performing unsafe access. Functions used by expression indexes and materialized views that need to reference non-default schemas must specify a search path during function creation.

- Restrict `ago` to only appear at the end in `interval` values (Joseph Koshakow) [](https://postgr.es/c/165d581f1) [](https://postgr.es/c/617f9b7d4)

  Also, prevent empty interval units from appearing multiple times.

- Remove server variable old_snapshot_threshold (Thomas Munro) [](https://postgr.es/c/f691f5b80)

  This variable allowed vacuum to remove rows that potentially could be still visible to running transactions, causing "snapshot too old" errors later if accessed. This feature might be re-added to PostgreSQL later if an improved implementation is found.

- Change [`SET SESSION AUTHORIZATION`](#sql-set-session-authorization) handling of the initial session user's superuser status (Joseph Koshakow) [](https://postgr.es/c/a0363ab7a)

  The new behavior is based on the session user's superuser status at the time the `SET SESSION AUTHORIZATION` command is issued, rather than their superuser status at connection time.

- Remove feature which simulated per-database users (Nathan Bossart) [](https://postgr.es/c/884eee5bf)

  The feature, `db_user_namespace`, was rarely used.

- Remove adminpack contrib extension (Daniel Gustafsson) [](https://postgr.es/c/cc09e6549)

  This was used by now end-of-life pgAdmin III.

- Remove [???](#guc-wal-sync-method) value `fsync_writethrough` on `Windows` (Thomas Munro) [](https://postgr.es/c/d0c28601e)

  This value was the same as `fsync` on `Windows`.

- Change file boundary handling of two WAL file name functions (Kyotaro Horiguchi, Andres Freund, Bruce Momjian) [](https://postgr.es/c/344afc776)

  The functions [`pg_walfile_name()`](#functions-admin-backup-table) and `pg_walfile_name_offset()` used to report the previous LSN segment number when the LSN was on a file segment boundary; it now returns the current LSN segment.

- Remove server variable `trace_recovery_messages` since it is no longer needed (Bharath Rupireddy) [](https://postgr.es/c/c7a3e6b46)

- Remove [information schema](#information-schema) column element_types.domain_default (Peter Eisentraut) [](https://postgr.es/c/78806a950)

- Change [???](#pgrowlocks) lock mode output labels (Bruce Momjian) [](https://postgr.es/c/15d5d7405)

- Remove buffers_backend and buffers_backend_fsync from [pg_stat_bgwriter](#monitoring-pg-stat-bgwriter-view) (Bharath Rupireddy) [](https://postgr.es/c/74604a37f)

  These fields are considered redundant to similar columns in [pg_stat_io](#monitoring-pg-stat-io-view).

- Rename I/O block read/write timing statistics columns of [???](#pgstatstatements) (Nazir Bilal Yavuz) [](https://postgr.es/c/13d00729d)

  This renames blk_read_time to shared_blk_read_time, and blk_write_time to shared_blk_write_time.

- Change [pg_attribute.attstattarget](#catalog-pg-attribute) and pg_statistic_ext.stxstattarget to represent the default statistics target as `NULL` (Peter Eisentraut) [](https://postgr.es/c/4f622503d) [](https://postgr.es/c/012460ee9)

- Rename [pg_collation.colliculocale](#catalog-pg-collation) to colllocale and [pg_database.daticulocale](#catalog-pg-database) to datlocale (Jeff Davis) [](https://postgr.es/c/f696c0cd5)

- Rename [pg_stat_progress_vacuum](#vacuum-progress-reporting) column max_dead_tuples to max_dead_tuple_bytes, rename num_dead_tuples to num_dead_item_ids, and add dead_tuple_bytes (Masahiko Sawada) [](https://postgr.es/c/667e65aac) [](https://postgr.es/c/f1affb670)

- Rename SLRU columns in system view [pg_stat_slru](#monitoring-pg-stat-slru-view) (Alvaro Herrera) [](https://postgr.es/c/bcdfa5f2e)

  The column names accepted by [`pg_stat_reset_slru()`](#monitoring-stats-funcs-table) are also changed.

## Changes

Below you will find a detailed account of the changes between PostgreSQL 17 and the previous major release.

### Server

#### Optimizer

- Allow the optimizer to improve CTE plans by considering the statistics and sort order of columns referenced in earlier row output clauses (Jian Guo, Richard Guo, Tom Lane) [](https://postgr.es/c/f7816aec2) [](https://postgr.es/c/a65724dfa)

- Improve optimization of `IS NOT NULL` and `IS NULL` query restrictions (David Rowley, Richard Guo, Andy Fan) [](https://postgr.es/c/b262ad440) [](https://postgr.es/c/3af704098)

  Remove `IS NOT NULL` restrictions from queries on `NOT NULL` columns and eliminate scans on `NOT NULL` columns if `IS NULL` is specified.

- Allow partition pruning on boolean columns on `IS [NOT] UNKNOWN` conditionals (David Rowley) [](https://postgr.es/c/07c36c133)

- Improve optimization of range values when using containment operators \<@ and @\> (Kim Johan Andersson, Jian He) [](https://postgr.es/c/075df6b20)

- Allow correlated `IN` subqueries to be transformed into joins (Andy Fan, Tom Lane) [](https://postgr.es/c/9f1337639)

- Improve optimization of the `LIMIT` clause on partitioned tables, inheritance parents, and `UNION ALL` queries (Andy Fan, David Rowley) [](https://postgr.es/c/a8a968a82)

- Allow query nodes to be run in parallel in more cases (Tom Lane) [](https://postgr.es/c/e08d74ca1)

- Allow `GROUP BY` columns to be internally ordered to match `ORDER BY` (Andrei Lepikhov, Teodor Sigaev) [](https://postgr.es/c/0452b461b)

  This can be disabled using server variable [???](#guc-enable-groupby-reordering).

- Allow `UNION` (without `ALL`) to use MergeAppend (David Rowley) [](https://postgr.es/c/66c0185a3)

- Fix MergeAppend plans to more accurately compute the number of rows that need to be sorted (Alexander Kuzmenkov) [](https://postgr.es/c/9d1a5354f)

- Allow [GiST](#gist) and [SP-GiST](#spgist) indexes to be part of incremental sorts (Miroslav Bendik) [](https://postgr.es/c/625d5b3ca)

  This is particularly useful for `ORDER BY` clauses where the first column has a GiST and SP-GiST index, and other columns do not.

- Add columns to [pg_stats](#view-pg-stats) to report range-type histogram information (Egor Rogov, Soumyadeep Chakraborty) [](https://postgr.es/c/bc3c8db8a)

#### Indexes

- Allow [btree](#btree) indexes to more efficiently find a set of values, such as those supplied by `IN` clauses using constants (Peter Geoghegan, Matthias van de Meent) [](https://postgr.es/c/5bf748b86)

- Allow [BRIN](#brin) indexes to be created using parallel workers (Tomas Vondra, Matthias van de Meent) [](https://postgr.es/c/b43757171)

#### General Performance

- Allow vacuum to more efficiently remove and freeze tuples (Melanie Plageman, Heikki Linnakangas) [](https://postgr.es/c/6dbb49026)

  WAL traffic caused by vacuum is also more compact.

- Allow vacuum to more efficiently store tuple references (Masahiko Sawada, John Naylor) [](https://postgr.es/c/ee1b30f12) [](https://postgr.es/c/30e144287) [](https://postgr.es/c/667e65aac) [](https://postgr.es/c/6dbb49026)

  Additionally, vacuum is no longer silently limited to one gigabyte of memory when [???](#guc-maintenance-work-mem) or [???](#guc-autovacuum-work-mem) are higher.

- Optimize vacuuming of relations with no indexes (Melanie Plageman) [](https://postgr.es/c/c120550ed)

- Increase default [???](#guc-vacuum-buffer-usage-limit) to 2MB (Thomas Munro) [](https://postgr.es/c/98f320eb2)

- Improve performance when checking roles with many memberships (Nathan Bossart) [](https://postgr.es/c/d365ae705)

- Improve performance of heavily-contended WAL writes (Bharath Rupireddy) [](https://postgr.es/c/71e4cc6b8)

- Improve performance when transferring large blocks of data to a client (Melih Mutlu) [](https://postgr.es/c/c4ab7da60)

- Allow the grouping of file system reads with the new system variable [???](#guc-io-combine-limit) (Thomas Munro, Andres Freund, Melanie Plageman, Nazir Bilal Yavuz) [](https://postgr.es/c/210622c60) [](https://postgr.es/c/b7b0f3f27) [](https://postgr.es/c/041b96802)

#### Monitoring

- Create system view [pg_stat_checkpointer](#monitoring-pg-stat-checkpointer-view) (Bharath Rupireddy, Anton A. Melnikov, Alexander Korotkov) [](https://postgr.es/c/96f052613) [](https://postgr.es/c/12915a58e) [](https://postgr.es/c/e820db5b5)

  Relevant columns have been removed from [pg_stat_bgwriter](#pg-stat-bgwriter-view) and added to this new system view.

- Improve control over resetting statistics (Atsushi Torikoshi, Bharath Rupireddy) [](https://postgr.es/c/23c8c0c8f) [](https://postgr.es/c/2e8a0edc2) [](https://postgr.es/c/e5cca6288)

  Allow [`pg_stat_reset_shared()`](#monitoring-stats-funcs-table) (with no arguments) and pg_stat_reset_shared(`NULL`) to reset all shared statistics. Allow pg_stat_reset_shared('slru') and [`pg_stat_reset_slru()`](#monitoring-stats-funcs-table) (with no arguments) to reset SLRU statistics, which was already possible with pg_stat_reset_slru(NULL).

- Add log messages related to WAL recovery from backups (Andres Freund) [](https://postgr.es/c/1d35f705e)

- Add [???](#guc-log-connections) log line for `trust` connections (Jacob Champion) [](https://postgr.es/c/e48b19c5d)

- Add log message to report walsender acquisition and release of replication slots (Bharath Rupireddy) [](https://postgr.es/c/7c3fb505b)

  This is enabled by the server variable [???](#guc-log-replication-commands).

- Add system view [pg_wait_events](#view-pg-wait-events) that reports wait event types (Bertrand Drouvot) [](https://postgr.es/c/1e68e43d3)

  This is useful for adding descriptions to wait events reported in [pg_stat_activity](#monitoring-pg-stat-activity-view).

- Add [wait events](#view-pg-wait-events) for checkpoint delays (Thomas Munro) [](https://postgr.es/c/0013ba290)

- Allow vacuum to report the progress of index processing (Sami Imseih) [](https://postgr.es/c/46ebdfe16)

  This appears in system view [pg_stat_progress_vacuum](#pg-stat-progress-vacuum-view) columns indexes_total and indexes_processed.

#### Privileges

- Allow granting the right to perform maintenance operations (Nathan Bossart) [](https://postgr.es/c/ecb0fd337)

  The permission can be granted on a per-table basis using the [`MAINTAIN`](#ddl-priv-maintain) privilege and on a per-role basis via the [`pg_maintain`](#predefined-roles) predefined role. Permitted operations are `VACUUM`, `ANALYZE`, `REINDEX`, `REFRESH MATERIALIZED VIEW`, `CLUSTER`, and `LOCK TABLE`.

- Allow roles with [`pg_monitor`](#predefined-roles) membership to execute [`pg_current_logfile()`](#functions-info-session-table) (Pavlo Golub, Nathan Bossart) [](https://postgr.es/c/8d8afd48d)

#### Server Configuration

- Add system variable [???](#guc-allow-alter-system) to disallow [`ALTER SYSTEM`](#sql-altersystem) (Jelte Fennema-Nio, Gabriele Bartolini) [](https://postgr.es/c/d3ae2a24f)

- Allow [`ALTER SYSTEM`](#sql-altersystem) to set unrecognized custom server variables (Tom Lane) [](https://postgr.es/c/2d870b4ae)

  This is also possible with [`GRANT ON PARAMETER`](#sql-grant).

- Add server variable [???](#guc-transaction-timeout) to restrict the duration of transactions (Andrey Borodin, Japin Li, Junwang Zhao, Alexander Korotkov) [](https://postgr.es/c/51efe38cb) [](https://postgr.es/c/bf82f4379) [](https://postgr.es/c/28e858c0f)

- Add a builtin platform-independent collation provider (Jeff Davis) [](https://postgr.es/c/2d819a08a) [](https://postgr.es/c/846311051) [](https://postgr.es/c/f69319f2f) [](https://postgr.es/c/9acae56ce)

  This supports `C` and `C.UTF-8` collations.

- Add server variable [???](#guc-huge-pages-status) to report the use of huge pages by Postgres (Justin Pryzby) [](https://postgr.es/c/a14354cac)

  This is useful when [???](#guc-huge-pages) is set to `try`.

- Add server variable to disable event triggers (Daniel Gustafsson) [](https://postgr.es/c/7750fefdb)

  The setting, [???](#guc-event-triggers), allows for the temporary disabling of event triggers for debugging.

- Allow the [SLRU](#monitoring-pg-stat-slru-view) cache sizes to be configured (Andrey Borodin, Dilip Kumar, Alvaro Herrera) [](https://postgr.es/c/53c2a97a9)

  The new server variables are [???](#guc-commit-timestamp-buffers), [???](#guc-multixact-member-buffers), [???](#guc-multixact-offset-buffers), [???](#guc-notify-buffers), [???](#guc-serializable-buffers), [???](#guc-subtransaction-buffers), and [???](#guc-transaction-buffers). [???](#guc-commit-timestamp-buffers), [???](#guc-transaction-buffers), and [???](#guc-subtransaction-buffers) scale up automatically with [???](#guc-shared-buffers).

#### Streaming Replication and Recovery

- Add support for incremental file system backup (Robert Haas, Jakub Wartak, Tomas Vondra) [](https://postgr.es/c/dc2123400) [](https://postgr.es/c/f8ce4ed78)

  Incremental backups can be created using [pg_basebackup](#app-pgbasebackup)'s new `--incremental` option. The new application [pg_combinebackup](#app-pgcombinebackup) allows manipulation of base and incremental file system backups.

- Allow the creation of WAL summarization files (Robert Haas, Nathan Bossart, Hubert Depesz Lubaczewski) [](https://postgr.es/c/174c48050) [](https://postgr.es/c/d97ef756a) [](https://postgr.es/c/f896057e4) [](https://postgr.es/c/d9ef650fc)

  These files record the block numbers that have changed within an [LSN](#datatype-pg-lsn) range and are useful for incremental file system backups. This is controlled by the server variables [???](#guc-summarize-wal) and [???](#guc-wal-summary-keep-time), and introspected with [`pg_available_wal_summaries()`](#functions-wal-summary), `pg_wal_summary_contents()`, and `pg_get_wal_summarizer_state()`.

- Add the system identifier to file system [backup manifest](#backup-manifest-format) files (Amul Sul) [](https://postgr.es/c/2041bc427)

  This helps detect invalid WAL usage.

- Allow connection string value `dbname` to be written when [pg_basebackup](#app-pgbasebackup) writes connection information to `postgresql.auto.conf` (Vignesh C, Hayato Kuroda) [](https://postgr.es/c/a145f424d)

- Add column [pg_replication_slots.invalidation_reason](#view-pg-replication-slots) to report the reason for invalid slots (Shveta Malik, Bharath Rupireddy) [](https://postgr.es/c/007693f2a) [](https://postgr.es/c/6ae701b43)

- Add column [pg_replication_slots.inactive_since](#view-pg-replication-slots) to report slot inactivity duration (Bharath Rupireddy) [](https://postgr.es/c/a11f330b5) [](https://postgr.es/c/6d49c8d4b) [](https://postgr.es/c/6f132ed69)

- Add function [`pg_sync_replication_slots()`](#functions-replication-table) to synchronize logical replication slots (Hou Zhijie, Shveta Malik, Ajin Cherian, Peter Eisentraut) [](https://postgr.es/c/ddd5f4f54) [](https://postgr.es/c/7a424ece4)

- Add the `failover` property to the [replication protocol](#protocol-replication) (Hou Zhijie, Shveta Malik) [](https://postgr.es/c/732924043)

#### [Logical Replication](#logical-replication)

- Add application [pg_createsubscriber](#app-pgcreatesubscriber) to create a logical replica from a physical standby server (Euler Taveira) [](https://postgr.es/c/d44032d01)

- Have [pg_upgrade](#pgupgrade) migrate valid logical slots and subscriptions (Hayato Kuroda, Hou Zhijie, Vignesh C, Julien Rouhaud, Shlok Kyal) [](https://postgr.es/c/29d0a77fa) [](https://postgr.es/c/9a17be1e2)

  This allows logical replication to continue quickly after the upgrade. This only works for old PostgreSQL clusters that are version 17 or later.

- Enable the failover of [logical slots](#logical-replication-subscription-slot) (Hou Zhijie, Shveta Malik, Ajin Cherian) [](https://postgr.es/c/c393308b6)

  This is controlled by an optional fifth argument to [`pg_create_logical_replication_slot()`](#functions-replication-table).

- Add server variable [???](#guc-sync-replication-slots) to enable failover logical slot synchronization (Shveta Malik, Hou Zhijie, Peter Smith) [](https://postgr.es/c/93db6cbda) [](https://postgr.es/c/60c07820d)

- Add logical replication failover control to [`CREATE/ALTER SUBSCRIPTION`](#sql-createsubscription) (Shveta Malik, Hou Zhijie, Ajin Cherian) [](https://postgr.es/c/776621a5e) [](https://postgr.es/c/22f7e61a6)

- Allow the application of logical replication changes to use [hash](#hash-index) indexes on the subscriber (Hayato Kuroda) [](https://postgr.es/c/edca34243)

  Previously only [btree](#btree) indexes could be used for this purpose.

- Improve [logical decoding](#logicaldecoding) performance in cases where there are many subtransactions (Masahiko Sawada) [](https://postgr.es/c/5bec1d6bc)

- Restart apply workers if subscription owner's superuser privileges are revoked (Vignesh C) [](https://postgr.es/c/79243de13)

  This forces reauthentication.

- Add `flush` option to [`pg_logical_emit_message()`](#functions-replication-table) (Michael Paquier) [](https://postgr.es/c/173b56f1e)

  This makes the message durable.

- Allow specification of physical standbys that must be synchronized before they are visible to subscribers (Hou Zhijie, Shveta Malik) [](https://postgr.es/c/bf279ddd1) [](https://postgr.es/c/0f934b073)

  The new server variable is [???](#guc-synchronized-standby-slots).

- Add worker type column to [pg_stat_subscription](#monitoring-pg-stat-subscription) (Peter Smith) [](https://postgr.es/c/13aeaf079)

### Utility Commands

- Add new [`COPY`](#sql-copy) option `ON_ERROR ignore` to discard error rows (Damir Belyalov, Atsushi Torikoshi, Alex Shulgin, Jian He, Yugo Nagata) [](https://postgr.es/c/9e2d87011) [](https://postgr.es/c/b725b7eec) [](https://postgr.es/c/40bbc8cf0) [](https://postgr.es/c/a6d0fa5ef)

  The default behavior is `ON_ERROR stop`.

- Add new `COPY` option `LOG_VERBOSITY` which reports `COPY FROM` ignored error rows (Bharath Rupireddy) [](https://postgr.es/c/f5a227895)

- Allow `COPY FROM` to report the number of skipped rows during processing (Atsushi Torikoshi) [](https://postgr.es/c/729439607)

  This appears in system view column [pg_stat_progress_copy.tuples_skipped](#copy-progress-reporting).

- In `COPY FROM`, allow easy specification that all columns should be forced null or not null (Zhang Mingli) [](https://postgr.es/c/f6d4c9cf1)

- Allow partitioned tables to have identity columns (Ashutosh Bapat) [](https://postgr.es/c/699586315)

- Allow [exclusion constraints](#ddl-constraints-exclusion) on partitioned tables (Paul A. Jungwirth) [](https://postgr.es/c/8c852ba9a)

  As long as exclusion constraints compare partition key columns for equality, other columns can use exclusion constraint-specific comparisons.

- Add clearer [`ALTER TABLE`](#sql-altertable) method to set a column to the default statistics target (Peter Eisentraut) [](https://postgr.es/c/4f622503d)

  The new syntax is `ALTER TABLE ... SET STATISTICS DEFAULT`; using `SET STATISTICS -1` is still supported.

- Allow `ALTER TABLE` to change a column's generation expression (Amul Sul) [](https://postgr.es/c/5d06e99a3)

  The syntax is `ALTER TABLE ... ALTER COLUMN ... SET EXPRESSION`.

- Allow specification of [table access methods](#tableam) on partitioned tables (Justin Pryzby, Soumyadeep Chakraborty, Michael Paquier) [](https://postgr.es/c/374c7a229) [](https://postgr.es/c/e2395cdbe)

- Add `DEFAULT` setting for `ALTER TABLE .. SET ACCESS METHOD` (Michael Paquier) [](https://postgr.es/c/d61a6cad6)

- Add support for [event triggers](#sql-createeventtrigger) that fire at connection time (Konstantin Knizhnik, Mikhail Gribkov) [](https://postgr.es/c/e83d1b0c4)

- Add event trigger support for [`REINDEX`](#sql-reindex) (Garrett Thornburg, Jian He) [](https://postgr.es/c/f21848de2)

- Allow parenthesized syntax for [`CLUSTER`](#sql-cluster) options if a table name is not specified (Nathan Bossart) [](https://postgr.es/c/cdaedfc96)

#### [`EXPLAIN`](#sql-explain)

- Allow `EXPLAIN` to report optimizer memory usage (Ashutosh Bapat) [](https://postgr.es/c/5de890e36)

  The option is called `MEMORY`.

- Add `EXPLAIN` option `SERIALIZE` to report the cost of converting data for network transmission (Stepan Rutz, Matthias van de Meent) [](https://postgr.es/c/06286709e)

- Add local I/O block read/write timing statistics to `EXPLAIN`'s `BUFFERS` output (Nazir Bilal Yavuz) [](https://postgr.es/c/295c36c0c)

- Improve `EXPLAIN`'s display of SubPlan nodes and output parameters (Tom Lane, Dean Rasheed) [](https://postgr.es/c/fd0398fcb)

- Add JIT `deform_counter` details to `EXPLAIN` (Dmitry Dolgov) [](https://postgr.es/c/5a3423ad8)

### Data Types

- Allow the `interval` data type to support `+/-infinity` values (Joseph Koshakow, Jian He, Ashutosh Bapat) [](https://postgr.es/c/519fc1bd9)

- Allow the use of an [`ENUM`](#datatype-enum) added via [`ALTER TYPE`](#sql-altertype) if the type was created in the same transaction (Tom Lane) [](https://postgr.es/c/af1d39584)

  This was previously disallowed.

### [MERGE](#sql-merge)

- Allow `MERGE` to modify updatable views (Dean Rasheed) [](https://postgr.es/c/5f2e179bd)

- Add `WHEN NOT MATCHED BY SOURCE` to `MERGE` (Dean Rasheed) [](https://postgr.es/c/0294df2f1)

  `WHEN NOT MATCHED` on target rows was already supported.

- Allow `MERGE` to use the `RETURNING` clause (Dean Rasheed) [](https://postgr.es/c/c649fa24a)

  The new `RETURNING` function `merge_action()` reports on the DML that generated the row.

### Functions

- Add function [`JSON_TABLE()`](#functions-sqljson-table) to convert `JSON` data to a table representation (Nikita Glukhov, Teodor Sigaev, Oleg Bartunov, Alexander Korotkov, Andrew Dunstan, Amit Langote, Jian He) [](https://postgr.es/c/de3600452) [](https://postgr.es/c/bb766cde6)

  This function can be used in the `FROM` clause of `SELECT` queries as a tuple source.

- Add SQL/JSON constructor functions [`JSON()`](#functions-json-creation-table), `JSON_SCALAR()`, and `JSON_SERIALIZE()` (Nikita Glukhov, Teodor Sigaev, Oleg Bartunov, Alexander Korotkov, Andrew Dunstan, Amit Langote) [](https://postgr.es/c/03734a7fe)

- Add SQL/JSON query functions [`JSON_EXISTS()`](#functions-sqljson-querying), `JSON_QUERY()`, and `JSON_VALUE()` (Nikita Glukhov, Teodor Sigaev, Oleg Bartunov, Alexander Korotkov, Andrew Dunstan, Amit Langote, Peter Eisentraut, Jian He) [](https://postgr.es/c/aaaf9449e) [](https://postgr.es/c/1edb3b491) [](https://postgr.es/c/6185c9737) [](https://postgr.es/c/c0fc07518) [](https://postgr.es/c/ef744ebb7)

- Add [jsonpath](#functions-sqljson-path-operators) methods to convert `JSON` values to other `JSON` data types (Jeevan Chalke) [](https://postgr.es/c/66ea94e8e)

  The jsonpath methods are `.bigint()`, `.boolean()`, `.date()`, `.decimal([precision [, scale]])`, `.integer()`, `.number()`, `.string()`, `.time()`, `.time_tz()`, `.timestamp()`, and `.timestamp_tz()`.

- Add [`to_timestamp()`](#functions-formatting-table) time zone format specifiers (Tom Lane) [](https://postgr.es/c/8ba6fdf90)

  `TZ` accepts time zone abbreviations or numeric offsets, while `OF` accepts only numeric offsets.

- Allow the session [time zone](#guc-timezone) to be specified by `AT LOCAL` (Vik Fearing) [](https://postgr.es/c/97957fdba)

  This is useful when converting adding and removing time zones from time stamps values, rather than specifying the literal session time zone.

- Add functions [`uuid_extract_timestamp()`](#functions-uuid) and `uuid_extract_version()` to return UUID information (Andrey Borodin) [](https://postgr.es/c/794f10f6b)

- Add functions to generate random numbers in a specified range (Dean Rasheed) [](https://postgr.es/c/e6341323a)

  The functions are [`random(min, max)`](#functions-math-random-table) and they take values of type `integer`, `bigint`, and `numeric`.

- Add functions to convert integers to binary and octal strings (Eric Radman, Nathan Bossart) [](https://postgr.es/c/260a1f18d)

  The functions are [`to_bin()`](#functions-string-other) and `to_oct()`.

- Add Unicode informational functions (Jeff Davis) [](https://postgr.es/c/a02b37fc0)

  Function [`unicode_version()`](#functions-info-version) returns the Unicode version, `icu_unicode_version()` returns the ICU version, and `unicode_assigned()` returns if the characters are assigned Unicode codepoints.

- Add function [`xmltext()`](#functions-producing-xml-xmltext) to convert text to a single `XML` text node (Jim Jones) [](https://postgr.es/c/526fe0d79)

- Add function [`to_regtypemod()`](#functions-info-catalog-table) to return the type modifier of a type specification (David Wheeler, Erik Wienhold) [](https://postgr.es/c/1218ca995)

- Add [`pg_basetype()`](#functions-info-catalog-table) function to return a domain's base type (Steve Chavez) [](https://postgr.es/c/b154d8a6d)

- Add function [`pg_column_toast_chunk_id()`](#functions-admin-dbsize) to return a value's [TOAST](#storage-toast) identifier (Yugo Nagata) [](https://postgr.es/c/d1162cfda)

  This returns `NULL` if the value is not stored in TOAST.

### [PL/pgSQL](#plpgsql)

- Allow plpgsql [`%TYPE`](#plpgsql-declaration-type) and `%ROWTYPE` specifications to represent arrays of non-array types (Quan Zongliang, Pavel Stehule) [](https://postgr.es/c/5e8674dc8)

- Allow plpgsql `%TYPE` specification to reference composite column (Tom Lane) [](https://postgr.es/c/43b46aae1)

### [libpq](#libpq)

- Add libpq function to change role passwords (Joe Conway) [](https://postgr.es/c/a7be2a6c2)

  The new function, [`PQchangePassword()`](#libpq-PQchangePassword), hashes the new password before sending it to the server.

- Add libpq functions to close portals and prepared statements (Jelte Fennema-Nio) [](https://postgr.es/c/28b572656)

  The functions are [`PQclosePrepared()`](#libpq-PQclosePrepared), [`PQclosePortal()`](#libpq-PQclosePortal), [`PQsendClosePrepared()`](#libpq-PQsendClosePrepared), and [`PQsendClosePortal()`](#libpq-PQsendClosePortal).

- Add libpq API which allows for blocking and non-blocking [cancel requests](#libpq-cancel), with encryption if already in use (Jelte Fennema-Nio) [](https://postgr.es/c/61461a300)

  Previously only blocking, unencrypted cancel requests were supported.

- Add libpq function [`PQsocketPoll()`](#libpq-PQsocketPoll) to allow polling of network sockets (Tristan Partin, Tom Lane) [](https://postgr.es/c/f5e4dedfa) [](https://postgr.es/c/105024a47)

- Add libpq function [`PQsendPipelineSync()`](#libpq-PQsendPipelineSync) to send a pipeline synchronization point (Anton Kirilov) [](https://postgr.es/c/4794c2d31)

  This is similar to [`PQpipelineSync()`](#libpq-PQpipelineSync) but it does not flush to the server unless the size threshold of the output buffer is reached.

- Add libpq function [`PQsetChunkedRowsMode()`](#libpq-PQsetChunkedRowsMode) to allow retrieval of results in chunks (Daniel Vrit) [](https://postgr.es/c/4643a2b26)

- Allow TLS connections without requiring a network round-trip negotiation (Greg Stark, Heikki Linnakangas, Peter Eisentraut, Michael Paquier, Daniel Gustafsson) [](https://postgr.es/c/d39a49c1e) [](https://postgr.es/c/91044ae4b) [](https://postgr.es/c/44e27f0a6) [](https://postgr.es/c/d80f2ce29) [](https://postgr.es/c/03a0e0d4b) [](https://postgr.es/c/17a834a04) [](https://postgr.es/c/407e0b023) [](https://postgr.es/c/fb5718f35)

  This is enabled with the client-side option [`sslnegotiation=direct`](#libpq-connect-sslnegotiation), requires ALPN, and only works on PostgreSQL 17 and later servers.

### [???](#app-psql)

- Improve psql display of default and empty privileges (Erik Wienhold, Laurenz Albe) [](https://postgr.es/c/d1379ebf4)

  Command `\dp` now displays `(none)` for empty privileges; default still displays as empty.

- Have backslash commands honor `\pset null` (Erik Wienhold, Laurenz Albe) [](https://postgr.es/c/d1379ebf4)

  Previously `\pset null` was ignored.

- Allow psql's `\watch` to stop after a minimum number of rows returned (Greg Sabino Mullane) [](https://postgr.es/c/f347ec76e)

  The parameter is `min_rows`.

- Allow psql connection attempts to be canceled with control-C (Tristan Partin) [](https://postgr.es/c/cafe10565)

- Allow psql to honor `FETCH_COUNT` for non-`SELECT` queries (Daniel Vrit) [](https://postgr.es/c/90f517821)

- Improve psql tab completion (Dagfinn Ilmari Mannsker, Gilles Darold, Christoph Heiss, Steve Chavez, Vignesh C, Pavel Borisov, Jian He) [](https://postgr.es/c/c951e9042) [](https://postgr.es/c/d16eb83ab) [](https://postgr.es/c/cd3424748) [](https://postgr.es/c/816f10564) [](https://postgr.es/c/927332b95) [](https://postgr.es/c/f1bb9284f) [](https://postgr.es/c/304b6b1a6) [](https://postgr.es/c/2800fbb2b)

### Server Applications

- Add application [pg_walsummary](#app-pgwalsummary) to dump WAL summary files (Robert Haas) [](https://postgr.es/c/ee1bfd168)

- Allow [pg_dump](#app-pgdump)'s large objects to be restorable in batches (Tom Lane) [](https://postgr.es/c/a45c78e32)

  This allows the restoration of many large objects to avoid transaction limits and to be restored in parallel.

- Add pg_dump option `--exclude-extension` (Ayush Vatsa) [](https://postgr.es/c/522ed12f7)

- Allow [pg_dump](#app-pgdump), [pg_dumpall](#app-pg-dumpall), and [pg_restore](#app-pgrestore) to specify include/exclude objects in a file (Pavel Stehule, Daniel Gustafsson) [](https://postgr.es/c/a5cf808be)

  The option is called `--filter`.

- Add the `--sync-method` parameter to several client applications (Justin Pryzby, Nathan Bossart) [](https://postgr.es/c/8c16ad3b4)

  The applications are [initdb](#app-initdb), [pg_basebackup](#app-pgbasebackup), [pg_checksums](#app-pgchecksums), [pg_dump](#app-pgdump), [pg_rewind](#app-pgrewind), and [pg_upgrade](#pgupgrade).

- Add [pg_restore](#app-pgrestore) option `--transaction-size` to allow object restores in transaction batches (Tom Lane) [](https://postgr.es/c/959b38d77)

  This allows the performance benefits of transaction batches without the problems of excessively large transaction blocks.

- Change [pgbench](#pgbench) debug mode option from `-d` to `--debug` (Greg Sabino Mullane) [](https://postgr.es/c/3ff01b2b6)

  Option `-d` is now used for the database name, and the new `--dbname` option can be used as well.

- Add pgbench option `--exit-on-abort` to exit after any client aborts (Yugo Nagata) [](https://postgr.es/c/3c662643c)

- Add pgbench command `\syncpipeline` to allow sending of sync messages (Anthonin Bonnefoy) [](https://postgr.es/c/94edfe250)

- Allow [pg_archivecleanup](#pgarchivecleanup) to remove backup history files (Atsushi Torikoshi) [](https://postgr.es/c/3f8c98d0b)

  The option is `--clean-backup-history`.

- Add some long options to pg_archivecleanup (Atsushi Torikoshi) [](https://postgr.es/c/dd7c60f19)

  The long options are `--debug`, `--dry-run`, and `--strip-extension`.

- Allow [pg_basebackup](#app-pgbasebackup) and [pg_receivewal](#app-pgreceivewal) to use dbname in their connection specification (Jelte Fennema-Nio) [](https://postgr.es/c/cca97ce6a)

  This is useful for connection poolers that are sensitive to the database name.

- Add [pg_upgrade](#pgupgrade) option `--copy-file-range` (Thomas Munro) [](https://postgr.es/c/d93627bcb)

  This is supported on `Linux` and `FreeBSD`.

- Allow [reindexdb](#app-reindexdb) `--index` to process indexes from different tables in parallel (Maxim Orlov, Svetlana Derevyanko, Alexander Korotkov) [](https://postgr.es/c/47f99a407)

- Allow [reindexdb](#app-reindexdb), [vacuumdb](#app-vacuumdb), and [clusterdb](#app-clusterdb) to process objects in all databases matching a pattern (Nathan Bossart) [](https://postgr.es/c/24c928ad9) [](https://postgr.es/c/648928c79) [](https://postgr.es/c/1b49d56d3)

  The new option `--all` controls this behavior.

### Source Code

- Remove support for OpenSSL 1.0.1 (Michael Paquier) [](https://postgr.es/c/8e278b657)

- Allow tests to pass in OpenSSL FIPS mode (Peter Eisentraut) [](https://postgr.es/c/284cbaea7) [](https://postgr.es/c/3c44e7d8d)

- Use CPU AVX-512 instructions for bit counting (Paul Amonson, Nathan Bossart, Ants Aasma) [](https://postgr.es/c/792752af4) [](https://postgr.es/c/41c51f0c6)

- Require LLVM version 10 or later (Thomas Munro) [](https://postgr.es/c/820b5af73)

- Use native CRC instructions on 64-bit LoongArch CPUs (Xudong Yang) [](https://postgr.es/c/4d14ccd6a)

- Remove `AIX` support (Heikki Linnakangas) [](https://postgr.es/c/0b16bb877)

- Remove the Microsoft Visual Studio-specific PostgreSQL build option (Michael Paquier) [](https://postgr.es/c/1301c80b2)

  Meson is now the only available method for Visual Studio builds.

- Remove configure option `--disable-thread-safety` (Thomas Munro, Heikki Linnakangas) [](https://postgr.es/c/68a4b58ec) [](https://postgr.es/c/ce0b0fa3e)

  We now assume all supported platforms have sufficient thread support.

- Remove configure option `--with-CC` (Heikki Linnakangas) [](https://postgr.es/c/1c1eec0f2)

  Setting the `CC` environment variable is now the only supported method for specifying the compiler.

- User-defined data type receive functions will no longer receive their data null-terminated (David Rowley) [](https://postgr.es/c/f0efa5aec)

- Add incremental `JSON` parser for use with huge `JSON` documents (Andrew Dunstan) [](https://postgr.es/c/3311ea86e)

- Convert top-level `README` file to Markdown (Nathan Bossart) [](https://postgr.es/c/363eb0599)

- Remove no longer needed top-level `INSTALL` file (Tom Lane) [](https://postgr.es/c/e2b73f4a4)

- Remove make's `distprep` option (Peter Eisentraut) [](https://postgr.es/c/721856ff2)

- Add make support for Android shared libraries (Peter Eisentraut) [](https://postgr.es/c/79b03dbb3)

- Add backend support for injection points (Michael Paquier) [](https://postgr.es/c/d86d20f0b) [](https://postgr.es/c/37b369dc6) [](https://postgr.es/c/f587338de) [](https://postgr.es/c/bb93640a6)

  This is used for server debugging and they must be enabled at server compile time.

- Add dynamic shared memory registry (Nathan Bossart) [](https://postgr.es/c/8b2bcf3f2)

  This allows shared libraries which are not initialized at startup to coordinate dynamic shared memory access.

- Fix `emit_log_hook` to use the same time value as other log records for the same query (Kambam Vinay, Michael Paquier) [](https://postgr.es/c/2a217c371)

- Improve documentation for using `jsonpath` for predicate checks (David Wheeler) [](https://postgr.es/c/7014c9a4b)

### Additional Modules

- Allow joins with non-join qualifications to be pushed down to foreign servers and custom scans (Richard Guo, Etsuro Fujita) [](https://postgr.es/c/9e9931d2b)

  Foreign data wrappers and custom scans will need to be modified to handle these cases.

- Allow pushdown of `EXISTS` and `IN` subqueries to [???](#postgres-fdw) foreign servers (Alexander Pyhalov) [](https://postgr.es/c/824dbea3e)

- Increase the default foreign data wrapper tuple cost (David Rowley, Umair Shahid) [](https://postgr.es/c/cac169d68) [](https://postgr.es/c/f7f694b21)

  This value is used by the optimizer.

- Allow [dblink](#dblink) database operations to be interrupted (Noah Misch) [](https://postgr.es/c/d3c5f37dd)

- Allow the creation of hash indexes on [???](#ltree) columns (Tommy Pavlicek) [](https://postgr.es/c/485f0aa85)

  This also enables hash join and hash aggregation on ltree columns.

- Allow [???](#unaccent) character translation rules to contain whitespace and quotes (Michael Paquier) [](https://postgr.es/c/59f47fb98)

  The syntax for the `unaccent.rules` file has changed.

- Allow [???](#amcheck) to check for unique constraint violations using new option `--checkunique` (Anastasia Lubennikova, Pavel Borisov, Maxim Orlov) [](https://postgr.es/c/5ae208720)

- Allow [???](#citext) tests to pass in OpenSSL FIPS mode (Peter Eisentraut) [](https://postgr.es/c/3c551ebed)

- Allow [???](#pgcrypto) tests to pass in OpenSSL FIPS mode (Peter Eisentraut) [](https://postgr.es/c/795592865)

- Remove some unused [SPI](#spi) macros (Bharath Rupireddy) [](https://postgr.es/c/75680c3d8)

- Allow [`ALTER OPERATOR`](#sql-alteroperator) to set more optimization attributes (Tommy Pavlicek) [](https://postgr.es/c/2b5154bea)

  This is useful for extensions.

- Allow extensions to define [custom wait events](#xfunc-addin-wait-events) (Masahiro Ikeda) [](https://postgr.es/c/c9af05465) [](https://postgr.es/c/c8e318b1b) [](https://postgr.es/c/d61f2538a) [](https://postgr.es/c/c789f0f6c)

  Custom wait events have been added to [???](#postgres-fdw) and [???](#dblink).

- Add [???](#pgbuffercache) function `pg_buffercache_evict()` to allow shared buffer eviction (Palak Chaturvedi, Thomas Munro) [](https://postgr.es/c/13453eedd)

  This is useful for testing.

#### [pg_stat_statements](#pgstatstatements)

- Replace [`CALL`](#sql-call) parameters in pg_stat_statements with placeholders (Sami Imseih) [](https://postgr.es/c/11c34b342)

- Replace savepoint names stored in pg_stat_statements with placeholders (Greg Sabino Mullane) [](https://postgr.es/c/31de7e60d)

  This greatly reduces the number of entries needed to record [`SAVEPOINT`](#sql-savepoint), [`RELEASE SAVEPOINT`](#sql-release-savepoint), and [`ROLLBACK TO SAVEPOINT`](#sql-rollback-to) commands.

- Replace the two-phase commit GIDs stored in pg_stat_statements with placeholders (Michael Paquier) [](https://postgr.es/c/638d42a3c)

  This greatly reduces the number of entries needed to record [`PREPARE TRANSACTION`](#sql-prepare-transaction), [`COMMIT PREPARED`](#sql-commit-prepared), and [`ROLLBACK PREPARED`](#sql-rollback-prepared).

- Track [`DEALLOCATE`](#sql-deallocate) in pg_stat_statements (Dagfinn Ilmari Mannsker, Michael Paquier) [](https://postgr.es/c/bb45156f3)

  `DEALLOCATE` names are stored in pg_stat_statements as placeholders.

- Add local I/O block read/write timing statistics columns of pg_stat_statements (Nazir Bilal Yavuz) [](https://postgr.es/c/295c36c0c) [](https://postgr.es/c/5147ab1dd)

  The new columns are local_blk_read_time and local_blk_write_time.

- Add JIT deform_counter details to pg_stat_statements (Dmitry Dolgov) [](https://postgr.es/c/5a3423ad8)

- Add optional fourth argument (`minmax_only`) to `pg_stat_statements_reset()` to allow for the resetting of only min/max statistics (Andrei Zubkov) [](https://postgr.es/c/dc9f8a798)

  This argument defaults to `false`.

- Add pg_stat_statements columns stats_since and minmax_stats_since to track entry creation time and last min/max reset time (Andrei Zubkov) [](https://postgr.es/c/dc9f8a798)

## Acknowledgments

The following individuals (in alphabetical order) have contributed to this release as patch authors, committers, reviewers, testers, or reporters of issues.

Abhijit Menon-Sen

Adnan Dautovic

Aidar Imamov

Ajin Cherian

Akash Shankaran

Akshat Jaimini

Alaa Attya

Aleksander Alekseev

Aleksej Orlov

Alena Rybakina

Alex Hsieh

Alex Malek

Alex Shulgin

Alex Work

Alexander Korotkov

Alexander Kozhemyakin

Alexander Kuzmenkov

Alexander Lakhin

Alexander Pyhalov

Alexey Palazhchenko

Alfons Kemper

Álvaro Herrera

Amadeo Gallardo

Amit Kapila

Amit Langote

Amul Sul

Anastasia Lubennikova

Anatoly Zaretsky

Andreas Karlsson

Andreas Ulbrich

Andrei Lepikhov

Andrei Zubkov

Andres Freund

Andrew Alsup

Andrew Atkinson

Andrew Bille

Andrew Dunstan

Andrew Kane

Andrey Borodin

Andrey Rachitskiy

Andrey Sokolov

Andy Fan

Anthonin Bonnefoy

Anthony Hsu

Anton Kirilov

Anton Melnikov

Anton Voloshin

Antonin Houska

Ants Aasma

Antti Lampinen

Aramaki Zyake

Artem Anisimov

Artur Zakirov

Ashutosh Bapat

Ashutosh Sharma

Atsushi Torikoshi

Attila Gulyás

Ayush Tiwari

Ayush Vatsa

Bartosz Chrol

Benoît Ryder

Bernd Helmle

Bertrand Drouvot

Bharath Rupireddy

Bo Andreson

Boshomi Phenix

Bowen Shi

Boyu Yang

Bruce Momjian

Cameron Vogt

Cary Huang

Cédric Villemain

Changhong Fei

Chantal Keller

Chapman Flack

Chengxi Sun

Chris Travers

Christian Maurer

Christian Stork

Christoph Berg

Christoph Heiss

Christophe Courtois

Christopher Kline

Claudio Freire

Colin Caine

Corey Huinker

Curt Kolovson

Dag Lem

Dagfinn Ilmari Mannsåker

Damir Belyalov

Daniel Fredouille

Daniel Gustafsson

Daniel Shelepanov

Daniel Vérité

Daniel Westermann

Darren Rush

Dave Cramer

Dave Page

David Christensen

David Cook

David G. Johnston

David Geier

David Hillman

David Perez

David Rowley

David Steele

David Wheeler

David Zhang

Dean Rasheed

Denis Erokhin

Denis Laxalde

Devrim Gündüz

Dilip Kumar

Dimitrios Apostolou

Dmitry Dolgov

Dmitry Koval

Dmitry Vasiliev

Dominique Devienne

Dong Wook Lee

Donghang Lin

Dongming Liu

Drew Callahan

Drew Kimball

Dzmitry Jachnik

Egor Chindyaskin

Egor Rogov

Ekaterina Kiryanova

Elena Indrupskaya

Elizabeth Christensen

Emre Hasegeli

Eric Cyr

Eric Mutta

Eric Radman

Eric Ridge

Erik Rijkers

Erik Wienhold

Erki Eessaar

Ethan Mertz

Etsuro Fujita

Eugen Konkov

Euler Taveira

Evan Macbeth

Evgeny Morozov

Fabien Coelho

Fabrízio de Royes Mello

Farias de Oliveira

Feliphe Pozzer

Fire Emerald

Flavien Guedez

Floris Van Nee

Francesco Degrassi

Frank Streitzig

Gabriele Bartolini

Garrett Thornburg

Gavin Flower

Gavin Panella

Gilles Darold

Gilles Parc

Grant Gryczan

Greg Nancarrow

Greg Sabino Mullane

Greg Stark

Gurjeet Singh

Haiying Tang

Hajime Matsunaga

Hal Takahara

Hanefi Onaldi

Hannu Krosing

Hans Buschmann

Hao Wu

Hao Zhang

Hayato Kuroda

Heikki Linnakangas

Hemanth Sandrana

Himanshu Upadhyaya

Hironobu Suzuki

Holger Reise

Hongxu Ma

Hongyu Song

Horst Reiterer

Hubert Lubaczewski

Hywel Carver

Ian Barwick

Ian Ilyasov

Ilya Nenashev

Isaac Morland

Israel Barth Rubio

Ivan Kartyshov

Ivan Kolombet

Ivan Lazarev

Ivan Panchenko

Ivan Trofimov

Jacob Champion

Jacob Speidel

Jacques Combrink

Jaime Casanova

Jakub Wartak

James Coleman

James Pang

Jani Rahkola

Japin Li

Jeevan Chalke

Jeff Davis

Jeff Janes

Jelte Fennema-Nio

Jeremy Schneider

Jian Guo

Jian He

Jim Jones

Jim Keener

Jim Nasby

Jingtang Zhang

Jingxian Li

Jingzhou Fu

Joe Conway

Joel Jacobson

John Ekins

John Hsu

John Morris

John Naylor

John Russell

Jonathan Katz

Jordi Gutiérrez

Joseph Koshakow

Josh Kupershmidt

Joshua D. Drake

Joshua Uyehara

Jubilee Young

Julien Rouhaud

Junwang Zhao

Justin Pryzby

Kaido Vaikla

Kambam Vinay

Karen Talarico

Karina Litskevich

Karl O. Pinc

Kashif Zeeshan

Kim Johan Andersson

Kirill Reshke

Kirk Parker

Kirk Wolak

Kisoon Kwon

Koen De Groote

Kohei KaiGai

Kong Man

Konstantin Knizhnik

Kouhei Sutou

Krishnakumar R

Kuntal Ghosh

Kurt Roeckx

Kyotaro Horiguchi

Lang Liu

Lars Kanis

Laurenz Albe

Lauri Laanmets

Legs Mansion

Lukas Fittl

Magnus Hagander

Mahendrakar Srinivasarao

Maiquel Grassi

Manos Emmanouilidis

Marcel Hofstetter

Marcos Pegoraro

Marian Krucina

Marina Polyakova

Mark Dilger

Mark Guertin

Mark Sloan

Markus Winand

Marlene Reiterer

Martín Marqués

Martin Nash

Martin Schlossarek

Masahiko Sawada

Masahiro Ikeda

Masaki Kuwamura

Masao Fujii

Mason Sharp

Matheus Alcantara

Mats Kindahl

Matthias Kuhn

Matthias van de Meent

Maxim Boguk

Maxim Orlov

Maxim Yablokov

Maxime Boyer

Melanie Plageman

Melih Mutlu

Merlin Moncure

Micah Gate

Michael Banck

Michael Bondarenko

Michael Paquier

Michael Wang

Michael Zhilin

Michail Nikolaev

Michal Bartak

Michal Kleczek

Mikhail Gribkov

Mingli Zhang

Miroslav Bendik

Mitsuru Hinata

Moaaz Assali

Muralikrishna Bandaru

Nathan Bossart

Nazir Bilal Yavuz

Neil Tiffin

Ngigi Waithaka

Nikhil Benesch

Nikhil Raj

Nikita Glukhov

Nikita Kalinin

Nikita Malakhov

Nikolay Samokhvalov

Nikolay Shaplov

Nisha Moond

Nishant Sharma

Nitin Jadhav

Noah Misch

Noriyoshi Shinoda

Ole Peder Brandtzæg

Oleg Bartunov

Oleg Sibiryakov

Oleg Tselebrovskiy

Olleg Samoylov

Onder Kalaci

Ondrej Navratil

Pablo Kharo

Palak Chaturvedi

Pantelis Theodosiou

Paul Amonson

Paul Jungwirth

Pavel Borisov

Pavel Kulakov

Pavel Luzanov

Pavel Stehule

Pavlo Golub

Pedro Gallegos

Pete Storer

Peter Eisentraut

Peter Geoghegan

Peter Smith

Philip Warner

Philipp Salvisberg

Pierre Ducroquet

Pierre Fortin

Przemyslaw Sztoch

Quynh Tran

Raghuveer Devulapalli

Ranier Vilela

Reid Thompson

Rian McGuire

Richard Guo

Richard Vesely

Ridvan Korkmaz

Robert Haas

Robert Scott

Robert Treat

Roberto Mello

Robins Tharakan

Roman Lozko

Ronan Dunklau

Rui Zhao

Ryo Matsumura

Ryoga Yoshida

Sameer Kumar

Sami Imseih

Samuel Dussault

Sanjay Minni

Satoru Koizumi

Sebastian Skalacki

Sergei Glukhov

Sergei Kornilov

Sergey Prokhorenko

Sergey Sargsyan

Sergey Shinderuk

Shaozhong Shi

Shaun Thomas

Shay Rojansky

Shihao Zhong

Shinya Kato

Shlok Kyal

Shruthi Gowda

Shubham Khanna

Shulin Zhou

Shveta Malik

Simon Riggs

Soumyadeep Chakraborty

Sravan Velagandula

Stan Hu

Stepan Neretin

Stepan Rutz

Stéphane Schildknecht

Stephane Tachoires

Stephen Frost

Steve Atkins

Steve Chavez

Suraj Khamkar

Suraj Kharage

Svante Richter

Svetlana Derevyanko

Sylvain Frandaz

Takayuki Tsunakawa

Tatsuo Ishii

Tatsuro Yamada

Tender Wang

Teodor Sigaev

Thom Brown

Thomas Munro

Tim Carey-Smith

Tim Needham

Tim Palmer

Tobias Bussmann

Tom Lane

Tomas Vondra

Tommy Pavlicek

Tomonari Katsumata

Tristan Partin

Tristen Raab

Tung Nguyen

Umair Shahid

Uwe Binder

Valerie Woolard

Vallimaharajan G

Vasya Boytsov

Victor Wagner

Victor Yegorov

Victoria Shepard

Vidushi Gupta

Vignesh C

Vik Fearing

Viktor Leis

Vinayak Pokale

Vitaly Burovoy

Vojtech Benes

Wei Sun

Wei Wang

Wenjiang Zhang

Will Mortensen

Willi Mann

Wolfgang Walther

Xiang Liu

Xiaoran Wang

Xing Guo

Xudong Yang

Yahor Yuzefovich

Yajun Hu

Yaroslav Saburov

Yong Li

Yongtao Huang

Yugo Nagata

Yuhang Qiu

Yuki Seino

Yura Sokolov

Yurii Rashkovskii

Yuuki Fujii

Yuya Watari

Yves Colin

Zhihong Yu

Zhijie Hou

Zongliang Quan

Zubeyr Eryilmaz

Zuming Jiang
