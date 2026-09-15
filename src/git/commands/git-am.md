---
title: git-am
description: Apply a series of patches from a mailbox
source_url: https://git-scm.com/doc/git-am
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-am.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 20
---

git-am(1) =========

NAME ---- git-am - Apply a series of patches from a mailbox

SYNOPSIS --------

git am \[--signoff\] \[--keep\] \[--\[no-\]keep-cr\] \[--\[no-\]utf8\] \[--\[no-\]verify\] \[--\[no-\]3way\] \[--interactive\] \[--committer-date-is-author-date\] \[--ignore-date\] \[--ignore-space-change \| --ignore-whitespace\] \[--whitespace=\<action\>\] \[-C\<n\>\] \[-p\<n\>\] \[--directory=\<dir\>\] \[--exclude=\<path\>\] \[--include=\<path\>\] \[--reject\] \[-q \| --quiet\] \[--\[no-\]scissors\] \[-S\[\<key-id\>\]\] \[--patch-format=\<format\>\] \[--quoted-cr=\<action\>\] \[--empty=(stop\|drop\|keep)\] \[(\<mbox\> \| \<Maildir\>)…\] git am (--continue \| --skip \| --abort \| --quit \| --retry \| --show-current-patch\[=(diff\|raw)\] \| --allow-empty)

DESCRIPTION ----------- Splits mail messages in a mailbox into commit log messages, authorship information, and patches, and applies them to the current branch. You could think of it as a reverse operation of [git-format-patch](git-format-patch.md) run on a branch with a straight history without merges.

OPTIONS ------- `(<mbox>|<Maildir>)…`:: The list of mailbox files to read patches from. If you do not supply this argument, the command reads from the standard input. If you supply directories, they will be treated as Maildirs.

`-s`  

`--signoff`  
Add a `Signed-off-by` trailer to the commit message (see [git-interpret-trailers](git-interpret-trailers.md)), using the committer identity of yourself. See the signoff option in [git-commit](git-commit.md) for more information.

`-k`  

`--keep`  
Pass `-k` flag to [git-mailinfo](git-mailinfo.md).

`--keep-non-patch`  
Pass `-b` flag to [git-mailinfo](git-mailinfo.md).

`--keep-cr`  

`--no-keep-cr`  
With `--keep-cr`, call [git-mailsplit](git-mailsplit.md) with the same option, to prevent it from stripping CR at the end of lines. `am.keepcr` configuration variable can be used to specify the default behaviour. `--no-keep-cr` is useful to override `am.keepcr`.

`-c`  

`--scissors`  
Remove everything in body before a scissors line (see [git-mailinfo](git-mailinfo.md)). Can be activated by default using the `mailinfo.scissors` configuration variable.

`--no-scissors`  
Ignore scissors lines (see [git-mailinfo](git-mailinfo.md)).

`--quoted-cr=<action>`  
This flag will be passed down to [git-mailinfo](git-mailinfo.md).

`--empty=(drop|keep|stop)`  
How to handle an e-mail message lacking a patch:

<div>

`drop`;; The e-mail message will be skipped. `keep`;; An empty commit will be created, with the contents of the e-mail message as its log. `stop`;; The command will fail, stopping in the middle of the current `am` session. This is the default behavior.

</div>

`-m`  

`--message-id`  
Pass the `-m` flag to [git-mailinfo](git-mailinfo.md), so that the `Message-ID` header is added to the commit message. The `am.messageid` configuration variable can be used to specify the default behaviour.

`--no-message-id`  
Do not add the Message-ID header to the commit message. `--no-message-id` is useful to override `am.messageid`.

`-q`  

`--quiet`  
Be quiet. Only print error messages.

`-u`  

`--utf8`  
Pass `-u` flag to [git-mailinfo](git-mailinfo.md). The proposed commit log message taken from the e-mail is re-coded into UTF-8 encoding (configuration variable `i18n.commitEncoding` can be used to specify the project’s preferred encoding if it is not UTF-8).

This was optional in prior versions of git, but now it is the default. You can use `--no-utf8` to override this.

`--no-utf8`  
Pass `-n` flag to [git-mailinfo](git-mailinfo.md).

