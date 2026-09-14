---
title: readline_add_history
description: Se añade una línea al historial
source_url: https://www.php.net/manual/es/function.readline-add-history.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-add-history.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: be246a268
order: 68710
---

readline_add_history

Se añade una línea al historial

## Descripción

```php
readline_add_history(string $prompt): true
```php

Se añade una línea al historial.

## Parámetros

`prompt`  
La línea a añadir al historial.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.5.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
