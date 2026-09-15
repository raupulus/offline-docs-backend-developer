---
title: gitglossary
description: A Git Glossary
source_url: https://git-scm.com/doc/gitglossary
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: gitglossary.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: guides
order: 1870
---

gitglossary(7) ==============

NAME ---- gitglossary - A Git Glossary

SYNOPSIS -------- \*

DESCRIPTION -----------

<div class="included" data-path="glossary-content.adoc">

<span id="def_alternate_object_database"></span>alternate object database  
Via the alternates mechanism, a <a href="#def_repository" class="cross-reference">repository</a> can inherit part of its <a href="#def_object_database" class="cross-reference">object database</a> from another object database, which is called an "alternate".

<span id="def_bare_repository"></span>bare repository  
A bare repository is normally an appropriately named <a href="#def_directory" class="cross-reference">directory</a> with a `.git` suffix that does not have a locally checked-out copy of any of the files under revision control. That is, all of the Git administrative and control files that would normally be present in the hidden `.git` sub-directory are directly present in the `repository.git` directory instead, and no other files are present and checked out. Usually publishers of public repositories make bare repositories available.

<span id="def_blob_object"></span>blob object  
Untyped <a href="#def_object" class="cross-reference">object</a>, e.g. the contents of a file.

<span id="def_branch"></span>branch  
A "branch" is a line of development. The most recent <a href="#def_commit" class="cross-reference">commit</a> on a branch is referred to as the tip of that branch. The tip of the branch is <a href="#def_ref" class="cross-reference">referenced</a> by a branch <a href="#def_head" class="cross-reference">head</a>, which moves forward as additional development is done on the branch. A single Git <a href="#def_repository" class="cross-reference">repository</a> can track an arbitrary number of branches, but your <a href="#def_working_tree" class="cross-reference">working tree</a> is associated with just one of them (the "current" or "checked out" branch), and <a href="#def_HEAD" class="cross-reference">HEAD</a> points to that branch.

<span id="def_cache"></span>cache  
Obsolete for: <a href="#def_index" class="cross-reference">index</a>.

<span id="def_chain"></span>chain  
A list of objects, where each <a href="#def_object" class="cross-reference">object</a> in the list contains a reference to its successor (for example, the successor of a <a href="#def_commit" class="cross-reference">commit</a> could be one of its <a href="#def_parent" class="cross-reference">parents</a>).

<span id="def_changeset"></span>changeset  
BitKeeper/cvsps speak for "<a href="#def_commit" class="cross-reference">commit</a>". Since Git does not store changes, but states, it really does not make sense to use the term "changesets" with Git.

<span id="def_checkout"></span>checkout  
The action of updating all or part of the <a href="#def_working_tree" class="cross-reference">working tree</a> with a <a href="#def_tree_object" class="cross-reference">tree object</a> or <a href="#def_blob_object" class="cross-reference">blob</a> from the <a href="#def_object_database" class="cross-reference">object database</a>, and updating the <a href="#def_index" class="cross-reference">index</a> and <a href="#def_HEAD" class="cross-reference">HEAD</a> if the whole working tree has been pointed at a new <a href="#def_branch" class="cross-reference">branch</a>.

<span id="def_cherry-picking"></span>cherry-picking  
In <a href="#def_SCM" class="cross-reference">SCM</a> jargon, "cherry pick" means to choose a subset of changes out of a series of changes (typically commits) and record them as a new series of changes on top of a different codebase. In Git, this is performed by the "git cherry-pick" command to extract the change introduced by an existing <a href="#def_commit" class="cross-reference">commit</a> and to record it based on the tip of the current <a href="#def_branch" class="cross-reference">branch</a> as a new commit.

<span id="def_clean"></span>clean  
A <a href="#def_working_tree" class="cross-reference">working tree</a> is clean, if it corresponds to the <a href="#def_revision" class="cross-reference">revision</a> referenced by the current <a href="#def_head" class="cross-reference">head</a>. Also see "<a href="#def_dirty" class="cross-reference">dirty</a>".

<span id="def_commit"></span>commit  
As a noun: A single point in the Git history; the entire history of a project is represented as a set of interrelated commits. The word "commit" is often used by Git in the same places other revision control systems use the words "revision" or "version". Also used as a short hand for <a href="#def_commit_object" class="cross-reference">commit object</a>.

As a verb: The action of storing a new snapshot of the project’s state in the Git history, by creating a new commit representing the current state of the <a href="#def_index" class="cross-reference">index</a> and advancing <a href="#def_HEAD" class="cross-reference">HEAD</a> to point at the new commit.

<span id="def_commit_graph_general"></span>commit graph concept, representations and usage  
A synonym for the <a href="#def_DAG" class="cross-reference">DAG</a> structure formed by the commits in the object database, <a href="#def_ref" class="cross-reference">referenced</a> by branch tips, using their <a href="#def_chain" class="cross-reference">chain</a> of linked commits. This structure is the definitive commit graph. The graph can be represented in other ways, e.g. the <a href="#def_commit_graph_file" class="cross-reference">"commit-graph" file</a>.

