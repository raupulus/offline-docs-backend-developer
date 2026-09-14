---
title: OAuth::setTimestamp
description: Define el timestamp
source_url: https://www.php.net/manual/es/oauth.settimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/settimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56880
---

OAuth::setTimestamp

Define el timestamp

## Descripción

```php
public OAuth::setTimestamp(string $timestamp): mixed
```php

Define el timestamp OAuth para las próximas peticiones.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`timestamp`  
El timestamp.

## Valores devueltos

Retorna `true`, o `false` si `timestamp` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |

## Véase también

OAuth::setNonce
