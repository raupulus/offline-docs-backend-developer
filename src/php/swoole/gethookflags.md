---
title: Swoole\Runtime::getHookFlags
description: Obtiene los flags de hook actuales
source_url: https://www.php.net/manual/es/swoole-runtime.get-hook-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/runtime/getHookFlags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: f03cb84c3
order: 92470
---

Swoole\Runtime::getHookFlags

Obtiene los flags de hook actuales

## Descripción

```php
public static Swoole\Runtime::getHookFlags(): int
```php

Obtiene los flags de hook actuales. Tenga en cuenta que los flags devueltos pueden diferir de lo que se estableció si algunos hooks fallaron.

## Parámetros

Esta función no tiene parámetros.

## Valores devueltos

Devuelve los flags de hook actuales como una máscara de bits.