<span id="def_commit_graph_file"></span>commit-graph file  
The "commit-graph" (normally hyphenated) file is a supplemental representation of the <a href="#def_commit_graph_general" class="cross-reference">commit graph</a> which accelerates commit graph walks. The "commit-graph" file is stored either in the .git/objects/info directory or in the info directory of an alternate object database.

<span id="def_commit_object"></span>commit object  
An <a href="#def_object" class="cross-reference">object</a> which contains the information about a particular <a href="#def_revision" class="cross-reference">revision</a>, such as <a href="#def_parent" class="cross-reference">parents</a>, committer, author, date and the <a href="#def_tree_object" class="cross-reference">tree object</a> which corresponds to the top <a href="#def_directory" class="cross-reference">directory</a> of the stored revision.

<span id="def_commit-ish"></span>commit-ish (also committish)  
A <a href="#def_commit_object" class="cross-reference">commit object</a> or an <a href="#def_object" class="cross-reference">object</a> that can be recursively <a href="#def_dereference" class="cross-reference">dereferenced</a> to a commit object. The following are all commit-ishes: a commit object, a <a href="#def_tag_object" class="cross-reference">tag object</a> that points to a commit object, a tag object that points to a tag object that points to a commit object, etc.

<span id="def_core_git"></span>core Git  
Fundamental data structures and utilities of Git. Exposes only limited source code management tools.

<span id="def_DAG"></span>DAG  
Directed acyclic graph. The <a href="#def_commit_object" class="cross-reference">commit objects</a> form a directed acyclic graph, because they have parents (directed), and the graph of commit objects is acyclic (there is no <a href="#def_chain" class="cross-reference">chain</a> which begins and ends with the same <a href="#def_object" class="cross-reference">object</a>).

<span id="def_dangling_object"></span>dangling object  
An <a href="#def_unreachable_object" class="cross-reference">unreachable object</a> which is not <a href="#def_reachable" class="cross-reference">reachable</a> even from other unreachable objects; a dangling object has no references to it from any reference or <a href="#def_object" class="cross-reference">object</a> in the <a href="#def_repository" class="cross-reference">repository</a>.

<span id="def_dereference"></span>dereference  
Referring to a <a href="#def_symref" class="cross-reference">symbolic ref</a>: the action of accessing the <a href="#def_ref" class="cross-reference">reference</a> pointed at by a symbolic ref. Recursive dereferencing involves repeating the aforementioned process on the resulting ref until a non-symbolic reference is found.

Referring to a <a href="#def_tag_object" class="cross-reference">tag object</a>: the action of accessing the <a href="#def_object" class="cross-reference">object</a> a tag points at. Tags are recursively dereferenced by repeating the operation on the result object until the result has either a specified <a href="#def_object_type" class="cross-reference">object type</a> (where applicable) or any non-"tag" object type. A synonym for "recursive dereference" in the context of tags is "<a href="#def_peel" class="cross-reference">peel</a>".

Referring to a <a href="#def_commit_object" class="cross-reference">commit object</a>: the action of accessing the commit’s tree object. Commits cannot be dereferenced recursively.

Unless otherwise specified, "dereferencing" as it used in the context of Git commands or protocols is implicitly recursive.

<span id="def_detached_HEAD"></span>detached HEAD  
Normally the <a href="#def_HEAD" class="cross-reference">HEAD</a> stores the name of a <a href="#def_branch" class="cross-reference">branch</a>, and commands that operate on the history HEAD represents operate on the history leading to the tip of the branch the HEAD points at. However, Git also allows you to <a href="#def_checkout" class="cross-reference">check out</a> an arbitrary <a href="#def_commit" class="cross-reference">commit</a> that isn’t necessarily the tip of any particular branch. The HEAD in such a state is called "detached".

Note that commands that operate on the history of the current branch (e.g. `git` `commit` to build a new history on top of it) still work while the HEAD is detached. They update the HEAD to point at the tip of the updated history without affecting any branch. Commands that update or inquire information *about* the current branch (e.g. `git` `branch` `--set-upstream-to` that sets what remote-tracking branch the current branch integrates with) obviously do not work, as there is no (real) current branch to ask about in this state.

<span id="def_directory"></span>directory  
The list you get with "ls" :-)

<span id="def_dirty"></span>dirty  
A <a href="#def_working_tree" class="cross-reference">working tree</a> is said to be "dirty" if it contains modifications which have not been <a href="#def_commit" class="cross-reference">committed</a> to the current <a href="#def_branch" class="cross-reference">branch</a>.

<span id="def_evil_merge"></span>evil merge  
An evil merge is a <a href="#def_merge" class="cross-reference">merge</a> that introduces changes that do not appear in any <a href="#def_parent" class="cross-reference">parent</a>.

