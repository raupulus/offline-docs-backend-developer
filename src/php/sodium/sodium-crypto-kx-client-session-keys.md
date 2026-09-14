---
title: sodium_crypto_kx_client_session_keys
description: Calcula las claves de sesión del lado del cliente.
source_url: https://www.php.net/manual/es/function.sodium-crypto-kx-client-session-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-kx-client-session-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76530
---

sodium_crypto_kx_client_session_keys

Calcula las claves de sesión del lado del cliente.

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_kx_client_session_keys(string $client_key_pair, string $server_key): array
```php

Calcula las claves de sesión del lado del cliente, utilizando el método de intercambio de claves X25519 + BLAKE2b.

## Parámetros

`client_key_pair`  
Un par de claves crypto_kx, como las generadas por `sodium_crypto_kx_keypair`.

`server_key`  
Una clave pública crypto_kx.

## Valores devueltos

Un array compuesto de dos strings. La primera debe ser utilizada para recibir datos del servidor. La segunda debe ser utilizada para enviar datos al servidor.
