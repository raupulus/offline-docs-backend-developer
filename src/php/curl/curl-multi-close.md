---
title: curl_multi_close
description: Eliminar todos los gestores cURL de un gestor múltiple
source_url: https://www.php.net/manual/es/function.curl-multi-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9920
---

curl_multi_close

Eliminar todos los gestores cURL de un gestor múltiple

## Descripción

```php
curl_multi_close(CurlMultiHandle $multi_handle): void
```php

Elimina todos los `CurlHandle`s adjuntos al `CurlMultiHandle`, como si `curl_multi_remove_handle` hubiera sido llamado para cada uno de ellos.

Antes de PHP 8.0.0, esta función también cerraba el recurso de gestor múltiple cURL, dejándolo inutilizable.

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

`curl_multi_init`
