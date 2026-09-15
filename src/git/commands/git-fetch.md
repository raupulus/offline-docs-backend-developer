---
title: git-fetch
description: Download objects and refs from another repository
source_url: https://git-scm.com/doc/git-fetch
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-fetch.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 510
---

git-fetch(1) ============

NAME ---- git-fetch - Download objects and refs from another repository

SYNOPSIS --------

git fetch \[\<options\>\] \[\<repository\> \[\<refspec\>…\]\] git fetch \[\<options\>\] \<group\> git fetch --multiple \[\<options\>\] \[(\<repository\>\|\<group\>)…\] git fetch --all \[\<options\>\]

DESCRIPTION ----------- Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories. Remote-tracking branches are updated (see the description of *\<refspec\>* below for ways to control this behavior).

By default, any tag that points into the histories being fetched is also fetched; the effect is to fetch tags that point at branches that you are interested in. This default behavior can be changed by using the `--tags` or `--no-tags` options or by configuring `remote.<name>.tagOpt`. By using a refspec that fetches tags explicitly, you can fetch tags that do not point into branches you are interested in as well.

`git` `fetch` can fetch from either a single named repository or URL, or from several repositories at once if *\<group\>* is given and there is a `remotes.<group>` entry in the configuration file. (See [git-config](git-config.md)).

When no remote is specified, by default the `origin` remote will be used, unless there’s an upstream branch configured for the current branch.

The names of refs that are fetched, together with the object names they point at, are written to `.git/FETCH_HEAD`. This information may be used by scripts or other git commands, such as [git-pull](git-pull.md).

OPTIONS ------- include::fetch-options.adoc\[\]

<div class="included" data-path="pull-fetch-param.adoc">

*\<repository\>*  
The "remote" repository that is the source of a fetch or pull operation. This parameter can be either a URL (see the section <a href="#URLS" class="cross-reference">GIT URLS</a> below) or the name of a remote (see the section <a href="#REMOTES" class="cross-reference">REMOTES</a> below).

ifndef  
git-pull\[\]

*\<group\>*  
A name referring to a list of repositories as the value of `remotes.<group>` in the configuration file. (See [git-config](git-config.md)).

endif  
git-pull\[\]

<div id="fetch-refspec" data-wrapper="1">

*\<refspec\>*  
Specifies which refs to fetch and which local refs to update. When no *\<refspec\>*s appear on the command line, the refs to fetch are read from `remote.<repository>.fetch` variables instead

ifndef  
git-pull\[\] (see <a href="#CRTB" class="cross-reference">CONFIGURED REMOTE-TRACKING BRANCHES</a> below).

endif  
git-pull\[\]

ifdef  
git-pull\[\] (see the section "CONFIGURED REMOTE-TRACKING BRANCHES" in [git-fetch](git-fetch.md)).

endif  
git-pull\[\]

The format of a *\<refspec\>* parameter is an optional plus `+`, followed by the source *\<src\>*, followed by a colon `:`, followed by the destination *\<dst\>*. The colon can be omitted when *\<dst\>* is empty. *\<src\>* is typically a ref, or a glob pattern with a single `*` that is used to match a set of refs, but it can also be a fully spelled hex object name.

A *\<refspec\>* may contain a `*` in its *\<src\>* to indicate a simple pattern match. Such a refspec functions like a glob that matches any ref with the pattern. A pattern *\<refspec\>* must have one and only one `*` in both the *\<src\>* and *\<dst\>*. It will map refs to the destination by replacing the `*` with the contents matched from the source.

If a refspec is prefixed by `^`, it will be interpreted as a negative refspec. Rather than specifying which refs to fetch or which local refs to update, such a refspec will instead specify refs to exclude. A ref will be considered to match if it matches at least one positive refspec, and does not match any negative refspec. Negative refspecs can be useful to restrict the scope of a pattern refspec so that it will not include specific refs. Negative refspecs can themselves be pattern refspecs. However, they may only contain a *\<src\>* and do not specify a *\<dst\>*. Fully spelled out hex object names are also not supported.

`tag` `<tag>` means the same as `refs/tags/<tag>:refs/tags/<tag>`; it requests fetching everything up to the given tag.

The remote ref that matches *\<src\>* is fetched, and if *\<dst\>* is not an empty string, an attempt is made to update the local ref that matches it.