<span id="def_fast_forward"></span>fast-forward  
A fast-forward is a special type of <a href="#def_merge" class="cross-reference">merge</a> where you have a <a href="#def_revision" class="cross-reference">revision</a> and you are "merging" another <a href="#def_branch" class="cross-reference">branch</a>’s changes that happen to be a descendant of what you have. In such a case, you do not make a new <a href="#def_merge" class="cross-reference">merge</a> <a href="#def_commit" class="cross-reference">commit</a> but instead just update your branch to point at the same revision as the branch you are merging. This will happen frequently on a <a href="#def_remote_tracking_branch" class="cross-reference">remote-tracking branch</a> of a remote <a href="#def_repository" class="cross-reference">repository</a>.

<span id="def_fetch"></span>fetch  
Fetching a <a href="#def_branch" class="cross-reference">branch</a> means to get the branch’s <a href="#def_head_ref" class="cross-reference">head ref</a> from a remote <a href="#def_repository" class="cross-reference">repository</a>, to find out which objects are missing from the local <a href="#def_object_database" class="cross-reference">object database</a>, and to get them, too. See also [git-fetch](git-fetch.md).

<span id="def_file_system"></span>file system  
Linus Torvalds originally designed Git to be a user space file system, i.e. the infrastructure to hold files and directories. That ensured the efficiency and speed of Git.

<span id="def_git_archive"></span>Git archive  
Synonym for <a href="#def_repository" class="cross-reference">repository</a> (for arch people).

<span id="def_gitfile"></span>gitfile  
A plain file `.git` at the root of a working tree that points at the directory that is the real repository. For proper use see [git-worktree](git-worktree.md) or [git-submodule](git-submodule.md). For syntax see [gitrepository-layout](gitrepository-layout.md).

<span id="def_grafts"></span>grafts  
Grafts enable two otherwise different lines of development to be joined together by recording fake ancestry information for commits. This way you can make Git pretend the set of <a href="#def_parent" class="cross-reference">parents</a> a <a href="#def_commit" class="cross-reference">commit</a> has is different from what was recorded when the commit was created. Configured via the `.git/info/grafts` file.

Note that the grafts mechanism is outdated and can lead to problems transferring objects between repositories; see [git-replace](git-replace.md) for a more flexible and robust system to do the same thing.

<span id="def_hash"></span>hash  
In Git’s context, synonym for <a href="#def_object_name" class="cross-reference">object name</a>.

<span id="def_head"></span>head  
A <a href="#def_ref" class="cross-reference">named reference</a> to the <a href="#def_commit" class="cross-reference">commit</a> at the tip of a <a href="#def_branch" class="cross-reference">branch</a>. Heads are stored in a file in `$GIT_DIR/refs/heads/` directory, except when using packed refs. (See [git-pack-refs](git-pack-refs.md).)

<span id="def_HEAD"></span>HEAD  
The current <a href="#def_branch" class="cross-reference">branch</a>. In more detail: Your \<\<def_working_tree, working tree\>\> is normally derived from the state of the tree referred to by HEAD. HEAD is a reference to one of the <a href="#def_head" class="cross-reference">heads</a> in your repository, except when using a <a href="#def_detached_HEAD" class="cross-reference">detached HEAD</a>, in which case it directly references an arbitrary commit.

<span id="def_head_ref"></span>head ref  
A synonym for <a href="#def_head" class="cross-reference">head</a>.

<span id="def_hook"></span>hook  
During the normal execution of several Git commands, call-outs are made to optional scripts that allow a developer to add functionality or checking. Typically, the hooks allow for a command to be pre-verified and potentially aborted, and allow for a post-notification after the operation is done. The hook scripts are found in the `$GIT_DIR/hooks/` directory, and are enabled by simply removing the `.sample` suffix from the filename. In earlier versions of Git you had to make them executable.

<span id="def_index"></span>index  
A collection of files with stat information, whose contents are stored as objects. The index is a stored version of your <a href="#def_working_tree" class="cross-reference">working tree</a>. Truth be told, it can also contain a second, and even a third version of a working tree, which are used when <a href="#def_merge" class="cross-reference">merging</a>. See "THE INDEX" in [gitdatamodel](gitdatamodel.md) for details.

<span id="def_index_entry"></span>index entry  
The information regarding a particular file, stored in the <a href="#def_index" class="cross-reference">index</a>. An index entry can be unmerged, if a <a href="#def_merge" class="cross-reference">merge</a> was started, but not yet finished (i.e. if the index contains multiple versions of that file).

<span id="def_master"></span>master  
The default development <a href="#def_branch" class="cross-reference">branch</a>. Whenever you create a Git <a href="#def_repository" class="cross-reference">repository</a>, a branch named "master" is created, and becomes the active branch. In most cases, this contains the local development, though that is purely by convention and is not required.

