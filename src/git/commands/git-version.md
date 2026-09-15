---
title: git-version
description: Display version information about Git
source_url: https://git-scm.com/doc/git-version
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-version.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1650
---

git-version(1) ==============

NAME ---- git-version - Display version information about Git

SYNOPSIS --------

> ’git version’ \[--build-options\]

DESCRIPTION ----------- With no options given, the version of ’git’ is printed on the standard output.

Note that `git` `--version` is identical to `git` `version` because the former is internally converted into the latter.

OPTIONS ------- --build-options:: Include additional information about how git was built for diagnostic purposes.\
The libraries used to implement the SHA-1 and SHA-256 algorithms are displayed in the form `SHA-1:` `<option>` and `SHA-256:` `<option>`. Note that the SHA-1 options `SHA1_APPLE`, `SHA1_OPENSSL`, and `SHA1_BLK` do not use a collision detection algorithm and thus may be vulnerable to known SHA-1 collision attacks. When a faster SHA-1 implementation without collision detection is used for only non-cryptographic purposes, the algorithm is displayed in the form `non-collision-detecting-SHA-1:` `<option>`.

GIT --- Part of the [git](git.md) suite
