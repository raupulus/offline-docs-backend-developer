---
title: git-remote-fd
description: Reflect smart transport stream back to caller
source_url: https://git-scm.com/doc/git-remote-fd
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-remote-fd.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1170
---

git-remote-fd(1) ================

NAME ---- git-remote-fd - Reflect smart transport stream back to caller

SYNOPSIS -------- "fd::\<infd\>\[,\<outfd\>\]\[/\<anything\>\]" (as URL)

DESCRIPTION ----------- This helper uses specified file descriptors to connect to a remote Git server. This is not meant for end users but for programs and scripts calling git fetch, push, or archive.

If only \<infd\> is given, it is assumed to be a bidirectional socket connected to a remote Git server (git-upload-pack, git-receive-pack, or git-upload-archive). If both \<infd\> and \<outfd\> are given, they are assumed to be pipes connected to a remote Git server (\<infd\> being the inbound pipe and \<outfd\> being the outbound pipe).

It is assumed that any handshaking procedures have already been completed (such as sending service request for git://) before this helper is started.

\<anything\> can be any string. It is ignored. It is meant for providing information to the user in the URL in case that URL is displayed in some context.

ENVIRONMENT VARIABLES --------------------- GIT_TRANSLOOP_DEBUG:: If set, prints debugging information about various reads/writes.

EXAMPLES -------- `git` `fetch` `fd::17` `master`:: Fetch master, using file descriptor \#17 to communicate with git-upload-pack.

\`git fetch fd  

17/foo master\`  
Same as above.

\`git push fd  

7,8 master (as URL)\`  
Push master, using file descriptor \#7 to read data from git-receive-pack and file descriptor \#8 to write data to the same service.

\`git push fd  

7,8/bar master\`  
Same as above.

SEE ALSO -------- [gitremote-helpers](gitremote-helpers.md)

GIT --- Part of the [git](git.md) suite
