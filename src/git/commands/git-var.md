---
title: git-var
description: Show a Git logical variable
source_url: https://git-scm.com/doc/git-var
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-var.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1610
---

git-var(1) ==========

NAME ---- git-var - Show a Git logical variable

SYNOPSIS --------

git var (-l \| \<variable\>)

DESCRIPTION ----------- Prints a Git logical variable. Exits with code 1 if the variable has no value.

OPTIONS ------- `-l`:: Display the logical variables. In addition, all the variables of the Git configuration file .git/config are listed as well. (However, the configuration variables listing functionality is deprecated in favor of `git` `config` `list`.)

EXAMPLES -------- \$ git var GIT_AUTHOR_IDENT Eric W. Biederman \<[ebiederm@lnxi.com](ebiederm@lnxi.com)\> 1121223278 -0600

VARIABLES --------- `GIT_AUTHOR_IDENT`:: The author of a piece of code.

`GIT_COMMITTER_IDENT`  
The person who put a piece of code into Git.

`GIT_EDITOR`  
Text editor for use by Git commands. The value is meant to be interpreted by the shell when it is used. Examples: `~/bin/vi`, `$SOME_ENVIRONMENT_VARIABLE`, `"C:Program` `FilesVimgvim.exe"` `--nofork`. The order of preference is `$GIT_EDITOR`, then `core.editor` configuration value, then `$VISUAL`, then `$EDITOR`, and then the default chosen at compile time, which is usually ’vi’.

ifdef  
git-default-editor\[\] The build you are using chose ’{git-default-editor}’ as the default.

endif  
git-default-editor\[\]

`GIT_SEQUENCE_EDITOR`  
Text editor used to edit the ’todo’ file while running `git` `rebase` `-i`. Like `GIT_EDITOR`, the value is meant to be interpreted by the shell when it is used. The order of preference is `$GIT_SEQUENCE_EDITOR`, then `sequence.editor` configuration value, and then the value of `git` `var` `GIT_EDITOR`.

`GIT_PAGER`  
Text viewer for use by Git commands (e.g., ’less’). The value is meant to be interpreted by the shell. The order of preference is `$GIT_PAGER`, then the value of `core.pager` configuration, then `$PAGER`, and then the default chosen at compile time (usually `less`).

ifdef  
git-default-pager\[\] The build you are using chose ’{git-default-pager}’ as the default.

endif  
git-default-pager\[\]

`GIT_DEFAULT_BRANCH`  
The name of the first branch created in newly initialized repositories.

`GIT_SHELL_PATH`  
The path of the binary providing the POSIX shell for commands which use the shell.

`GIT_ATTR_SYSTEM`  
The path to the system [gitattributes](gitattributes.md) file, if one is enabled.

`GIT_ATTR_GLOBAL`  
The path to the global (per-user) [gitattributes](gitattributes.md) file.

`GIT_CONFIG_SYSTEM`  
The path to the system configuration file, if one is enabled.

`GIT_CONFIG_GLOBAL`  
The path to the global (per-user) configuration files, if any.

Most path values contain only one value. However, some can contain multiple values, which are separated by newlines, and are listed in order from highest to lowest priority. Callers should be prepared for any such path value to contain multiple items.

Note that paths are printed even if they do not exist, but not if they are disabled by other environment variables.

SEE ALSO -------- [git-commit-tree](git-commit-tree.md) [git-tag](git-tag.md) [git-config](git-config.md)

GIT --- Part of the [git](git.md) suite
