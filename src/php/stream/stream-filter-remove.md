---
title: stream_filter_remove
description: Elimina un filtro de un flujo
source_url: https://www.php.net/manual/es/function.stream-filter-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-filter-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: a9ada9d6f
order: 87940
---

stream_filter_remove

Elimina un filtro de un flujo

## Descripción

```php
stream_filter_remove(resource $stream_filter): bool
```php

Elimina un filtro de flujo previamente añadido al flujo con `stream_filter_prepend` o `stream_filter_append`. Cualquier información restante en el buffer interno del filtro será volcada al siguiente filtro antes de eliminarla.

## Parámetros

`stream_filter`  
El filtro de flujo a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Refiltrar dináminamente un flujo

```
<?php
/* Abrir un archivo de prueba para lectura y escritura */
$fp = fopen("prueba.txt", "rw");

$filtro_rot13 = stream_filter_append($fp, "string.rot13", STREAM_FILTER_WRITE);
fwrite($fp, "Esto es ");
stream_filter_remove($filtro_rot13);
fwrite($fp, "una prueba\n");

rewind($fp);
fpassthru($fp);
fclose($fp);

?>

    
```php

El ejemplo anterior mostrará:

    Rfgb rf una prueba

## Véase también

`stream_filter_register`, `stream_filter_append`, `stream_filter_prepend`
