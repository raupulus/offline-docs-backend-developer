---
title: OAuth::getLastResponseInfo
description: Obtiene la información HTTP sobre la última respuesta
source_url: https://www.php.net/manual/es/oauth.getlastresponseinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/getlastresponseinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56790
---

OAuth::getLastResponseInfo

Obtiene la información HTTP sobre la última respuesta

## Descripción

```php
public OAuth::getLastResponseInfo(): array
```php

Obtiene la información HTTP sobre la última respuesta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array conteniendo la información de respuesta de la última petición. Constantes de `curl_getinfo` pueden ser usadas.

## Véase también

OAuth::fetch

OAuth::getLastResponse
