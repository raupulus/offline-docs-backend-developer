---
title: Uri\WhatWg\Url::getScheme
description: Recupera el componente de esquema
source_url: https://www.php.net/manual/es/uri-whatwg-url.getscheme.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getscheme.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99910
---

Uri\WhatWg\Url::getScheme

Recupera el componente de esquema

## Descripción

```php
public Uri\WhatWg\Url::getScheme(): string
```php

Recupera el componente de esquema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de esquema como un `string` si el componente de esquema existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getScheme

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com");

echo $url->getScheme();
?>

   
```php

El ejemplo anterior mostrará:

    https

## Véase también

Uri\WhatWg\Url::withScheme

Uri\Rfc3986\Uri::getRawScheme

Uri\Rfc3986\Uri::getScheme
