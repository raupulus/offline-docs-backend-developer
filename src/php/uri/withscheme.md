---
title: Uri\Rfc3986\Uri::withScheme
description: Modifica el componente de esquema
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withscheme.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withscheme.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99790
---

Uri\Rfc3986\Uri::withScheme

Modifica el componente de esquema

## Descripción

```php
public Uri\Rfc3986\Uri::withScheme(string $scheme): static
```php

Crea una nueva URI y modifica su componente de esquema.

## Parámetros

`scheme`  
Nuevo componente de esquema.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withScheme

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com");
$uri = $uri->withScheme("http");

echo $uri->getScheme();
?>

   
```php

El ejemplo anterior mostrará:

    http

## Véase también

Uri\Rfc3986\Uri::getRawScheme

Uri\Rfc3986\Uri::getScheme

Uri\WhatWg\Url::withScheme
