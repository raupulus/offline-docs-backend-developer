---
title: OAuthProvider::callTimestampNonceHandler
description: Llama al callback timestampNonceHandler
source_url: https://www.php.net/manual/es/oauthprovider.calltimestampnoncehandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/calltimestampnoncehandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56950
---

OAuthProvider::callTimestampNonceHandler

Llama al callback timestampNonceHandler

## Descripción

```php
public OAuthProvider::callTimestampNonceHandler(): void
```php

Llama a la función callback del timestamp registrado, que fue establecido con OAuthProvider::timestampNonceHandler.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Emite un error `E_ERROR` si la función de devolución de llamada no puede ser llamada o no ha sido especificada.

## Véase también

OAuthProvider::timestampNonceHandler
