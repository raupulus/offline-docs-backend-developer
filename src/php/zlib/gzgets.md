---
title: gzgets
description: Obtiene la línea del apuntador al archivo
source_url: https://www.php.net/manual/es/function.gzgets.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzgets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: c2120bd34
order: 108810
---

gzgets

Obtiene la línea del apuntador al archivo

## Descripción

```php
gzgets(resource $stream, [int $length]): string
```php

Obtiene una cadena (sin comprimir) de hasta un largo de - 1 bytes leídos desde el apuntador al archivo dado. La lectura termina cuando el largo de - 1 bytes ha sido leído, en un salto de línea o cuando se alcance el fin del archivo (EOF), lo que ocurra primero.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

`length`  
La longitud de los datos a obtener.

## Valores devueltos

La cadena sin comprimir o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `length` ahora es anulable; anteriormente, el valor predeterminado era `1024`. |

## Ejemplos

Ejemplo de `gzgets`

```
<?php
$handle = gzopen('somefile.gz', 'r');
while (!gzeof($handle)) {
   $buffer = gzgets($handle, 4096);
   echo $buffer;
}
gzclose($handle);
?>

    
```php

## Véase también

`gzopen`, `gzgetc`, `gzwrite`
