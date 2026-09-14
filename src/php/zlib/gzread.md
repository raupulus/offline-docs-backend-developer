---
title: gzread
description: Lectura de archivo gz segura a nivel binario
source_url: https://www.php.net/manual/es/function.gzread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 02ba67b51
order: 108870
---

gzread

Lectura de archivo gz segura a nivel binario

## Descripción

```php
gzread(resource $stream, int $length): string
```php

`gzread` lee los bytes hasta el parámetro `length` desde el apuntador al archivo gz dado. La lectura se detiene cuando los bytes del parámetro `length` (sin comprimir) sean leídos o cuando se alcance el fin del archivo (EOF), lo que ocurra primero.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

`length`  
El número de bytes a leer.

## Valores devueltos

Los datos que han sido leídos, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Esta función ahora devuelve `false` en caso de fallo; antes se devolvía `0`. |

## Ejemplos

Ejemplo de `gzread`

```
<?php
// pasar los contenidos de un archivo gz a una cadena
$filename = "/usr/local/something.txt.gz";
$zd = gzopen($filename, "r");
$contents = gzread($zd, 10000);
gzclose($zd);
?>

    
```php

## Véase también

`gzwrite`, `gzopen`, `gzgets`, `gzgetss`, `gzfile`, `gzpassthru`
