---
title: phpdbg_break_file
description: Inserta un punto de interrupción en una línea de un fichero
source_url: https://www.php.net/manual/es/function.phpdbg-break-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phpdbg/functions/phpdbg-break-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phpdbg
translation_status: ready
translation_reviewed: false
translation_revision: 06f14554e
order: 64950
---

phpdbg_break_file

Inserta un punto de interrupción en una línea de un fichero

## Descripción

```php
phpdbg_break_file(string $file, int $line): void
```php

Inserta un punto de interrupción en la línea `line` en el fichero `file`.

## Parámetros

`file`  
El nombre del fichero.

`line`  
El número de la línea.

## Valores devueltos

No se retorna ningún valor.

## Véase también

phpdbg_break_function

phpdbg_break_method

phpdbg_break_next

phpdbg_clear
