---
title: PhpToken::isIgnorable
description: Indica si el token será ignorado por el analizador PHP.
source_url: https://www.php.net/manual/es/phptoken.isignorable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken/isIgnorable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 0e51e26bd
order: 94400
---

PhpToken::isIgnorable

Indica si el token será ignorado por el analizador PHP.

## Descripción

```php
public PhpToken::isIgnorable(): bool
```php

Indica si el token será ignorado por el analizador PHP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un valor booleano que indica si el token será ignorado por el analizador PHP (como los espacios o los comentarios).

## Ejemplos

Ejemplo de `PhpToken::isIgnorable`

```
<?php
$echo = new PhpToken(T_ECHO, 'echo');
var_dump($echo->isIgnorable());   // -> bool(false)

$space = new PhpToken(T_WHITESPACE, ' ');
var_dump($space->isIgnorable());  // -> bool(true)

   
```php

## Véase también

PhpToken::tokenize
