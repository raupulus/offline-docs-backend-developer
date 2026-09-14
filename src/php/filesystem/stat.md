---
title: stat
description: Proporciona información sobre un fichero
source_url: https://www.php.net/manual/es/function.stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: f80105b4f
order: 24030
---

stat

Proporciona información sobre un fichero

## Descripción

```php
stat(string $filename): array
```php

Proporciona información sobre el fichero `filename`. Si `filename` es un enlace simbólico, la información proviene del fichero en sí, y no del enlace simbólico. Antes de PHP 7.4.0, en Windows NTS compila los valores estáticos `size`, `atime`, `mtime` y `ctime` desde los enlaces simbólicos, en este caso.

`lstat` es idéntico a `stat` excepto que la información se basa en el enlace simbólico.

## Parámetros

`filename`  
La ruta al fichero.

## Valores devueltos

| Número | Nombre  | Descripción                                       |
|--------|---------|---------------------------------------------------|
| 0      | dev     | volumen (\*\*\*)                                  |
| 1      | ino     | Número de inodo (\*\*\*\*)                        |
| 2      | mode    | derechos de acceso al inodo \*\*\*\*\*            |
| 3      | nlink   | número de enlaces                                 |
| 4      | uid     | userid del propietario (\*)                       |
| 5      | gid     | groupid del propietario (\*)                      |
| 6      | rdev    | tipo de volumen, si el volumen es un inodo        |
| 7      | size    | tamaño en bytes                                   |
| 8      | atime   | fecha del último acceso (timestamp Unix)          |
| 9      | mtime   | fecha de la última modificación (timestamp Unix)  |
| 10     | ctime   | fecha del último cambio de inodo (timestamp Unix) |
| 11     | blksize | tamaño de bloque (\*\*)                           |
| 12     | blocks  | número de bloques de 512 bytes asignados (\*\*)   |

Formato del resultado de `stat` y `fstat`

\* - En Windows, esto siempre será `0`.

\*\* - Solo en sistemas que soportan el tipo `st_blksize`. Los otros sistemas (ej. Windows) devuelven `-1`.

\*\*\* - En Windows, desde PHP 7.4.0, será el número de serie del volumen que contiene el fichero, que será un entero 64-bit *sin signo* que puede desbordarse. Anteriormente, era la representación numérica de la letra del volumen (ej. `2` para `C:`) para la función `stat`, y `0` para la función `lstat`.

\*\*\*\* - En Windows, desde PHP 7.4.0, es el identificador asociado con el fichero, que será un entero 64-bit *sin signo* que puede desbordarse. Anteriormente, siempre era `0`.

\*\*\*\*\* En Windows, el bit de permiso de escritura se define en función del atributo de solo lectura del fichero, y el mismo valor se reporta para todos los usuarios, grupo y propietario. El ACL no se tiene en cuenta, a diferencia de `is_writable`.

El valor de `mode` contiene información leída por varias funciones. Cuando se escribe en octal, comenzando por la derecha, los tres primeros dígitos son devueltos por `chmod`. El siguiente dígito es ignorado por PHP. Los dos siguientes dígitos indican el tipo de fichero:

| `mode` en octal | Significado             |
|-----------------|-------------------------|
| `0140000`       | socket                  |
| `0120000`       | enlace simbólico        |
| `0100000`       | fichero regular         |
| `0060000`       | dispositivo de bloque   |
| `0040000`       | directorio              |
| `0020000`       | dispositivo de carácter |
| `0010000`       | FIFO (un tubo nombrado) |

Los tipos de ficheros `mode`

Por ejemplo, un fichero regular podría ser `0100644` y un directorio podría `0040755`.

En caso de error, `stat` devuelve `false`.

> [!NOTE]
> Como el tipo entero de PHP es firmado y que muchas plataformas utilizan enteros de 32 bits, algunas funciones relacionadas con el sistema de archivos pueden retornar resultados extraños para ficheros de tamaño superior a 2 Go.

## Errores/Excepciones

Si ocurre un error, se emite una advertencia de tipo `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | En Windows, el número del volumen es ahora el número de serie que contiene el fichero, y el número de inodo es el identificador asociado con el fichero. |
| 7.4.0 | Los valores estáticos `size`, `atime`, `mtime` y `ctime` de los enlaces simbólicos son siempre los de la meta. Esto no era así previamente para los builds NTS en Windows. |

## Ejemplos

Ejemplo con `stat`

```
<?php
/* Obtención de la información */
$stat = stat('C:\php\php.exe');

/*
 * Mostrar la fecha y hora del acceso a este fichero,
 * idéntico a la llamada a la función fileatime()
 */
echo 'Fecha y hora de acceso : ' . $stat['atime'];

/*
 * Mostrar la fecha y hora de modificación del fichero,
 * idéntico a la llamada a la función filemtime()
 */
echo 'Fecha y hora de modificación : ' . $stat['mtime'];

/* Mostrar el número del dispositivo */
echo 'Número del dispositivo : ' . $stat['dev'];
?>

    
```php

Uso de la información obtenida de `stat` junto con la función `touch`

```
<?php
/* Obtención de la información de la función stat */
$stat = stat('C:\php\php.exe');

/* ¿Ha fallado el acceso a la información? */
if (!$stat) {
    echo 'La llamada a stat() ha fallado...';
} else {
    /*
     * Queremos que la fecha y hora de acceso sea una
     * semana después de la fecha actual.
     */
    $atime = $stat['atime'] + 604800;

    /* Modificamos el fichero */
    if(!touch('some_file.txt', time(), $atime)) {
        echo 'Fallo al llamar a la función touch()...';
    } else {
        echo 'La llamada a touch() ha tenido éxito...';
    }
}
?>

    
```php

## Notas

> [!NOTE]
> Tenga en cuenta que la precisión temporal puede variar según el sistema de archivos utilizado.

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`lstat`, `fstat`, `filemtime`, `filegroup`, `SplFileInfo`
