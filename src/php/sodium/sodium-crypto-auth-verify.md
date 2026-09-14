---
title: sodium_crypto_auth_verify
description: Verifica que la etiqueta es válida para el mensaje
source_url: https://www.php.net/manual/es/function.sodium-crypto-auth-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-auth-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76210
---

sodium_crypto_auth_verify

Verifica que la etiqueta es válida para el mensaje

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_auth_verify(string $mac, string $message, string $key): bool
```php

Verifica que la etiqueta es válida para un mensaje y una clave dados.

A diferencia de las firmas digitales (por ejemplo `sodium_crypto_sign_verify_detached`), cualquier parte capaz de verificar un mensaje también es capaz de autenticar sus propios mensajes. (De ahí, la autenticación simétrica.)

## Parámetros

`mac`  
Etiqueta de autenticación producida por `sodium_crypto_auth`

`message`  
Mensaje

`key`  
La clave de autenticación

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
