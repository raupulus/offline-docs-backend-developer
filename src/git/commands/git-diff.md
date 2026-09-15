---
title: git-diff
description: Show changes between commits, commit and working tree, etc
source_url: https://git-scm.com/doc/git-diff
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-diff.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 460
---

git-diff(1) ===========

NAME ---- git-diff - Show changes between commits, commit and working tree, etc

SYNOPSIS --------

git diff \[\<options\>\] \[\<commit\>\] \[--\] \[\<path\>…\] git diff \[\<options\>\] --cached \[--merge-base\] \[\<commit\>\] \[--\] \[\<path\>…\] git diff \[\<options\>\] \[--merge-base\] \<commit\> \[\<commit\>…\] \<commit\> \[--\] \[\<path\>…\] git diff \[\<options\>\] \<commit\>…\<commit\> \[--\] \[\<path\>…\] git diff \[\<options\>\] \<blob\> \<blob\> git diff \[\<options\>\] --no-index \[--\] \<path\> \<path\> \[\<pathspec\>…\]

DESCRIPTION ----------- Show changes between the working tree and the index or a tree, changes between the index and a tree, changes between two trees, changes resulting from a merge, changes between two blob objects, or changes between two files on disk.

`git` `diff` `[<options>]` `[--]` `[<path>…]`  

<!-- -->

    This form is to view the changes you made relative to
    the index (staging area for the next commit).  In other
    words, the differences are what you _could_ tell Git to
    further add to the index but you still haven't.  You can
    stage these changes by using [git-add](git-add.md).

`git` `diff` `[<options>]` `--no-index` `[--]` `<path>` `<path>` `[<pathspec>…]`  

<!-- -->

    This form is to compare the given two paths on the
    filesystem.  You can omit the `--no-index` option when
    running the command in a working tree controlled by Git and
    at least one of the paths points outside the working tree,
    or when running the command outside a working tree
    controlled by Git. This form implies `--exit-code`. If both
    paths point to directories, additional pathspecs may be
    provided. These will limit the files included in the
    difference. All such pathspecs must be relative as they
    apply to both sides of the diff.

`git` `diff` `[<options>]` `--cached` `[--merge-base]` `[<commit>]` `[--]` `[<path>…]`  

<!-- -->

    This form is to view the changes you staged for the next
    commit relative to the named _<commit>_.  Typically you
    would want comparison with the latest commit, so if you
    do not give _<commit>_, it defaults to `HEAD`.
    If `HEAD` does not exist (e.g. unborn branches) and
    _<commit>_ is not given, it shows all staged changes.
    `--staged` is a synonym of `--cached`.

\
If `--merge-base` is given, instead of using *\<commit\>*, use the merge base of *\<commit\>* and `HEAD`. `git` `diff` `--cached` `--merge-base` `A` is equivalent to `git` `diff` `--cached` `$(git` `merge-base` `A` `HEAD)`.

`git` `diff` `[<options>]` `[--merge-base]` `<commit>` `[--]` `[<path>…]`  

<!-- -->

    This form is to view the changes you have in your
    working tree relative to the named _<commit>_.  You can
    use `HEAD` to compare it with the latest commit, or a
    branch name to compare with the tip of a different
    branch.

\
If `--merge-base` is given, instead of using *\<commit\>*, use the merge base of *\<commit\>* and `HEAD`. `git` `diff` `--merge-base` `A` is equivalent to `git` `diff` `$(git` `merge-base` `A` `HEAD)`.

`git` `diff` `[<options>]` `[--merge-base]` `<commit>` `<commit>` `[--]` `[<path>…]`  

<!-- -->

    This is to view the changes between two arbitrary
    _<commit>_.

\
If `--merge-base` is given, use the merge base of the two commits for the "before" side. `git` `diff` `--merge-base` `A` `B` is equivalent to `git` `diff` `$(git` `merge-base` `A` `B)` `B`.

`git` `diff` `[<options>]` `<commit>` `<commit>…<commit>` `[--]` `[<path>…]`  

<!-- -->

    This form is to view the results of a merge commit.  The first
    listed _<commit>_ must be the merge itself; the remaining two or
    more commits should be its parents.  Convenient ways to produce
    the desired set of revisions are to use the suffixes `@` and
    `^!`.  If `A` is a merge commit, then `git diff A A^@`,
    `git diff A^!` and `git show A` all give the same combined diff.

