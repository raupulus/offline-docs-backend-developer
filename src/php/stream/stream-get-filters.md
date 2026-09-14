---
title: stream_get_filters
description: Lista los filtros registrados
source_url: https://www.php.net/manual/es/function.stream-get-filters.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-get-filters.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: adc94ff1a
order: 87960
---

stream_get_filters

Lista los filtros registrados

## Descripción

```php
stream_get_filters(): array
```php

`stream_get_filters` lee la lista de los filtros registrados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array indexado que contiene la lista de los filtros de flujo disponibles en el sistema.

## Ejemplos

Ejemplo con `stream_get_filters`

```
<?php
$streamlist = stream_get_filters();
print_r($streamlist);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array (
      [0] => string.rot13
      [1] => string.toupper
      [2] => string.tolower
      [3] => string.base64
      [4] => string.quoted-printable
    )

## Véase también

stream_filter_register

stream_get_wrappers
