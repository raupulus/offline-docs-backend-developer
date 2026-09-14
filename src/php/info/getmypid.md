---
title: getmypid
description: Devuelve el número de proceso actual de PHP
source_url: https://www.php.net/manual/es/function.getmypid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/getmypid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 8dd14a886
order: 38990
---

getmypid

Devuelve el número de proceso actual de PHP

## Descripción

```php
getmypid(): int
```php

Devuelve el número de proceso actual de PHP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de proceso actual de PHP, o `false` en caso de error.

## Notas

> [!WARNING]
> Los identificadores de proceso no son únicos, y constituyen una fuente de entropía baja. Se recomienda no utilizar los pid para garantizar la seguridad de un sistema.

## Véase también

`getmygid`, `getmyuid`, `get_current_user`, `getmyinode`, `getlastmod`
