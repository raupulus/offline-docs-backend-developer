---
title: git-difftool
description: Show changes using common diff tools
source_url: https://git-scm.com/doc/git-difftool
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-difftool.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 470
---

git-difftool(1) ===============

NAME ---- git-difftool - Show changes using common diff tools

SYNOPSIS --------

git difftool \[\<options\>\] \[\<commit\> \[\<commit\>\]\] \[--\] \[\<path\>…\]

DESCRIPTION ----------- `git` `difftool` is a Git command that allows you to compare and edit files between revisions using common diff tools. `git` `difftool` is a frontend to `git` `diff` and accepts the same options and arguments. See [git-diff](git-diff.md).

OPTIONS ------- `-d`:: `--dir-diff`:: Copy the modified files to a temporary location and perform a directory diff on them. This mode never prompts before launching the diff tool.

`-y`  

`--no-prompt`  
Do not prompt before launching a diff tool.

`--prompt`  
Prompt before each invocation of the diff tool. This is the default behaviour; the option is provided to override any configuration settings.

`--rotate-to=<file>`  
Start showing the diff for *\<file\>*, the paths before it will move to the end and output.

`--skip-to=<file>`  
Start showing the diff for *\<file\>*, skipping all the paths before it.

`-t` `<tool>`  

`--tool=<tool>`  
Use the diff tool specified by *\<tool\>*. Valid values include emerge, kompare, meld, and vimdiff. Run `git` `difftool` `--tool-help` for the list of valid *\<tool\>* settings.

If a diff tool is not specified, `git` `difftool` will use the configuration variable `diff.tool`. If the configuration variable `diff.tool` is not set, `git` `difftool` will pick a suitable default.

You can explicitly provide a full path to the tool by setting the configuration variable `difftool.<tool>.path`. For example, you can configure the absolute path to kdiff3 by setting `difftool.kdiff3.path`. Otherwise, `git` `difftool` assumes the tool is available in PATH.

Instead of running one of the known diff tools, `git` `difftool` can be customized to run an alternative program by specifying the command line to invoke in a configuration variable `difftool.<tool>.cmd`.

When `git` `difftool` is invoked with this tool (either through the `-t` or `--tool` option or the `diff.tool` configuration variable) the configured command line will be invoked with the following variables available: `$LOCAL` is set to the name of the temporary file containing the contents of the diff pre-image and `$REMOTE` is set to the name of the temporary file containing the contents of the diff post-image. `$MERGED` is the name of the file which is being compared. `$BASE` is provided for compatibility with custom merge tool commands and has the same value as `$MERGED`.

`--tool-help`  
Print a list of diff tools that may be used with `--tool`.

`--symlinks`  

`--no-symlinks`  
`git` `difftool`’s default behavior is to create symlinks to the working tree when run in `--dir-diff` mode and the right-hand side of the comparison yields the same content as the file in the working tree.

Specifying `--no-symlinks` instructs `git` `difftool` to create copies instead. `--no-symlinks` is the default on Windows.

`-x` `<command>`  

`--extcmd=<command>`  
Specify a custom command for viewing diffs. `git-difftool` ignores the configured defaults and runs `<command>` `$LOCAL` `$REMOTE` when this option is specified. Additionally, `$BASE` is set in the environment.

`-g`  

`--gui`  

`--no-gui`  
When `git-difftool` is invoked with the `-g` or `--gui` option the default diff tool will be read from the configured `diff.guitool` variable instead of `diff.tool`. This may be selected automatically using the configuration variable `difftool.guiDefault`. The `--no-gui` option can be used to override these settings. If `diff.guitool` is not set, we will fallback in the order of `merge.guitool`, `diff.tool`, `merge.tool` until a tool is found.

`--trust-exit-code`  

`--no-trust-exit-code`  
Errors reported by the diff tool are ignored by default. Use `--trust-exit-code` to make `git-difftool` exit when an invoked diff tool returns a non-zero exit code.

`git-difftool` will forward the exit code of the invoked tool when `--trust-exit-code` is used.

See [git-diff](git-diff.md) for the full list of supported options.

CONFIGURATION ------------- `git` `difftool` falls back to `git` `mergetool` config variables when the difftool equivalents have not been defined.

<div class="included" data-path="includes/cmd-config-section-rest.adoc">

Everything above this line in this section isn’t included from the [git-config](git-config.md) documentation. The content that follows is the same as what’s found there:

</div>

<div class="included" data-path="config/difftool.adoc">

`diff.tool`  
Controls which diff tool is used by [git-difftool](git-difftool.md). This variable overrides the value configured in `merge.tool`. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding `difftool.<tool>.cmd` variable is defined.

`diff.guitool`  
Controls which diff tool is used by [git-difftool](git-difftool.md) when the `-g`/`--gui` flag is specified. This variable overrides the value configured in `merge.guitool`. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding `difftool.<guitool>.cmd` variable is defined.

include  
{build_dir}/mergetools-diff.adoc\[\]

`difftool.<tool>.cmd`  
Specify the command to invoke the specified diff tool. The specified command is evaluated in shell with the following variables available: `LOCAL` is set to the name of the temporary file containing the contents of the diff pre-image and `REMOTE` is set to the name of the temporary file containing the contents of the diff post-image.

See the `--tool=<tool>` option in [git-difftool](git-difftool.md) for more details.

`difftool.<tool>.path`  
Override the path for the given tool. This is useful in case your tool is not in the PATH.

`difftool.trustExitCode`  
Exit difftool if the invoked diff tool returns a non-zero exit status.

See the `--trust-exit-code` option in [git-difftool](git-difftool.md) for more details.

`difftool.prompt`  
Prompt before each invocation of the diff tool.

`difftool.guiDefault`  
Set `true` to use the `diff.guitool` by default (equivalent to specifying the `--gui` argument), or `auto` to select `diff.guitool` or `diff.tool` depending on the presence of a `DISPLAY` environment variable value. The default is `false`, where the `--gui` argument must be provided explicitly for the `diff.guitool` to be used.

</div>

SEE ALSO -------- [git-diff](git-diff.md):: Show changes between commits, commit and working tree, etc

[git-mergetool](git-mergetool.md)  
Run merge conflict resolution tools to resolve merge conflicts

[git-config](git-config.md)  
Get and set repository or global options

GIT --- Part of the [git](git.md) suite
