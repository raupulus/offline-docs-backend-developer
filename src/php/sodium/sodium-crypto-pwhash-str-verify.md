---
title: sodium_crypto_pwhash_str_verify
description: Verifica que una contraseña corresponde a un hash
source_url: https://www.php.net/manual/es/function.sodium-crypto-pwhash-str-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-pwhash-str-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76630
---

sodium_crypto_pwhash_str_verify

Verifica que una contraseña corresponde a un hash

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_pwhash_str_verify(string $hash, string $password): bool
```php

Verifica que un hash de contraseña creado utilizando `sodium_crypto_pwhash_str` corresponde a una contraseña en texto claro dada. Tenga en cuenta que los argumentos están en el orden inverso de los mismos argumentos en la función similar `password_verify`.

## Parámetros

`hash`  
Un hash creado por la función `password_hash`.

`password`  
La contraseña del usuario.

## Valores devueltos

Devuelve `true` si la contraseña y el hash coinciden, o `false` en caso contrario.

## Notas

> [!NOTE]
> Los hashes se calculan utilizando el algoritmo Argon2ID, proporcionando resistencia tanto a los ataques GPU como a los ataques por canales laterales.

## Véase también

sodium_crypto_pwhash_str

password_hash

password_verify
