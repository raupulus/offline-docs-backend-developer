---
title: Parle\Lexer::callout
description: Define una función de retrollamada de token
source_url: https://www.php.net/manual/es/parle-lexer.callout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/lexer/callout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 0dad2268d
order: 60420
---

Parle\Lexer::callout

Define una función de retrollamada de token

## Descripción

```php
public Parle\Lexer::callout(int $id, callable $callback): void
```php

Define una función de retrollamada a invocar una vez que el lexer encuentre un token particular.

## Parámetros

`id`  
El identificador del token.

`callback`  
La función de retrollamada a invocar. La función de retrollamada no recibe ningún argumento y su valor de retorno es ignorado.

## Valores devueltos

No se retorna ningún valor.
