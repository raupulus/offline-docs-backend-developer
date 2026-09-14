---
title: readline_read_history
description: Lee el historial
source_url: https://www.php.net/manual/es/function.readline-read-history.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-read-history.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: 53208f9bd
order: 68800
---

readline_read_history

Lee el historial

## Descripción

```php
readline_read_history([string $filename]): bool
```php

Lee una línea del historial desde el fichero `filename`.

## Parámetros

`filename`  
Ruta de acceso al fichero que contiene el historial de comandos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `filename` ahora es nullable. |