<span id="def_merge"></span>merge  
As a verb: To bring the contents of another <a href="#def_branch" class="cross-reference">branch</a> (possibly from an external <a href="#def_repository" class="cross-reference">repository</a>) into the current branch. In the case where the merged-in branch is from a different repository, this is done by first <a href="#def_fetch" class="cross-reference">fetching</a> the remote branch and then merging the result into the current branch. This combination of fetch and merge operations is called a <a href="#def_pull" class="cross-reference">pull</a>. Merging is performed by an automatic process that identifies changes made since the branches diverged, and then applies all those changes together. In cases where changes conflict, manual intervention may be required to complete the merge.

As a noun: unless it is a <a href="#def_fast_forward" class="cross-reference">fast-forward</a>, a successful merge results in the creation of a new <a href="#def_commit" class="cross-reference">commit</a> representing the result of the merge, and having as <a href="#def_parent" class="cross-reference">parents</a> the tips of the merged <a href="#def_branch" class="cross-reference">branches</a>. This commit is referred to as a "merge commit", or sometimes just a "merge".

<span id="def_object"></span>object  
The unit of storage in Git. It is uniquely identified by the <a href="#def_SHA1" class="cross-reference">SHA-1</a> of its contents. Consequently, an object cannot be changed. See "OBJECTS" in [gitdatamodel](gitdatamodel.md) for details.

<span id="def_object_database"></span>object database  
Stores a set of "objects", and an individual <a href="#def_object" class="cross-reference">object</a> is identified by its <a href="#def_object_name" class="cross-reference">object name</a>. The objects usually live in `$GIT_DIR/objects/`.

<span id="def_object_identifier"></span>object identifier, object ID, oid  
Synonyms for <a href="#def_object_name" class="cross-reference">object name</a>.

<span id="def_object_name"></span>object name  
The unique identifier of an <a href="#def_object" class="cross-reference">object</a>. The object name is usually represented by a 40 character hexadecimal string. Also colloquially called <a href="#def_SHA1" class="cross-reference">SHA-1</a>.

<span id="def_object_type"></span>object type  
One of the identifiers "<a href="#def_commit_object" class="cross-reference">commit</a>", "<a href="#def_tree_object" class="cross-reference">tree</a>", "<a href="#def_tag_object" class="cross-reference">tag</a>" or "<a href="#def_blob_object" class="cross-reference">blob</a>" describing the type of an <a href="#def_object" class="cross-reference">object</a>.

<span id="def_octopus"></span>octopus  
To <a href="#def_merge" class="cross-reference">merge</a> more than two <a href="#def_branch" class="cross-reference">branches</a>.

<span id="def_orphan"></span>orphan  
The act of getting on a <a href="#def_branch" class="cross-reference">branch</a> that does not exist yet (i.e., an <a href="#def_unborn" class="cross-reference">unborn</a> branch). After such an operation, the commit first created becomes a commit without a parent, starting a new history.

<span id="def_origin"></span>origin  
The default upstream <a href="#def_repository" class="cross-reference">repository</a>. Most projects have at least one upstream project which they track. By default ’origin’ is used for that purpose. New upstream updates will be fetched into <a href="#def_remote_tracking_branch" class="cross-reference">remote-tracking branches</a> named origin/name-of-upstream-branch, which you can see using `git` `branch` `-r`.

<span id="def_overlay"></span>overlay  
Only update and add files to the working directory, but don’t delete them, similar to how ’cp -R’ would update the contents in the destination directory. This is the default mode in a <a href="#def_checkout" class="cross-reference">checkout</a> when checking out files from the <a href="#def_index" class="cross-reference">index</a> or a <a href="#def_tree-ish" class="cross-reference">tree-ish</a>. In contrast, no-overlay mode also deletes tracked files not present in the source, similar to ’rsync --delete’.

<span id="def_pack"></span>pack  
A set of objects which have been compressed into one file (to save space or to transmit them efficiently).

<span id="def_pack_index"></span>pack index  
The list of identifiers, and other information, of the objects in a <a href="#def_pack" class="cross-reference">pack</a>, to assist in efficiently accessing the contents of a pack.

<span id="def_pathspec"></span>pathspec  
Pattern used to limit paths in Git commands.

Pathspecs are used on the command line of "git ls-files", "git ls-tree", "git add", "git grep", "git diff", "git checkout", and many other commands to limit the scope of operations to some subset of the tree or working tree. See the documentation of each command for whether paths are relative to the current directory or toplevel. The pathspec syntax is as follows:

<div>

- any path matches itself

- the pathspec up to the last slash represents a directory prefix. The scope of that pathspec is limited to that subtree.

- the rest of the pathspec is a pattern for the remainder of the pathname. Paths relative to the directory prefix will be matched against that pattern using fnmatch(3); in particular, ’\*’ and ’?’ *can* match directory separators.

<div>

