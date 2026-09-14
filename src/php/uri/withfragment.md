---
title: Uri\Rfc3986\Uri::withFragment
description: Modifica el componente de fragmento
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99740
---

Uri\Rfc3986\Uri::withFragment

Modifica el componente de fragmento

## Descripción

```php
public Uri\Rfc3986\Uri::withFragment(string $fragment): static
```php

Crea una nueva URI y modifica su componente de fragmento.

## Parámetros

`fragment`  
Nuevo componente de fragmento.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withFragment

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com/#foo");
$uri = $uri->withFragment("bar");

echo $uri->getFragment();
?>

   
```php

El ejemplo anterior mostrará:

    bar

## Véase también

Uri\Rfc3986\Uri::getFragment

Uri\Rfc3986\Uri::getRawFragment

Uri\WhatWg\Url::withFragment
