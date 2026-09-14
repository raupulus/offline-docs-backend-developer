---
title: Parle\RLexer::callout
description: Define una función de retrollamada de token
source_url: https://www.php.net/manual/es/parle-rlexer.callout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/rlexer/callout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 0dad2268d
order: 60690
---

Parle\RLexer::callout

Define una función de retrollamada de token

## Descripción

```php
public Parle\RLexer::callout(int $id, callable $callback): void
```php

Define una función de retrollamada a invocar una vez que el lexer encuentre un token particular.

## Parámetros

`id`  
El identificador del token.

`callback`  
La función de retrollamada a invocar. La función de retrollamada no recibe ningún argumento y su valor de retorno es ignorado.

## Valores devueltos

No se retorna ningún valor.
