---
title: PhpToken::__toString
description: Devuelve el contenido textual del token.
source_url: https://www.php.net/manual/es/phptoken.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken/toString.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 0e51e26bd
order: 94410
---

PhpToken::\_\_toString

Devuelve el contenido textual del token.

## Descripción

```php
public PhpToken::__toString(): string
```php

Devuelve el contenido textual del token.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El contenido textual del token.

## Ejemplos

Ejemplo de `PhpToken::__toString`

```
<?php
$token = new PhpToken(T_ECHO, 'echo');
echo $token;

   
```php

Los ejemplos anteriores mostrarán:

    echo

## Véase también

token_name
