---
title: OAuth::generateSignature
description: Genera una firma
source_url: https://www.php.net/manual/es/oauth.generatesignature.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/generatesignature.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56740
---

OAuth::generateSignature

Genera una firma

## Descripción

```php
public OAuth::generateSignature(string $http_method, string $url, [mixed $extra_parameters]): string
```php

Genera una firma basada en el método HTTP final, la URL y una cadena/array de parámetros.

## Parámetros

`http_method`  
Método HTTP para la petición.

`url`  
URL de la petición.

`extra_parameters`  
Cadena o array de parámetros adicionales.

## Valores devueltos

Una cadena que contiene la firma generada o `false` si ocurre un error