`git` `diff` `[<options>]` `<commit>..<commit>` `[--]` `[<path>…]`  

<!-- -->

    This is synonymous to the earlier form (without the `..`) for
    viewing the changes between two arbitrary _<commit>_.  If _<commit>_ on
    one side is omitted, it will have the same effect as
    using `HEAD` instead.

`git` `diff` `[<options>]` `<commit>…<commit>` `[--]` `[<path>…]`  

<!-- -->

    This form is to view the changes on the branch containing
    and up to the second _<commit>_, starting at a common ancestor
    of both _<commit>_.  `git diff A...B` is equivalent to
    `git diff $(git merge-base A B) B`.  You can omit any one
    of _<commit>_, which has the same effect as using `HEAD` instead.

Just in case you are doing something exotic, it should be noted that all of the *\<commit\>* in the above description, except in the `--merge-base` case and in the last two forms that use `..` notations, can be any *\<tree\>*. A tree of interest is the one pointed to by the ref named `AUTO_MERGE`, which is written by the `ort` merge strategy upon hitting merge conflicts (see [git-merge](git-merge.md)). Comparing the working tree with `AUTO_MERGE` shows changes you’ve made so far to resolve textual conflicts (see the examples below).

For a more complete list of ways to spell *\<commit\>*, see "SPECIFYING REVISIONS" section in [gitrevisions](gitrevisions.md). However, `diff` is about comparing two *endpoints*, not ranges, and the range notations (`<commit>..<commit>` and `<commit>…<commit>`) do not mean a range as defined in the "SPECIFYING RANGES" section in [gitrevisions](gitrevisions.md).

`git` `diff` `[<options>]` `<blob>` `<blob>`  

<!-- -->

    This form is to view the differences between the raw
    contents of two blob objects.

OPTIONS ------- :git-diff: 1 include::diff-options.adoc\[\]

`-1`  

`--base`  

`-2`  

`--ours`  

`-3`  

`--theirs`  
Compare the working tree with

<div>

