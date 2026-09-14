---
title: Uri\Rfc3986\Uri::withHost
description: Modifica el componente de host
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withhost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withhost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99750
---

Uri\Rfc3986\Uri::withHost

Modifica el componente de host

## Descripción

```php
public Uri\Rfc3986\Uri::withHost(string $host): static
```php

Crea una nueva URI y modifica su componente de host.

## Parámetros

`host`  
Nuevo componente de host.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withHost

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com");
$uri = $uri->withHost("example.net");

echo $uri->getHost();
?>

   
```php

El ejemplo anterior mostrará:

    example.net

## Véase también

Uri\Rfc3986\Uri::getHost

Uri\Rfc3986\Uri::getRawHost

Uri\WhatWg\Url::withHost
