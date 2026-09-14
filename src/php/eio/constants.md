---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/eio.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_reviewed: false
translation_revision: '213250199'
order: 16660
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Constantes de prioridad de petición:

`EIO_PRI_MIN` (`int`)  
Prioridad de petición mínima.

`EIO_PRI_DEFAULT` (`int`)  
Prioridad de petición predeterminada.

`EIO_PRI_MAX` (`int`)  
Prioridad de petición máxima.

El argumento `whence` de `eio_seek`:

`EIO_SEEK_SET` (`int`)  
El índice es establecido para espcificar el número de bytes (`offset`).

`EIO_SEEK_CUR` (`int`)  
El índice es establecido a su ubicación actual más `offset` bytes.

`EIO_SEEK_END` (`int`)  
El índice es establecido a el tamaño del fichero más `offset` bytes.

Banderas usadas con `eio_readdir`:

`EIO_READDIR_DENTS` (`int`)  
Bandera `eio_readdir`. Si se especifica, el argumento resultante de la llamada de retorno se convierte en un array con las siguientes claves: `'names'` - array de nombres de directorios `'dents'` - array de `structura eio_dirent`-como los arrays pero teniendo las siguientes claves: `'name'` - el nombre del directorio; `'type'` - una de las constantes *EIO_DT\_\**; `'inode'` - el número de inodo, si está disponible, de otro modo sin especificar.

`EIO_READDIR_DIRS_FIRST` (`int`)  
Cuando se especifica esta bandera, los nombres serán devueltos en un orden donde probablemente los directorios vallan primero, en un orden de estadísticas óptimo.

`EIO_READDIR_STAT_ORDER` (`int`)  
Cuando se especifica esta bandera, los nombres serán devueltos en un orden apropiado para realizar estadísticas (`stat`) con cada uno. Cuando se planea usar la función `stat` para realizar estadísticas de todos los archivos del directorio dado, el orden devuelto probablemente sea más rápido.

`EIO_READDIR_FOUND_UNKNOWN` (`int`)  

`EIO_DT_UNKNOWN` (`int`)  
Tipo de nodo desconocido (muy común). Se necistan más estadísticas (`stat`).

`EIO_DT_FIFO` (`int`)  
Tipo de nodo FIFO.

`EIO_DT_CHR` (`int`)  
Tipo de nodo.

`EIO_DT_MPC` (`int`)  
Tipo de nodo de dispositivo de caracteres multiplexado (v7+coherent).

`EIO_DT_DIR` (`int`)  
Tipo de nodo de directorio.

`EIO_DT_NAM` (`int`)  
Tipo de nodo de fichero Xenix nominado especial.

`EIO_DT_BLK` (`int`)  
Tipo de nodo.

`EIO_DT_MPB` (`int`)  
Dispositivo de bloqueo multiplexado (v7+coherent).

`EIO_DT_REG` (`int`)  
Tipo de nodo.

`EIO_DT_NWK` (`int`)  

`EIO_DT_CMP` (`int`)  
Tipo de nodo especial de red HP-UX.

`EIO_DT_LNK` (`int`)  
Tipo de nodo de vínculo.

`EIO_DT_SOCK` (`int`)  
Tipo de nodo socket.

`EIO_DT_DOOR` (`int`)  
Tipo de nodo de puerta de Solaris.

`EIO_DT_WHT` (`int`)  
Tipo de nodo.

`EIO_DT_MAX` (`int`)  
Valor de tipo de nodo más alto.

Modo de acceso para el argumento `flags` de `eio_open`:

`EIO_O_RDONLY` (`int`)  

`EIO_O_WRONLY` (`int`)  

`EIO_O_RDWR` (`int`)  

`EIO_O_NONBLOCK` (`int`)  

`EIO_O_APPEND` (`int`)  

`EIO_O_CREAT` (`int`)  

`EIO_O_TRUNC` (`int`)  

`EIO_O_EXCL` (`int`)  

`EIO_O_FSYNC` (`int`)  

Banderas del argumento `mode` de `eio_open`:

`EIO_S_IRUSR` (`int`)  

`EIO_S_IWUSR` (`int`)  

`EIO_S_IXUSR` (`int`)  

`EIO_S_IRGRP` (`int`)  

`EIO_S_IWGRP` (`int`)  

`EIO_S_IXGRP` (`int`)  

`EIO_S_IROTH` (`int`)  

`EIO_S_IWOTH` (`int`)  

`EIO_S_IXOTH` (`int`)  

`EIO_S_IFREG` (`int`)  

`EIO_S_IFCHR` (`int`)  

`EIO_S_IFBLK` (`int`)  

`EIO_S_IFIFO` (`int`)  

`EIO_S_IFSOCK` (`int`)  

Banderas de `eio_sync_file_range`:

`EIO_SYNC_FILE_RANGE_WAIT_BEFORE` (`int`)  

`EIO_SYNC_FILE_RANGE_WRITE` (`int`)  

`EIO_SYNC_FILE_RANGE_WAIT_AFTER` (`int`)  

Banderas de `eio_fallocate`:

`EIO_FALLOC_FL_KEEP_SIZE` (`int`)  

> [!NOTE]
> Las constantes *EIO_S_I\** tienen el mismo significado que sus homónimos *S_I\** de POSIX.

> [!NOTE]
> *EIO_SYNC_FILE\_\**tienen el mismo significado que sus homónimos *SYNC_FILE\_\*\**.

> [!NOTE]
> *EIO_O\_\**tienen el mismo significado que sus homónimos *O\_\**de POSIX.
