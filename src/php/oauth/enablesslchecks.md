---
title: OAuth::enableSSLChecks
description: Activa la verificación SSL
source_url: https://www.php.net/manual/es/oauth.enablesslchecks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/enablesslchecks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: true
translation_revision: bdee7e8c1
order: 56720
---

OAuth::enableSSLChecks

Activa la verificación SSL

## Descripción

```php
public OAuth::enableSSLChecks(): bool
```php

Activa las verificaciones de certificados y de hosts SSL (activado por omisión). Alternativamente, la propiedad [sslChecks](#oauth.props.sslchecks) puede ser definida sobre un valor diferente de `false` para activar las verificaciones SSL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true`

## Historial de cambios

| Versión           | Descripción                          |
|-------------------|--------------------------------------|
| PECL oauth 0.99.8 | La propiedad `debug` ha sido añadida |

## Véase también

OAuth::disableSSLChecks
