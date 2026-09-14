---
title: Uri\Rfc3986\Uri::getPort
description: Recupera el componente de puerto normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: c5ff5efb9
order: 99550
---

Uri\Rfc3986\Uri::getPort

Recupera el componente de puerto normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getPort(): int
```php

Recupera el componente de puerto normalizado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de puerto normalizado como un `int` si el componente de puerto existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getPort

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com:443");

echo $uri->getPort();
?>

   
```php

El ejemplo anterior mostrará:

    443

## Véase también

Uri\Rfc3986\Uri::withPort

Uri\WhatWg\Url::getPort
