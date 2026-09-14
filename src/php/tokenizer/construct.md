---
title: PhpToken::__construct
description: Devuelve un nuevo objeto PhpToken
source_url: https://www.php.net/manual/es/phptoken.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 0e51e26bd
order: 94370
---

PhpToken::\_\_construct

Devuelve un nuevo objeto PhpToken

## Descripción

```php
final public PhpToken::__construct(int $id, string $text, [int $line], [int $pos])
```php

Devuelve un nuevo objeto PhpToken

## Parámetros

`id`  
Una de las constantes T\_\* (ver [???](#tokens)), o un codepoint ASCII que representa un token de un solo carácter.

`text`  
El contenido textual del token.

`line`  
El número de línea (a partir de 1) del token.

`pos`  
La posición de inicio (a partir de 0) en la cadena tokenizada (el número de bytes).

## Véase también

PhpToken::tokenize
