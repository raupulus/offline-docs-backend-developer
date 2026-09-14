---
title: phpdbg_exec
description: Intenta definir el contexto de ejecución
source_url: https://www.php.net/manual/es/function.phpdbg-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phpdbg/functions/phpdbg-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phpdbg
translation_status: ready
translation_reviewed: false
translation_revision: 06f14554e
order: 65020
---

phpdbg_exec

Intenta definir el contexto de ejecución

## Descripción

```php
phpdbg_exec(string $context): string
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`context`  

## Valores devueltos

Si el contexto de ejecución ha sido definido con éxito, este contexto será devuelto. Si el contexto de ejecución no ha sido definido, `true` será devuelto. Si un error ha ocurrido durante la definición del contexto, `false` será devuelto y un error de nivel `E_WARNING` será emitido.
