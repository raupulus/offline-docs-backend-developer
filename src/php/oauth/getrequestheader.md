---
title: OAuth::getRequestHeader
description: Genera una firma de encabezado OAuth
source_url: https://www.php.net/manual/es/oauth.getrequestheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/getrequestheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56800
---

OAuth::getRequestHeader

Genera una firma de encabezado OAuth

## Descripción

```php
public OAuth::getRequestHeader(string $http_method, string $url, [mixed $extra_parameters]): string
```php

Genera una firma de encabezado OAuth basada en el método HTTP final, así como en la URL y sus parámetros.

## Parámetros

`http_method`  
Método HTTP para la petición.

`url`  
URL de la petición.

`extra_parameters`  
Parámetros adicionales (`string` o array).

## Valores devueltos

Un `string` que contiene el encabezado generado de la petición o `false` si ocurre un error
