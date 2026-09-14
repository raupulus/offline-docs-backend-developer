---
title: Uri\Rfc3986\Uri::getQuery
description: Recupera el componente de consulta normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: c5ff5efb9
order: 99560
---

Uri\Rfc3986\Uri::getQuery

Recupera el componente de consulta normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getQuery(): string
```php

Recupera el componente de consulta normalizado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de consulta normalizado como un `string` si el componente de consulta existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getQuery

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com?foo=bar");

echo $uri->getQuery();
?>

   
```php

El ejemplo anterior mostrará:

    foo=bar

## Véase también

Uri\Rfc3986\Uri::getRawQuery

Uri\Rfc3986\Uri::withQuery

Uri\WhatWg\Url::getQuery
