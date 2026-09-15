---
title: External Projects
source_url: https://www.postgresql.org/docs/17/external-projects.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: external-projects.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 520
---

## External Projects

PostgreSQL is a complex software project, and managing the project is difficult. We have found that many enhancements to PostgreSQL can be more efficiently developed separately from the core project.

## Client Interfaces

interfaces

externally maintained

There are only two client interfaces included in the base PostgreSQL distribution:

- [libpq](#libpq) is included because it is the primary C language interface, and because many other client interfaces are built on top of it.

- [ECPG](#ecpg) is included because it depends on the server-side SQL grammar, and is therefore sensitive to changes in PostgreSQL itself.

All other language interfaces are external projects and are distributed separately. A [list of language interfaces](https://wiki.postgresql.org/wiki/List_of_drivers) is maintained on the PostgreSQL wiki. Note that some of these packages are not released under the same license as PostgreSQL. For more information on each language interface, including licensing terms, refer to its website and documentation.

[](https://wiki.postgresql.org/wiki/List_of_drivers)

## Administration Tools

administration tools

externally maintained

There are several administration tools available for PostgreSQL. The most popular is [pgAdmin](https://www.pgadmin.org/), and there are several commercially available ones as well.

## Procedural Languages

procedural language

externally maintained

PostgreSQL includes several procedural languages with the base distribution: [PL/pgSQL](#plpgsql), [PL/Tcl](#pltcl), [PL/Perl](#plperl), and [PL/Python](#plpython).

In addition, there are a number of procedural languages that are developed and maintained outside the core PostgreSQL distribution. A list of [procedural languages](https://wiki.postgresql.org/wiki/PL_Matrix) is maintained on the PostgreSQL wiki. Note that some of these projects are not released under the same license as PostgreSQL. For more information on each procedural language, including licensing information, refer to its website and documentation.

[](https://wiki.postgresql.org/wiki/PL_Matrix)

## Extensions

extension

externally maintained

PostgreSQL is designed to be easily extensible. For this reason, extensions loaded into the database can function just like features that are built in. The `contrib/` directory shipped with the source code contains several extensions, which are described in [???](#contrib). Other extensions are developed independently, like [PostGIS](https://postgis.net/). Even PostgreSQL replication solutions can be developed externally. For example, [Slony-I](https://www.slony.info) is a popular primary/standby replication solution that is developed independently from the core project.
