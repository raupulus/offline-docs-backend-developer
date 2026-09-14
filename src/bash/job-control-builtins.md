---
title: Job Control Builtins
source_url: https://www.gnu.org/software/bash/manual
source_path: 037-job-control-builtins.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 370
---

## Job Control Builtins

`bg`  

bg

    bg [jobspec …]

Resume each suspended job \<jobspec\> in the background, as if it had been started with ‘`&`’. If \<jobspec\> is not supplied, the shell uses its notion of the current job. `bg` returns zero unless it is run when job control is not enabled, or, when run with job control enabled, any \<jobspec\> was not found or specifies a job that was started without job control.

`fg`  

fg

    fg [jobspec]

Resume the job \<jobspec\> in the foreground and make it the current job. If \<jobspec\> is not supplied, `fg` resumes the current job. The return status is that of the command placed into the foreground, or non-zero if run when job control is disabled or, when run with job control enabled, \<jobspec\> does not specify a valid job or \<jobspec\> specifies a job that was started without job control.

`jobs`  

jobs

    jobs [-lnprs] [jobspec]
    jobs -x command [arguments]

The first form lists the active jobs. The options have the following meanings:

`-l`  
List process IDs in addition to the normal information.

`-n`  
Display information only about jobs that have changed status since the user was last notified of their status.

`-p`  
List only the process ID of the job’s process group leader.

`-r`  
Display only running jobs.

`-s`  
Display only stopped jobs.

If \<jobspec\> is supplied, `jobs` restricts output to information about that job. If \<jobspec\> is not supplied, `jobs` lists the status of all jobs. The return status is zero unless an invalid option is encountered or an invalid \<jobspec\> is supplied.

If the `-x` option is supplied, `jobs` replaces any \<jobspec\> found in \<command\> or \<arguments\> with the corresponding process group ID, and executes \<command\>, passing it \<argument\>s, returning its exit status.

`kill`  

kill

    kill [-s sigspec] [-n signum] [-sigspec] id […]
    kill -l|-L [exit_status]

Send a signal specified by \<sigspec\> or \<signum\> to the processes named by each \<id\>. Each \<id\> may be a job specification \<jobspec\> or process ID \<pid\>. \<sigspec\> is either a case-insensitive signal name such as `SIGINT` (with or without the `SIG` prefix) or a signal number; \<signum\> is a signal number. If \<sigspec\> and \<signum\> are not present, `kill` sends `SIGTERM`.

The `-l` option lists the signal names. If any arguments are supplied when `-l` is supplied, `kill` lists the names of the signals corresponding to the arguments, and the return status is zero. \<exit_status\> is a number specifying a signal number or the exit status of a process terminated by a signal; if it is supplied, `kill` prints the name of the signal that caused the process to terminate. `kill` assumes that process exit statuses are greater than 128; anything less than that is a signal number. The `-L` option is equivalent to `-l`.

The return status is zero if at least one signal was successfully sent, or non-zero if an error occurs or an invalid option is encountered.

`wait`  

wait

    wait [-fn] [-p varname] [id …]

Wait until the child process specified by each \<id\> exits and return the exit status of the last \<id\>. Each \<id\> may be a process ID \<pid\> or a job specification \<jobspec\>; if a jobspec is supplied, `wait` waits for all processes in the job.

If no options or \<id\>s are supplied, `wait` waits for all running background jobs and the last-executed process substitution, if its process id is the same as \<\$!\>, and the return status is zero.

If the `-n` option is supplied, `wait` waits for any one of the \<id\>s or, if no \<id\>s are supplied, any job or process substitution, to complete and returns its exit status. If none of the supplied \<id\>s is a child of the shell, or if no arguments are supplied and the shell has no unwaited-for children, the exit status is 127.

If the `-p` option is supplied, `wait` assigns the process or job identifier of the job for which the exit status is returned to the variable \<varname\> named by the option argument. The variable, which cannot be readonly, will be unset initially, before any assignment. This is useful only when used with the `-n` option.

Supplying the `-f` option, when job control is enabled, forces `wait` to wait for each \<id\> to terminate before returning its status, instead of returning when it changes status.

If none of the \<id\>s specify one of the shell’s an active child processes, the return status is 127. If `wait` is interrupted by a signal, any \<varname\> will remain unset, and the return status will be greater than 128, as described above (see [Signals](#Signals)). Otherwise, the return status is the exit status of the last \<id\>.

`disown`  

disown

    disown [-ar] [-h] [id …]

Without options, remove each \<id\> from the table of active jobs. Each \<id\> may be a job specification \<jobspec\> or a process ID \<pid\>; if \<id\> is a \<pid\>, `disown` uses the job containing \<pid\> as \<jobspec\>.

If the `-h` option is supplied, `disown` does not remove the jobs corresponding to each `id` from the jobs table, but rather marks them so the shell does not send `SIGHUP` to the job if the shell receives a `SIGHUP`.

If no \<id\> is supplied, the `-a` option means to remove or mark all jobs; the `-r` option without an \<id\> argument removes or marks running jobs. If no \<id\> is supplied, and neither the `-a` nor the `-r` option is supplied, `disown` removes or marks the current job.

The return value is 0 unless an \<id\> does not specify a valid job.

`suspend`  

suspend

    suspend [-f]

Suspend the execution of this shell until it receives a `SIGCONT` signal. A login shell, or a shell without job control enabled, cannot be suspended; the `-f` option will override this and force the suspension. The return status is 0 unless the shell is a login shell or job control is not enabled and `-f` is not supplied.

When job control is not active, the `kill` and `wait` builtins do not accept \<jobspec\> arguments. They must be supplied process IDs.