\
For example, Documentation/\*.jpg will match all .jpg files in the Documentation subtree, including Documentation/chapter_1/figure_1.jpg.\
A pathspec that begins with a colon `:` has special meaning. In the short form, the leading colon `:` is followed by zero or more "magic signature" letters (which optionally is terminated by another colon `:`), and the remainder is the pattern to match against the path. The "magic signature" consists of ASCII symbols that are neither alphanumeric, glob, regex special characters nor colon. The optional colon that terminates the "magic signature" can be omitted if the pattern begins with a character that does not belong to "magic signature" symbol set and is not a colon.\
In the long form, the leading colon `:` is followed by an open parenthesis `(`, a comma-separated list of zero or more "magic words", and a close parentheses `)`, and the remainder is the pattern to match against the path.\
A pathspec with only a colon means "there is no pathspec". This form should not be combined with other pathspec. +

</div>

top;; The magic word `top` (magic signature: `/`) makes the pattern match from the root of the working tree, even when you are running the command from inside a subdirectory.

literal;; Wildcards in the pattern such as `*` or `?` are treated as literal characters.

icase;; Case insensitive match.

glob;; Git treats the pattern as a shell glob suitable for consumption by fnmatch(3) with the FNM_PATHNAME flag: wildcards in the pattern will not match a / in the pathname. For example, "Documentation/\*.html" matches "Documentation/git.html" but not "Documentation/ppc/ppc.html" or "tools/perf/Documentation/perf.html".\
Two consecutive asterisks (“\*\*”) in patterns matched against full pathname may have special meaning:

- A leading “\*\*” followed by a slash means match in all directories. For example, “\*\*/foo” matches file or directory “foo” anywhere. “\*\*/foo/bar” matches file or directory “bar” anywhere that is directly under directory “foo”.

<!-- -->

- A trailing “/\*\*” matches everything inside. For example, “abc/\*\*” matches all files inside directory "abc", relative to the location of the `.gitignore` file, with infinite depth.

<!-- -->

- A slash followed by two consecutive asterisks then a slash matches zero or more directories. For example, “a/\*\*/b” matches “a/b”, “a/x/b”, “a/x/y/b” and so on.

<!-- -->

- Other consecutive asterisks are considered invalid.

\
Glob magic is incompatible with literal magic.

attr;; After `attr:` comes a space separated list of "attribute requirements", all of which must be met in order for the path to be considered a match; this is in addition to the usual non-magic pathspec pattern matching. See [gitattributes](gitattributes.md).\
Each of the attribute requirements for the path takes one of these forms:

- “ATTR” requires that the attribute `ATTR` be set.

<!-- -->

- “-ATTR” requires that the attribute `ATTR` be unset.

<!-- -->

- “ATTR=VALUE” requires that the attribute `ATTR` be set to the string `VALUE`.

<!-- -->

- “!ATTR” requires that the attribute `ATTR` be unspecified.

\
Note that when matching against a tree object, attributes are still obtained from working tree, not from the given tree object.

exclude;; After a path matches any non-exclude pathspec, it will be run through all exclude pathspecs (magic signature: `!` or its synonym `^`). If it matches, the path is ignored. When there is no non-exclude pathspec, the exclusion is applied to the result set as if invoked without any pathspec.

</div>

<span id="def_parent"></span>parent  
A <a href="#def_commit_object" class="cross-reference">commit object</a> contains a (possibly empty) list of the logical predecessor(s) in the line of development, i.e. its parents.

<span id="def_peel"></span>peel  
The action of recursively <a href="#def_dereference" class="cross-reference">dereferencing</a> a <a href="#def_tag_object" class="cross-reference">tag object</a>.

<span id="def_pickaxe"></span>pickaxe  
The term <a href="#def_pickaxe" class="cross-reference">pickaxe</a> refers to an option to the diffcore routines that help select changes that add or delete a given text string. With the `--pickaxe-all` option, it can be used to view the full <a href="#def_changeset" class="cross-reference">changeset</a> that introduced or removed, say, a particular line of text. See [git-diff](git-diff.md).

<span id="def_plumbing"></span>plumbing  
Cute name for <a href="#def_core_git" class="cross-reference">core Git</a>.

<span id="def_porcelain"></span>porcelain  
Cute name for programs and program suites depending on <a href="#def_core_git" class="cross-reference">core Git</a>, presenting a high level access to core Git. Porcelains expose more of a <a href="#def_SCM" class="cross-reference">SCM</a> interface than the <a href="#def_plumbing" class="cross-reference">plumbing</a>.

<span id="def_per_worktree_ref"></span>per-worktree ref  
Refs that are per-<a href="#def_worktree" class="cross-reference">worktree</a>, rather than global. This is presently only <a href="#def_HEAD" class="cross-reference">HEAD</a> and any refs that start with `refs/bisect/`, but might later include other unusual refs.

