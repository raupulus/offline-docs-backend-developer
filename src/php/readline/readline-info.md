---
title: readline_info
description: Lee o modifica diversas variables internas de readline
source_url: https://www.php.net/manual/es/function.readline-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: 53208f9bd
order: 68770
---

readline_info

Lee o modifica diversas variables internas de readline

## Descripción

```php
readline_info([string $var_name], [int $value]): mixed
```php

Lee/modifica diversas variables internas.

## Parámetros

`var_name`  
Un nombre de variable.

`value`  
Si se proporciona, será el nuevo valor a definir.

## Valores devueltos

Cuando se invoca sin parámetros, `readline_info` devuelve un array que contiene los valores de los parámetros de Readline. Los elementos estarán indexados por las claves siguientes : `"done"`, `"end"`, `"erase_empty_line"`, `"library_version"`, `"line_buffer"`, `"mark"`, `"pending_input"`, `"point"`, `"prompt"`, `"readline_name"` y `"terminal_name"`. El `array` solo contendrá los elementos que sean soportados por la biblioteca utilizada para construir la extensión readline.

Si se invoca con uno o dos parámetros, se devuelve el valor anterior.

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 8.0.0   | `var_name` y `value` ahora son nullable. |
