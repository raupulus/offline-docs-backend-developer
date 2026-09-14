---
title: sodium_crypto_auth
description: Calcula una etiqueta para el mensaje
source_url: https://www.php.net/manual/es/function.sodium-crypto-auth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-auth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76220
---

sodium_crypto_auth

Calcula una etiqueta para el mensaje

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_auth(string $message, string $key): string
```php

El mensaje de autenticación simétrica a través de `sodium_crypto_auth` proporciona integridad, pero no confidencialidad.

A diferencia de las firmas digitales (por ejemplo `sodium_crypto_sign_detached`), cualquier parte capaz de verificar un mensaje también es capaz de autenticar sus propios mensajes. (De ahí, la autenticación simétrica.)

## Parámetros

`message`  
El mensaje que se desea autenticar

`key`  
La clave de autenticación

## Valores devueltos

La clave de autenticación
