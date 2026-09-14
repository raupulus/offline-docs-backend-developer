---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/posix.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: be0867e64
order: 65090
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

## Constantes `posix_access`

> [!NOTE]
> Se debe tener en cuenta que algunas de estas constantes pueden no estar disponibles en cada sistema.

`POSIX_F_OK` (`int`)  
Verifica si el fichero existe.

`POSIX_R_OK` (`int`)  
Verifica si el fichero existe y tiene los permisos de lectura.

`POSIX_W_OK` (`int`)  
Verifica si el fichero existe y tiene los permisos de escritura.

`POSIX_X_OK` (`int`)  
Verifica si el fichero existe y tiene los permisos de ejecución.

## Constantes `posix_mknod`

> [!NOTE]
> Tenga en cuenta que algunas de ellas pueden no estar disponibles en su sistema.

`POSIX_S_IFBLK` (`int`)  
Archivos especiales de bloque

`POSIX_S_IFCHR` (`int`)  
Archivos especiales de carácter

`POSIX_S_IFIFO` (`int`)  
FIFO (pipe nombrado) de archivos especiales

`POSIX_S_IFREG` (`int`)  
Archivo normal

`POSIX_S_IFSOCK` (`int`)  
Socket

## Constantes `posix_setrlimit`

> [!NOTE]
> Tenga en cuenta que algunas de ellas pueden no estar disponibles en su sistema.

> [!NOTE]
> Se debe leer las notas siguientes además del manual de usuario sobre la función `setrlimit` de su sistema específico, sabiendo que puede haber variación en la interpretación de estos límites, incluso entre varios sistemas que afirman aplicar POSIX en su totalidad.