Whether that update is allowed without `--force` depends on the ref namespace it’s being fetched to, the type of object being fetched, and whether the update is considered to be a fast-forward. Generally, the same rules apply for fetching as when pushing, see the `<refspec>…` section of [git-push](git-push.md) for what those are. Exceptions to those rules particular to `git` `fetch` are noted below.

Until Git version 2.20, and unlike when pushing with [git-push](git-push.md), any updates to `refs/tags/*` would be accepted without `+` in the refspec (or `--force`). When fetching, we promiscuously considered all tag updates from a remote to be forced fetches. Since Git version 2.20, fetching to update `refs/tags/*` works the same way as when pushing. I.e. any updates will be rejected without `+` in the refspec (or `--force`).

Unlike when pushing with [git-push](git-push.md), any updates outside of `refs/{tags,heads}/*` will be accepted without `+` in the refspec (or `--force`), whether that’s swapping e.g. a tree object for a blob, or a commit for another commit that doesn’t have the previous commit as an ancestor etc.

Unlike when pushing with [git-push](git-push.md), there is no configuration which’ll amend these rules, and nothing like a `pre-fetch` hook analogous to the `pre-receive` hook.

As with pushing with [git-push](git-push.md), all of the rules described above about what’s not allowed as an update can be overridden by adding an optional leading `+` to a refspec (or using the `--force` command line option). The only exception to this is that no amount of forcing will make the `refs/heads/*` namespace accept a non-commit object.

When the remote branch you want to fetch is known to be rewound and rebased regularly, it is expected that its new tip will not be a descendant of its previous tip (as stored in your remote-tracking branch the last time you fetched). You would want to use the `+` sign to indicate non-fast-forward updates will be needed for such branches. There is no way to determine or declare that a branch will be made available in a repository with this behavior; the pulling user simply must know this is the expected usage pattern for a branch.

ifdef  
git-pull\[\]

There is a difference between listing multiple *\<refspec\>* directly on `git` `pull` command line and having multiple `remote.<repository>.fetch` entries in your configuration for a *\<repository\>* and running a `git` `pull` command without any explicit *\<refspec\>* parameters. *\<refspec\>*s listed explicitly on the command line are always merged into the current branch after fetching. In other words, if you list more than one remote ref, `git` `pull` will create an Octopus merge. On the other hand, if you do not list any explicit *\<refspec\>* parameter on the command line, `git` `pull` will fetch all the *\<refspec\>*s it finds in the `remote.<repository>.fetch` configuration and merge only the first *\<refspec\>* found into the current branch. This is because making an Octopus from remote refs is rarely done, while keeping track of multiple remote heads in one-go by fetching more than one is often useful.

endif  
git-pull\[\]

</div>

</div>

`--stdin`  
Read refspecs, one per line, from stdin in addition to those provided as arguments. The "tag *\<name\>*" format is not supported.

include  
urls-remotes.adoc\[\]

<div id="CRTB" data-wrapper="1">

CONFIGURED REMOTE-TRACKING BRANCHES -----------------------------------

</div>

You often interact with the same remote repository by regularly and repeatedly fetching from it. In order to keep track of the progress of such a remote repository, `git` `fetch` allows you to configure `remote.<repository>.fetch` configuration variables.

