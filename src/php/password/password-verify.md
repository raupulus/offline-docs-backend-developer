---
title: password_verify
description: Verifica que una contraseña coincide con un hash
source_url: https://www.php.net/manual/es/function.password-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/functions/password-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_reviewed: false
translation_revision: 5baba54a6
order: 61130
---

password_verify

Verifica que una contraseña coincide con un hash

## Descripción

```php
#[\SensitiveParameter] password_verify(string $password, string $hash): bool
```php

Verifica que el hash proporcionado coincide con la contraseña proporcionada. La función `password_verify` es compatible con la función `crypt`. Por lo tanto, una contraseña hasheada por la función `crypt` puede ser utilizada con la función `password_verify`.

Tenga en cuenta que la función `password_hash` devuelve el algoritmo, el "cost", y el salt como partes del hash devuelto. Sin embargo, toda la información necesaria para verificar el hash está incluida. Esto permite a la función verificar el hash sin necesidad de almacenamiento separado para la información concerniente al algoritmo y al salt.

Esta función es segura contra ataques por tiempo.

## Parámetros

`password`  
La contraseña del usuario.

`hash`  
Un hash creado por la función `password_hash`.

## Valores devueltos

Devuelve `true` si la contraseña y el hash coinciden, o `false` en caso contrario.

## Ejemplos

Ejemplo con `password_verify`

Este es un ejemplo simplificado; se recomienda re-hashear una contraseña correcta si es necesario; ver la función `password_needs_rehash` para un ejemplo.

```
<?php
// Ver el ejemplo proporcionado en la página de la función password_hash()
// para saber de dónde proviene esto.
$hash = '$2y$12$4Umg0rCJwMswRw/l.SwHvuQV01coP0eWmGzd61QH2RvAOMANUBGC.';

if (password_verify('rasmuslerdorf', $hash)) {
    echo 'La contraseña es válida !';
} else {
    echo 'La contraseña es inválida.';
}
?>

    
```php

El ejemplo anterior mostrará:

    La contraseña es válida !

## Véase también

`password_needs_rehash`, `password_hash`, `sodium_crypto_pwhash_str_verify`
