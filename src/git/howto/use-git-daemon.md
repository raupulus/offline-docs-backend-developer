---
title: use-git-daemon
source_url: https://git-scm.com/doc/use-git-daemon
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: howto/use-git-daemon.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: howto
order: 2220
---

Content-type: text/asciidoc

How to use git-daemon =====================

Git can be run in inetd mode and in stand alone mode. But all you want is to let a coworker pull from you, and therefore need to set up a Git server real quick, right?

Note that git-daemon is not really chatty at the moment, especially when things do not go according to plan (e.g. a socket could not be bound).

Another word of warning: if you run

    $ git ls-remote git://127.0.0.1/rule-the-world.git

and you see a message like

    fatal: The remote end hung up unexpectedly

it only means that *something* went wrong. To find out *what* went wrong, you have to ask the server. (Git refuses to be more precise for your security only. Take off your shoes now. You have any coins in your pockets? Sorry, not allowed — who knows what you planned to do with them?)

With these two caveats, let’s see an example:

    $ git daemon --reuseaddr --verbose --base-path=/home/gitte/git \
      --export-all -- /home/gitte/git/rule-the-world.git

(Of course, unless your user name is `gitte` *and* your repository is in ~/rule-the-world.git, you have to adjust the paths. If your repository is not bare, be aware that you have to type the path to the .git directory!)

This invocation tries to reuse the address if it is already taken (this can save you some debugging, because otherwise killing and restarting git-daemon could just silently fail to bind to a socket).

Also, it is (relatively) verbose when somebody actually connects to it. It also sets the base path, which means that all the projects which can be accessed using this daemon have to reside in or under that path.

The option `--export-all` just means that you *don’t* have to create a file named `git-daemon-export-ok` in each exported repository. (Otherwise, git-daemon would complain loudly, and refuse to cooperate.)

Last of all, the repository which should be exported is specified. It is a good practice to put the paths after a "--" separator.

Now, test your daemon with

    $ git ls-remote git://127.0.0.1/rule-the-world.git

If this does not work, find out why, and submit a patch to this document.
