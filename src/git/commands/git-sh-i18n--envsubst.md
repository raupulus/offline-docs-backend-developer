---
title: git-sh-i18n—​envsubst
description: Git’s own envsubst(1) for i18n fallbacks
source_url: https://git-scm.com/doc/git-sh-i18n--envsubst
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-sh-i18n--envsubst.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1330
---

git-sh-i18n{litdd}envsubst(1) =============================

NAME ---- git-sh-i18n—​envsubst - Git’s own envsubst(1) for i18n fallbacks

SYNOPSIS --------

> eval_gettext () {\
> printf "%s" "\$1" \| (\
> export PATH \$(’git sh-i18n{litdd}envsubst’ --variables "\$1");\
> ’git sh-i18n{litdd}envsubst’ "\$1"\
> )\
> }

DESCRIPTION -----------

This is not a command the end user would want to run. Ever. This documentation is meant for people who are studying the plumbing scripts and/or are writing new ones.

’git sh-i18n{litdd}envsubst’ is Git’s stripped-down copy of the GNU `envsubst(1)` program that comes with the GNU gettext package. It’s used internally by [git-sh-i18n](git-sh-i18n.md) to interpolate the variables passed to the `eval_gettext` function.

No promises are made about the interface, or that this program won’t disappear without warning in the next version of Git. Don’t use it.

GIT --- Part of the [git](git.md) suite
