---
title: OAuth::disableSSLChecks
description: Desactiva la verificación SSL
source_url: https://www.php.net/manual/es/oauth.disablesslchecks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/disablesslchecks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: true
translation_revision: bdee7e8c1
order: 56690
---

OAuth::disableSSLChecks

Desactiva la verificación SSL

## Descripción

```php
public OAuth::disableSSLChecks(): bool
```php

Desactiva las verificaciones de certificados y de hosts SSL (activado por omisión). Se recomienda no utilizar esta función en producción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true`

## Historial de cambios

| Versión           | Descripción                        |
|-------------------|------------------------------------|
| PECL oauth 0.99.8 | Se ha añadido la propiedad `debug` |

## Véase también

OAuth::enableSSLChecks