<span id="def_pseudoref"></span>pseudoref  
A ref that has different semantics than normal refs. These refs can be read via normal Git commands, but cannot be written to by commands like [git-update-ref](git-update-ref.md).

The following pseudorefs are known to Git:

- `FETCH_HEAD` is written by [git-fetch](git-fetch.md) or [git-pull](git-pull.md). It may refer to multiple object IDs. Each object ID is annotated with metadata indicating where it was fetched from and its fetch status.

<!-- -->

- `MERGE_HEAD` is written by [git-merge](git-merge.md) when resolving merge conflicts. It contains all commit IDs which are being merged.

<span id="def_pull"></span>pull  
Pulling a <a href="#def_branch" class="cross-reference">branch</a> means to <a href="#def_fetch" class="cross-reference">fetch</a> it and <a href="#def_merge" class="cross-reference">merge</a> it. See also [git-pull](git-pull.md).

<span id="def_push"></span>push  
Pushing a <a href="#def_branch" class="cross-reference">branch</a> means to get the branch’s <a href="#def_head_ref" class="cross-reference">head ref</a> from a remote <a href="#def_repository" class="cross-reference">repository</a>, find out if it is an ancestor to the branch’s local head ref, and in that case, putting all objects, which are <a href="#def_reachable" class="cross-reference">reachable</a> from the local head ref, and which are missing from the remote repository, into the remote <a href="#def_object_database" class="cross-reference">object database</a>, and updating the remote head ref. If the remote <a href="#def_head" class="cross-reference">head</a> is not an ancestor to the local head, the push fails.

<span id="def_reachable"></span>reachable  
All of the ancestors of a given <a href="#def_commit" class="cross-reference">commit</a> are said to be "reachable" from that commit. More generally, one <a href="#def_object" class="cross-reference">object</a> is reachable from another if we can reach the one from the other by a <a href="#def_chain" class="cross-reference">chain</a> that follows <a href="#def_tag" class="cross-reference">tags</a> to whatever they tag, <a href="#def_commit_object" class="cross-reference">commits</a> to their parents or trees, and <a href="#def_tree_object" class="cross-reference">trees</a> to the trees or <a href="#def_blob_object" class="cross-reference">blobs</a> that they contain.

<span id="def_reachability_bitmap"></span>reachability bitmaps  
Reachability bitmaps store information about the <a href="#def_reachable" class="cross-reference">reachability</a> of a selected set of commits in a packfile, or a multi-pack index (MIDX), to speed up object search. The bitmaps are stored in a ".bitmap" file. A repository may have at most one bitmap file in use. The bitmap file may belong to either one pack, or the repository’s multi-pack index (if it exists).

<span id="def_rebase"></span>rebase  
To reapply a series of changes from a <a href="#def_branch" class="cross-reference">branch</a> to a different base, and reset the <a href="#def_head" class="cross-reference">head</a> of that branch to the result.

<span id="def_ref"></span>ref  
A name that points to an <a href="#def_object_name" class="cross-reference">object name</a> or another ref (the latter is called a <a href="#def_symref" class="cross-reference">symbolic ref</a>). For convenience, a ref can sometimes be abbreviated when used as an argument to a Git command; see [gitrevisions](gitrevisions.md) for details. Refs are stored in the <a href="#def_repository" class="cross-reference">repository</a>.

The ref namespace is hierarchical. Ref names must either start with `refs/` or be located in the root of the hierarchy. For the latter, their name must follow these rules:

<div>

- The name consists of only upper-case characters or underscores.

<!-- -->

- The name ends with “\_HEAD” or is equal to “HEAD”.

  <div>

  \
  There are some irregular refs in the root of the hierarchy that do not match these rules. The following list is exhaustive and shall not be extended in the future: +

  </div>

- `AUTO_MERGE`

<!-- -->

- `BISECT_EXPECTED_REV`

<!-- -->

- `NOTES_MERGE_PARTIAL`

<!-- -->

- `NOTES_MERGE_REF`

<!-- -->

- `MERGE_AUTOSTASH`

</div>

Different subhierarchies are used for different purposes. For example, the `refs/heads/` hierarchy is used to represent local branches whereas the `refs/tags/` hierarchy is used to represent local tags..

See also "REFERENCES" in [gitdatamodel](gitdatamodel.md).

<span id="def_reflog"></span>reflog  
A reflog shows the local "history" of a ref. In other words, it can tell you what the 3rd last revision in *this* repository was, and what was the current state in *this* repository, yesterday 9:14pm.

See "REFLOGS" in [gitdatamodel](gitdatamodel.md) for a short explanation of the format. See [git-reflog](git-reflog.md) for details.

<span id="def_refspec"></span>refspec  
A "refspec" is used by <a href="#def_fetch" class="cross-reference">fetch</a> and <a href="#def_push" class="cross-reference">push</a> to describe the mapping between remote <a href="#def_ref" class="cross-reference">ref</a> and local ref. See [git-fetch](git-fetch.md) or [git-push](git-push.md) for details.