`POSIX_RLIMIT_AS` (`int`)  
El tamaño máximo del espacio de direcciones del proceso, en bytes. Ver también la directiva de configuración PHP [memory_limit](#ini.memory-limit).

`POSIX_RLIMIT_CORE` (`int`)  
El tamaño máximo de un archivo de núcleo. Si el límite se establece en 0, no se generará ningún archivo de núcleo.

`POSIX_RLIMIT_CPU` (`int`)  
La cantidad máxima de tiempo de CPU que el proceso puede utilizar, en segundos. Cuando se alcanza el límite soft, se emitirá una señal `SIGXCPU`, que puede ser interceptada con la función `pcntl_signal`. Según el sistema, las señales `SIGXCPU` también pueden emitirse cada segundo mientras se alcance el límite hard, en cuyo caso, se emitirá una señal `SIGKILL` no interceptable.

Ver también la función `set_time_limit`.

`POSIX_RLIMIT_DATA` (`int`)  
El tamaño máximo de un segmento de datos del proceso, en bytes. Es poco probable que esto tenga algún efecto en la ejecución de PHP mientras se esté utilizando una extensión y llame a la función `brk` o `sbrk`.

`POSIX_RLIMIT_FSIZE` (`int`)  
El tamaño máximo de los archivos que el proceso puede crear, en bytes.

`POSIX_RLIMIT_LOCKS` (`int`)  
El número máximo de cerrojos que el proceso puede crear. Esto solo es soportado en núcleos Linux muy antiguos.

`POSIX_RLIMIT_MEMLOCK` (`int`)  
El número máximo de bytes que pueden bloquearse en memoria.

`POSIX_RLIMIT_MSGQUEUE` (`int`)  
El número máximo de bytes que pueden asignarse para la cola de mensajes POSIX. PHP no viene con soporte para la cola de mensajes POSIX, por lo tanto, este límite no tendrá ningún efecto a menos que utilice una extensión que implemente este soporte.

`POSIX_RLIMIT_NICE` (`int`)  
El valor máximo al cual el proceso puede ser [cambiado de prioridad](#function.pcntl-setpriority). El valor utilizado será `20 - limit`, sabiendo que los valores límite del recurso no pueden ser negativos.

`POSIX_RLIMIT_NOFILE` (`int`)  
Un valor superior al número máximo de descriptores de archivo que pueden abrirse por este proceso.

`POSIX_RLIMIT_NPROC` (`int`)  
El número máximo de procesos (y/o hilos, según el sistema) que pueden crearse para el ID de usuario real del proceso.

`POSIX_RLIMIT_RSS` (`int`)  
El tamaño máximo del juego residente del proceso, en páginas.

`POSIX_RLIMIT_RTPRIO` (`int`)  
La prioridad máxima de tiempo real que puede establecerse mediante las llamadas al sistema `sched_setscheduler` y `sched_setparam`.

`POSIX_RLIMIT_RTTIME` (`int`)  
La cantidad máxima de tiempo de CPU, en microsegundos, que el proceso puede consumir sin hacer una llamada al sistema bloqueante si utiliza el reloj de tiempo real.

`POSIX_RLIMIT_SIGPENDING` (`int`)  
El número máximo de señales que pueden ponerse en cola para el ID de usuario real del proceso.

`POSIX_RLIMIT_STACK` (`int`)  
El tamaño máximo de la pila del proceso, en bytes.

`POSIX_RLIMIT_INFINITY` (`int`)  
Utilizado para indicar un valor infinito para un límite de recurso.

`POSIX_RLIMIT_KQUEUES` (`int`)  
El número máximo de kqueues que este id de usuario está autorizado a crear (FreeBSD). Disponible a partir de PHP 8.1.0.

`POSIX_RLIMIT_NPTS` (`int`)  
El número máximo de pseudo-terminales que este id de usuario está autorizado a crear (FreeBSD). Disponible a partir de PHP 8.1.0.

## Constantes de `posix_pathconf`

`POSIX_PC_LINK_MAX` (`int`)  
El número máximo de enlaces que un fichero o directorio dado puede tener. Disponible a partir de PHP 8.3.0.

`POSIX_PC_MAX_CANON` (`int`)  
El número máximo de bytes en un búfer de entrada canónica de terminal (el camino siendo entonces un fichero especial de caracteres). Disponible a partir de PHP 8.3.0.

`POSIX_PC_MAX_INPUT` (`int`)  
El número máximo de bytes en una cola de entrada de terminal (el camino siendo entonces un fichero especial de caracteres). Disponible a partir de PHP 8.3.0.

`POSIX_PC_NAME_MAX` (`int`)  
El número máximo de caracteres para un nombre de fichero solo, sin su camino. Disponible a partir de PHP 8.3.0.

`POSIX_PC_PATH_MAX` (`int`)  
El número máximo de caracteres para un camino completo. Disponible a partir de PHP 8.3.0.

`POSIX_PC_PIPE_BUF` (`int`)  
El número máximo de bytes que pueden escribirse en un tubo en una sola operación. Disponible a partir de PHP 8.3.0.

`POSIX_PC_CHOWN_RESTRICTED` (`int`)  
Si se requieren privilegios para permitir que `chown` funcione. Disponible a partir de PHP 8.3.0.

`POSIX_PC_NO_TRUNC` (`int`)  
Si un nombre de fichero (o ficheros bajo un directorio) es más largo que `POSIX_PC_NAME_MAX`. Disponible a partir de PHP 8.3.0.

`POSIX_PC_ALLOC_SIZE_MIN` (`int`)  
El número mínimo de bytes de almacenamiento asignados para cualquier parte de un fichero. Disponible a partir de PHP 8.3.0.

`POSIX_PC_ALLOC_SYMLINK_MAX` (`int`)  
El número máximo de enlaces simbólicos que un fichero o directorio dado puede tener. Disponible a partir de PHP 8.3.0.

`POSIX_PC_SYMLINK_MAX` (`int`)  
El número máximo de bytes en un enlace simbólico. Disponible a partir de PHP 8.3.0.

## Constantes de `posix_sysconf`

`POSIX_SC_ARG_MAX` (`int`)  
El número máximo de bytes que pueden tener los argumentos (y las variables de entorno). Disponible a partir de PHP 8.3.0.

`POSIX_SC_PAGESIZE` (`int`)  
El número de bytes de la página actual. Disponible a partir de PHP 8.3.0.

`POSIX_SC_NPROCESSORS_CONF` (`int`)  
El número de procesadores configurados en todo el sistema. Disponible a partir de PHP 8.3.0.

`POSIX_SC_NPROCESSORS_ONLN` (`int`)  
El número de procesadores actualmente activos en todo el sistema. Disponible a partir de PHP 8.3.0.

`POSIX_SC_CHILD_MAX` (`int`)  
El número máximo de procesos simultáneos por usuario. Disponible a partir de PHP 8.4.0.

`POSIX_SC_CLK_TCK` (`int`)  
El número de ticks de reloj por segundo. Disponible a partir de PHP 8.4.0.
