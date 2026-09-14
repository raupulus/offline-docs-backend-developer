---
title: Uri\Rfc3986\Uri::withQuery
description: Modifica el componente de consulta
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99780
---

Uri\Rfc3986\Uri::withQuery

Modifica el componente de consulta

## Descripción

```php
public Uri\Rfc3986\Uri::withQuery(string $query): static
```php

Crea una nueva URI y modifica su componente de consulta.

## Parámetros

`query`  
Nuevo componente de consulta.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withQuery

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com?foo=bar");
$uri = $uri->withQuery("foo=baz");

echo $uri->getQuery();
?>

   
```php

El ejemplo anterior mostrará:

    foo=baz

## Véase también

Uri\Rfc3986\Uri::getRawQuery

Uri\Rfc3986\Uri::getQuery

Uri\WhatWg\Url::withQuery
