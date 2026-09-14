---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pcntl.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 71fa455c5
order: 61160
---

## Constantes predefinidas

La lista siguiente representa los señales soportadas por las funciones de gestión de procesos. Consulte el manual de su sistema (signal(7)) para más detalles sobre estas señales.

`WNOHANG` (`int`)  

`WUNTRACED` (`int`)  

`WCONTINUED` (`int`)  

`WEXITED` (`int`)  

`WSTOPPED` (`int`)  

`WNOWAIT` (`int`)  

<!-- -->

`SIG_IGN` (`int`)  

`SIG_DFL` (`int`)  

`SIG_ERR` (`int`)  

`SIGHUP` (`int`)  

`SIGINFO` (`int`)  

`SIGINT` (`int`)  

`SIGQUIT` (`int`)  

`SIGILL` (`int`)  

`SIGTRAP` (`int`)  

`SIGABRT` (`int`)  

`SIGIOT` (`int`)  

`SIGBUS` (`int`)  

`SIGFPE` (`int`)  

`SIGKILL` (`int`)  

`SIGUSR1` (`int`)  

`SIGSEGV` (`int`)  

`SIGUSR2` (`int`)  

`SIGPIPE` (`int`)  

`SIGALRM` (`int`)  

`SIGTERM` (`int`)  

`SIGSTKFLT` (`int`)  

`SIGCLD` (`int`)  

`SIGCHLD` (`int`)  

`SIGCONT` (`int`)  

`SIGSTOP` (`int`)  

`SIGTSTP` (`int`)  

`SIGTTIN` (`int`)  

`SIGTTOU` (`int`)  

`SIGURG` (`int`)  

`SIGXCPU` (`int`)  

`SIGXFSZ` (`int`)  

`SIGVTALRM` (`int`)  

`SIGPROF` (`int`)  

`SIGWINCH` (`int`)  

`SIGPOLL` (`int`)  

`SIGIO` (`int`)  

`SIGPWR` (`int`)  

`SIGSYS` (`int`)  

`SIGBABY` (`int`)  

`SIGRTMIN` (`int`)  

`SIGRTMAX` (`int`)  

`SIG_BLOCK` (`int`)  

`SIG_UNBLOCK` (`int`)  

`SIG_SETMASK` (`int`)  

`SIGCKPT` (`int`)  
Genera/restituye un punto de control. Disponible a partir de PHP 8.4.0 (únicamente en DragonFlyBSD).

`SIGCKPTEXIT` (`int`)  
Genera/restituye un punto de control y sale. Disponible a partir de PHP 8.4.0 (únicamente en DragonFlyBSD).

<!-- -->

`SI_USER` (`int`)  

`SI_NOINFO` (`int`)  

`SI_KERNEL` (`int`)  

`SI_QUEUE` (`int`)  

`SI_TIMER` (`int`)  

`SI_MSGGQ` (`int`)  

`SI_ASYNCIO` (`int`)  

`SI_SIGIO` (`int`)  

`SI_TKILL` (`int`)  

`SI_MESGQ` (`int`)  

<!-- -->

`CLD_EXITED` (`int`)  

`CLD_KILLED` (`int`)  

`CLD_DUMPED` (`int`)  

`CLD_TRAPPED` (`int`)  

`CLD_STOPPED` (`int`)  

`CLD_CONTINUED` (`int`)  

<!-- -->

`TRAP_BRKPT` (`int`)  

`TRAP_TRACE` (`int`)  

<!-- -->

`POLL_IN` (`int`)  

`POLL_OUT` (`int`)  

`POLL_MSG` (`int`)  

`POLL_ERR` (`int`)  

`POLL_PRI` (`int`)  

`POLL_HUP` (`int`)  

<!-- -->

`ILL_ILLOPC` (`int`)  

`ILL_ILLOPN` (`int`)  

`ILL_ILLADR` (`int`)  

`ILL_ILLTRP` (`int`)  

`ILL_PRVOPC` (`int`)  

`ILL_PRVREG` (`int`)  

`ILL_COPROC` (`int`)  

`ILL_BADSTK` (`int`)  

<!-- -->

`FPE_INTDIV` (`int`)  

`FPE_INTOVF` (`int`)  

`FPE_FLTDIV` (`int`)  

`FPE_FLTOVF` (`int`)  

`FPE_FLTUND` (`int`)  

`FPE_FLTRES` (`int`)  

`FPE_FLTINV` (`int`)  

`FPE_FLTSUB` (`int`)  

<!-- -->

`SEGV_MAPERR` (`int`)  

`SEGV_ACCERR` (`int`)  

<!-- -->

`BUS_ADRALN` (`int`)  

`BUS_ADRERR` (`int`)  

`BUS_OBJERR` (`int`)  

<!-- -->

`CLONE_NEWNS` (`int`)  
Disponible a partir de PHP 7.4.0