`-3`  

`--3way`  

`--no-3way`  
When the patch does not apply cleanly, fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally. `--no-3way` can be used to override `am.threeWay` configuration variable. For more information, see `am.threeWay` in [git-config](git-config.md).

include  
rerere-options.adoc\[\]

`--ignore-space-change`  

`--ignore-whitespace`  

`--whitespace=<action>`  

`-C<n>`  

`-p<n>`  

`--directory=<dir>`  

`--exclude=<path>`  

`--include=<path>`  

`--reject`  
These flags are passed to the [git-apply](git-apply.md) program that applies the patch.

Valid *\<action\>* for the `--whitespace` option are: `nowarn`, `warn`, `fix`, `error`, and `error-all`.

`--patch-format`  
By default the command will try to detect the patch format automatically. This option allows the user to bypass the automatic detection and specify the patch format that the patch(es) should be interpreted as. Valid formats are mbox, mboxrd, stgit, stgit-series, and hg.

`-i`  

`--interactive`  
Run interactively.

`--verify`  

`-n`  

`--no-verify`  
Run the `pre-applypatch` and `applypatch-msg` hooks. This is the default. Skip these hooks with `-n` or `--no-verify`. See also [githooks](githooks.md).

Note that `post-applypatch` cannot be skipped.

`--committer-date-is-author-date`  
By default the command records the date from the e-mail message as the commit author date, and uses the time of commit creation as the committer date. This allows the user to lie about the committer date by using the same value as the author date.

> [!WARNING]
> The history walking machinery assumes that commits have non-decreasing commit timestamps. You should consider if you really need to use this option. Then you should only use this option to override the committer date when applying commits on top of a base which commit is older (in terms of the commit date) than the oldest patch you are applying.

`--ignore-date`  
By default the command records the date from the e-mail message as the commit author date, and uses the time of commit creation as the committer date. This allows the user to lie about the author date by using the same value as the committer date.

`--skip`  
Skip the current patch. This is only meaningful when restarting an aborted patch.

`-S[<key-id>]`  

`--gpg-sign[=<key-id>]`  

