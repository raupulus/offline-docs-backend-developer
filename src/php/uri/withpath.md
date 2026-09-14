---
title: Uri\Rfc3986\Uri::withPath
description: Modifica el componente de ruta
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99760
---

Uri\Rfc3986\Uri::withPath

Modifica el componente de ruta

## Descripción

```php
public Uri\Rfc3986\Uri::withPath(string $path): static
```php

Crea una nueva URI y modifica su componente de ruta.

## Parámetros

`path`  
Nuevo componente de ruta.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withPath

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com/foo/bar");
$uri = $uri->withPath("/baz");

echo $uri->getPath();
?>

   
```php

El ejemplo anterior mostrará:

    /baz

## Véase también

Uri\Rfc3986\Uri::getPath

Uri\Rfc3986\Uri::getRawPath

Uri\WhatWg\Url::withPath
