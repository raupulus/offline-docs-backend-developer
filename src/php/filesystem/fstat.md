---
title: fstat
description: Lee las informaciones sobre un fichero a partir de un puntero de fichero
source_url: https://www.php.net/manual/es/function.fstat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fstat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23680
---

fstat

Lee las informaciones sobre un fichero a partir de un puntero de fichero

## Descripción

```php
fstat(resource $stream): array
```php

Recopila las informaciones sobre el fichero del cual se conoce el puntero `stream`. `fstat` es similar a la función `stat`, excepto que utiliza un puntero de fichero, en lugar de un nombre de fichero.

## Parámetros

`stream`  
Un puntero al sistema de ficheros de tipo `resource` que típicamente se crea utilizando `fopen`.

## Valores devueltos

Devuelve un array que contiene las estadísticas para el fichero; el formato de este array se describe en detalle en la página de documentación de la función `stat`. Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `fstat`

```
<?php

// abre un fichero
$fp = fopen("/etc/passwd", "r");

// lee las informaciones
$fstat = fstat($fp);

// cierra el fichero
fclose($fp);

// muestra el resultado
print_r(array_slice($fstat, 13));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [dev] => 771
        [ino] => 488704
        [mode] => 33188
        [nlink] => 1
        [uid] => 0
        [gid] => 0
        [rdev] => 0
        [size] => 1114
        [atime] => 1061067181
        [mtime] => 1056136526
        [ctime] => 1056136526
        [blksize] => 4096
        [blocks] => 8
    )

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.
