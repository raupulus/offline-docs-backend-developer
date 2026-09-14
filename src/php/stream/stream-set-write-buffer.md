---
title: stream_set_write_buffer
description: Configura el buffer de escritura de un flujo
source_url: https://www.php.net/manual/es/function.stream-set-write-buffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-set-write-buffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: c3067ab0a
order: 88110
---

stream_set_write_buffer

Configura el buffer de escritura de un flujo

## Descripción

```php
stream_set_write_buffer(resource $stream, int $size): int
```php

`stream_set_write_buffer` configura el buffer de escritura del flujo `stream` al tamaño de `size` bytes.

## Parámetros

`stream`  
El puntero de fichero.

`size`  
El número de bytes a almacenar en el buffer. Si `size` es 0, las operaciones se realizan sin buffer. Esto garantiza que las operaciones con `fwrite` se completen antes de que otros procesos puedan escribir en el flujo de salida.

## Valores devueltos

Devuelve 0 en caso de éxito, o otro valor si la petición falla.

## Ejemplos

Ejemplo con `stream_set_write_buffer`

El ejemplo siguiente ilustra el uso de `stream_set_write_buffer` para crear un flujo sin buffer.

```
<?php
$fp = fopen($file, "w");
if ($fp) {
  if (stream_set_write_buffer($fp, 0) !== 0) {
      // la modificación del buffer ha fallado
  }
  fwrite($fp, $output);
  fclose($fp);
}
?>

    
```php

## Véase también

fopen

fwrite
