---
title: PhpToken::is
description: Indica si el token es de un tipo dado.
source_url: https://www.php.net/manual/es/phptoken.is.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken/is.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 0e51e26bd
order: 94390
---

PhpToken::is

Indica si el token es de un tipo dado.

## Descripción

```php
public PhpToken::is(int $kind): bool
```php

Indica si el token es de un tipo (`kind`) dado.

## Parámetros

`kind`  
Un valor único para coincidir con el id o el contenido textual del token, o un array de estos valores.

## Valores devueltos

Un valor bool que indica si el token es del tipo dado.

## Ejemplos

Ejemplo de`PhpToken::is`

```
<?php
$token = new PhpToken(T_ECHO, 'echo');
var_dump($token->is(T_ECHO));        // -> bool(true)
var_dump($token->is('echo'));        // -> bool(true)
var_dump($token->is(T_FOREACH));     // -> bool(false)
var_dump($token->is('foreach'));     // -> bool(false)

   
```php

Uso con array

```
<?php
function isClassType(PhpToken $token): bool {
    return $token->is([T_CLASS, T_INTERFACE, T_TRAIT]);
}

$interface = new PhpToken(T_INTERFACE, 'interface');
var_dump(isClassType($interface));   // -> bool(true)

$function = new PhpToken(T_FUNCTION, 'function');
var_dump(isClassType($function));    // -> bool(false)

   
```php

## Véase también

token_name
