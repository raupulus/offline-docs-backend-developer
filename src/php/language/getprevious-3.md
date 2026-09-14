---
title: Throwable::getPrevious
description: Devuelve el objeto Throwable previo
source_url: https://www.php.net/manual/es/throwable.getprevious.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/throwable/getprevious.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 4000
---

Throwable::getPrevious

Devuelve el objeto Throwable previo

## Descripción

```php
public Throwable::getPrevious(): Throwable
```php

Devuelve el objeto Throwable previo (por ejemplo, uno proporcionado como tercer parámetro de Exception::\_\_construct).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el objeto `Throwable` anterior si está disponible, o `null` si no lo está.

## Véase también

Exception::getPrevious