- the "base" version (stage \#1) when using `-1` or `--base`,

- "our branch" (stage \#2) when using `-2` or `--ours`, or

- "their branch" (stage \#3) when using `-3` or `--theirs`.

</div>

The index contains these stages only for unmerged entries i.e. while resolving conflicts. See [git-read-tree](git-read-tree.md) section "3-Way Merge" for detailed information.

`-0`  
Omit diff output for unmerged entries and just show "Unmerged". Can be used only when comparing the working tree with the index.

`<path>…`  
The *\<path\>* parameters, when given, are used to limit the diff to the named paths (you can give directory names and get diff for all files under them).

include  
diff-format.adoc\[\]

EXAMPLES --------

Various ways to check your working tree  
    $ git diff ①
    $ git diff --cached ②
    $ git diff HEAD ③
    $ git diff AUTO_MERGE ④

<div class="callout-list">

1.  Changes in the working tree not yet staged for the next commit.

2.  Changes between the index and your last commit; what you would be committing if you run `git` `commit` without `-a` option.

3.  Changes in the working tree since your last commit; what you would be committing if you run `git` `commit` `-a`

4.  Changes in the working tree you’ve made to resolve textual conflicts so far.

</div>

Comparing with arbitrary commits  
    $ git diff test ①
    $ git diff HEAD -- ./test ②
    $ git diff HEAD^ HEAD ③

<div class="callout-list">

1.  Instead of using the tip of the current branch, compare with the tip of "test" branch.

2.  Instead of comparing with the tip of "test" branch, compare with the tip of the current branch, but limit the comparison to the file "test".

3.  Compare the version before the last commit and the last commit.

</div>

Comparing branches  
    $ git diff topic master ①
    $ git diff topic..master ②
    $ git diff topic...master ③

<div class="callout-list">

1.  Changes between the tips of the topic and the master branches.

2.  Same as above.

3.  Changes that occurred on the master branch since when the topic branch was started off it.

</div>

Limiting the diff output  
    $ git diff --diff-filter=MRC ①
    $ git diff --name-status ②
    $ git diff arch/i386 include/asm-i386 ③

<div class="callout-list">

1.  Show only modification, rename, and copy, but not addition or deletion.

2.  Show only names and the nature of change, but not actual diff output.

3.  Limit diff output to named subtrees.

</div>

Munging the diff output  
    $ git diff --find-copies-harder -B -C ①
    $ git diff -R ②

<div class="callout-list">

1.  Spend extra cycles to find renames, copies and complete rewrites (very expensive).

2.  Output diff in reverse.

</div>

CONFIGURATION -------------

<div class="included" data-path="includes/cmd-config-section-all.adoc">

Everything below this line in this section is selectively included from the [git-config](git-config.md) documentation. The content is the same as what’s found there:

</div>

<div class="included" data-path="config/diff.adoc">

`diff.autoRefreshIndex`  
When using `git` `diff` to compare with work tree files, do not consider stat-only changes as changed. Instead, silently run `git` `update-index` `--refresh` to update the cached stat information for paths whose contents in the work tree match the contents in the index. This option defaults to `true`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`.

`diff.dirstat`  

ifdef  
git-diff\[\] A comma separated list of `--dirstat` parameters specifying the default behavior of the `--dirstat` option to `git` `diff` and friends.

endif  
git-diff\[\]

ifndef  
git-diff\[\] A comma separated list of `--dirstat` parameters specifying the default behavior of the `--dirstat` option to [git-diff](git-diff.md) and friends.

endif  
git-diff\[\] The defaults can be overridden on the command line (using `--dirstat=<param>,…`). The fallback defaults (when not changed by `diff.dirstat`) are `changes,noncumulative,3`. The following parameters are available:

<div>

`changes`;; Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given. `lines`;; Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options. `files`;; Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all. `cumulative`;; Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter. *\<limit\>*;; An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.

</div>

Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `files,10,cumulative`.

`diff.statNameWidth`  
Limit the width of the filename part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`.

`diff.statGraphWidth`  
Limit the width of the graph part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`.

`diff.context`  
Generate diffs with *\<n\>* lines of context instead of the default of 3. This value is overridden by the `-U` option.

`diff.interHunkContext`  
Show the context between diff hunks, up to the specified number of lines, thereby fusing the hunks that are close to each other. This value serves as the default for the `--inter-hunk-context` command line option.

`diff.external`  
If this config variable is set, diff generation is not performed using the internal diff machinery, but using the given command. Can be overridden with the `GIT_EXTERNAL_DIFF` environment variable. The command is called with parameters as described under "git Diffs" in [git](git.md). Note: if you want to use an external diff program only on a subset of your files, you might want to use [gitattributes](gitattributes.md) instead.

`diff.trustExitCode`  
If this boolean value is set to `true` then the `diff.external` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code `0` regardless of equality. Any other exit code causes Git to report a fatal error.

`diff.ignoreSubmodules`  
Sets the default value of `--ignore-submodules`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`. `git` `checkout` and `git` `switch` also honor this setting when reporting uncommitted changes. Setting it to `all` disables the submodule summary normally shown by `git` `commit` and `git` `status` when `status.submoduleSummary` is set unless it is overridden by using the `--ignore-submodules` command-line option. The `git` `submodule` commands are not affected by this setting. By default this is set to untracked so that any untracked submodules are ignored.

`diff.mnemonicPrefix`  
If set, `git` `diff` uses a prefix pair that is different from the standard `a/` and `b/` depending on what is being compared. When this configuration is in effect, reverse diff output also swaps the order of the prefixes: `git` `diff`;; compares the (i)ndex and the (w)ork tree; `git` `diff` `HEAD`;; compares a (c)ommit and the (w)ork tree; `git` `diff` `--cached`;; compares a (c)ommit and the (i)ndex; `git` `diff` `HEAD:<file1>` `<file2>`;; compares an (o)bject and a (w)ork tree entity; `git` `diff` `--no-index` `<a>` `<b>`;; compares two non-git things *\<a\>* and *\<b\>*.

`diff.noPrefix`  
If set, `git` `diff` does not show any source or destination prefix.

`diff.srcPrefix`  
If set, `git` `diff` uses this source prefix. Defaults to `a/`.

`diff.dstPrefix`  
If set, `git` `diff` uses this destination prefix. Defaults to `b/`.

`diff.relative`  
If set to `true`, `git` `diff` does not show changes outside of the directory and show pathnames relative to the current directory.

`diff.orderFile`  
File indicating how to order files within a diff.

ifdef  
git-diff\[\] See the `-O` option for details.

endif  
git-diff\[\]

ifndef  
git-diff\[\] See the `-O` option to [git-diff](git-diff.md) for details.

endif  
git-diff\[\] If `diff.orderFile` is a relative pathname, it is treated as relative to the top of the working tree.

`diff.renameLimit`  
The number of files to consider in the exhaustive portion of copy/rename detection; equivalent to the `git` `diff` option `-l`. If not set, the default value is currently 1000. This setting has no effect if rename detection is turned off.

`diff.renames`  
Whether and how Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. If set to `copies` or `copy`, Git will detect copies, as well. Defaults to `true`. Note that this affects only `git` `diff` Porcelain like [git-diff](git-diff.md) and [git-log](git-log.md), and not lower level commands such as [git-diff-files](git-diff-files.md).

`diff.suppressBlankEmpty`  
A boolean to inhibit the standard behavior of printing a space before each empty output line. Defaults to `false`.

`diff.submodule`  
Specify the format in which differences in submodules are shown. The `short` format just shows the names of the commits at the beginning and end of the range. The `log` format lists the commits in the range like [git-submodule](git-submodule.md) `summary` does. The `diff` format shows an inline diff of the changed contents of the submodule. Defaults to `short`.

`diff.wordRegex`  
A POSIX Extended Regular Expression used to determine what is a "word" when performing word-by-word difference calculations. Character sequences that match the regular expression are "words", all other characters are **ignorable** whitespace.

`diff.<driver>.command`  
The custom diff driver command. See [gitattributes](gitattributes.md) for details.

`diff.<driver>.trustExitCode`  
If this boolean value is set to `true` then the `diff.<driver>.command` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code 0 regardless of equality. Any other exit code causes Git to report a fatal error.

`diff.<driver>.xfuncname`  
The regular expression that the diff driver should use to recognize the hunk header. A built-in pattern may also be used. See [gitattributes](gitattributes.md) for details.

`diff.<driver>.binary`  
Set this option to `true` to make the diff driver treat files as binary. See [gitattributes](gitattributes.md) for details.

`diff.<driver>.textconv`  
The command that the diff driver should call to generate the text-converted version of a file. The result of the conversion is used to generate a human-readable diff. See [gitattributes](gitattributes.md) for details.

`diff.<driver>.wordRegex`  
The regular expression that the diff driver should use to split words in a line. See [gitattributes](gitattributes.md) for details.

`diff.<driver>.cachetextconv`  
Set this option to `true` to make the diff driver cache the text conversion outputs. See [gitattributes](gitattributes.md) for details.

`diff.indentHeuristic`  
Set this option to `false` to disable the default heuristics that shift diff hunk boundaries to make patches easier to read.

`diff.algorithm`  
Choose a diff algorithm. The variants are as follows:

<div>

`default`;; `myers`;; The basic greedy diff algorithm. Currently, this is the default. `minimal`;; Spend extra time to make sure the smallest possible diff is produced. `patience`;; Use "patience diff" algorithm when generating patches. `histogram`;; This algorithm extends the patience algorithm to "support low-occurrence common elements".

</div>

`diff.wsErrorHighlight`  
Highlight whitespace errors in the `context`, `old` or `new` lines of the diff. Multiple values are separated by comma, `none` resets previous values, `default` reset the list to `new` and `all` is a shorthand for `old,new,context`. The whitespace errors are colored with `color.diff.whitespace`. The command line option `--ws-error-highlight=<kind>` overrides this setting.

`diff.colorMoved`  
If set to either a valid *\<mode\>* or a `true` value, moved lines in a diff are colored differently.

ifdef  
git-diff\[\] For details of valid modes see `--color-moved`.

endif  
git-diff\[\]

ifndef  
git-diff\[\] For details of valid modes see `--color-moved` in [git-diff](git-diff.md).

endif  
git-diff\[\] If simply set to `true` the default color mode will be used. When set to `false`, moved lines are not colored.

`diff.colorMovedWS`  
When moved lines are colored using e.g. the `diff.colorMoved` setting, this option controls the mode how spaces are treated. For details of valid modes see `--color-moved-ws` in [git-diff](git-diff.md).

</div>

SEE ALSO -------- `diff`(1), [git-difftool](git-difftool.md), [git-log](git-log.md), [gitdiffcore](gitdiffcore.md), [git-format-patch](git-format-patch.md), [git-apply](git-apply.md), [git-show](git-show.md)

GIT --- Part of the [git](git.md) suite
