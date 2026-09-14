---
title: Swoole\Runtime::setHookFlags
description: Establece los flags de hook para corrutinas
source_url: https://www.php.net/manual/es/swoole-runtime.set-hook-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/runtime/setHookFlags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: f03cb84c3
order: 92480
---

Swoole\Runtime::setHookFlags

Establece los flags de hook para corrutinas

## Descripción

```php
public static Swoole\Runtime::setHookFlags(int $flags): bool
```php

Establece los flags de hook para el soporte de corrutinas. Esto cambia dinámicamente los flags de hook en tiempo de ejecución.

## Parámetros

`flags`  
Máscara de bits de flags que especifica qué funciones se deben hookear. Los mismos flags que enableCoroutine.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
