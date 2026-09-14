---
title: ps_continue_text
description: Continuar el texto en la siguiente línea
source_url: https://www.php.net/manual/es/function.ps-continue-text.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-continue-text.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65710
---

ps_continue_text

Continuar el texto en la siguiente línea

## Descripción

```php
ps_continue_text(resource $psdoc, string $text): bool
```php

Imprime un texto una línea por debajo de la última línea. La interlínea se toma del valor "leading", el cual debe establecerse con la función `ps_set_value`. La posición actual del texto se determina por los valores "textx" y "texty", los cuales pueden solicitarse con la función `ps_get_value`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto a imprimir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_show`, `ps_show_xy`, `ps_show_boxed`