<span id="def_remote"></span>remote repository  
A <a href="#def_repository" class="cross-reference">repository</a> which is used to track the same project but resides somewhere else. To communicate with remotes, see <a href="#def_fetch" class="cross-reference">fetch</a> or <a href="#def_push" class="cross-reference">push</a>.

<span id="def_remote_tracking_branch"></span>remote-tracking branch  
A <a href="#def_ref" class="cross-reference">ref</a> that is used to follow changes from another <a href="#def_repository" class="cross-reference">repository</a>. It typically looks like ’refs/remotes/foo/bar’ (indicating that it tracks a branch named ’bar’ in a remote named ’foo’), and matches the right-hand-side of a configured fetch <a href="#def_refspec" class="cross-reference">refspec</a>. A remote-tracking branch should not contain direct modifications or have local commits made to it.

<span id="def_repository"></span>repository  
A collection of <a href="#def_ref" class="cross-reference">refs</a> together with an <a href="#def_object_database" class="cross-reference">object database</a> containing all objects which are <a href="#def_reachable" class="cross-reference">reachable</a> from the refs, possibly accompanied by meta data from one or more <a href="#def_porcelain" class="cross-reference">porcelains</a>. A repository can share an object database with other repositories via <a href="#def_alternate_object_database" class="cross-reference">alternates mechanism</a>.

<span id="def_resolve"></span>resolve  
The action of fixing up manually what a failed automatic <a href="#def_merge" class="cross-reference">merge</a> left behind.

<span id="def_revision"></span>revision  
Synonym for <a href="#def_commit" class="cross-reference">commit</a> (the noun).

<span id="def_rewind"></span>rewind  
To throw away part of the development, i.e. to assign the <a href="#def_head" class="cross-reference">head</a> to an earlier <a href="#def_revision" class="cross-reference">revision</a>.

<span id="def_SCM"></span>SCM  
Source code management (tool).

<span id="def_SHA1"></span>SHA-1  
"Secure Hash Algorithm 1"; a cryptographic hash function. In the context of Git used as a synonym for <a href="#def_object_name" class="cross-reference">object name</a>.

<span id="def_shallow_clone"></span>shallow clone  
Mostly a synonym to <a href="#def_shallow_repository" class="cross-reference">shallow repository</a> but the phrase makes it more explicit that it was created by running `git` `clone` `--depth=…` command.

<span id="def_shallow_repository"></span>shallow repository  
A shallow <a href="#def_repository" class="cross-reference">repository</a> has an incomplete history some of whose <a href="#def_commit" class="cross-reference">commits</a> have <a href="#def_parent" class="cross-reference">parents</a> cauterized away (in other words, Git is told to pretend that these commits do not have the parents, even though they are recorded in the \<\<def_commit_object,commit object\>\>). This is sometimes useful when you are interested only in the recent history of a project even though the real history recorded in the upstream is much larger. A shallow repository is created by giving the `--depth` option to [git-clone](git-clone.md), and its history can be later deepened with [git-fetch](git-fetch.md).

<span id="def_stash"></span>stash entry  
An <a href="#def_object" class="cross-reference">object</a> used to temporarily store the contents of a <a href="#def_dirty" class="cross-reference">dirty</a> working directory and the index for future reuse.

<span id="def_submodule"></span>submodule  
A <a href="#def_repository" class="cross-reference">repository</a> that holds the history of a separate project inside another repository (the latter of which is called <a href="#def_superproject" class="cross-reference">superproject</a>).

<span id="def_superproject"></span>superproject  
A <a href="#def_repository" class="cross-reference">repository</a> that references repositories of other projects in its working tree as <a href="#def_submodule" class="cross-reference">submodules</a>. The superproject knows about the names of (but does not hold copies of) commit objects of the contained submodules.

<span id="def_symref"></span>symref  
Symbolic reference: instead of containing the <a href="#def_SHA1" class="cross-reference">SHA-1</a> id itself, it is of the format ’ref: refs/some/thing’ and when referenced, it recursively <a href="#def_dereference" class="cross-reference">dereferences</a> to this reference. ’<a href="#def_HEAD" class="cross-reference">HEAD</a>’ is a prime example of a symref. Symbolic references are manipulated with the [git-symbolic-ref](git-symbolic-ref.md) command.

<span id="def_tag"></span>tag  
A <a href="#def_ref" class="cross-reference">ref</a> under `refs/tags/` namespace that points to an object of an arbitrary type (typically a tag points to either a <a href="#def_tag_object" class="cross-reference">tag</a> or a <a href="#def_commit_object" class="cross-reference">commit object</a>). In contrast to a <a href="#def_head" class="cross-reference">head</a>, a tag is not updated by the `commit` command. A Git tag has nothing to do with a Lisp tag (which would be called an <a href="#def_object_type" class="cross-reference">object type</a> in Git’s context). A tag is most typically used to mark a particular point in the commit ancestry <a href="#def_chain" class="cross-reference">chain</a>.

