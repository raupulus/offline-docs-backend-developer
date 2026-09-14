---
title: phpdbg_break_method
description: Inserta un punto de interrupción en la entrada de un método
source_url: https://www.php.net/manual/es/function.phpdbg-break-method.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phpdbg/functions/phpdbg-break-method.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phpdbg
translation_status: ready
translation_reviewed: false
translation_revision: 06f14554e
order: 64970
---

phpdbg_break_method

Inserta un punto de interrupción en la entrada de un método

## Descripción

```php
phpdbg_break_method(string $class, string $method): void
```php

Inserta un punto de interrupción en la entrada del método `method` de la clase `class`.

## Parámetros

`class`  
El nombre de la clase.

`method`  
El nombre del método.

## Valores devueltos

No se retorna ningún valor.

## Véase también

phpdbg_break_file

phpdbg_break_function

phpdbg_break_next

phpdbg_clear
