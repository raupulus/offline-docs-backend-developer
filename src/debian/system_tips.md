---
title: System tips
source_url: https://www.debian.org/doc/manuals/debian-reference/_system_tips
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 09_system_tips.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 100
---

## System tips

Here, I describe basic tips to configure and manage systems, mostly from the console.

## The screen program

`screen(1)` is a very useful tool for people to access remote sites via unreliable or intermittent connections since it supports interrupted network connections.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `screen` | @-@popcon1@-@ | @-@psize1@-@ | terminal multiplexer with VT100/ANSI terminal emulation |
| `tmux` | @-@popcon1@-@ | @-@psize1@-@ | terminal multiplexer alternative (Use "Control-B" instead) |

List of programs to support interrupted network connections

### The use scenario for screen(1)

`screen(1)` not only allows one terminal window to work with multiple processes, but also allows **remote shell process to survive interrupted connections**. Here is a typical use scenario of `screen(1)`.

1.  You login to a remote machine.

2.  You start `screen` on a single console.

3.  You execute multiple programs in `screen` windows created with `^A c` ("Control-A" followed by "c").

4.  You switch among the multiple `screen` windows by `^A n` ("Control-A" followed by "n").

5.  Suddenly you need to leave your terminal, but you don't want to lose your active work by keeping the connection.

6.  You may **detach** the `screen` session by any methods.

    - Brutally unplug your network connection

    - Type `^A d` ("Control-A" followed by "d") and manually logging out from the remote connection

    - Type `^A DD` ("Control-A" followed by "DD") to have `screen` detach and log you out

7.  You log in again to the same remote machine (even from a different terminal).

8.  You start `screen` as "`screen -r`".

9.  `screen` magically **reattaches** all previous `screen` windows with all actively running programs.

> [!TIP]
> You can save connection fees with `screen` for metered network connections such as dial-up and packet ones, because you can leave a process active while disconnected, and then re-attach it later when you connect again.

### Key bindings for the screen command

In a `screen` session, all keyboard inputs are sent to your current window except for the command keystroke. All `screen` command keystrokes are entered by typing `^A` ("Control-A") plus a single key \[plus any parameters\]. Here are important ones to remember.

| key binding | meaning                                           |
|:------------|:--------------------------------------------------|
| `^A ?`      | show a help screen (display key bindings)         |
| `^A c`      | create a new window and switch to it              |
| `^A n`      | go to next window                                 |
| `^A p`      | go to previous window                             |
| `^A 0`      | go to window number 0                             |
| `^A 1`      | go to window number 1                             |
| `^A w`      | show a list of windows                            |
| `^A a`      | send a Ctrl-A to current window as keyboard input |
| `^A h`      | write a hardcopy of current window to file        |
| `^A H`      | begin/end logging current window to file          |
| `^A ^X`     | lock the terminal (password protected)            |
| `^A d`      | detach screen session from the terminal           |
| `^A DD`     | detach screen session and log out                 |

List of key bindings for screen

See `screen(1)` for details.

## Data recording and presentation

### The log daemon

Many programs record their activities under the "`/var/log/`" directory.

- The system log daemon: `rsyslogd(8)`

