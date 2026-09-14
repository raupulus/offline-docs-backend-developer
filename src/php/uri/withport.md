---
title: Uri\Rfc3986\Uri::withPort
description: Modifica el componente de puerto
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99770
---

Uri\Rfc3986\Uri::withPort

Modifica el componente de puerto

## Descripción

```php
public Uri\Rfc3986\Uri::withPort(int $port): static
```php

Crea una nueva URI y modifica su componente de puerto.

## Parámetros

`port`  
Nuevo componente de puerto.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withPort

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com:8080");
$uri = $uri->withPort(443);

echo $uri->getPort();
?>

   
```php

El ejemplo anterior mostrará:

    443

## Véase también

Uri\Rfc3986\Uri::getPort

Uri\WhatWg\Url::withPort
