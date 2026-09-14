---
title: phpdbg_color
description: Define el color de ciertos elementos
source_url: https://www.php.net/manual/es/function.phpdbg-color.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phpdbg/functions/phpdbg-color.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phpdbg
translation_status: ready
translation_reviewed: false
translation_revision: 06f14554e
order: 65000
---

phpdbg_color

Define el color de ciertos elementos

## Descripción

```php
phpdbg_color(int $element, string $color): void
```php

Define el color `color` para el elemento `element`.

## Parámetros

`element`  
Una de las constantes `PHPDBG_COLOR_*`.

`color`  
El nombre del color. Puede ser `white`, `red`, `green`, `yellow`, `blue`, `purple`, `cyan` o `black`, y, opcionalmente, con los complementos `-bold` o `-underline`; por ejemplo `white-bold` o `green-underline`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

phpdbg_prompt