See [???](#_the_system_message) and [???](#_the_kernel_message).

### Log analyzer

Here are notable log analyzers ("`~Gsecurity::log-analyzer`" in `aptitude(8)`).

| package | popcon | size | description |
|:---|:---|:---|:---|
| `logwatch` | @-@popcon1@-@ | @-@psize1@-@ | log analyzer with nice output written in Perl |
| `fail2ban` | @-@popcon1@-@ | @-@psize1@-@ | ban IPs that cause multiple authentication errors |
| `analog` | @-@popcon1@-@ | @-@psize1@-@ | web server log analyzer |
| `awstats` | @-@popcon1@-@ | @-@psize1@-@ | powerful and featureful web server log analyzer |
| `sarg` | @-@popcon1@-@ | @-@psize1@-@ | squid analysis report generator |
| `pflogsumm` | @-@popcon1@-@ | @-@psize1@-@ | Postfix log entry summarizer |
| `syslog-summary` | @-@popcon1@-@ | @-@psize1@-@ | summarize the contents of a syslog log file |
| `fwlogwatch` | @-@popcon1@-@ | @-@psize1@-@ | firewall log analyzer |
| `squidview` | @-@popcon1@-@ | @-@psize1@-@ | monitor and analyze squid access.log files |
| `swatch` | @-@popcon1@-@ | @-@psize1@-@ | log file viewer with regexp matching, highlighting, and hooks |
| `crm114` | @-@popcon1@-@ | @-@psize1@-@ | Controllable Regex Mutilator and Spam Filter (CRM114) |
| `icmpinfo` | @-@popcon1@-@ | @-@psize1@-@ | interpret ICMP messages |

List of system log analyzers

> [!NOTE]
> [CRM114](http://crm114.sourceforge.net/) provides language infrastructure to write **fuzzy** filters with the [TRE regex library](http://www.laurikari.net/tre/). Its popular use is spam mail filter but it can be used as log analyzer.

### Recording the shell activities cleanly

The simple use of `script(1)` (see [???](#_recording_the_shell_activities)) to record shell activity produces a file with control characters. This can be avoided by using `col(1)` as the following.

    $ script
    Script started, file is typescript

Do whatever … and press `Ctrl-D` to exit `script`.

    $ col -bx <typescript >cleanedfile
    $ vim cleanedfile

If you don't have `script` (for example, during the boot process in the initramfs), you can use the following instead.

    $ sh -i 2>&1 | tee typescript

> [!TIP]
> Some `x-terminal-emulator` such as `gnome-terminal` can record. You may wish to extend line buffer for scrollback.

> [!TIP]
> You may use `screen(1)` with "`^A H`" (see [Key bindings for the screen command](#_key_bindings_for_the_screen_command)) to perform recording of console.

> [!TIP]
> You may use `emacs(1)` with "`M-x shell`", "`M-x eshell`", or "`M-x term`" to perform recording of console. You may later use "`C-x C-w`" to write the buffer to a file.

### Customized display of text data

Although pager tools such as `more(1)` and `less(1)` (see [???](#_the_pager)) and custom tools for highlighting and formatting (see [???](#_highlighting_and_formatting_plain_text_data)) can display text data nicely, general purpose editors (see [???](#_the_text_editor)) are most versatile and customizable.

> [!TIP]
> For `vim(1)` and its pager mode alias `view(1)`, "`:set hls`" enables highlighted search.

### Customized display of time and date

The default display format of time and date by the "`ls -l`" command depends on the **locale** (see [???](#_timestamps) for value). The "`$LANG`" variable is referred first and it can be overridden by the "`$LC_TIME`" variable.

The actual default display format for each locale depends on the version of the standard C library (the `libc6` package) used. I.e., different releases of Debian had different defaults.

If you really wish to customize this display format of time and date beyond the **locale**, you should set the **time style value** by the "`--time-style`" argument or by the "`$TIME_STYLE`" value (see `ls(1)`, `date(1)`, "`info coreutils 'ls invocation'`").

| time style value | locale | display of time and date |
|:---|:---|:---|
| `iso` | any | `01-19 00:15` |
| `long-iso` | any | `2009-01-19 00:15` |
| `full-iso` | any | `2009-01-19 00:15:16.000000000 +0900` |
| `locale` | `C` | `Jan 19 00:15` |
| `locale` | `en_US.UTF-8` | `Jan 19 00:15` |
| `locale` | `es_ES.UTF-8` | `ene 19 00:15` |
| `+%d.%m.%y %H:%M` | any | `19.01.09 00:15` |
| `+%d.%b.%y %H:%M` | `C` or `en_US.UTF-8` | `19.Jan.09 00:15` |
| `+%d.%b.%y %H:%M` | `es_ES.UTF-8` | `19.ene.09 00:15` |

Display examples of time and date for the "`ls -l`" command for `wheezy`

> [!TIP]
> You can eliminate typing long option on commandline using command alias, e.g. "`alias ls='ls --time-style=+%d.%m.%y\ %H:%M'`" (see [???](#_command_alias)).

> [!TIP]
> [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is followed for these iso-formats.

### Colorized shell echo

Shell echo to most modern terminals can be colorized using [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) (see "`/usr/share/doc/xterm/ctlseqs.txt.gz`").

For example, try the following

    $ RED=$(printf "\x1b[31m")
    $ NORMAL=$(printf "\x1b[0m")
    $ REVERSE=$(printf "\x1b[7m")
    $ echo "${RED}RED-TEXT${NORMAL} ${REVERSE}REVERSE-TEXT${NORMAL}"

### Colorized commands

Colorized commands are handy for inspecting their output in the interactive environment. I include the following in my "`~/.bashrc`".

    if [ "$TERM" != "dumb" ]; then
        eval "`dircolors -b`"
        alias ls='ls --color=always'
        alias ll='ls --color=always -l'
        alias la='ls --color=always -A'
        alias less='less -R'
        alias ls='ls --color=always'
        alias grep='grep --color=always'
        alias egrep='egrep --color=always'
        alias fgrep='fgrep --color=always'
        alias zgrep='zgrep --color=always'
    else
        alias ll='ls -l'
        alias la='ls -A'
    fi

The use of alias limits color effects to the interactive command usage. It has advantage over exporting environment variable "`export GREP_OPTIONS='--color=auto'`" since color can be seen under pager programs such as `less(1)`. If you wish to suppress color when piping to other programs, use "`--color=auto`" instead in the above example for "`~/.bashrc`".

> [!TIP]
> You can turn off these colorizing aliases in the interactive environment by invoking shell with "`TERM=dumb bash`".

### Recording the editor activities for complex repeats

You can record the editor activities for complex repeats.

For [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)), as follows.

- "`qa`": start recording typed characters into named register "`a`".

- … editor activities

- "`q`": end recording typed characters.

- "`@a`": execute the contents of register "`a`".

For [Emacs](https://en.wikipedia.org/wiki/Emacs), as follows.

- "`C-x (`": start defining a keyboard macro.

- … editor activities

- "`C-x )`": end defining a keyboard macro.

- "`C-x e`": execute a keyboard macro.

### Recording the graphic image of an X application

There are few ways to record the graphic image of an X application, including an `xterm` display.

| package         | popcon        | size         | command     |
|:----------------|:--------------|:-------------|:------------|
| `xbase-clients` | @-@popcon1@-@ | @-@psize1@-@ | `xwd(1)`    |
| `gimp`          | @-@popcon1@-@ | @-@psize1@-@ | GUI menu    |
| `imagemagick`   | @-@popcon1@-@ | @-@psize1@-@ | `import(1)` |
| `scrot`         | @-@popcon1@-@ | @-@psize1@-@ | `scrot(1)`  |

List of graphic image manipulation tools

### Recording changes in configuration files

There are specialized tools to record changes in configuration files with help of DVCS system.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `etckeeper` | @-@popcon1@-@ | @-@psize1@-@ | store configuration files and their metadata with [Git](https://en.wikipedia.org/wiki/Git_(software)) (default), [Mercurial](https://en.wikipedia.org/wiki/Mercurial_(software)), or [Bazaar](https://en.wikipedia.org/wiki/Bazaar_(software)) (new) |
| `changetrack` | @-@popcon1@-@ | @-@psize1@-@ | store configuration files with [RCS](https://en.wikipedia.org/wiki/Revision_Control_System) (old) |

List of packages to record configuration history in VCS

I recommend to use the `etckeeper` package with `git(1)` which put entire "`/etc`" under VCS control. Its installation guide and tutorial are found in "`/usr/share/doc/etckeeper/README.gz`".

Essentially, running "`sudo etckeeper init`" initializes the git repository for "`/etc`" just like the process explained in [???](#_git_for_recording_configuration_history) but with special hook scripts for more thorough setups.

As you change your configuration, you can use `git(1)` normally to record them. It automatically records changes nicely every time you run package management commands, too.

> [!TIP]
> You can browse the change history of "`/etc`" by executing "`sudo GIT_DIR=/etc/.git gitk`" with clear view for new installed packages, removed packages, and version changes of packages.

## Monitoring, controlling, and starting program activities

Program activities can be monitored and controlled using specialized tools.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `coreutils` | @-@popcon1@-@ | @-@psize1@-@ | `nice(1)`: run a program with modified scheduling priority |
| `bsdutils` | @-@popcon1@-@ | @-@psize1@-@ | `renice(1)`: modify the scheduling priority of a running process |
| `procps` | @-@popcon1@-@ | @-@psize1@-@ | "`/proc`" filesystem utilities: `ps(1)`, `top(1)`, `kill(1)`, `watch(1)`, … |
| `psmisc` | @-@popcon1@-@ | @-@psize1@-@ | "`/proc`" filesystem utilities: `killall(1)`, `fuser(1)`, `peekfd(1)`, `pstree(1)` |
| `time` | @-@popcon1@-@ | @-@psize1@-@ | `time(1)`: run a program to report system resource usages with respect to time |
| `sysstat` | @-@popcon1@-@ | @-@psize1@-@ | `sar(1)`, `iostat(1)`, `mpstat(1)`, …: system performance tools for Linux |
| `isag` | @-@popcon1@-@ | @-@psize1@-@ | Interactive System Activity Grapher for sysstat |
| `lsof` | @-@popcon1@-@ | @-@psize1@-@ | `lsof(8)`: list files opened by a running process using "`-p`" option |
| `strace` | @-@popcon1@-@ | @-@psize1@-@ | `strace(1)`: trace system calls and signals |
| `ltrace` | @-@popcon1@-@ | @-@psize1@-@ | `ltrace(1)`: trace library calls |
| `xtrace` | @-@popcon1@-@ | @-@psize1@-@ | `xtrace(1)`: trace communication between X11 client and server |
| `powertop` | @-@popcon1@-@ | @-@psize1@-@ | `powertop(1)`: information about system power use |
| `cron` | @-@popcon1@-@ | @-@psize1@-@ | run processes according to a schedule in background from `cron(8)` daemon |
| `anacron` | @-@popcon1@-@ | @-@psize1@-@ | cron-like command scheduler for systems that don't run 24 hours a day |
| `at` | @-@popcon1@-@ | @-@psize1@-@ | `at(1)` or `batch(1)`: run a job at a specified time or below certain load level |

List of tools for monitoring and controlling program activities

> [!TIP]
> The `procps` packages provide very basics of monitoring, controlling, and starting program activities. You should learn all of them.

### Timing a process

Display time used by the process invoked by the command.

    # time some_command >/dev/null
    real    0m0.035s       # time on wall clock (elapsed real time)
    user    0m0.000s       # time in user mode
    sys     0m0.020s       # time in kernel mode

### The scheduling priority

A nice value is used to control the scheduling priority for the process.

| nice value | scheduling priority                            |
|:-----------|:-----------------------------------------------|
| 19         | lowest priority process (nice)                 |
| 0          | very high priority process for user            |
| -20        | very high priority process for root (not-nice) |

List of nice values for the scheduling priority

    # nice  -19 top                                      # very nice
    # nice --20 wodim -v -eject speed=2 dev=0,0 disk.img # very fast

Sometimes an extreme nice value does more harm than good to the system. Use this command carefully.

### The ps command

The `ps(1)` command on a Debian system support both BSD and SystemV features and helps to identify the process activity statically.

| style    | typical command | feature           |
|:---------|:----------------|:------------------|
| BSD      | `ps aux`        | display %CPU %MEM |
| System V | `ps -efH`       | display PPID      |

List of ps command styles

For the zombie (defunct) children process, you can kill them by the parent process ID identified in the "`PPID`" field.

The `pstree(1)` command display a tree of processes.

### The top command

`top(1)` on the Debian system has rich features and helps to identify what process is acting funny dynamically.

It is an interactive full screen program. You can get its usage help press by pressing the "h"-key and terminate it by pressing the "q"-key.

### Listing files opened by a process

You can list all files opened by a process with a process ID (PID), e.g. 1, by the following.

    $ sudo lsof -p 1

PID=1 is usually the `init` program.

### Tracing program activities

You can trace program activity with `strace(1)`, `ltrace(1)`, or `xtrace(1)` for system calls and signals, library calls, or communication between X11 client and server.

You can trace system calls of the `ls` command as the following.

    $ sudo strace ls

### Identification of processes using files or sockets

You can also identify processes using files by `fuser(1)`, e.g. for "`/var/log/mail.log`" by the following.

    $ sudo fuser -v /var/log/mail.log
                         USER        PID ACCESS COMMAND
    /var/log/mail.log:   root       2946 F.... rsyslogd

You see that file "`/var/log/mail.log`" is open for writing by the `rsyslogd(8)` command.

You can also identify processes using sockets by `fuser(1)`, e.g. for "`smtp/tcp`" by the following.

    $ sudo fuser -v smtp/tcp
                         USER        PID ACCESS COMMAND
    smtp/tcp:            Debian-exim   3379 F.... exim4

Now you know your system runs `exim4(8)` to handle [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) connections to [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) port (25).

### Repeating a command with a constant interval

`watch(1)` executes a program repeatedly with a constant interval while showing its output in fullscreen.

    $ watch w

This displays who is logged on to the system updated every 2 seconds.

### Repeating a command looping over files

There are several ways to repeat a command looping over files matching some condition, e.g. matching glob pattern "`*.ext`".

- Shell for-loop method (see [???](#_shell_loops)):

<!-- -->

    for x in *.ext; do if [ -f "$x"]; then command "$x" ; fi; done

- `find(1)` and `xargs(1)` combination:

<!-- -->

    find . -type f -maxdepth 1 -name '*.ext' -print0 | xargs -0 -n 1 command

- `find(1)` with "`-exec`" option with a command:

<!-- -->

    find . -type f -maxdepth 1 -name '*.ext' -exec command '{}' \;

- `find(1)` with "`-exec`" option with a short shell script:

<!-- -->

    find . -type f -maxdepth 1 -name '*.ext' -exec sh -c "command '{}' && echo 'successful'" \;

The above examples are written to ensure proper handling of funny file names such as ones containing spaces. See [???](#_idioms_for_the_selection_of_files) for more advance uses of `find(1)`.

### Starting a program from GUI

For the [command-line interface (CLI)](https://en.wikipedia.org/wiki/Command-line_interface), the first program with the matching name found in the directories specified in the `$PATH` environment variable is executed. See [???](#_the_literal_path_literal_variable).

For the [graphical user interface (GUI)](https://en.wikipedia.org/wiki/Graphical_user_interface) compliant to the [freedesktop.org](http://www.freedesktop.org/) standards, the `*.desktop` files in the `/usr/share/applications/` directory provide necessary attributes for the GUI menu display of each program. See [???](#_freedesktop_org_menu).

For example, the `chromium.desktop` file defines attributes for the "Chromium Web Browser" such as "Name" for the program name, "Exec" for the program execution path and arguments, "Icon" for the icon used, etc. (see the [Desktop Entry Specification](http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)) as follows:

    [Desktop Entry]
    Version=1.0
    Name=Chromium Web Browser
    GenericName=Web Browser
    Comment=Access the Internet
    Comment[fr]=Explorer le Web
    Exec=/usr/bin/chromium %U
    Terminal=false
    X-MultipleArgs=false
    Type=Application
    Icon=chromium
    Categories=Network;WebBrowser;
    MimeType=text/html;text/xml;application/xhtml_xml;x-scheme-handler/http;x-scheme-handler/https;
    StartupWMClass=Chromium
    StartupNotify=true

This is an oversimplified description. The `*.desktop` files are scanned as follows.

The desktop environment sets `$XDG_DATA_HOME` and `$XDG_DATA_DIR` environment variables. For example, under the GNOME 3:

- `$XDG_DATA_HOME` is unset. (The default value of `$HOME/.local/share` is used.)

- `$XDG_DATA_DIRS` is set to `/usr/share/gnome:/usr/local/share/:/usr/share/`.

So the base directories (see [XDG Base Directory Specification](http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html)) and the `applications` directories are as follows.

- `$HOME/.local/share/` → `$HOME/.local/share/applications/`

- `/usr/share/gnome/` → `/usr/share/gnome/applications/`

- `/usr/local/share/` → `/usr/local/share/applications/`

- `/usr/share/` → `/usr/share/applications/`

The `*.desktop` files are scanned in these `applications` directories in this order.

> [!TIP]
> A user custom GUI menu entry can be created by adding a `*.desktop` file in the `$HOME/.local/share/applications/` directory.

> [!TIP]
> Similarly, if a `*.desktop` file is created in the `autostart` directory under these base directories, the specified program in the `*.desktop` file is executed automatically when the desktop environment is started. See [Desktop Application Autostart Specification](http://standards.freedesktop.org/autostart-spec/autostart-spec-latest.html).

> [!TIP]
> Similarly, if a `*.desktop` file is created in the `$HOME/Desktop` directory and the Desktop environment is configured to support the desktop icon launcher feature, the specified program in it is executed upon clicking the icon. Please note that the actual name of the `$HOME/Desktop` directory is locale dependent. See `xdg-user-dirs-update(1)`.

### Customizing program to be started

Some programs start another program automatically. Here are check points for customizing this process.

- Application configuration menu:

  - GNOME3 desktop: "Settings" → "System" → "Details" → "Default Applications"

  - KDE desktop: "K" → "Control Center" → "KDE Components" → "Component Chooser"

  - Iceweasel browser: "Edit" → "Preferences" → "Applications"

  - `mc(1)`: "`/etc/mc/mc.ext`"

- Environment variables such as "`$BROWSER`", "`$EDITOR`", "`$VISUAL`", and "`$PAGER`" (see `eviron(7)`)

- The `update-alternatives(1)` system for programs such as "`editor`", "`view`", "`x-www-browser`", "`gnome-www-browser`", and "`www-browser`" (see [???](#_setting_a_default_text_editor))

- the "`~/.mailcap`" and "`/etc/mailcap`" file contents which associate [MIME](https://en.wikipedia.org/wiki/MIME) type with program (see `mailcap(5)`)

- The "`~/.mime.types`" and "`/etc/mime.types`" file contents which associate file name extension with [MIME](https://en.wikipedia.org/wiki/MIME) type (see `run-mailcap(1)`)

> [!TIP]
> `update-mime(8)` updates the "`/etc/mailcap`" file using "`/etc/mailcap.order`" file (see `mailcap.order(5)`).

> [!TIP]
> The `debianutils` package provides `sensible-browser(1)`, `sensible-editor(1)`, and `sensible-pager(1)` which make sensible decisions on which editor, pager, and web browser to call, respectively. I recommend you to read these shell scripts.

> [!TIP]
> In order to run a console application such as `mutt` under X as your preferred application, you should create an X application as following and set "`/usr/local/bin/mutt-term`" as your preferred application to be started as described.

    # cat /usr/local/bin/mutt-term <<EOF
    #!/bin/sh
    gnome-terminal -e "mutt \$@"
    EOF
    chmod 755 /usr/local/bin/mutt-term

### Killing a process

Use `kill(1)` to kill (or send a signal to) a process by the process ID.

Use `killall(1)` or `pkill(1)` to do the same by the process command name and other attributes.

| signal value | signal name | function       |
|:-------------|:------------|:---------------|
| 1            | HUP         | restart daemon |
| 15           | TERM        | normal kill    |
| 9            | KILL        | kill hard      |

List of frequently used signals for kill command

### Scheduling tasks once

Run the `at(1)` command to schedule a one-time job by the following.

    $ echo 'command -args'| at 3:40 monday

### Scheduling tasks regularly

Use `cron(8)` to schedule tasks regularly. See `crontab(1)` and `crontab(5)`.

You can schedule to run processes as a normal user, e.g. `foo` by creating a `crontab(5)` file as "`/var/spool/cron/crontabs/foo`" with "`crontab -e`" command.

Here is an example of a `crontab(5)` file.

    # use /bin/sh to run commands, no matter what /etc/passwd says
    SHELL=/bin/sh
    # mail any output to paul, no matter whose crontab this is
    MAILTO=paul
    # Min Hour DayOfMonth Month DayOfWeek command (Day... are OR'ed)
    # run at 00:05, every day
    5  0  *  * *   $HOME/bin/daily.job >> $HOME/tmp/out 2>&1
    # run at 14:15 on the first of every month -- output mailed to paul
    15 14 1  * *   $HOME/bin/monthly
    # run at 22:00 on weekdays(1-5), annoy Joe. % for newline, last % for cc:
    0 22 *   * 1-5 mail -s "It's 10pm" joe%Joe,%%Where are your kids?%.%%
    23 */2 1 2 *   echo "run 23 minutes after 0am, 2am, 4am ..., on Feb 1"
    5  4 *   * sun echo "run at 04:05 every Sunday"
    # run at 03:40 on the first Monday of each month
    40 3 1-7 * *   [ "$(date +%a)" == "Mon" ] && command -args

> [!TIP]
> For the system not running continuously, install the `anacron` package to schedule periodic commands at the specified intervals as closely as machine-uptime permits. See `anacron(8)` and `anacrontab(5)`.

> [!TIP]
> For scheduled system maintenance scripts, you can run them periodically from root account by placing such scripts in "`/etc/cron.hourly/`", "`/etc/cron.daily/`", "`/etc/cron.weekly/`", or "`/etc/cron.monthly/`". Execution timings of these scripts can be customized by "`/etc/crontab`" and "`/etc/anacrontab`".

### Alt-SysRq key

Insurance against system malfunction is provided by the kernel compile option "Magic SysRq key" ([SAK](https://en.wikipedia.org/wiki/Secure_attention_key) key) which is now the default for the Debian kernel. Pressing Alt-SysRq followed by one of the following keys does the magic of rescuing control of the system.

| key following Alt-SysRq | description of action |
|:---|:---|
| `r` | restore the keyboard from **r**aw mode after X crashes |
| `0` | change the console loglevel to **0** to reduce error messages |
| `k` | **k**ill all processes on the **current virtual console** |
| `e` | send a SIGT**E**RM to all processes, except for `init(8)` |
| `i` | send a SIGK**I**LL to all processes, except for `init(8)` |
| `s` | **s**ync all mounted filesystems to avoid data corruption |
| `u` | remount all mounted filesystems read-only (**u**mount) |
| `b` | re**b**oot the system without syncing or unmounting |

List of SAK command keys

> [!TIP]
> Read the `signal(7)`, `kill(1)`, and `sync(1)` manpages to understand the description above.

The combination of "Alt-SysRq s", "Alt-SysRq u", and "Alt-SysRq r" is good for getting out of really bad situations and gaining usable keyboard access without stopping the system.

See "`/usr/share/doc/linux-doc-3.*/Documentation/sysrq.txt.gz`".

> [!CAUTION]
> The Alt-SysRq feature may be considered a security risk by allowing users access to root-privileged functions. Placing "`echo 0 >/proc/sys/kernel/sysrq`" in "`/etc/rc.local`" or "`kernel.sysrq = 0`" in "`/etc/sysctl.conf`" disables the Alt-SysRq feature.

> [!TIP]
> From SSH terminal etc., you can use the Alt-SysRq feature by writing to the "`/proc/sysrq-trigger`". For example, "`echo s > /proc/sysrq-trigger; echo u > /proc/sysrq-trigger`" from the root shell prompt **s**yncs and **u**mounts all mounted filesystems.

## System maintenance tips

### Who is on the system?

You can check who is on the system by the following.

- `who(1)` shows who is logged on.

- `w(1)` shows who is logged on and what they are doing.

- `last(1)` shows listing of last logged in user.

- `lastb(1)` shows listing of last bad logged in users.

> [!TIP]
> "`/var/run/utmp`", and "`/var/log/wtmp`" hold such user information. See `login(1)` and `utmp(5)`.

### Warning everyone

You can send message to everyone who is logged on to the system with `wall(1)` by the following.

    $ echo "We are shutting down in 1 hour" | wall

### Hardware identification

For the [PCI](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect)-like devices ([AGP](https://en.wikipedia.org/wiki/Accelerated_Graphics_Port), [PCI-Express](https://en.wikipedia.org/wiki/PCI_Express), [CardBus](https://en.wikipedia.org/wiki/PC_Card#CardBus), [ExpressCard](https://en.wikipedia.org/wiki/ExpressCard), etc.), `lspci(8)` (probably with "`-nn`" option) is a good start for the hardware identification.

Alternatively, you can identify the hardware by reading contents of "`/proc/bus/pci/devices`" or browsing directory tree under "`/sys/bus/pci`" (see [???](#_procfs_and_sysfs)).

| package | popcon | size | description |
|:---|:---|:---|:---|
| `pciutils` | @-@popcon1@-@ | @-@psize1@-@ | Linux PCI Utilities: `lspci(8)` |
| `usbutils` | @-@popcon1@-@ | @-@psize1@-@ | Linux USB utilities: `lsusb(8)` |
| `pcmciautils` | @-@popcon1@-@ | @-@psize1@-@ | PCMCIA utilities for Linux: `pccardctl(8)` |
| `scsitools` | @-@popcon1@-@ | @-@psize1@-@ | collection of tools for SCSI hardware management: `lsscsi(8)` |
| `procinfo` | @-@popcon1@-@ | @-@psize1@-@ | system information obtained from "`/proc`": `lsdev(8)` |
| `lshw` | @-@popcon1@-@ | @-@psize1@-@ | information about hardware configuration: `lshw(1)` |
| `discover` | @-@popcon1@-@ | @-@psize1@-@ | hardware identification system: `discover(8)` |

List of hardware identification tools

### Hardware configuration

Although most of the hardware configuration on modern GUI desktop systems such as GNOME and KDE can be managed through accompanying GUI configuration tools, it is a good idea to know some basics methods to configure them.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `console-setup` | @-@popcon1@-@ | @-@psize1@-@ | Linux console font and keytable utilities |
| `x11-xserver-utils` | @-@popcon1@-@ | @-@psize1@-@ | X server utilities: `xset(1)`, `xmodmap(1)` |
| `acpid` | @-@popcon1@-@ | @-@psize1@-@ | daemon to manage events delivered by the Advanced Configuration and Power Interface (ACPI) |
| `acpi` | @-@popcon1@-@ | @-@psize1@-@ | utility to display information on ACPI devices |
| `sleepd` | @-@popcon1@-@ | @-@psize1@-@ | daemon to put a laptop to sleep during inactivity |
| `hdparm` | @-@popcon1@-@ | @-@psize1@-@ | hard disk access optimization (see [Optimization of hard disk](#_optimization_of_hard_disk)) |
| `smartmontools` | @-@popcon1@-@ | @-@psize1@-@ | control and monitor storage systems using [S.M.A.R.T.](https://en.wikipedia.org/wiki/S.M.A.R.T.) |
| `setserial` | @-@popcon1@-@ | @-@psize1@-@ | collection of tools for serial port management |
| `memtest86+` | @-@popcon1@-@ | @-@psize1@-@ | collection of tools for memory hardware management |
| `scsitools` | @-@popcon1@-@ | @-@psize1@-@ | collection of tools for [SCSI](https://en.wikipedia.org/wiki/SCSI) hardware management |
| `setcd` | @-@popcon1@-@ | @-@psize1@-@ | compact disc drive access optimization |
| `big-cursor` | @-@popcon1@-@ | @-@psize1@-@ | larger mouse cursors for X |

List of hardware configuration tools

Here, [ACPI](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface) is a newer framework for the power management system than [APM](https://en.wikipedia.org/wiki/Advanced_Power_Management).

> [!TIP]
> CPU frequency scaling on modern system is governed by kernel modules such as `acpi_cpufreq`.

### System and hardware time

The following sets system and hardware time to MM/DD hh:mm, CCYY.

    # date MMDDhhmmCCYY
    # hwclock --utc --systohc
    # hwclock --show

Times are normally displayed in the local time on the Debian system but the hardware and system time usually use [UTC(GMT)](https://en.wikipedia.org/wiki/UTC).

If the hardware (BIOS) time is set to UTC, change the setting to "`UTC=yes`" in the "`/etc/default/rcS`".

The following reconfigure the timezone used by the Debian system.

    # dpkg-reconfigure tzdata

If you wish to update system time via network, consider to use the [NTP](https://en.wikipedia.org/wiki/Network_Time_Protocol) service with the packages such as `ntp`, `ntpdate`, and `chrony`.

> [!TIP]
> Under [systemd](https://en.wikipedia.org/wiki/Systemd), use `systemd-timesyncd` for the network time synchronization instead. See `systemd-timesyncd(8)`.

See the following.

- [Managing Accurate Date and Time HOWTO](http://www.tldp.org/HOWTO/TimePrecision-HOWTO/index.html)

- [NTP Public Services Project](http://www.ntp.org/)

- The `ntp-doc` package

> [!TIP]
> `ntptrace(8)` in the `ntp` package can trace a chain of NTP servers back to the primary source.

### The terminal configuration

There are several components to configure character console and `ncurses(3)` system features.

- The "`/etc/terminfo/*/*`" file (`terminfo(5)`)

- The "`$TERM`" environment variable (`term(7)`)

- `setterm(1)`, `stty(1)`, `tic(1)`, and `toe(1)`

If the `terminfo` entry for `xterm` doesn't work with a non-Debian `xterm`, change your terminal type, "`$TERM`", from "`xterm`" to one of the feature-limited versions such as "`xterm-r6`" when you log in to a Debian system remotely. See "`/usr/share/doc/libncurses5/FAQ`" for more. "`dumb`" is the lowest common denominator for "`$TERM`".

### The sound infrastructure

Device drivers for sound cards for current Linux are provided by [Advanced Linux Sound Architecture (ALSA)](https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture). ALSA provides emulation mode for previous [Open Sound System (OSS)](https://en.wikipedia.org/wiki/Open_Sound_System) for compatibility.

> [!TIP]
> Use "`cat /dev/urandom > /dev/audio`" or `speaker-test(1)` to test speaker (^C to stop).

> [!TIP]
> If you can not get sound, your speaker may be connected to a muted output. Modern sound system has many outputs. `alsamixer(1)` in the `alsa-utils` package is useful to configure volume and mute settings.

Application softwares may be configured not only to access sound devices directly but also to access them via some standardized sound server system.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `alsa-utils` | @-@popcon1@-@ | @-@psize1@-@ | utilities for configuring and using ALSA |
| `oss-compat` | @-@popcon1@-@ | @-@psize1@-@ | OSS compatibility under ALSA preventing "`/dev/dsp not found`" errors |
| `jackd` | @-@popcon1@-@ | @-@psize1@-@ | [JACK Audio Connection Kit. (JACK)](https://en.wikipedia.org/wiki/JACK_Audio_Connection_Kit) server (low latency) |
| `libjack0` | @-@popcon1@-@ | @-@psize1@-@ | [JACK Audio Connection Kit. (JACK)](https://en.wikipedia.org/wiki/JACK_Audio_Connection_Kit) library (low latency) |
| `nas` | @-@popcon1@-@ | @-@psize1@-@ | [Network Audio System (NAS)](https://en.wikipedia.org/wiki/Network_Audio_System) server |
| `libaudio2` | @-@popcon1@-@ | @-@psize1@-@ | [Network Audio System (NAS)](https://en.wikipedia.org/wiki/Network_Audio_System) library |
| `pulseaudio` | @-@popcon1@-@ | @-@psize1@-@ | [PulseAudio](https://en.wikipedia.org/wiki/PulseAudio) server, replacement for ESD |
| `libpulse0` | @-@popcon1@-@ | @-@psize1@-@ | [PulseAudio](https://en.wikipedia.org/wiki/PulseAudio) client library, replacement for ESD |
| `libgstreamer1.0-0` | @-@popcon1@-@ | @-@psize1@-@ | [GStreamer](https://en.wikipedia.org/wiki/GStreamer): GNOME sound engine |
| `libphonon4` | @-@popcon1@-@ | @-@psize1@-@ | [Phonon](https://en.wikipedia.org/wiki/Phonon_(KDE)): KDE sound engine |

List of sound packages

There is usually a common sound engine for each popular desktop environment. Each sound engine used by the application can choose to connect to different sound servers.

### Disabling the screen saver

For disabling the screen saver, use following commands.

| environment | command |
|:---|:---|
| The Linux console | `setterm -powersave off` |
| The X Window (turning off screensaver) | `xset s off` |
| The X Window (disabling dpms) | `xset -dpms` |
| The X Window (GUI configuration of screen saver) | `xscreensaver-command -prefs` |

List of commands for disabling the screen saver

### Disabling beep sounds

One can always unplug the PC speaker to disable beep sounds. Removing `pcspkr` kernel module does this for you.

The following prevents the `readline(3)` program used by `bash(1)` to beep when encountering an alert character (ASCII=7).

    $ echo "set bell-style none">> ~/.inputrc

### Memory usage

There are 2 resources available for you to get the memory usage situation.

- The kernel boot message in the "`/var/log/dmesg`" contains the total exact size of available memory.

- `free(1)` and `top(1)` display information on memory resources on the running system.

Here is an example.

    # grep '\] Memory' /var/log/dmesg
    [    0.004000] Memory: 990528k/1016784k available (1975k kernel code, 25868k reserved, 931k data, 296k init)
    $ free -k
                 total       used       free     shared    buffers     cached
    Mem:        997184     976928      20256          0     129592     171932
    -/+ buffers/cache:     675404     321780
    Swap:      4545576          4    4545572

You may be wondering "dmesg tells me a free of 990 MB, and free -k says 320 MB is free. More than 600 MB missing …".

Do not worry about the large size of "`used`" and the small size of "`free`" in the "`Mem:`" line, but read the one under them (675404 and 321780 in the example above) and relax.

For my MacBook with 1GB=1048576k DRAM (video system steals some of this), I see the following.

| report              | size                             |
|:--------------------|:---------------------------------|
| Total size in dmesg | 1016784k = 1GB - 31792k          |
| Free in dmesg       | 990528k                          |
| Total under shell   | 997184k                          |
| Free under shell    | 20256k (but effectively 321780k) |

List of memory sizes reported

### System security and integrity check

Poor system maintenance may expose your system to external exploitation.

For system security and integrity check, you should start with the following.

- The `debsums` package, see `debsums(1)` and [???](#_top_level_release_file_and_authenticity).

- The `chkrootkit` package, see `chkrootkit(1)`.

- The `clamav` package family, see `clamscan(1)` and `freshclam(1)`.

- [Debian security FAQ](https://www.debian.org/security/faq).

- [Securing Debian Manual](https://www.debian.org/doc/manuals/securing-debian-howto/).

| package | popcon | size | description |
|:---|:---|:---|:---|
| `logcheck` | @-@popcon1@-@ | @-@psize1@-@ | daemon to mail anomalies in the system logfiles to the administrator |
| `debsums` | @-@popcon1@-@ | @-@psize1@-@ | utility to verify installed package files against MD5 checksums |
| `chkrootkit` | @-@popcon1@-@ | @-@psize1@-@ | [rootkit](https://en.wikipedia.org/wiki/Rootkit) detector |
| `clamav` | @-@popcon1@-@ | @-@psize1@-@ | anti-virus utility for Unix - command-line interface |
| `tiger` | @-@popcon1@-@ | @-@psize1@-@ | report system security vulnerabilities |
| `tripwire` | @-@popcon1@-@ | @-@psize1@-@ | file and directory integrity checker |
| `john` | @-@popcon1@-@ | @-@psize1@-@ | active password cracking tool |
| `aide` | @-@popcon1@-@ | @-@psize1@-@ | Advanced Intrusion Detection Environment - static binary |
| `integrit` | @-@popcon1@-@ | @-@psize1@-@ | file integrity verification program |
| `crack` | @-@popcon1@-@ | @-@psize1@-@ | password guessing program |

List of tools for system security and integrity check

Here is a simple script to check for typical world writable incorrect file permissions.

    # find / -perm 777 -a \! -type s -a \! -type l -a \! \( -type d -a -perm 1777 \)

> [!CAUTION]
> Since the `debsums` package uses [MD5](https://en.wikipedia.org/wiki/MD5) checksums stored locally, it can not be fully trusted as the system security audit tool against malicious attacks.

## Data storage tips

Booting your system with Linux [live CDs](https://en.wikipedia.org/wiki/Live_CD) or [debian-installer CDs](https://www.debian.org/releases/stable/debian-installer/) in rescue mode makes it easy for you to reconfigure data storage on your boot device.

### Disk space usage

The disk space usage can be evaluated by programs provided by the `mount`, `coreutils`, and `xdu` packages:

- `mount(8)` reports all mounted filesystems (= disks).

- `df(1)` reports the disk space usage for the file system.

- `du(1)` reports the disk space usage for the directory tree.

> [!TIP]
> You can feed the output of `du(8)` to `xdu(1x)` to produce its graphical and interactive presentation with "`du -k . |xdu`", "`sudo du -k -x / |xdu`", etc.

### Disk partition configuration

For [disk partition](https://en.wikipedia.org/wiki/Disk_partitioning) configuration, although `fdisk(8)` has been considered standard, `parted(8)` deserves some attention. "Disk partitioning data", "partition table", "partition map", and "disk label" are all synonyms.

Most PCs use the classic [Master Boot Record (MBR)](https://en.wikipedia.org/wiki/Master_boot_record) scheme to hold [disk partitioning](https://en.wikipedia.org/wiki/Disk_partitioning) data in the first sector, i.e., [LBA](https://en.wikipedia.org/wiki/Logical_block_addressing) sector 0 (512 bytes).

> [!NOTE]
> Some new PCs with [Extensible Firmware Interface (EFI)](https://en.wikipedia.org/wiki/Extensible_Firmware_Interface), including Intel-based Macs, use [GUID Partition Table (GPT)](https://en.wikipedia.org/wiki/GUID_Partition_Table) scheme to hold [disk partitioning](https://en.wikipedia.org/wiki/Disk_partitioning) data not in the first sector.

Although `fdisk(8)` has been standard for the disk partitioning tool, `parted(8)` is replacing it.

| package | popcon | size | GPT | description |
|:---|:---|:---|:---|:---|
| `util-linux` | @-@popcon1@-@ | @-@psize1@-@ | Not supported | miscellaneous system utilities including `fdisk(8)` and `cfdisk(8)` |
| `parted` | @-@popcon1@-@ | @-@psize1@-@ | Supported | GNU Parted disk partition resizing program |
| `gparted` | @-@popcon1@-@ | @-@psize1@-@ | Supported | GNOME partition editor based on `libparted` |
| `gdisk` | @-@popcon1@-@ | @-@psize1@-@ | Supported | partition editor for the GPT disk |
| `kpartx` | @-@popcon1@-@ | @-@psize1@-@ | Supported | program to create device mappings for partitions |

List of disk partition management packages

> [!CAUTION]
> Although `parted(8)` claims to create and to resize filesystem too, it is safer to do such things using best maintained specialized tools such as `mkfs(8)` (`mkfs.msdos(8)`, `mkfs.ext2(8)`, `mkfs.ext3(8)`, `mkfs.ext4(8)`, …) and `resize2fs(8)`.

> [!NOTE]
> In order to switch between [GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table) and [MBR](https://en.wikipedia.org/wiki/Master_boot_record), you need to erase first few blocks of disk contents directly (see [Clearing file contents](#_clearing_file_contents)) and use "`parted /dev/sdx mklabel gpt`" or "`parted /dev/sdx mklabel msdos`" to set it. Please note "`msdos`" is use here for [MBR](https://en.wikipedia.org/wiki/Master_boot_record).

### Accessing partition using UUID

Although reconfiguration of your partition or activation order of removable storage media may yield different names for partitions, you can access them consistently. This is also helpful if you have multiple disks and your BIOS doesn't give them consistent device names.

- `mount(8)` with "`-U`" option can mount a block device using [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier), instead of using its file name such as "`/dev/sda3`".

- "`/etc/fstab`" (see `fstab(5)`) can use [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier).

- Boot loaders ([???](#_stage_2_the_boot_loader)) may use [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier) too.

> [!TIP]
> You can probe [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier) of a block special device with `blkid(8)`.

> [!TIP]
> Device nodes of devices such as removable storage media can be made static by using [udev rules](http://www.reactivated.net/writing_udev_rules.html), if needed. See [???](#_the_udev_system).

### LVM2

LVM2 is a [logical volume manager](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)) for the Linux kernel. With LVM2, disk partitions can be created on logical volumes instead of the physical harddisks.

LVM requires the following.

- device-mapper support in the Linux kernel (default for Debian kernels)

- the userspace device-mapper support library (`libdevmapper*` package)

- the userspace LVM2 tools (`lvm2` package)

Please start learning LVM2 from the following manpages.

- `lvm(8)`: Basics of LVM2 mechanism (list of all LVM2 commands)

- `lvm.conf(5)`: Configuration file for LVM2

- `lvs(8)`: Report information about logical volumes

- `vgs(8)`: Report information about volume groups

- `pvs(8)`: Report information about physical volumes

### Filesystem configuration

For [ext4](https://en.wikipedia.org/wiki/Ext4) filesystem, the `e2fsprogs` package provides the following.

- `mkfs.ext4(8)` to create new [ext4](https://en.wikipedia.org/wiki/Ext4) filesystem

- `fsck.ext4(8)` to check and to repair existing [ext4](https://en.wikipedia.org/wiki/Ext4) filesystem

- `tune2fs(8)` to configure superblock of [ext4](https://en.wikipedia.org/wiki/Ext4) filesystem

- `debugfs(8)` to debug [ext4](https://en.wikipedia.org/wiki/Ext4) filesystem interactively. (It has `undel` command to recover deleted files.)

The `mkfs(8)` and `fsck(8)` commands are provided by the `e2fsprogs` package as front-ends to various filesystem dependent programs (`mkfs.fstype` and `fsck.fstype`). For [ext4](https://en.wikipedia.org/wiki/Ext4) filesystem, they are `mkfs.ext4(8)` and `fsck.ext4(8)` (they are symlinked to `mke2fs(8)` and `e2fsck(8)`).

Similar commands are available for each filesystem supported by Linux.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `e2fsprogs` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [ext2](https://en.wikipedia.org/wiki/Ext2)/[ext3](https://en.wikipedia.org/wiki/Ext3)/[ext4](https://en.wikipedia.org/wiki/Ext4) filesystems |
| `reiserfsprogs` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [Reiserfs](https://en.wikipedia.org/wiki/Reiserfs) filesystem |
| `dosfstools` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [FAT](https://en.wikipedia.org/wiki/File_Allocation_Table) filesystem. (Microsoft: MS-DOS, Windows) |
| `xfsprogs` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [XFS](https://en.wikipedia.org/wiki/XFS) filesystem. (SGI: IRIX) |
| `ntfs-3g` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [NTFS](https://en.wikipedia.org/wiki/NTFS) filesystem. (Microsoft: Windows NT, …) |
| `jfsutils` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [JFS](https://en.wikipedia.org/wiki/JFS_(file_system)) filesystem. (IBM: AIX, OS/2) |
| `reiser4progs` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [Reiser4](https://en.wikipedia.org/wiki/Reiser4) filesystem |
| `hfsprogs` | @-@popcon1@-@ | @-@psize1@-@ | utilities for [HFS](https://en.wikipedia.org/wiki/Hierarchical_File_System) and [HFS Plus](https://en.wikipedia.org/wiki/HFS_Plus) filesystem. (Apple: Mac OS) |
| `btrfs-progs` | @-@popcon1@-@ | @-@psize1@-@ | utilities for the [Btrfs](https://en.wikipedia.org/wiki/Btrfs) filesystem |
| `zerofree` | @-@popcon1@-@ | @-@psize1@-@ | program to zero free blocks from ext2/3/4 filesystems |

List of filesystem management packages

> [!TIP]
> [Ext4](https://en.wikipedia.org/wiki/Ext4) filesystem is the default filesystem for the Linux system and strongly recommended to use it unless you have some specific reasons not to.

> [!TIP]
> [Btrfs](https://en.wikipedia.org/wiki/Btrfs) filesystem is available in Linux kernel 3.2 (Debian `wheezy`). It is expected to be the next default filesystem after the ext4 filesystem.

> [!WARNING]
> You should not use the Btrfs filesystem for your critical data yet before it acquires the live kernel space `fsck(8)` feature and the boot loader support.

> [!TIP]
> Some tools allow access to filesystem without Linux kernel support (see [Manipulating files without mounting disk](#_manipulating_files_without_mounting_disk)).

### Filesystem creation and integrity check

The `mkfs(8)` command creates the filesystem on a Linux system. The `fsck(8)` command provides the filesystem integrity check and repair on a Linux system.

Debian now defaults to no periodic `fsck` after filesystem creation.

> [!CAUTION]
> It is generally not safe to run `fsck` on **mounted filesystems**.

> [!TIP]
> You can run the `fsck(8)` command safely on all filesystems including root filesystem on reboot by setting "`enable_periodic_fsck`" in "`/etc/mke2fs.conf`" and the max mount count to 0 using "`tune2fs -c0 /dev/<partition_name>`". See `mke2fs.conf(5)` and `tune2fs(8)`.

> [!TIP]
> Check files in "`/var/log/fsck/`" for the result of the `fsck(8)` command run from the boot script.

### Optimization of filesystem by mount options

The basic static filesystem configuration is given by "`/etc/fstab`". For example,

    # <file system> <mount point>   <type>  <options>       <dump>  <pass>
    proc            /proc           proc    defaults        0       0
    UUID=709cbe4c-80c1-56db-8ab1-dbce3146d2f7 / ext4 noatime,errors=remount-ro 0 1
    UUID=817bae6b-45d2-5aca-4d2a-1267ab46ac23 none swap sw  0       0
    /dev/scd0       /media/cdrom0   udf,iso9660 user,noauto 0       0

> [!TIP]
> [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier) (see [Accessing partition using UUID](#_accessing_partition_using_uuid)) may be used to identify a block device instead of normal block device names such as "`/dev/sda1`", "`/dev/sda2`", …

Performance and characteristics of a filesystem can be optimized by mount options used on it (see `fstab(5)` and `mount(8)`). Notable ones are the following.

- "`defaults`" option implies default options: "`rw,suid,dev,exec,auto,nouser,async`". (general)

- "`noatime`" or "`relatime`" option is very effective for speeding up the read access. (general)

- "`user`" option allows an ordinary user to mount the filesystem. This option implies "`noexec,nosuid,nodev`" option combination. (general, used for CDs or usb storage devices)

- "`noexec,nodev,nosuid`" option combination is used to enhance security. (general)

- "`noauto`" option limits mounting by explicit operation only. (general)

- "`data=journal`" option for ext3fs can enhance data integrity against power failure with some loss of write speed.

> [!TIP]
> You need to provide kernel boot parameter (see [???](#_stage_2_the_boot_loader)), e.g. "`rootflags=data=journal`" to deploy a non-default journaling mode for the root filesystem. For `lenny`, the default jounaling mode is "`rootflags=data=ordered`". For `squeeze`, it is "`rootflags=data=writeback`".

### Optimization of filesystem via superblock

Characteristics of a filesystem can be optimized via its superblock using the `tune2fs(8)` command.

- Execution of "`sudo tune2fs -l /dev/hda1`" displays the contents of the filesystem superblock on "`/dev/hda1`".

- Execution of "`sudo tune2fs -c 50 /dev/hda1`" changes frequency of filesystem checks (`fsck` execution during boot-up) to every 50 boots on "`/dev/hda1`".

- Execution of "`sudo tune2fs -j /dev/hda1`" adds journaling capability to the filesystem, i.e. filesystem conversion from [ext2](https://en.wikipedia.org/wiki/Ext2) to [ext3](https://en.wikipedia.org/wiki/Ext3) on "`/dev/hda1`". (Do this on the unmounted filesystem.)

- Execution of "`sudo tune2fs -O extents,uninit_bg,dir_index /dev/hda1 && fsck -pf /dev/hda1`" converts it from [ext3](https://en.wikipedia.org/wiki/Ext3) to [ext4](https://en.wikipedia.org/wiki/Ext4) on "`/dev/hda1`". (Do this on the unmounted filesystem.)

> [!TIP]
> Despite its name, `tune2fs(8)` works not only on the [ext2](https://en.wikipedia.org/wiki/Ext2) filesystem but also on the [ext3](https://en.wikipedia.org/wiki/Ext3) and [ext4](https://en.wikipedia.org/wiki/Ext4) filesystems.

### Optimization of hard disk

> [!WARNING]
> Please check your hardware and read manpage of `hdparam(8)` before playing with hard disk configuration because this may be quite dangerous for the data integrity.

You can test disk access speed of a hard disk, e.g. "`/dev/hda`", by "`hdparm -tT /dev/hda`". For some hard disk connected with (E)IDE, you can speed it up with "`hdparm -q -c3 -d1 -u1 -m16 /dev/hda`" by enabling the "(E)IDE 32-bit I/O support", enabling the "using_dma flag", setting "interrupt-unmask flag", and setting the "multiple 16 sector I/O" (dangerous!).

You can test write cache feature of a hard disk, e.g. "`/dev/sda`", by "`hdparm -W /dev/sda`". You can disable its write cache feature with "`hdparm -W 0 /dev/sda`".

You may be able to read badly pressed CDROMs on modern high speed CD-ROM drive by slowing it down with "`setcd -x 2`".

### Optimization of solid state drive

Performance and disk wear of the [solid state drive (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive) can be optimized as follows.

- Use the latest Linux kernel. (\>= 3.2)

- Reduce disk writes for read disk accesses.

  - Set "`noatime`" or "`relatime`" mount option in `/etc/fstab`.

- Enable the [TRIM](https://en.wikipedia.org/wiki/TRIM) command.

  - Set "`discard`" mount option in `/etc/fstab` for the ext4 filesystem, swap partition, Btrfs, etc. See `fstab(5)`.

  - Set "`discard`" option in `/etc/lvm/lvm.conf` for [LVM](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)). See `lvm.conf(5)`.

  - Set "`discard`" option in `/etc/crypttab` for [dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt). See `crypttab(5)`.

- Enable the SSD optimized disk space allocation scheme.

  - Set "`ssd`" mount option in `/etc/fstab` for the Btrfs.

- Make system flush data to the disk every 10 minutes for laptop PCs.

  - Set "`commit=600`" mount option in `/etc/fstab`. See `fstab(5)`.

  - Set pm-utils to use laptop-mode even under AC operation. See [Debian BTS \#659260](http://bugs.debian.org/659260).

> [!WARNING]
> Changing flushing interval from normal 5 seconds to 10 minutes makes your data vulnerable to the power failure.

### Using SMART to predict hard disk failure

You can monitor and log your hard disk which is compliant to [SMART](https://en.wikipedia.org/wiki/S.M.A.R.T.) with the `smartd(8)` daemon.

1.  Enable [SMART](https://en.wikipedia.org/wiki/S.M.A.R.T.) feature in [BIOS](https://en.wikipedia.org/wiki/BIOS).

2.  Install the `smartmontools` package.

3.  Identify your hard disk drives by listing them with `df(1)`.

    - Let's assume a hard disk drive to be monitored as "`/dev/hda`".

4.  Check the output of "`smartctl -a /dev/hda`" to see if [SMART](https://en.wikipedia.org/wiki/S.M.A.R.T.) feature is actually enabled.

    - If not, enable it by "`smartctl -s on -a /dev/hda`".

5.  Enable `smartd(8)` daemon to run by the following.

    - uncomment "`start_smartd=yes`" in the "`/etc/default/smartmontools`" file.

    - restart the `smartd(8)` daemon by "`sudo /etc/init.d/smartmontools restart`".

> [!TIP]
> The `smartd(8)` daemon can be customized with the `/etc/smartd.conf` file including how to be notified of warnings.

### Specify temporary storage directory via \$TMPDIR

Applications create temporary files normally under the temporary storage directory "`/tmp`". If "`/tmp`" does not provide enough space, you can specify such temporary storage directory via the `$TMPDIR` variable for well-behaving programs.

### Expansion of usable storage space via LVM

For partitions created on [Logical Volume Manager (LVM)](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)) (Linux feature) at install time, they can be resized easily by concatenating extents onto them or truncating extents from them over multiple storage devices without major system reconfiguration.

### Expansion of usable storage space by mounting another partition

If you have an empty partition (e.g., "`/dev/sdx`"), you can format it with `mkfs.ext4(1)` and `mount(8)` it to a directory where you need more space. (You need to copy original data contents.)

    $ sudo mv work-dir old-dir
    $ sudo mkfs.ext4 /dev/sdx
    $ sudo mount -t ext4 /dev/sdx work-dir
    $ sudo cp -a old-dir/* work-dir
    $ sudo rm -rf old-dir

> [!TIP]
> You may alternatively mount an empty disk image file (see [Making the empty disk image file](#_making_the_empty_disk_image_file)) as a loop device (see [Mounting the disk image file](#_mounting_the_disk_image_file)). The actual disk usage grows with the actual data stored.

### Expansion of usable storage space by bind-mounting another directory

If you have an empty directory (e.g., "`/path/to/emp-dir`") on another partition with usable space, you can mount(8) it with "`--bind`" option to a directory (e.g., "`work-dir`") where you need more space.

    $ sudo mount --bind /path/to/emp-dir work-dir

### Expansion of usable storage space by overlay-mounting another directory

If you have usable space in another partition (e.g., "`/path/to/empty`" and "`/path/to/work`"), you can create a directory in it and stack that on to an old directory (e.g., "`/path/to/old`") where you need space using the [OverlayFS](https://en.wikipedia.org/wiki/OverlayFS) for Linux kernel 3.18 or newer (Debian Stretch 9.0 or newer).

    $ sudo mount -t overlay overlay \
      -olowerdir=/path/to/old-dir,upperdir=/path/to/empty,workdir=/path/to/work

Here, "`/path/to/empty`" and "`/path/to/work`" should be on the RW-enabled partition to write on "`/path/to/old`".

### Expansion of usable storage space using symlink

> [!CAUTION]
> This is a deprecated method. Some software may not function well with "symlink to a directory". Instead, use the "mounting" approaches described in the above.

If you have an empty directory (e.g., "`/path/to/emp-dir`") in another partition with usable space, you can create a symlink to the directory with `ln(8)`.

    $ sudo mv work-dir old-dir
    $ sudo mkdir -p /path/to/emp-dir
    $ sudo ln -sf /path/to/emp-dir work-dir
    $ sudo cp -a old-dir/* work-dir
    $ sudo rm -rf old-dir

> [!WARNING]
> Do not use "symlink to a directory" for directories managed by the system such as "`/opt`". Such a symlink may be overwritten when the system is upgraded.

## The disk image

Here, we discuss manipulations of the disk image.

### Making the disk image file

The disk image file, "`disk.img`", of an unmounted device, e.g., the second SCSI or serial ATA drive "`/dev/sdb`", can be made using `cp(1)` or `dd(1)` by the following.

    # cp /dev/sdb disk.img
    # dd if=/dev/sdb of=disk.img

The disk image of the traditional PC's [master boot record (MBR)](https://en.wikipedia.org/wiki/Master_boot_record) (see [Disk partition configuration](#_disk_partition_configuration)) which reside on the first sector on the primary IDE disk can be made by using `dd(1)` by the following.

    # dd if=/dev/hda of=mbr.img bs=512 count=1
    # dd if=/dev/hda of=mbr-nopart.img bs=446 count=1
    # dd if=/dev/hda of=mbr-part.img skip=446 bs=1 count=66

- "`mbr.img`": The MBR with the partition table

- "`mbr-nopart.img`": The MBR without the partition table

- "`mbr-part.img`": The partition table of the MBR only

If you have an SCSI or serial ATA device as the boot disk, substitute "`/dev/hda`" with "`/dev/sda`".

If you are making an image of a disk partition of the original disk, substitute "`/dev/hda`" with "`/dev/hda1`" etc.

### Writing directly to the disk

The disk image file, "`disk.img`" can be written to an unmounted device, e.g., the second SCSI drive "`/dev/sdb`" with matching size, by the following.

    # dd if=disk.img of=/dev/sdb

Similarly, the disk partition image file, "`partition.img`" can be written to an unmounted partition, e.g., the first partition of the second SCSI drive "`/dev/sdb1`" with matching size, by the following.

    # dd if=partition.img of=/dev/sdb1

### Mounting the disk image file

The disk image "`partition.img`" containing a single partition image can be mounted and unmounted by using the [loop device](https://en.wikipedia.org/wiki/Loop_device) as follows.

    # losetup -v -f partition.img
    Loop device is /dev/loop0
    # mkdir -p /mnt/loop0
    # mount -t auto /dev/loop0 /mnt/loop0
    ...hack...hack...hack
    # umount /dev/loop0
    # losetup -d /dev/loop0

This can be simplified as follows.

    # mkdir -p /mnt/loop0
    # mount -t auto -o loop partition.img /mnt/loop0
    ...hack...hack...hack
    # umount partition.img

Each partition of the disk image "`disk.img`" containing multiple partitions can be mounted by using the [loop device](https://en.wikipedia.org/wiki/Loop_device). Since the loop device does not manage partitions by default, we need to reset it as follows.

    # modinfo -p loop # verify kernel capability
    max_part:Maximum number of partitions per loop device
    max_loop:Maximum number of loop devices
    # losetup -a # verify nothing using the loop device
    # rmmod loop
    # modprobe loop max_part=16

Now, the loop device can manage up to 16 partitions.

    # losetup -v -f disk.img
    Loop device is /dev/loop0
    # fdisk -l /dev/loop0

    Disk /dev/loop0: 5368 MB, 5368709120 bytes
    255 heads, 63 sectors/track, 652 cylinders
    Units = cylinders of 16065 * 512 = 8225280 bytes
    Disk identifier: 0x452b6464

          Device Boot      Start         End      Blocks   Id  System
    /dev/loop0p1               1         600     4819468+  83  Linux
    /dev/loop0p2             601         652      417690   83  Linux
    # mkdir -p /mnt/loop0p1
    # mount -t ext4 /dev/loop0p1 /mnt/loop0p1
    # mkdir -p /mnt/loop0p2
    # mount -t ext4 /dev/loop0p2 /mnt/loop0p2
    ...hack...hack...hack
    # umount /dev/loop0p1
    # umount /dev/loop0p2
    # losetup -d /dev/loop0

Alternatively, similar effects can be done by using the [device mapper](https://en.wikipedia.org/wiki/Device_mapper) devices created by `kpartx(8)` from the `kpartx` package as follows.

    # kpartx -a -v disk.img
    ...
    # mkdir -p /mnt/loop0p2
    # mount -t ext4 /dev/mapper/loop0p2 /mnt/loop0p2
    ...
    ...hack...hack...hack
    # umount /dev/mapper/loop0p2
    ...
    # kpartx -d /mnt/loop0

> [!NOTE]
> You can mount a single partition of such disk image with [loop device](https://en.wikipedia.org/wiki/Loop_device) using offset to skip [MBR](https://en.wikipedia.org/wiki/Master_boot_record) etc., too. But this is more error prone.

### Cleaning a disk image file

A disk image file, "`disk.img`" can be cleaned of all removed files into clean sparse image "`new.img`" by the following.

    # mkdir old; mkdir new
    # mount -t auto -o loop disk.img old
    # dd bs=1 count=0 if=/dev/zero of=new.img seek=5G
    # mount -t auto -o loop new.img new
    # cd old
    # cp -a --sparse=always ./ ../new/
    # cd ..
    # umount new.img
    # umount disk.img

If "`disk.img`" is in ext2, ext3 or ext4, you can also use `zerofree(8)` from the `zerofree` package as follows.

    # losetup -f -v disk.img
    Loop device is /dev/loop3
    # zerofree /dev/loop3
    # cp --sparse=always disk.img new.img

### Making the empty disk image file

The empty disk image "`disk.img`" which can grow up to 5GiB can be made using `dd(1)` as follows.

    $ dd bs=1 count=0 if=/dev/zero of=disk.img seek=5G

You can create an ext4 filesystem on this disk image "`disk.img`" using the [loop device](https://en.wikipedia.org/wiki/Loop_device) as follows.

    # losetup -f -v disk.img
    Loop device is /dev/loop1
    # mkfs.ext4 /dev/loop1
    ...hack...hack...hack
    # losetup -d /dev/loop1
    $ du  --apparent-size -h disk.img
    5.0G  disk.img
    $ du -h disk.img
    83M disk.img

For "`disk.img`", its file size is 5.0 GiB and its actual disk usage is mere 83MiB. This discrepancy is possible since [ext4](https://en.wikipedia.org/wiki/Ext4) can hold [sparse file](https://en.wikipedia.org/wiki/Sparse_file).

> [!TIP]
> The actual disk usage of [sparse file](https://en.wikipedia.org/wiki/Sparse_file) grows with data which are written to it.

Using similar operation on devices created by the [loop device](https://en.wikipedia.org/wiki/Loop_device) or the [device mapper](https://en.wikipedia.org/wiki/Device_mapper) devices as [Mounting the disk image file](#_mounting_the_disk_image_file), you can partition this disk image "`disk.img`" using `parted(8)` or `fdisk(8)`, and can create filesystem on it using `mkfs.ext4(8)`, `mkswap(8)`, etc.

### Making the ISO9660 image file

The [ISO9660](https://en.wikipedia.org/wiki/ISO_9660) image file, "`cd.iso`", from the source directory tree at "`source_directory`" can be made using `genisoimage(1)` provided by [cdrkit](https://en.wikipedia.org/wiki/Cdrkit) by the following.

    #  genisoimage -r -J -T -V volume_id -o cd.iso source_directory

Similarly, the bootable ISO9660 image file, "`cdboot.iso`", can be made from `debian-installer` like directory tree at "`source_directory`" by the following.

    #  genisoimage -r -o cdboot.iso -V volume_id \
       -b isolinux/isolinux.bin -c isolinux/boot.cat \
       -no-emul-boot -boot-load-size 4 -boot-info-table source_directory

Here [Isolinux boot loader](https://en.wikipedia.org/wiki/SYSLINUX) (see [???](#_stage_2_the_boot_loader)) is used for booting.

You can calculate the md5sum value and make the ISO9660 image directly from the CD-ROM device as follows.

    $ isoinfo -d -i /dev/cdrom
    CD-ROM is in ISO 9660 format
    ...
    Logical block size is: 2048
    Volume size is: 23150592
    ...
    # dd if=/dev/cdrom bs=2048 count=23150592 conv=notrunc,noerror | md5sum
    # dd if=/dev/cdrom bs=2048 count=23150592 conv=notrunc,noerror > cd.iso

> [!WARNING]
> You must carefully avoid ISO9660 filesystem read ahead bug of Linux as above to get the right result.

### Writing directly to the CD/DVD-R/RW

> [!TIP]
> DVD is only a large CD to `wodim(1)` provided by [cdrkit](https://en.wikipedia.org/wiki/Cdrkit).

You can find a usable device by the following.

    # wodim --devices

Then the blank CD-R is inserted to the CD drive, and the ISO9660 image file, "`cd.iso`" is written to this device, e.g., "`/dev/hda`", using `wodim(1)` by the following.

    # wodim -v -eject dev=/dev/hda cd.iso

If CD-RW is used instead of CD-R, do this instead by the following.

    # wodim -v -eject blank=fast dev=/dev/hda cd.iso

> [!TIP]
> If your desktop system mounts CDs automatically, unmount it by "`sudo umount /dev/hda`" from console before using `wodim(1)`.

### Mounting the ISO9660 image file

If "`cd.iso`" contains an ISO9660 image, then the following manually mounts it to "`/cdrom`".

    # mount -t iso9660 -o ro,loop cd.iso /cdrom

> [!TIP]
> Modern desktop system may mount removable media such as ISO9660 formatted CD automatically (see [???](#_removable_storage_device)).

## The binary data

Here, we discuss direct manipulations of the binary data on storage media.

### Viewing and editing binary data

The most basic viewing method of binary data is to use "`od -t x1`" command.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `coreutils` | @-@popcon1@-@ | @-@psize1@-@ | basic package which has `od(1)` to dump files (HEX, ASCII, OCTAL, …) |
| `bsdmainutils` | @-@popcon1@-@ | @-@psize1@-@ | utility package which has `hd(1)` to dump files (HEX, ASCII, OCTAL, …) |
| `hexedit` | @-@popcon1@-@ | @-@psize1@-@ | binary editor and viewer (HEX, ASCII) |
| `bless` | @-@popcon1@-@ | @-@psize1@-@ | full featured hexadecimal editor (GNOME) |
| `okteta` | @-@popcon1@-@ | @-@psize1@-@ | full featured hexadecimal editor (KDE4) |
| `ncurses-hexedit` | @-@popcon1@-@ | @-@psize1@-@ | binary editor and viewer (HEX, ASCII, EBCDIC) |
| `beav` | @-@popcon1@-@ | @-@psize1@-@ | binary editor and viewer (HEX, ASCII, EBCDIC, OCTAL, …) |

List of packages which view and edit binary data

> [!TIP]
> HEX is used as an acronym for [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) format with [radix](https://en.wikipedia.org/wiki/Radix) 16. OCTAL is for [octal](https://en.wikipedia.org/wiki/Octal) format with [radix](https://en.wikipedia.org/wiki/Radix) 8. ASCII is for [American Standard Code for Information Interchange](https://en.wikipedia.org/wiki/ASCII), i.e., normal English text code. EBCDIC is for [Extended Binary Coded Decimal Interchange Code](https://en.wikipedia.org/wiki/Extended_Binary_Coded_Decimal_Interchange_Code) used on [IBM mainframe](https://en.wikipedia.org/wiki/IBM_mainframe) operating systems.

### Manipulating files without mounting disk

There are tools to read and write files without mounting disk.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `mtools` | @-@popcon1@-@ | @-@psize1@-@ | utilities for MSDOS files without mounting them |
| `hfsutils` | @-@popcon1@-@ | @-@psize1@-@ | utilities for HFS and HFS+ files without mounting them |

List of packages to manipulate files without mounting disk

### Data redundancy

Software [RAID](https://en.wikipedia.org/wiki/RAID) systems offered by the Linux kernel provide data redundancy in the kernel filesystem level to achieve high levels of storage reliability.

There are tools to add data redundancy to files in application program level to achieve high levels of storage reliability, too.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `par2` | @-@popcon1@-@ | @-@psize1@-@ | Parity Archive Volume Set, for checking and repair of files |
| `dvdisaster` | @-@popcon1@-@ | @-@psize1@-@ | data loss/scratch/aging protection for CD/DVD media |
| `dvbackup` | @-@popcon1@-@ | @-@psize1@-@ | backup tool using MiniDV camcorders (providing `rsbep(1)`) |
| `vdmfec` | @-@popcon1@-@ | @-@psize1@-@ | recover lost blocks using Forward Error Correction |

List of tools to add data redundancy to files

### Data file recovery and forensic analysis

There are tools for data file recovery and forensic analysis.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `testdisk` | @-@popcon1@-@ | @-@psize1@-@ | utilities for partition scan and disk recovery |
| `magicrescue` | @-@popcon1@-@ | @-@psize1@-@ | utility to recover files by looking for magic bytes |
| `scalpel` | @-@popcon1@-@ | @-@psize1@-@ | frugal, high performance file carver |
| `myrescue` | @-@popcon1@-@ | @-@psize1@-@ | rescue data from damaged harddisks |
| `extundelete` | @-@popcon1@-@ | @-@psize1@-@ | utility to undelete files on the ext3/4 filesystem |
| `ext4magic` | @-@popcon1@-@ | @-@psize1@-@ | utility to undelete files on the ext3/4 filesystem |
| `ext3grep` | @-@popcon1@-@ | @-@psize1@-@ | tool to help recover deleted files on the ext3 filesystem |
| `scrounge-ntfs` | @-@popcon1@-@ | @-@psize1@-@ | data recovery program for NTFS filesystems |
| `gzrt` | @-@popcon1@-@ | @-@psize1@-@ | gzip recovery toolkit |
| `sleuthkit` | @-@popcon1@-@ | @-@psize1@-@ | tools for forensics analysis. (Sleuthkit) |
| `autopsy` | @-@popcon1@-@ | @-@psize1@-@ | graphical interface to SleuthKit |
| `foremost` | @-@popcon1@-@ | @-@psize1@-@ | forensics application to recover data |
| `guymager` | @-@popcon1@-@ | @-@psize1@-@ | forensic imaging tool based on Qt |
| `dcfldd` | @-@popcon1@-@ | @-@psize1@-@ | enhanced version of `dd` for forensics and security |

List of packages for data file recovery and forensic analysis

> [!TIP]
> You can undelete files on the ext2 filesystem using `list_deleted_inodes` and `undel` commands of `debugfs(8)` in the `e2fsprogs` package.

### Splitting a large file into small files

When a data is too big to backup as a single file, you can backup its content after splitting it into, e.g. 2000MiB chunks and merge those chunks back into the original file later.

    $ split -b 2000m large_file
    $ cat x* >large_file

> [!CAUTION]
> Please make sure you do not have any files starting with "`x`" to avoid name crashes.

### Clearing file contents

In order to clear the contents of a file such as a log file, do not use `rm(1)` to delete the file and then create a new empty file, because the file may still be accessed in the interval between commands. The following is the safe way to clear the contents of the file.

    $ :>file_to_be_cleared

### Dummy files

The following commands create dummy or empty files.

    $ dd if=/dev/zero    of=5kb.file bs=1k count=5
    $ dd if=/dev/urandom of=7mb.file bs=1M count=7
    $ touch zero.file
    $ : > alwayszero.file

You should find following files.

- "`5kb.file`" is 5KB of zeros.

- "`7mb.file`" is 7MB of random data.

- "`zero.file`" may be a 0 byte file. If it existed, its `mtime` is updated while its content and its length are kept.

- "`alwayszero.file`" is always a 0 byte file. If it existed, its `mtime` is updated and its content is reset.

### Erasing an entire hard disk

There are several ways to completely erase data from an entire hard disk like device, e.g., USB memory stick at "`/dev/sda`".

> [!CAUTION]
> Check your USB memory stick location with `mount(8)` first before executing commands here. The device pointed by "`/dev/sda`" may be SCSI hard disk or serial-ATA hard disk where your entire system resides.

Erase all the disk content by resetting data to 0 with the following.

    # dd if=/dev/zero of=/dev/sda

Erase everything by overwriting with random data as follows.

    # dd if=/dev/urandom of=/dev/sda

Erase everything by overwriting with random data very efficiently as follows.

    # shred -v -n 1 /dev/sda

Since `dd(1)` is available from the shell of many bootable Linux CDs such as Debian installer CD, you can erase your installed system completely by running an erase command from such media on the system hard disk, e.g., "`/dev/hda`", "`/dev/sda`", etc.

### Erasing unused area of an hard disk

Unused area on an hard disk (or USB memory stick), e.g. "`/dev/sdb1`" may still contain erased data themselves since they are only unlinked from the filesystem. These can be cleaned by overwriting them.

    # mount -t auto /dev/sdb1 /mnt/foo
    # cd /mnt/foo
    # dd if=/dev/zero of=junk
    dd: writing to `junk': No space left on device
    ...
    # sync
    # umount /dev/sdb1

> [!WARNING]
> This is usually good enough for your USB memory stick. But this is not perfect. Most parts of erased filenames and their attributes may be hidden and remain in the filesystem.

### Undeleting deleted but still open files

Even if you have accidentally deleted a file, as long as that file is still being used by some application (read or write mode), it is possible to recover such a file.

For example, try the following

    $ echo foo > bar
    $ less bar
    $ ps aux | grep ' less[ ]'
    bozo    4775  0.0  0.0  92200   884 pts/8    S+   00:18   0:00 less bar
    $ rm bar
    $ ls -l /proc/4775/fd | grep bar
    lr-x------ 1 bozo bozo 64 2008-05-09 00:19 4 -> /home/bozo/bar (deleted)
    $ cat /proc/4775/fd/4 >bar
    $ ls -l
    -rw-r--r-- 1 bozo bozo 4 2008-05-09 00:25 bar
    $ cat bar
    foo

Execute on another terminal (when you have the `lsof` package installed) as follows.

    $ ls -li bar
    2228329 -rw-r--r-- 1 bozo bozo 4 2008-05-11 11:02 bar
    $ lsof |grep bar|grep less
    less 4775 bozo 4r REG 8,3 4 2228329 /home/bozo/bar
    $ rm bar
    $ lsof |grep bar|grep less
    less 4775 bozo 4r REG 8,3 4 2228329 /home/bozo/bar (deleted)
    $ cat /proc/4775/fd/4 >bar
    $ ls -li bar
    2228302 -rw-r--r-- 1 bozo bozo 4 2008-05-11 11:05 bar
    $ cat bar
    foo

### Searching all hardlinks

Files with hardlinks can be identified by "`ls -li`".

    $ ls -li
    total 0
    2738405 -rw-r--r-- 1 root root 0 2008-09-15 20:21 bar
    2738404 -rw-r--r-- 2 root root 0 2008-09-15 20:21 baz
    2738404 -rw-r--r-- 2 root root 0 2008-09-15 20:21 foo

Both "`baz`" and "`foo`" have link counts of "2" (\>1) showing them to have hardlinks. Their [inode](https://en.wikipedia.org/wiki/Inode) numbers are common "2738404". This means they are the same hardlinked file. If you do not happen to find all hardlinked files by chance, you can search it by the [inode](https://en.wikipedia.org/wiki/Inode), e.g., "2738404" as the following.

    # find /path/to/mount/point -xdev -inum 2738404

### Invisible disk space consumption

All deleted but open files consume disk space although they are not visible from normal `du(1)`. They can be listed with their size by the following.

    # lsof -s -X / |grep deleted

## Data encryption tips

With physical access to your PC, anyone can easily gain root privilege and access all the files on your PC (see [???](#_securing_the_root_password)). This means that login password system can not secure your private and sensitive data against possible theft of your PC. You must deploy data encryption technology to do it. Although [GNU privacy guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) (see [???](#_data_security_infrastructure)) can encrypt files, it takes some user efforts.

[dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt) and [eCryptfs](http://ecryptfs.sourceforge.net/) facilitates automatic data encryption natively via Linux kernel modules with minimal user efforts.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `cryptsetup` | @-@popcon1@-@ | @-@psize1@-@ | utilities for encrypted block device ([dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt) / [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup)) |
| `cryptmount` | @-@popcon1@-@ | @-@psize1@-@ | utilities for encrypted block device ([dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt) / [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup)) with focus on mount/unmount by normal users |
| `ecryptfs-utils` | @-@popcon1@-@ | @-@psize1@-@ | utilities for encrypted stacked filesystem ([eCryptfs](http://ecryptfs.sourceforge.net/)) |

List of data encryption utilities

[Dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt) is a cryptographic filesystem using [device-mapper](https://en.wikipedia.org/wiki/Device_mapper). [Device-mapper](https://en.wikipedia.org/wiki/Device_mapper) maps one block device to another.

[eCryptfs](http://ecryptfs.sourceforge.net/) is another cryptographic filesystem using stacked filesystem. Stacked filesystem stacks itself on top of an existing directory of a mounted filesystem.

> [!CAUTION]
> Data encryption costs CPU time etc. Please weigh its benefits and costs.

> [!NOTE]
> Entire Debian system can be installed on a encrypted disk by the [debian-installer](https://www.debian.org/devel/debian-installer/) (lenny or newer) using [dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt)/[LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) and initramfs.

> [!TIP]
> See [???](#_data_security_infrastructure) for user space encryption utility: [GNU Privacy Guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard).

### Removable disk encryption with dm-crypt/LUKS

You can encrypt contents of removable mass devices, e.g. USB memory stick on "`/dev/sdx`", using [dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt)/[LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup). You simply format it as the following.

    # badblocks -c 1024 -s -w -t random -v /dev/sdx
    # fdisk /dev/sdx
    ... "n" "p" "1" "return" "return" "w"
    # cryptsetup luksFormat /dev/sdx1
    ...
    # cryptsetup open --type luks /dev/sdx1 sdx1
    ...
    # ls -l /dev/mapper/
    total 0
    crw-rw---- 1 root root  10, 60 2008-10-04 18:44 control
    brw-rw---- 1 root disk 254,  0 2008-10-04 23:55 sdx1
    # mkfs.vfat /dev/mapper/sdx1
    ...
    # cryptsetup luksClose sdx1

Then, it can be mounted just like normal one on to "`/media/<disk_label>`", except for asking password (see [???](#_removable_storage_device)) under modern desktop environment, such as GNOME using `gnome-mount(1)`. The difference is that every data written to it is encrypted. You may alternatively format media in different filesystem, e.g., ext4 with "`mkfs.ext4 /dev/mapper/sdx1`".

> [!NOTE]
> If you are really paranoid for the security of data, you may need to overwrite multiple times (the "`badblocks`" command in the above example). This operation is very time consuming though.

### Encrypted swap partition with dm-crypt

Let's assume that your original "`/etc/fstab`" contains the following.

    /dev/sda7 swap sw 0 0

You can enable encrypted swap partition using [dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt) by as the following.

    # aptitude install cryptsetup
    # swapoff -a
    # echo "cswap /dev/sda7 /dev/urandom swap" >> /etc/crypttab
    # perl -i -p -e "s/\/dev\/sda7/\/dev\/mapper\/cswap/" /etc/fstab
    # /etc/init.d/cryptdisks restart
     ...
    # swapon -a

### Mounting encrypted disk with dm-crypt/LUKS

An encrypted disk partition created with dm-crypt/LUKS on "`/dev/sdc5`" can be mounted onto "`/mnt`" as follows:

    $ sudo cryptsetup open /dev/sdc5 ninja --type luks
    Enter passphrase for /dev/sdc5: ****
    $ sudo lvm
    lvm> lvscan
      inactive          '/dev/ninja-vg/root' [13.52 GiB] inherit
      inactive          '/dev/ninja-vg/swap_1' [640.00 MiB] inherit
      ACTIVE            '/dev/goofy/root' [180.00 GiB] inherit
      ACTIVE            '/dev/goofy/swap' [9.70 GiB] inherit
    lvm> lvchange -a y /dev/ninja-vg/root
    lvm> exit
      Exiting.
    $ sudo mount /dev/ninja-vg/root /mnt

### Automatically encrypting files with eCryptfs

You can encrypt files written under "`~/Private/`" automatically using [eCryptfs](http://ecryptfs.sourceforge.net/) and the `ecryptfs-utils` package.

- Run `ecryptfs-setup-private(1)` and set up "`~/Private/`" by following prompts.

- Activate "`~/Private/`" by running `ecryptfs-mount-private(1)`.

- Move sensitive data files to "`~/Private/`" and make symlinks as needed.

  - Candidates: "`~/.fetchmailrc`", "`~/.ssh/identity`", "`~/.ssh/id_rsa`", "`~/.ssh/id_dsa`" and other files with "`go-rwx`"

- Move sensitive data directories to a subdirectory in "`~/Private/`" and make symlinks as needed.

  - Candidates: "`~/.gnupg`" and other directories with "`go-rwx`"

- Create symlink from "`~/Desktop/Private/`" to "`~/Private/`" for easier desktop operations.

- Deactivate "`~/Private/`" by running `ecryptfs-umount-private(1)`.

- Activate "`~/Private/`" by issuing "`ecryptfs-mount-private`" as you need encrypted data.

> [!TIP]
> Since [eCryptfs](http://ecryptfs.sourceforge.net/) selectively encrypt only the sensitive files, its system cost is much less than using [dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt) on the entire root or "`/home`" device. It does not require any special on-disk storage allocation effort but cannot keep all filesystem metadata confidential.

### Automatically mounting eCryptfs

If you use your login password for wrapping encryption keys, you can automate mounting eCryptfs via [PAM (Pluggable Authentication Modules)](https://en.wikipedia.org/wiki/Pluggable_Authentication_Modules).

Insert the following line just before "`pam_permit.so`" in "`/etc/pam.d/common-auth`".

    auth required pam_ecryptfs.so unwrap

Insert the following line just at the last line in "`/etc/pam.d/common-session`".

    session optional pam_ecryptfs.so unwrap

Insert the following line at first active line in "`/etc/pam.d/common-password`".

    password required pam_ecryptfs.so

This is quite convenient.

> [!WARNING]
> Configuration errors of [PAM](https://en.wikipedia.org/wiki/Pluggable_Authentication_Modules) may lock you out of your own system. See [???](#_authentication).

> [!CAUTION]
> If you use your login password for wrapping encryption keys, your encrypted data are as secure as your user login password (see [???](#_good_password)). Unless you are careful to set up a [strong password](https://en.wikipedia.org/wiki/Password_strength), your data is at risk when someone runs [password cracking](https://en.wikipedia.org/wiki/Password_cracking) software after stealing your laptop (see [???](#_securing_the_root_password)).

## The kernel

Debian distributes modularized [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel) as packages for supported architectures.

### Linux kernel 2.6/3.x

There are few notable features on Linux kernel 2.6/3.x compared to 2.4.

- Devices are created by the udev system (see [???](#_the_udev_system)).

- Read/write accesses to IDE CD/DVD devices do not use the `ide-scsi` module.

- Network packet filtering functions use `iptables` kernel modules.

The version bump from Linux 2.6.39 to Linux 3.0 is not about major technological changes but about the 20th anniversary.

### Kernel parameters

Many Linux features are configurable via kernel parameters as follows.

- Kernel parameters initialized by the bootloader (see [???](#_stage_2_the_boot_loader))

- Kernel parameters changed by `sysctl(8)` at runtime for ones accessible via sysfs (see [???](#_procfs_and_sysfs))

- Module parameters set by arguments of `modprobe(8)` when a module is activated (see [Mounting the disk image file](#_mounting_the_disk_image_file))

See "`kernel-parameters.txt(.gz)`" and other related documents in the Linux kernel documentation ("`/usr/share/doc/linux-doc-3.*/Documentation/filesystems/*`") provided by the `linux-doc-3.*` package.

### Kernel headers

Most **normal programs** don't need kernel headers and in fact may break if you use them directly for compiling. They should be compiled against the headers in "`/usr/include/linux`" and "`/usr/include/asm`" provided by the `libc6-dev` package (created from the `glibc` source package) on the Debian system.

> [!NOTE]
> For compiling some kernel-specific programs such as the kernel modules from the external source and the automounter daemon (`amd`), you must include path to the corresponding kernel headers, e.g. "`-I/usr/src/linux-particular-version/include/`", to your command line. `module-assistant(8)` (or its short form `m-a`) helps users to build and install module package(s) easily for one or more custom kernels.

### Compiling the kernel and related modules

Debian has its own method of compiling the kernel and related modules.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `build-essential` | @-@popcon1@-@ | @-@psize1@-@ | essential packages for building Debian packages: `make`, `gcc`, … |
| `bzip2` | @-@popcon1@-@ | @-@psize1@-@ | compress and decompress utilities for bz2 files |
| `libncurses5-dev` | @-@popcon1@-@ | @-@psize1@-@ | developer's libraries and docs for ncurses |
| `git` | @-@popcon1@-@ | @-@psize1@-@ | git: distributed revision control system used by the Linux kernel |
| `fakeroot` | @-@popcon1@-@ | @-@psize1@-@ | provide fakeroot environment for building package as non-root |
| `initramfs-tools` | @-@popcon1@-@ | @-@psize1@-@ | tool to build an initramfs (Debian specific) |
| `dkms` | @-@popcon1@-@ | @-@psize1@-@ | [dynamic kernel module support (DKMS)](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) (generic) |
| `devscripts` | @-@popcon1@-@ | @-@psize1@-@ | helper scripts for a Debian Package maintainer (Debian specific) |

List of key packages to be installed for the kernel recompilation on the Debian system

If you use `initrd` in [???](#_stage_2_the_boot_loader), make sure to read the related information in `initramfs-tools(8)`, `update-initramfs(8)`, `mkinitramfs(8)` and `initramfs.conf(5)`.

> [!WARNING]
> Do not put symlinks to the directories in the source tree (e.g. "`/usr/src/linux*`") from "`/usr/include/linux`" and "`/usr/include/asm`" when compiling the Linux kernel source. (Some outdated documents suggest this.)

> [!NOTE]
> When compiling the latest Linux kernel on the Debian `stable` system, the use of backported latest tools from the Debian `unstable` may be needed.

> [!NOTE]
> The [dynamic kernel module support (DKMS)](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) is a new distribution independent framework designed to allow individual kernel modules to be upgraded without changing the whole kernel. This is used for the maintenance of out-of-tree modules. This also makes it very easy to rebuild modules as you upgrade kernels.

### Compiling the kernel source: Debian Kernel Team recommendation

For building custom kernel binary packages from the upstream kernel source, you should use the "`deb-pkg`" target provided by it.

    $ sudo apt-get build-dep linux
    $ cd /usr/src
    $ wget http://www.kernel.org/pub/linux/kernel/v3.11/linux-<version>.tar.bz2
    $ tar -xjvf linux-<version>.tar.bz2
    $ cd linux-<version>
    $ cp /boot/config-<version> .config
    $ make menuconfig
     ...
    $ make deb-pkg

> [!TIP]
> The linux-source-\<version\> package provides the Linux kernel source with Debian patches as "`/usr/src/linux-<version>.tar.bz2`".

For building specific binary packages from the Debian kernel source package, you should use the "`binary-arch_<architecture>_<featureset>_<flavour>`" targets in "`debian/rules.gen`".

    $ sudo apt-get build-dep linux
    $ apt-get source linux
    $ cd linux-3.*
    $ fakeroot make -f debian/rules.gen binary-arch_i386_none_686

See further information:

- Debian Wiki: [KernelFAQ](http://wiki.debian.org/KernelFAQ)

- Debian Wiki: [DebianKernel](http://wiki.debian.org/DebianKernel)

- Debian Linux Kernel Handbook: <https://kernel-handbook.debian.net>

### Hardware drivers and firmware

The hardware driver is the code running on the target system. Most hardware drivers are available as free software now and are included in the normal Debian kernel packages in the `main` area.

- [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) driver

  - Intel GPU driver (`main`)

  - AMD/ATI GPU driver (`main`)

  - NVIDIA GPU driver (`main` for [nouveau](https://en.wikipedia.org/wiki/Nouveau_(software)) driver, and `non-free` for binary-only drivers supported by the vendor.)

- [Softmodem](https://en.wikipedia.org/wiki/Softmodem) driver

  - martian-modem and sl-modem-dkms packages (`non-free`)

The firmware is the code or data loaded on the device (e.g., CPU [microcode](https://en.wikipedia.org/wiki/Microcode), rendering code running on GPU, or [FPGA](https://en.wikipedia.org/wiki/FPGA) / [CPLD](https://en.wikipedia.org/wiki/Complex_programmable_logic_device) data, …). Some firmware packages are available as free software but many firmware packages are not available as free software since they contain sourceless binary data.

- firmware-linux-free (`main`)

- firmware-linux-nonfree (`non-free`)

- firmware-linux-\* (`non-free`)

- \*-firmware (`non-free`)

- intel-microcode (`non-free`)

- amd64-microcode (`non-free`)

Please note that `non-free` and `contrib` packages are not part of the Debian system. The access configuration to enable and to disable the `non-free` and `contrib` areas is described in [???](#_debian_archive_basics). You should be aware of negatives associated with the use of the `non-free` and `contrib` packages as described in [???](#_debian_is_100_free_software).

## Virtualized system

Use of virtualized system enables us to run multiple instances of system simultaneously on a single hardware.

> [!TIP]
> See <http://wiki.debian.org/SystemVirtualization>.

### Virtualization tools

There are several system [virtualization](https://en.wikipedia.org/wiki/Virtualization) and [emulation](https://en.wikipedia.org/wiki/Emulator) related packages in Debian beyond simple [chroot](https://en.wikipedia.org/wiki/Chroot). Some packages also help you to setup such system.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `schroot` | @-@popcon1@-@ | @-@psize1@-@ | specialized tool for executing Debian binary packages in chroot |
| `sbuild` | @-@popcon1@-@ | @-@psize1@-@ | tool for building Debian binary packages from Debian sources |
| `pbuilder` | @-@popcon1@-@ | @-@psize1@-@ | personal package builder for Debian packages |
| `debootstrap` | @-@popcon1@-@ | @-@psize1@-@ | bootstrap a basic Debian system (written in sh) |
| `cdebootstrap` | @-@popcon1@-@ | @-@psize1@-@ | bootstrap a Debian system (written in C) |
| `virt-manager` | @-@popcon1@-@ | @-@psize1@-@ | [Virtual Machine Manager](https://en.wikipedia.org/wiki/Virtual_Machine_Manager): desktop application for managing virtual machines |
| `libvirt-clients` | @-@popcon1@-@ | @-@psize1@-@ | programs for the [libvirt](https://en.wikipedia.org/wiki/Libvirt) library |
| `bochs` | @-@popcon1@-@ | @-@psize1@-@ | [Bochs](https://en.wikipedia.org/wiki/Bochs): IA-32 PC emulator |
| `qemu` | @-@popcon1@-@ | @-@psize1@-@ | [QEMU](https://en.wikipedia.org/wiki/QEMU): fast generic processor emulator |
| `qemu-system` | @-@popcon1@-@ | @-@psize1@-@ | [QEMU](https://en.wikipedia.org/wiki/QEMU): full system emulation binaries |
| `qemu-user` | @-@popcon1@-@ | @-@psize1@-@ | [QEMU](https://en.wikipedia.org/wiki/QEMU): user mode emulation binaries |
| `qemu-utils` | @-@popcon1@-@ | @-@psize1@-@ | [QEMU](https://en.wikipedia.org/wiki/QEMU): utilities |
| `qemu-kvm` | @-@popcon1@-@ | @-@psize1@-@ | [KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine): full virtualization on x86 hardware with the [hardware-assisted virtualization](https://en.wikipedia.org/wiki/Hardware-assisted_virtualization) |
| `virtualbox` | @-@popcon1@-@ | @-@psize1@-@ | [VirtualBox](https://en.wikipedia.org/wiki/VirtualBox): x86 virtualization solution on i386 and amd64 |
| `xen-tools` | @-@popcon1@-@ | @-@psize1@-@ | tools to manage debian [XEN](https://en.wikipedia.org/wiki/Xen) virtual server |
| `wine` | @-@popcon1@-@ | @-@psize1@-@ | [Wine](https://en.wikipedia.org/wiki/Wine_(software)): Windows API Implementation (standard suite) |
| `dosbox` | @-@popcon1@-@ | @-@psize1@-@ | [DOSBox](https://en.wikipedia.org/wiki/DOSBox): x86 emulator with Tandy/Herc/CGA/EGA/VGA/SVGA graphics, sound and DOS |
| `dosemu` | @-@popcon1@-@ | @-@psize1@-@ | [DOSEMU](https://en.wikipedia.org/wiki/DOSEMU): The Linux DOS Emulator |
| `vzctl` | @-@popcon1@-@ | @-@psize1@-@ | [OpenVZ](https://en.wikipedia.org/wiki/OpenVZ) server virtualization solution - control tools |
| `vzquota` | @-@popcon1@-@ | @-@psize1@-@ | [OpenVZ](https://en.wikipedia.org/wiki/OpenVZ) server virtualization solution - quota tools |
| `lxc` | @-@popcon1@-@ | @-@psize1@-@ | [Linux containers](http://lxc.sourceforge.net/) user space tools |

List of virtualization tools

See Wikipedia article [Comparison of platform virtual machines](https://en.wikipedia.org/wiki/Comparison_of_platform_virtual_machines) for detail comparison of different platform virtualization solutions.

### Virtualization work flow

> [!NOTE]
> Some functionalities described here are only available in `squeeze` or later.

> [!NOTE]
> Default Debian kernels support [KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine) since `lenny`.

Typical work flow for [virtualization](https://en.wikipedia.org/wiki/Virtualization) involves several steps.

- Create an empty filesystem (a file tree or a disk image).

  - The file tree can be created by "`mkdir -p /path/to/chroot`".

  - The raw disk image file can be created with `dd(1)` (see [Making the disk image file](#_making_the_disk_image_file) and [Making the empty disk image file](#_making_the_empty_disk_image_file)).

  - `qemu-img(1)` can be used to create and convert disk image files supported by [QEMU](https://en.wikipedia.org/wiki/QEMU).

  - The raw and [VMDK](https://en.wikipedia.org/wiki/VMDK) file format can be used as common format among virtualization tools.

- Mount the disk image with `mount(8)` to the filesystem (optional).

  - For the raw disk image file, mount it as [loop device](https://en.wikipedia.org/wiki/Loop_device) or [device mapper](https://en.wikipedia.org/wiki/Device_mapper) devices (see [Mounting the disk image file](#_mounting_the_disk_image_file)).

  - For disk images supported by [QEMU](https://en.wikipedia.org/wiki/QEMU), mount them as [network block device](https://en.wikipedia.org/wiki/Network_block_device) (see [Mounting the virtual disk image file](#_mounting_the_virtual_disk_image_file)).

- Populate the target filesystem with required system data.

  - The use of programs such as `debootstrap` and `cdebootstrap` helps with this process (see [Chroot system](#_chroot_system)).

  - Use installers of OSs under the full system emulation.

- Run a program under a virtualized environment.

  - [chroot](https://en.wikipedia.org/wiki/Chroot) provides basic virtualized environment enough to compile programs, run console applications, and run daemons in it.

  - [QEMU](https://en.wikipedia.org/wiki/QEMU) provides cross-platform CPU emulation.

  - [QEMU](https://en.wikipedia.org/wiki/QEMU) with [KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine) provides full system emulation by the [hardware-assisted virtualization](https://en.wikipedia.org/wiki/Hardware-assisted_virtualization).

  - [VirtualBox](https://en.wikipedia.org/wiki/VirtualBox) provides full system emulation on i386 and amd64 with or without the [hardware-assisted virtualization](https://en.wikipedia.org/wiki/Hardware-assisted_virtualization).

### Mounting the virtual disk image file

For the raw disk image file, see [The disk image](#_the_disk_image).

For other virtual disk image files, you can use `qemu-nbd(8)` to export them using [network block device](https://en.wikipedia.org/wiki/Network_block_device) protocol and mount them using the `nbd` kernel module.

`qemu-nbd(8)` supports disk formats supported by [QEMU](https://en.wikipedia.org/wiki/QEMU): [QEMU](https://en.wikipedia.org/wiki/QEMU) supports following disk formats: raw, [qcow2, qcow](https://en.wikipedia.org/wiki/Qcow), [vmdk](https://en.wikipedia.org/wiki/VMDK), [vdi](https://en.wikipedia.org/wiki/VirtualBox#Virtual_Desktop_Image), [bochs](https://en.wikipedia.org/wiki/Bochs), cow (user-mode Linux copy-on-write), [parallels](https://en.wikipedia.org/wiki/Parallels_Workstation), [dmg](https://en.wikipedia.org/wiki/Apple_Disk_Image), [cloop](https://en.wikipedia.org/wiki/Cloop), [vpc](https://en.wikipedia.org/wiki/VHD_(file_format)), vvfat (virtual VFAT), and host_device.

The [network block device](https://en.wikipedia.org/wiki/Network_block_device) can support partitions in the same way as the [loop device](https://en.wikipedia.org/wiki/Loop_device) (see [Mounting the disk image file](#_mounting_the_disk_image_file)). You can mount the first partition of "`disk.img`" as follows.

    # modprobe nbd max_part=16
    # qemu-nbd -v -c /dev/nbd0 disk.img
    ...
    # mkdir /mnt/part1
    # mount /dev/nbd0p1 /mnt/part1

> [!TIP]
> You may export only the first partition of "`disk.img`" using "`-P 1`" option to `qemu-nbd(8)`.

### Chroot system

`chroot(8)` offers most basic way to run different instances of the GNU/Linux environment on a single system simultaneously without rebooting.

> [!CAUTION]
> Examples below assumes both parent system and chroot system share the same CPU architecture.

You can learn how to setup and use `chroot(8)` by running `pbuilder(8)` program under `script(1)` as follows.

    $ sudo mkdir /sid-root
    $ sudo pbuilder --create --no-targz --debug --buildplace /sid-root

You see how `debootstrap(8)` or `cdebootstrap(1)` populate system data for `sid` environment under "`/sid-root`".

> [!TIP]
> These `debootstrap(8)` or `cdebootstrap(1)` are used to [install Debian](https://www.debian.org/releases/stable/installmanual) by the Debian Installer. These can also be used to install Debian to a system without using a Debian install disk, but instead from another GNU/Linux distribution.

    $ sudo pbuilder --login --no-targz  --debug --buildplace /sid-root

You see how a system shell running under `sid` environment is created as the following.

1.  Copy local configuration (`"/etc/hosts`", `"/etc/hostname`", `"/etc/resolv.conf`")

2.  Mount "`/proc`" filesystem

3.  Mount "`/dev/pts`" filesystem

4.  Create "`/usr/sbin/policy-rc.d`" which always exits with 101

5.  Run "`chroot /sid-root bin/bash -c 'exec -a -bash bin/bash'`"

> [!NOTE]
> Some programs under chroot may require access to more files from the parent system to function than `pbuilder` provides. For example, "`/sys`", "`/etc/passwd`", "`/etc/group`", "`/var/run/utmp`", "`/var/log/wtmp`", etc. may need to be bind-mounted or copied.

> [!NOTE]
> The "`/usr/sbin/policy-rc.d`" file prevents daemon programs to be started automatically on the Debian system. See "`/usr/share/doc/sysv-rc/README.policy-rc.d.gz`".

> [!TIP]
> The original purpose of the specialized chroot package, `pbuilder` is to construct a chroot system and builds a package inside the chroot. It is an ideal system to use to check that a package's build-dependencies are correct, and to be sure that unnecessary and wrong build dependencies do not exist in the resulting package.

> [!TIP]
> Similar `schroot` package may give you an idea to run `i386` chroot system under `amd64` parent system.

### Multiple desktop systems

I recommend you to use [QEMU](https://en.wikipedia.org/wiki/QEMU) or [VirtualBox](https://en.wikipedia.org/wiki/VirtualBox) on a Debian `stable` system to run multiple desktop systems safely using [virtualization](https://en.wikipedia.org/wiki/Virtualization). These enable you to run desktop applications of Debian `unstable` and `testing` without usual risks associated with them.

Since pure [QEMU](https://en.wikipedia.org/wiki/QEMU) is very slow, it is recommended to accelerate it with [KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine) when the host system support it.

The virtual disk image "`virtdisk.qcow2`" containing a Debian system for [QEMU](https://en.wikipedia.org/wiki/QEMU) can be created using [debian-installer: Small CDs](https://www.debian.org/distrib/netinst) as follows.

    $ wget http://cdimage.debian.org/debian-cd/5.0.3/amd64/iso-cd/debian-503-amd64-netinst.iso
    $ qemu-img create -f qcow2 virtdisk.qcow2 5G
    $ qemu -hda virtdisk.qcow2 -cdrom debian-503-amd64-netinst.iso -boot d -m 256
    ...

See more tips at [Debian wiki: QEMU](http://wiki.debian.org/QEMU).

[VirtualBox](https://en.wikipedia.org/wiki/VirtualBox) comes with [Qt](https://en.wikipedia.org/wiki/Qt_(toolkit)) GUI tools and quite intuitive. Its GUI and command line tools are explained in [VirtualBox User Manual](http://www.virtualbox.org/manual/UserManual.html) and [VirtualBox User Manual (PDF)](http://download.virtualbox.org/virtualbox/UserManual.pdf).

> [!TIP]
> Running other GNU/Linux distributions such as [Ubuntu](http://www.ubuntu.com/) and [Fedora](http://fedoraproject.org/) under [virtualization](https://en.wikipedia.org/wiki/Virtualization) is a great way to learn configuration tips. Other proprietary OSs may be run nicely under this GNU/Linux [virtualization](https://en.wikipedia.org/wiki/Virtualization), too.
