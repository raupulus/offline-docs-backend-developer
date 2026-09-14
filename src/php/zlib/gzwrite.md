---
title: gzwrite
description: Escritura en un archivo gz, segura a nivel binario
source_url: https://www.php.net/manual/es/function.gzwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 9d2b858bc
order: 108920
---

gzwrite

Escritura en un archivo gz, segura a nivel binario

## Descripción

```php
gzwrite(resource $stream, string $data, [int $length]): int
```php

`gzwrite` escribe el contenido de `data` al archivo gz dado.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

`data`  
La cadena a escribir.

`length`  
El número de bytes sin comprimir a escribir. Si se suministra, la escritura se detendrá después de que se hayan escrito los bytes (sin comprimir) del parámetro `length` o de que sea alcanzado el fin de la `data`, lo que ocurra primero.

## Valores devueltos

Retorna el número de bytes (sin comprimir) escritos en el flujo del archivo gz dado, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `length` ahora es anulable; anteriormente, el valor predeterminado era `0`. |
| 7.4.0 | Esta función ahora devuelve `false` en caso de fallo; antes se devolvía `0`. |

## Ejemplos

Ejemplo de `gzwrite`

```
<?php
$string = 'Some information to compress';
$gz = gzopen('somefile.gz','w9');
gzwrite($gz, $string);
gzclose($gz);
?>

    
```php

## Véase también

`gzread`, `gzopen`
