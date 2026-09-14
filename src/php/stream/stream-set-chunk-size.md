---
title: stream_set_size
description: Cambia el tamaño del segmento del flujo
source_url: https://www.php.net/manual/es/function.stream-set-chunk-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-set-chunk-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 51a2b54c3
order: 88080
---

stream_set_size

Cambia el tamaño del segmento del flujo

## Descripción

```php
stream_set_size(resource $stream, int $size): int
```php

Cambia el tamaño del segmento del flujo.

## Parámetros

`stream`  
El flujo en cuestión.

`size`  
El nuevo tamaño de segmento deseado.

## Valores devueltos

Devuelve el tamaño anterior del segmento en caso de éxito.

## Errores/Excepciones

Se lanza un `ValueError` si `size` es inferior a 1 o mayor que `PHP_INT_MAX`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora se lanza un `ValueError` si `size` es inferior a 1 o superior a `PHP_INT_MAX`. Anteriormente, se emitía un error de nivel `E_WARNING` y se devolvía `false`. |
