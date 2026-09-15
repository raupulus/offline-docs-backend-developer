---
title: The Source Code Repository
source_url: https://www.postgresql.org/docs/17/sourcerepo.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: sourcerepo.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3520
---

## The Source Code Repository

The PostgreSQL source code is stored and managed using the Git version control system. A public mirror of the master repository is available; it is updated within a minute of any change to the master repository.

Our wiki, [](https://wiki.postgresql.org/wiki/Working_with_Git), has some discussion on working with Git.

## Getting the Source via Git

With Git you will make a copy of the entire code repository on your local machine, so you will have access to all history and branches offline. This is the fastest and most flexible way to develop or test patches.

1.  You will need an installed version of Git, which you can get from [](https://git-scm.com). Many systems already have a recent version of Git installed by default, or available in their package distribution system.

2.  To begin using the Git repository, make a clone of the official mirror:

        git clone https://git.postgresql.org/git/postgresql.git

    This will copy the full repository to your local machine, so it may take a while to complete, especially if you have a slow Internet connection. The files will be placed in a new subdirectory `postgresql` of your current directory.

3.  Whenever you want to get the latest updates in the system, `cd` into the repository, and run:

        git fetch

Git can do a lot more things than just fetch the source. For more information, consult the Git man pages, or see the website at [](https://git-scm.com).
