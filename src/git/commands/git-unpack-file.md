---
title: git-unpack-file
description: Creates a temporary file with a blob’s contents
source_url: https://git-scm.com/doc/git-unpack-file
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-unpack-file.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1530
---

git-unpack-file(1) ==================

NAME ---- git-unpack-file - Creates a temporary file with a blob’s contents

SYNOPSIS --------

> ’git unpack-file’ \<blob\>

DESCRIPTION ----------- Creates a file holding the contents of the blob specified by sha1. It returns the name of the temporary file in the following format: .merge_file_XXXXX

OPTIONS ------- \<blob\>:: Must be a blob id

GIT --- Part of the [git](git.md) suite
