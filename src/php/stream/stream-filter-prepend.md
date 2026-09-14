---
title: stream_filter_prepend
description: Adjunta un filtro a un flujo al inicio de la lista
source_url: https://www.php.net/manual/es/function.stream-filter-prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-filter-prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: a684294e0
order: 87920
---

stream_filter_prepend

Adjunta un filtro a un flujo al inicio de la lista

## Descripción

```php
stream_filter_prepend(resource $stream, string $filter_name, [int $mode], [mixed $params]): resource
```php

`stream_filter_prepend` añade el filtro `filter_name` a la lista de filtros adjuntos al flujo `stream`.

## Parámetros

`stream`  
El flujo de destino.

`filter_name`  
El nombre del filtro.

`mode`  
Por omisión, `stream_filter_prepend` adjuntará el filtro a la `cadena de filtros de lectura` si el fichero ha sido abierto en modo lectura (es decir, modo `r`, y/o `+`). El filtro también será adjuntado a la `cadena de filtros de escritura` si el fichero ha sido abierto en modo escritura (es decir, modo `w`, `a`, y/o `+`). `STREAM_FILTER_READ`, `STREAM_FILTER_WRITE`, y/o `STREAM_FILTER_ALL` pueden también ser pasados en el parámetro `mode` para imponer el comportamiento deseado. Véase `stream_filter_append` para un ejemplo de uso de este parámetro.

`params`  
El filtro será añadido con los parámetros especificados en `params`, al *inicio* de la lista, y será llamado en primer lugar en las operaciones del flujo. Para añadir un filtro al final de la lista, utilice `stream_filter_append`.

## Valores devueltos

Devuelve un recurso en caso de éxito, o `false` en caso de error. El recurso puede ser utilizado para referirse a esta instancia de filtro durante una llamada a la función `stream_filter_remove`.

`false` es devuelto si `stream` no es un recurso, o si `filter_name` no puede ser alcanzado.

## Notas

> [!NOTE]
> `stream_register_filter` debe ser llamada antes que `stream_filter_prepend` para registrar el filtro bajo el nombre de `filter_name`.

> [!NOTE]
> Los datos del flujo (locales y remotos) son devueltos en fragmentos, los datos no encaminados son conservados en el búfer interno. Cuando un nuevo filtro es añadido al inicio del flujo, los datos en el búfer interno no son *pasados* al nuevo filtro en ese momento. Esto es diferente del comportamiento de `stream_filter_append`.

> [!NOTE]
> Cuando un filtro es añadido para lectura y escritura, se crean dos instancias del filtro. `stream_filter_prepend` debe ser llamada dos veces con `STREAM_FILTER_READ` y `STREAM_FILTER_WRITE` para obtener los recursos de los filtros.

## Véase también

stream_filter_register

stream_filter_append