`--no-gpg-sign`  
GPG-sign commits. The *\<key-id\>* is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`.

`--continue`  

`-r`  

`--resolved`  
After a patch failure (e.g. attempting to apply conflicting patch), the user has applied it by hand and the index file stores the result of the application. Make a commit using the authorship and commit log extracted from the e-mail message and the current index file, and continue.

`--resolvemsg=<msg>`  
When a patch failure occurs, *\<msg\>* will be printed to the screen before exiting. This overrides the standard message informing you to use `--continue` or `--skip` to handle the failure. This is solely for internal use between [git-rebase](git-rebase.md) and [git-am](git-am.md).

`--abort`  
Restore the original branch and abort the patching operation. Revert the contents of files involved in the am operation to their pre-am state.

`--quit`  
Abort the patching operation but keep `HEAD` and the index untouched.

`--retry`  
Try to apply the last conflicting patch again. This is generally only useful for passing extra options to the retry attempt (e.g., `--3way`), since otherwise you’ll just see the same failure again.

`--show-current-patch[=(diff|raw)]`  
Show the message at which [git-am](git-am.md) has stopped due to conflicts. If `raw` is specified, show the raw contents of the e-mail message; if `diff`, show the diff portion only. Defaults to `raw`.

`--allow-empty`  
After a patch failure on an input e-mail message lacking a patch, create an empty commit with the contents of the e-mail message as its log message.

<div id="discussion" data-wrapper="1">

DISCUSSION ----------

</div>

The commit author name is taken from the "From: " line of the message, and commit author date is taken from the "Date: " line of the message. The "Subject: " line is used as the title of the commit, after stripping common prefix "\[PATCH \<anything\>\]". The "Subject: " line is supposed to concisely describe what the commit is about in one line of text.

"From: ", "Date: ", and "Subject: " lines starting the body override the respective commit author name and title values taken from the headers.

The commit message is formed by the title taken from the "Subject: ", a blank line and the body of the message up to where the patch begins. Excess whitespace at the end of each line is automatically stripped.

The patch is expected to be inline, directly following the message. include::format-patch-end-of-commit-message.adoc\[\]

This means that the contents of the commit message can inadvertently interrupt the processing (see the <a href="#caveats" class="cross-reference">CAVEATS</a> section below).

When initially invoking [git-am](git-am.md), you give it the names of the mailboxes to process. Upon seeing the first patch that does not apply, it aborts in the middle. You can recover from this in one of two ways:

1.  skip the current patch by re-running the command with the `--skip` option.

<!-- -->

1.  hand resolve the conflict in the working directory, and update the index file to bring it into a state that the patch should have produced. Then run the command with the `--continue` option.

The command refuses to process new mailboxes until the current operation is finished, so if you decide to start over from scratch, run `git` `am` `--abort` before running the command with mailbox names.

Before any patches are applied, `ORIG_HEAD` is set to the tip of the current branch. This is useful if you have problems with multiple commits, like running [git-am](git-am.md) on the wrong branch or an error in the commits that is more easily fixed by changing the mailbox (e.g. errors in the `From:` lines).

<div id="caveats" data-wrapper="1">

CAVEATS -------

</div>

<div class="included" data-path="format-patch-caveats.adoc">

The output from [git-format-patch](git-format-patch.md) can lead to a different commit message when applied with [git-am](git-am.md). The patch that is applied may also be different from the one that was generated, or patch application may fail outright. ifdef::git-am\[\] See the <a href="#discussion" class="cross-reference">DISCUSSION</a> section above for the syntactic rules. endif::git-am\[\]

ifndef  
git-am\[\]

<div class="included" data-path="format-patch-end-of-commit-message.adoc">

Any line that is of the form:

- three-dashes and end-of-line, or

- a line that begins with `diff` `-`, or

- a line that begins with `Index:`

is taken as the beginning of a patch, and the commit log message is terminated before the first occurrence of such a line.

</div>

endif  
git-am\[\]

Note that this is especially problematic for unindented diffs that occur in the commit message; the diff in the commit message might get applied along with the patch section, or the patch application machinery might trip up because the patch target doesn’t apply. This could for example be caused by a diff in a Markdown code block.

The solution for this is to indent the diff or other text that could cause problems.

This loss of fidelity might be simple to notice if you are applying patches directly from a mailbox. However, changes originating from Git could be applied in bulk, in which case this would be much harder to notice. This could for example be a Linux distribution which uses patch files to apply changes on top of the commits from the upstream repositories. This goes to show that this behavior does not only impact email workflows.

Given these limitations, one might be tempted to use a general-purpose utility like `patch`(1) instead. However, `patch`(1) will not only look for unindented diffs (like [git-am](git-am.md)) but will try to apply indented diffs as well.

</div>

HOOKS ----- This command can run `applypatch-msg`, `pre-applypatch`, and `post-applypatch` hooks. See [githooks](githooks.md) for more information.

See the `--verify`/`-n`/`--no-verify` options.

CONFIGURATION -------------

<div class="included" data-path="includes/cmd-config-section-all.adoc">

Everything below this line in this section is selectively included from the [git-config](git-config.md) documentation. The content is the same as what’s found there:

</div>

<div class="included" data-path="config/am.adoc">

`am.keepcr`  
If true, [git-am](git-am.md) will call [git-mailsplit](git-mailsplit.md) for patches in mbox format with parameter `--keep-cr`. In this case [git-mailsplit](git-mailsplit.md) will not remove `r` from lines ending with `rn`. Can be overridden by giving `--no-keep-cr` from the command line.

`am.threeWay`  
By default, [git-am](git-am.md) will fail if the patch does not apply cleanly. When set to true, this setting tells [git-am](git-am.md) to fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally (equivalent to giving the `--3way` option from the command line). Defaults to `false`.

`am.messageId`  
Add a `Message-ID` trailer based on the email header to the commit when using [git-am](git-am.md) (see [git-interpret-trailers](git-interpret-trailers.md)). See also the `--message-id` and `--no-message-id` options.

</div>

SEE ALSO -------- [git-apply](git-apply.md), [git-format-patch](git-format-patch.md).

GIT --- Part of the [git](git.md) suite