Typically such a variable may look like this:

    [remote "origin"]
        fetch = +refs/heads/*:refs/remotes/origin/*

This configuration is used in two ways:

- When `git` `fetch` is run without specifying what branches and/or tags to fetch on the command line, e.g. `git` `fetch` `origin` or `git` `fetch`, `remote.<repository>.fetch` values are used as the refspecs—​they specify which refs to fetch and which local refs to update. The example above will fetch all branches that exist in the `origin` (i.e. any ref that matches the left-hand side of the value, `refs/heads/*`) and update the corresponding remote-tracking branches in the `refs/remotes/origin/*` hierarchy.

<!-- -->

- When `git` `fetch` is run with explicit branches and/or tags to fetch on the command line, e.g. `git` `fetch` `origin` `master`, the *\<refspec\>s* given on the command line determine what are to be fetched (e.g. `master` in the example, which is a short-hand for `master:`, which in turn means "fetch the `master` branch but I do not explicitly say what remote-tracking branch to update with it from the command line"), and the example command will fetch *only* the `master` branch. The `remote.<repository>.fetch` values determine which remote-tracking branch, if any, is updated. When used in this way, the `remote.<repository>.fetch` values do not have any effect in deciding *what* gets fetched (i.e. the values are not used as refspecs when the command-line lists refspecs); they are only used to decide *where* the refs that are fetched are stored by acting as a mapping.

The latter use of the `remote.<repository>.fetch` values can be overridden by giving the `--refmap=<refspec>` parameter(s) on the command line.

PRUNING -------

Git has a default disposition of keeping data unless it’s explicitly thrown away; this extends to holding onto local references to branches on remotes that have themselves deleted those branches.

If left to accumulate, these stale references might make performance worse on big and busy repos that have a lot of branch churn, and e.g. make the output of commands like `git` `branch` `-a` `--contains` `<commit>` needlessly verbose, as well as impacting anything else that’ll work with the complete set of known references.

These remote-tracking references can be deleted as a one-off with either of:

    # While fetching
    $ git fetch --prune <name>

    # Only prune, don't fetch
    $ git remote prune <name>

To prune references as part of your normal workflow without needing to remember to run that, set `fetch.prune` globally, or `remote.<name>.prune` per-remote in the config. See [git-config](git-config.md).

Here’s where things get tricky and more specific. The pruning feature doesn’t actually care about branches, instead it’ll prune local \<--\> remote-references as a function of the refspec of the remote (see `<refspec>` and <a href="#CRTB" class="cross-reference">CONFIGURED REMOTE-TRACKING BRANCHES</a> above).

Therefore if the refspec for the remote includes e.g. `refs/tags/`**`:refs/tags/`**, or you manually run e.g. `git` `fetch` `--prune` `<name>` `"refs/tags/`**`:refs/tags/`**`"` it won’t be stale remote tracking branches that are deleted, but any local tag that doesn’t exist on the remote.

This might not be what you expect, i.e. you want to prune remote *\<name\>*, but also explicitly fetch tags from it, so when you fetch from it you delete all your local tags, most of which may not have come from the *\<name\>* remote in the first place.

So be careful when using this with a refspec like `refs/tags/`**`:refs/tags/`**, or any other refspec which might map references from multiple remotes to the same local namespace.

Since keeping up-to-date with both branches and tags on the remote is a common use-case the `--prune-tags` option can be supplied along with `--prune` to prune local tags that don’t exist on the remote, and force-update those tags that differ. Tag pruning can also be enabled with `fetch.pruneTags` or `remote.<name>.pruneTags` in the config. See [git-config](git-config.md).

The `--prune-tags` option is equivalent to having `refs/tags/`**`:refs/tags/`** declared in the refspecs of the remote. This can lead to some seemingly strange interactions:

    # These both fetch tags
    $ git fetch --no-tags origin 'refs/tags/*:refs/tags/*'
    $ git fetch --no-tags --prune-tags origin

The reason it doesn’t error out when provided without `--prune` or its config versions is for flexibility of the configured versions, and to maintain a 1=1 mapping between what the command line flags do, and what the configuration versions do.

It’s reasonable to e.g. configure `fetch.pruneTags=true` in `~/.gitconfig` to have tags pruned whenever `git` `fetch` `--prune` is run, without making every invocation of `git` `fetch` without `--prune` an error.

Pruning tags with `--prune-tags` also works when fetching a URL instead of a named remote. These will all prune tags not found on origin:

    $ git fetch origin --prune --prune-tags
    $ git fetch origin --prune 'refs/tags/*:refs/tags/*'
    $ git fetch <url-of-origin> --prune --prune-tags
    $ git fetch <url-of-origin> --prune 'refs/tags/*:refs/tags/*'

OUTPUT ------

The output of "git fetch" depends on the transport method used; this section describes the output when fetching over the Git protocol (either locally or via ssh) and Smart HTTP protocol.

The status of the fetch is output in tabular form, with each line representing the status of a single ref. Each line is of the form:

     <flag> <summary> <from> -> <to> [<reason>]

When using `--porcelain`, the output format is intended to be machine-parseable. In contrast to the human-readable output formats it thus prints to standard output instead of standard error. Each line is of the form:

    <flag> <old-object-id> <new-object-id> <local-reference>

The status of up-to-date refs is shown only if the `--verbose` option is used.

In compact output mode, specified with configuration variable fetch.output, if either entire *\<from\>* or *\<to\>* is found in the other string, it will be substituted with `*` in the other string. For example, `master` `→` `origin/master` becomes `master` `→` `origin/*`.

flag  
A single character indicating the status of the ref: (space);; for a successfully fetched fast-forward; `+`;; for a successful forced update; `-`;; for a successfully pruned ref; `t`;; for a successful tag update; `*`;; for a successfully fetched new ref; `!`;; for a ref that was rejected or failed to update; and `=`;; for a ref that was up to date and did not need fetching.

summary  
For a successfully fetched ref, the summary shows the old and new values of the ref in a form suitable for using as an argument to `git` `log` (this is `<old>..<new>` in most cases, and `<old>…<new>` for forced non-fast-forward updates).

from  
The name of the remote ref being fetched from, minus its `refs/<type>/` prefix. In the case of deletion, the name of the remote ref is "(none)".

to  
The name of the local ref being updated, minus its `refs/<type>/` prefix.

reason  
A human-readable explanation. In the case of successfully fetched refs, no explanation is needed. For a failed ref, the reason for failure is described.

EXAMPLES --------

- Update the remote-tracking branches:

      $ git fetch origin

  The above command copies all branches from the remote `refs/heads/` namespace and stores them to the local `refs/remotes/origin/` namespace, unless the `remote.<repository>.fetch` option is used to specify a non-default refspec.

<!-- -->

- Using refspecs explicitly:

      $ git fetch origin +seen:seen maint:tmp

  This updates (or creates, as necessary) branches `seen` and `tmp` in the local repository by fetching from the branches (respectively) `seen` and `maint` from the remote repository.

  The `seen` branch will be updated even if it does not fast-forward, because it is prefixed with a plus sign; `tmp` will not be.

<!-- -->

- Peek at a remote’s branch, without configuring the remote in your local repository:

      $ git fetch git://git.kernel.org/pub/scm/git/git.git maint
      $ git log FETCH_HEAD

  The first command fetches the `maint` branch from the repository at `git://git.kernel.org/pub/scm/git/git.git` and the second command uses `FETCH_HEAD` to examine the branch with [git-log](git-log.md). The fetched objects will eventually be removed by git’s built-in housekeeping (see [git-gc](git-gc.md)).

<div class="included" data-path="transfer-data-leaks.adoc">

SECURITY -------- The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository.

The known attack vectors are as follows:

1.  The victim sends "have" lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn’t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to "merge" X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)

<!-- -->

1.  As in \#1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.

</div>

CONFIGURATION -------------

<div class="included" data-path="includes/cmd-config-section-all.adoc">

Everything below this line in this section is selectively included from the [git-config](git-config.md) documentation. The content is the same as what’s found there:

</div>

<div class="included" data-path="config/fetch.adoc">

`fetch.recurseSubmodules`  
This option controls whether `git` `fetch` (and the underlying fetch in `git` `pull`) will recursively fetch into populated submodules. This option can be set either to a boolean value or to `on-demand`. Setting it to a boolean changes the behavior of fetch and pull to recurse unconditionally into submodules when set to true or to not recurse at all when set to false. When set to `on-demand`, fetch and pull will only recurse into a populated submodule when its superproject retrieves a commit that updates the submodule’s reference. Defaults to `on-demand`, or to the value of `submodule.recurse` if set.

`fetch.fsckObjects`  
If it is set to true, git-fetch-pack will check all fetched objects. See `transfer.fsckObjects` for what’s checked. Defaults to `false`. If not set, the value of `transfer.fsckObjects` is used instead.

`fetch.fsck.<msg-id>`  
Acts like `fsck.<msg-id>`, but is used by [git-fetch-pack](git-fetch-pack.md) instead of [git-fsck](git-fsck.md). See the `fsck.<msg-id>` documentation for details.

`fetch.fsck.skipList`  
Acts like `fsck.skipList`, but is used by [git-fetch-pack](git-fetch-pack.md) instead of [git-fsck](git-fsck.md). See the `fsck.skipList` documentation for details.

`fetch.unpackLimit`  
If the number of objects fetched over the Git native transfer is below this limit, then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead.

`fetch.prune`  
If true, fetch will automatically behave as if the `--prune` option was given on the command line. See also `remote.<name>.prune` and the PRUNING section of [git-fetch](git-fetch.md).

`fetch.pruneTags`  
If true, fetch will automatically behave as if the `refs/tags/`**`:refs/tags/`** refspec was provided when pruning, if not set already. This allows for setting both this option and `fetch.prune` to maintain a 1=1 mapping to upstream refs. See also `remote.<name>.pruneTags` and the PRUNING section of [git-fetch](git-fetch.md).

`fetch.all`  
If true, fetch will attempt to update all available remotes. This behavior can be overridden by passing `--no-all` or by explicitly specifying one or more remote(s) to fetch from. Defaults to `false`.

`fetch.output`  
Control how ref update status is printed. Valid values are `full` and `compact`. Default value is `full`. See the OUTPUT section in [git-fetch](git-fetch.md) for details.

`fetch.negotiationAlgorithm`  
Control how information about the commits in the local repository is sent when negotiating the contents of the packfile to be sent by the server. Set to `consecutive` to use an algorithm that walks over consecutive commits checking each one. Set to `skipping` to use an algorithm that skips commits in an effort to converge faster, but may result in a larger-than-necessary packfile; or set to `noop` to not send any information at all, which will almost certainly result in a larger-than-necessary packfile, but will skip the negotiation step. Set to `default` to override settings made previously and use the default behaviour. The default is normally `consecutive`, but if `feature.experimental` is `true`, then the default is `skipping`. Unknown values will cause `git` `fetch` to error out.

See also the `--negotiate-only` and `--negotiation-restrict` options to [git-fetch](git-fetch.md).

`fetch.showForcedUpdates`  
Set to `false` to enable `--no-show-forced-updates` in [git-fetch](git-fetch.md) and [git-pull](git-pull.md) commands. Defaults to `true`.

`fetch.parallel`  
Specifies the maximal number of fetch operations to be run in parallel at a time (submodules, or remotes when the `--multiple` option of [git-fetch](git-fetch.md) is in effect).

A value of 0 will give some reasonable default. If unset, it defaults to 1.

For submodules, this setting can be overridden using the `submodule.fetchJobs` config setting.

`fetch.writeCommitGraph`  
Set to true to write a commit-graph after every `git` `fetch` command that downloads a pack-file from a remote. Using the `--split` option, most executions will create a very small commit-graph file on top of the existing commit-graph file(s). Occasionally, these files will merge and the write may take longer. Having an updated commit-graph file helps performance of many Git commands, including `git` `merge-base`, `git` `push` `-f`, and `git` `log` `--graph`. Defaults to `false`.

`fetch.bundleURI`  
This value stores a URI for downloading Git object data from a bundle URI before performing an incremental fetch from the origin Git server. This is similar to how the `--bundle-uri` option behaves in [git-clone](git-clone.md). `git` `clone` `--bundle-uri` will set the `fetch.bundleURI` value if the supplied bundle URI contains a bundle list that is organized for incremental fetches.

If you modify this value and your repository has a `fetch.bundleCreationToken` value, then remove that `fetch.bundleCreationToken` value before fetching from the new bundle URI.

`fetch.bundleCreationToken`  
When using `fetch.bundleURI` to fetch incrementally from a bundle list that uses the “creationToken” heuristic, this config value stores the maximum `creationToken` value of the downloaded bundles. This value is used to prevent downloading bundles in the future if the advertised `creationToken` is not strictly larger than this value.

The creation token values are chosen by the provider serving the specific bundle URI. If you modify the URI at `fetch.bundleURI`, then be sure to remove the value for the `fetch.bundleCreationToken` value before fetching.

`fetch.followRemoteHEAD`  
When fetching using a default refspec, this setting determines how to handle differences between a fetched remote’s `HEAD` and the local `remotes/<name>/HEAD` symbolic-ref. Its value is one of

<div>

`create`;; Create `remotes/<name>/HEAD` if a ref exists on the remote, but not locally. An existing symbolic-ref will not be touched. This is the default value. `warn`;; Display a warning if the remote advertises a different `HEAD` than what is set locally. Behaves like "create" if the local symbolic-ref doesn’t exist. `always`;; Silently update `remotes/<name>/HEAD` whenever the remote advertises a new value. `never`;; Never create or modify the `remotes/<name>/HEAD` symbolic-ref.

</div>

</div>

BUGS ---- Using `--recurse-submodules` can only fetch new commits in submodules that are present locally e.g. in `$GIT_DIR/modules/`. If the upstream adds a new submodule, that submodule cannot be fetched until it is cloned e.g. by `git` `submodule` `update`. This is expected to be fixed in a future Git version.

SEE ALSO -------- [git-pull](git-pull.md)

GIT --- Part of the [git](git.md) suite
