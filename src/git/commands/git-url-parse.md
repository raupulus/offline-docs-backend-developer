---
title: git-url-parse
description: Parse and extract git URL components
source_url: https://git-scm.com/doc/git-url-parse
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-url-parse.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1600
---

git-url-parse(1) ================

NAME ---- git-url-parse - Parse and extract git URL components

SYNOPSIS --------

git url-parse \[-c \<component\>\] \[--\] \<url\>…

DESCRIPTION -----------

Git supports many ways to specify URLs, some of them non-standard. For example, git supports the scp style \[user@\]host:\[path\] format. This command eases interoperability with git URLs by enabling the parsing and extraction of the components of all git URLs.

Any syntactically valid URL is parsed, even if the scheme is not one git supports for fetching or pushing.

OPTIONS -------

`-c` `<component>`  

`--component` `<component>`  
Extract the *\<component\>* component from the given Git URLs. *\<component\>* can be one of: `scheme`, `user`, `password`, `host`, `port`, `path`.

OUTPUT ------

When `--component` is given, the requested component of each URL is printed on its own line, in the order the URLs were given. If the URL has no such component (for example, a port in a URL that does not specify one), an empty line is printed in its place.

When `--component` is not given, no output is produced. The exit status is zero if every URL parses successfully and non-zero otherwise, allowing the command to be used purely as a validator.

EXAMPLES --------

- Print the host name:

      $ git url-parse --component host https://example.com/user/repo
      example.com

<!-- -->

- Print the path:

      $ git url-parse --component path https://example.com/user/repo
      /user/repo
      $ git url-parse --component path example.com:~user/repo
      ~user/repo
      $ git url-parse --component path example.com:user/repo
      /user/repo

<!-- -->

- Validate URLs without outputting anything:

      $ git url-parse https://example.com/user/repo example.com:~user/repo

SEE ALSO -------- [git-clone](git-clone.md), [git-fetch](git-fetch.md), [git-config](git-config.md)

GIT --- Part of the [git](git.md) suite