<span id="def_tag_object"></span>tag object  
An <a href="#def_object" class="cross-reference">object</a> containing a <a href="#def_ref" class="cross-reference">ref</a> pointing to another object, which can contain a message just like a <a href="#def_commit_object" class="cross-reference">commit object</a>. It can also contain a (PGP) signature, in which case it is called a "signed tag object".

<span id="def_topic_branch"></span>topic branch  
A regular Git <a href="#def_branch" class="cross-reference">branch</a> that is used by a developer to identify a conceptual line of development. Since branches are very easy and inexpensive, it is often desirable to have several small branches that each contain very well defined concepts or small incremental yet related changes.

<span id="def_trailer"></span>trailer  
Key-value metadata. Trailers are optionally found at the end of a commit message. Might be called "footers" or "tags" in other communities. See [git-interpret-trailers](git-interpret-trailers.md).

<span id="def_tree"></span>tree  
Either a <a href="#def_working_tree" class="cross-reference">working tree</a>, or a \<\<def_tree_object,tree object\>\> together with the dependent <a href="#def_blob_object" class="cross-reference">blob</a> and tree objects (i.e. a stored representation of a working tree).

<span id="def_tree_object"></span>tree object  
An <a href="#def_object" class="cross-reference">object</a> containing a list of file names and modes along with refs to the associated blob and/or tree objects. A <a href="#def_tree" class="cross-reference">tree</a> is equivalent to a <a href="#def_directory" class="cross-reference">directory</a>.

<span id="def_tree-ish"></span>tree-ish (also treeish)  
A <a href="#def_tree_object" class="cross-reference">tree object</a> or an <a href="#def_object" class="cross-reference">object</a> that can be recursively <a href="#def_dereference" class="cross-reference">dereferenced</a> to a tree object. Dereferencing a <a href="#def_commit_object" class="cross-reference">commit object</a> yields the tree object corresponding to the <a href="#def_revision" class="cross-reference">revision</a>’s top <a href="#def_directory" class="cross-reference">directory</a>. The following are all tree-ishes: a <a href="#def_commit-ish" class="cross-reference">commit-ish</a>, a tree object, a <a href="#def_tag_object" class="cross-reference">tag object</a> that points to a tree object, a tag object that points to a tag object that points to a tree object, etc.

<span id="def_unborn"></span>unborn  
The <a href="#def_HEAD" class="cross-reference">HEAD</a> can point at a <a href="#def_branch" class="cross-reference">branch</a> that does not yet exist and that does not have any commit on it yet, and such a branch is called an unborn branch. The most typical way users encounter an unborn branch is by creating a repository anew without cloning from elsewhere. The HEAD would point at the ’main’ (or ’master’, depending on your configuration) branch that is yet to be born. Also some operations can get you on an unborn branch with their <a href="#def_orphan" class="cross-reference">orphan</a> option.

<span id="def_unmerged_index"></span>unmerged index  
An <a href="#def_index" class="cross-reference">index</a> which contains unmerged <a href="#def_index_entry" class="cross-reference">index entries</a>.

<span id="def_unreachable_object"></span>unreachable object  
An <a href="#def_object" class="cross-reference">object</a> which is not <a href="#def_reachable" class="cross-reference">reachable</a> from a <a href="#def_branch" class="cross-reference">branch</a>, <a href="#def_tag" class="cross-reference">tag</a>, or any other reference.

<span id="def_upstream_branch"></span>upstream branch  
The default <a href="#def_branch" class="cross-reference">branch</a> that is merged into the branch in question (or the branch in question is rebased onto). It is configured via branch.\<name\>.remote and branch.\<name\>.merge. If the upstream branch of ’A’ is ’origin/B’ sometimes we say "’A’ is tracking ’origin/B’".

<span id="def_working_tree"></span>working tree  
The tree of actual checked out files. The working tree normally contains the contents of the <a href="#def_HEAD" class="cross-reference">HEAD</a> commit’s tree, plus any local changes that you have made but not yet committed.

<span id="def_worktree"></span>worktree  
A repository can have zero (i.e. bare repository) or one or more worktrees attached to it. One "worktree" consists of a "working tree" and repository metadata, most of which are shared among other worktrees of a single repository, and some of which are maintained separately per worktree (e.g. the index, HEAD and pseudorefs like MERGE_HEAD, per-worktree refs and per-worktree configuration file).

</div>

SEE ALSO -------- [gitdatamodel](gitdatamodel.md), [gittutorial](gittutorial.md), [gittutorial-2](gittutorial-2.md), [gitcvs-migration](gitcvs-migration.md), [giteveryday](giteveryday.md), [The Git User’s Manual](user-manual.html)

GIT --- Part of the [git](git.md) suite
