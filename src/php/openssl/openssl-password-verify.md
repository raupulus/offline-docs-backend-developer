---
title: openssl_password_verify
description: Verifica una contraseña frente a un hash usando la implementación de
  Argon2 de OpenSSL
source_url: https://www.php.net/manual/es/function.openssl-password-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-password-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_revision: 29cecd7f1
order: 59260
---

openssl_password_verify

Verifica una contraseña frente a un hash usando la implementación de Argon2 de OpenSSL

## Descripción

```php
openssl_password_verify(string $algo, string $password, string $hash): bool
```php

Verifica que una contraseña coincida con un hash creado por `openssl_password_hash`.

Esta función solo está disponible cuando PHP se compila con soporte de OpenSSL que incluye Argon2 (`HAVE_OPENSSL_ARGON2`).

## Parámetros

`algo`  
El algoritmo de hash de contraseña. Valores soportados: `"argon2id"` y `"argon2i"`.

`password`  
La contraseña del usuario.

`hash`  
Un hash creado por `openssl_password_hash`.

## Valores devueltos

Devuelve `true` si la contraseña y el hash coinciden, `false` en caso contrario.

## Errores/Excepciones

Lanza un `ValueError` si `algo` no es uno de los valores soportados (`"argon2i"` o `"argon2id"`).

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.4.0   | Se ha añadido la función. |

## Ejemplos

Ejemplo con `openssl_password_verify`

```
<?php
$hash = openssl_password_hash('argon2id', 'my-secret-password');

if (openssl_password_verify('argon2id', 'my-secret-password', $hash)) {
    echo 'La contraseña coincide.';
} else {
    echo 'La contraseña no coincide.';
}
?>

   
```php

## Véase también

`openssl_password_hash`, `password_verify`