`CLONE_NEWIPC` (`int`)  
Disponible a partir de PHP 7.4.0

`CLONE_NEWUTS` (`int`)  
Disponible a partir de PHP 7.4.0

`CLONE_NEWNET` (`int`)  
Disponible a partir de PHP 7.4.0

`CLONE_NEWPID` (`int`)  
Disponible a partir de PHP 7.4.0

`CLONE_NEWUSER` (`int`)  
Disponible a partir de PHP 7.4.0

`CLONE_NEWCGROUP` (`int`)  
Disponible a partir de PHP 7.4.0

<!-- -->

`PRIO_PGRP` (`int`)  

`PRIO_USER` (`int`)  

`PRIO_PROCESS` (`int`)  

`PRIO_DARWIN_BG` (`int`)  
Disponible a partir de PHP 8.1.0.

`PRIO_DARWIN_THREAD` (`int`)  
Disponible a partir de PHP 8.1.0.

`PCNTL_E2BIG` (`int`)  
Lista de argumentos demasiado larga

`PCNTL_EACCES` (`int`)  
Permiso denegado

`PCNTL_EAGAIN` (`int`)  
Recurso temporalmente no disponible

`PCNTL_ECAPMODE` (`int`)  
El proceso ha intentado una operación no autorizada en modo capacitario mientras se ejecutaba en modo capacitario.

`PCNTL_ECHILD` (`int`)  
Ningún proceso hijo

`PCNTL_EFAULT` (`int`)  
Dirección incorrecta

`PCNTL_EINTR` (`int`)  
Llamada de función interrumpida

`PCNTL_EINVAL` (`int`)  
Argumento no válido

`PCNTL_EIO` (`int`)  
Error de entrada/salida

`PCNTL_EISDIR` (`int`)  
Es un directorio

`PCNTL_ELIBBAD` (`int`)  
Acceso a una biblioteca compartida corrupta.

`PCNTL_ELOOP` (`int`)  
Demasiados niveles de enlaces simbólicos

`PCNTL_EMFILE` (`int`)  
Demasiados ficheros abiertos. Comúnmente causado por exceder el límite de recurso `RLIMIT_NOFILE`. También puede ser causado por exceder el límite especificado en `/proc/sys/fs/nr_open`.

`PCNTL_ENAMETOOLONG` (`int`)  
Nombre de fichero demasiado largo

`PCNTL_ENFILE` (`int`)  
Demasiados ficheros abiertos en el sistema. En Linux, esto probablemente se debe al encuentro con el límite `/proc/sys/fs/file-max`.

`PCNTL_ENOENT` (`int`)  
Ningún fichero o directorio de ese tipo. Típicamente, este error ocurre cuando una ruta de acceso especificada no existe, o cuando uno de los componentes en el prefijo de directorio de una ruta de acceso no existe, o cuando la ruta de acceso especificada es un enlace simbólico pendiente.

`PCNTL_ENOEXEC` (`int`)  
Error de formato de ejecución

`PCNTL_ENOMEM` (`int`)  
Espacio insuficiente/imposible asignar memoria

`PCNTL_ENOSPC` (`int`)  
No hay espacio disponible en el dispositivo

`PCNTL_ENOTDIR` (`int`)  
No es un directorio

`PCNTL_EPERM` (`int`)  
Operación no permitida

`PCNTL_ESRCH` (`int`)  
Ningún proceso encontrado

`PCNTL_ETXTBSY` (`int`)  
Fichero de texto ocupado

`PCNTL_EUSERS` (`int`)  
Demasiados usuarios

`FORK_NOSIGCHLD` (`int`)  

`FORK_WAITPID` (`int`)  

<!-- -->

`RFCFDG` (`int`)  

`RFFDG` (`int`)  

`RFLINUXTHPN` (`int`)  

`RFNOWAIT` (`int`)  

`RFPROC` (`int`)  

`RFTHREAD` (`int`)  

`RFTSIGZMB` (`int`)  

<!-- -->

`P_ALL` (`int`)  
Seleccionar cualquier hijo.

`P_PID` (`int`)  
Seleccionar por ID de proceso.

`P_PGID` (`int`)  
Seleccionar por ID de grupo de procesos.

`P_PIDFD` (`int`)  
Seleccionar por descriptor de fichero PID. Específico de Linux (desde Linux 5.4).

`P_UID` (`int`)  
Seleccionar por ID de usuario efectivo. Específico de NetBSD y FreeBSD.

`P_GID` (`int`)  
Seleccionar por ID de grupo efectivo. Específico de NetBSD y FreeBSD.

`P_SID` (`int`)  
Seleccionar por ID de sesión. Específico de NetBSD y FreeBSD.

`P_JAILID` (`int`)  
Seleccionar por identificador de jail. Específico de FreeBSD.
