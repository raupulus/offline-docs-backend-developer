---
title: stream_get_transports
description: Lista los gestores de transporte de sockets disponibles
source_url: https://www.php.net/manual/es/function.stream-get-transports.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-get-transports.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: adc94ff1a
order: 87990
---

stream_get_transports

Lista los gestores de transporte de sockets disponibles

## Descripción

```php
stream_get_transports(): array
```php

`stream_get_transports` devuelve un array indexado que contiene los nombres de los transportes de sockets disponibles para el sistema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array indexado de nombres de sockets de transporte.

## Ejemplos

Ejemplo con `stream_get_transports`

```
<?php
$xportlist = stream_get_transports();
print_r($xportlist);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array (
      [0] => tcp
      [1] => udp
      [2] => unix
      [3] => udg
    )
    ?>

## Véase también

stream_get_filters

stream_get_wrappers
