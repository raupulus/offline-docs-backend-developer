---
title: OAuth::getCAPath
description: Obtiene la información CA
source_url: https://www.php.net/manual/es/oauth.getcapath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/getcapath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56760
---

OAuth::getCAPath

Obtiene la información CA

## Descripción

```php
public OAuth::getCAPath(): array
```php

Obtiene la información del certificado de Autoridad, el cual incluye los ca_path y ca_info establecidos por OAuth::setCaPath.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` con información del Certificado de Autoridad, específicamente como claves `ca_path` y `ca_info` dentro del array asociativo devuelto.

## Véase también

OAuth::setCAPath

OAuth::getLastResponseInfo
