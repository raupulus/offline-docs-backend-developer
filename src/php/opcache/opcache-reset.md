---
title: opcache_reset
description: Reinicia el contenido del cache opcode
source_url: https://www.php.net/manual/es/function.opcache-reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 87d6bb1bb
order: 58640
---

opcache_reset

Reinicia el contenido del cache opcode

## Descripción

```php
opcache_reset(): bool
```php

Esta función reinicia el cache opcode en su totalidad. Tras la llamada a la función `opcache_reset`, todos los scripts serán recargados y reanalizados en sus próximos llamados. Esta función solo reinicia el cache en memoria, no el cache de los ficheros.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el cache opcode ha sido reiniciado, o `false` si el cache opcode está desactivado o si el reinicio está pendiente o en curso (ver `opcache_get_status`).

## Véase también

opcache_get_status
