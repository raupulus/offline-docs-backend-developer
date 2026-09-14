---
title: Job Control Basics
source_url: https://www.gnu.org/software/bash/manual
source_path: 036-job-control-basics.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 360
---

## Job Control Basics

job control

foreground

background

suspending jobs

Job control refers to the ability to selectively stop (suspend) the execution of processes and continue (resume) their execution at a later point. A user typically employs this facility via an interactive interface supplied jointly by the operating system kernel’s terminal driver and Bash.

The shell associates a \<job\> with each pipeline. It keeps a table of currently executing jobs, which the `jobs` command will display. Each job has a job number, which `jobs` displays between brackets. Job numbers start at 1. When Bash starts a job asynchronously, it prints a line that looks like:

    [1] 25647

indicating that this job is job number 1 and that the process ID of the last process in the pipeline associated with this job is 25647. All of the processes in a single pipeline are members of the same job. Bash uses the \<job\> abstraction as the basis for job control.

To facilitate the implementation of the user interface to job control, each process has a process group ID, and the operating system maintains the notion of a current terminal process group ID. This terminal process group ID is associated with the controlling terminal.

Processes that have the same process group ID are said to be part of the same process group. Members of the foreground process group (processes whose process group ID is equal to the current terminal process group ID) receive keyboard-generated signals such as `SIGINT`. Processes in the foreground process group are said to be foreground processes. Background processes are those whose process group ID differs from the controlling terminal’s; such processes are immune to keyboard-generated signals. Only foreground processes are allowed to read from or, if the user so specifies with `stty tostop`, write to the controlling terminal. The system sends a `SIGTTIN` (`SIGTTOU`) signal to background processes which attempt to read from (write to when `tostop` is in effect) the terminal, which, unless caught, suspends the process.

If the operating system on which Bash is running supports job control, Bash contains facilities to use it. Typing the suspend character (typically ‘`^Z`’, Control-Z) while a process is running stops that process and returns control to Bash. Typing the delayed suspend character (typically ‘`^Y`’, Control-Y) causes the process to stop when it attempts to read input from the terminal, and returns control to Bash. The user then manipulates the state of this job, using the `bg` command to continue it in the background, the `fg` command to continue it in the foreground, or the `kill` command to kill it. The suspend character takes effect immediately, and has the additional side effect of discarding any pending output and typeahead. If you want to force a background process to stop, or stop a process that’s not associated with your terminal session, send it the `SIGSTOP` signal using `kill`.

There are a number of ways to refer to a job in the shell. The ‘`%`’ character introduces a job specification (jobspec).

Job number `n` may be referred to as ‘`%n`’. A job may also be referred to using a prefix of the name used to start it, or using a substring that appears in its command line. For example, ‘`%ce`’ refers to a job whose command name begins with ‘`ce`’. Using ‘`%?ce`’, on the other hand, refers to any job containing the string ‘`ce`’ in its command line. If the prefix or substring matches more than one job, Bash reports an error.

The symbols ‘`%%`’ and ‘`%+`’ refer to the shell’s notion of the current job. A single ‘`%`’ (with no accompanying job specification) also refers to the current job. ‘`%-`’ refers to the previous job. When a job starts in the background, a job stops while in the foreground, or a job is resumed in the background, it becomes the current job. The job that was the current job becomes the previous job. When the current job terminates, the previous job becomes the current job. If there is only a single job, ‘`%+`’ and ‘`%-`’ can both be used to refer to that job. In output pertaining to jobs (e.g., the output of the `jobs` command), the current job is always marked with a ‘`+`’, and the previous job with a ‘`-`’.

Simply naming a job can be used to bring it into the foreground: ‘`%1`’ is a synonym for ‘`fg %1`’, bringing job 1 from the background into the foreground. Similarly, ‘`%1 &`’ resumes job 1 in the background, equivalent to ‘`bg %1`’.

The shell learns immediately whenever a job changes state. Normally, Bash waits until it is about to print a prompt before notifying the user about changes in a job’s status so as to not interrupt any other output, though it will notify of changes in a job’s status after a foreground command in a list completes, before executing the next command in the list. If the `-b` option to the `set` builtin is enabled, Bash reports status changes immediately (see [The Set Builtin](#The-Set-Builtin)). Bash executes any trap on `SIGCHLD` for each child process that terminates.

When a job terminates and Bash notifies the user about it, Bash removes the job from the jobs table. It will not appear in `jobs` output, but `wait` will report its exit status, as long as it’s supplied the process ID associated with the job as an argument. When the table is empty, job numbers start over at 1.

If a user attempts to exit Bash while jobs are stopped, (or running, if the `checkjobs` option is enabled – see [The Shopt Builtin](#The-Shopt-Builtin)), the shell prints a warning message, and if the `checkjobs` option is enabled, lists the jobs and their statuses. The `jobs` command may then be used to inspect their status. If the user immediately attempts to exit again, without an intervening command, Bash does not print another warning, and terminates any stopped jobs.

When the shell is waiting for a job or process using the `wait` builtin, and job control is enabled, `wait` will return when the job changes state. The `-f` option causes `wait` to wait until the job or process terminates before returning.
