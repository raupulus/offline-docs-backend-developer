---
title: stream_filter_append
description: Añade un filtro a un flujo al final de la lista
source_url: https://www.php.net/manual/es/function.stream-filter-append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-filter-append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: a684294e0
order: 87910
---

stream_filter_append

Añade un filtro a un flujo al final de la lista

## Descripción

```php
stream_filter_append(resource $stream, string $filter_name, [int $mode], [mixed $params]): resource
```php

`stream_filter_append` añade el filtro `filter_name` a la lista de filtros adjuntos al flujo `stream`.

## Parámetros

`stream`  
El flujo de destino.

`filter_name`  
El nombre del filtro.

`mode`  
Por omisión, `stream_filter_append` añadirá el filtro a la lista de filtros de lectura si el fichero se abrió en modo lectura (`r` y/o `+`). El filtro también se adjuntará a la lista de filtros de escritura si el fichero se abrió en modo escritura (`w`, `a` y/o `+`). `STREAM_FILTER_READ`, `STREAM_FILTER_WRITE`, y/o `STREAM_FILTER_ALL` pueden también ser utilizadas en el parámetro `mode` para controlar este comportamiento.

`params`  
Este filtro se añadirá con los parámetros `params` al *final* de la lista de filtros, y será llamado al final de las operaciones de filtros. Para añadir un filtro al principio de la lista, utilice la función `stream_filter_prepend`.

## Valores devueltos

Devuelve un recurso en caso de éxito, o `false` si ocurre un error. El recurso puede ser utilizado para referirse a la instancia de este filtro durante una llamada a la función `stream_filter_remove`.

`false` es devuelto si `stream` no es un recurso o si `filter_name` no puede ser alcanzado.

## Ejemplos

Controlar la aplicación de los filtros

```
<?php
// Apertura de un fichero de prueba en modo lectura/escritura
$fp = fopen('test.txt', 'w+');

/* Se aplica el filtro ROT13 al flujo de escritura, pero no al
 * de lectura */
stream_filter_append($fp, "string.rot13", STREAM_FILTER_WRITE);

/* Se añade una simple cadena al fichero, será
 * transformada por ROT13 al escribir */
fwrite($fp, "Ceci est un test\n");

/* Se vuelve al principio del fichero */
rewind($fp);

/* Se lee el contenido del fichero.
 * Si se aplicara el filtro ROT13 tendríamos la
 * cadena en su estado original */
fpassthru($fp);

fclose($fp);

/* Resultado esperado
   ----------------

Guvf vf n grfg

*/
?>

      
```php

## Notas

> [!NOTE]
> `stream_register_filter` debe ser llamada antes de `stream_filter_append` para registrar el filtro bajo el nombre de `filter_name`.

> [!NOTE]
> Los datos del flujo (locales y remotos) son devueltos en fragmentos, los datos no procesados se conservan en el búfer interno. Cuando un nuevo filtro es añadido al final del flujo, los datos en el búfer interno son pasados al nuevo filtro en ese momento. Esto es diferente del comportamiento de `stream_filter_prepend`.

> [!NOTE]
> Cuando un filtro es añadido para lectura y escritura, se crean dos instancias del filtro. `stream_filter_prepend` debe ser llamada dos veces con `STREAM_FILTER_READ` y `STREAM_FILTER_WRITE` para obtener los recursos de los filtros.

## Véase también

stream_filter_register

stream_filter_prepend

stream_get_filters
