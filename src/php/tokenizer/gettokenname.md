---
title: PhpToken::getTokenName
description: Devuelve el nombre del token.
source_url: https://www.php.net/manual/es/phptoken.gettokenname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken/getTokenName.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 0e51e26bd
order: 94380
---

PhpToken::getTokenName

Devuelve el nombre del token.

## Descripción

```php
public PhpToken::getTokenName(): string
```php

Devuelve el nombre del token.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un carácter ASCII para los tokens de un solo carácter, o una de las constantes T\_\* para los tokens conocidos (ver [???](#tokens)), o `null` para los tokens desconocidos.

## Ejemplos

Ejemplo de `PhpToken::getTokenName`

```
<?php
// token conocido
$token = new PhpToken(T_ECHO, 'echo');
var_dump($token->getTokenName());   // -> string(6) "T_ECHO"

// token de un solo carácter
$token = new PhpToken(ord(';'), ';');
var_dump($token->getTokenName());   // -> string(1) ";"

// token desconocido
$token = new PhpToken(10000 , "\0");
var_dump($token->getTokenName());   // -> NULL

   
```php

## Véase también

PhpToken::tokenize

token_name
