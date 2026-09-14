---
title: Uri\WhatWg\Url::getPath
description: Recupera el componente de ruta
source_url: https://www.php.net/manual/es/uri-whatwg-url.getpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99880
---

Uri\WhatWg\Url::getPath

Recupera el componente de ruta

## Descripción

```php
public Uri\WhatWg\Url::getPath(): string
```php

Recupera el componente de ruta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de ruta como un `string`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getPath

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com/foo/bar");

echo $url->getPath();
?>

   
```php

El ejemplo anterior mostrará:

    /foo/bar

## Véase también

Uri\WhatWg\Url::withPath

Uri\Rfc3986\Uri::getRawPath

Uri\Rfc3986\Uri::getPath
