---
title: Uri\WhatWg\Url::getFragment
description: Recupera el componente de fragmento
source_url: https://www.php.net/manual/es/uri-whatwg-url.getfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99860
---

Uri\WhatWg\Url::getFragment

Recupera el componente de fragmento

## Descripción

```php
public Uri\WhatWg\Url::getFragment(): string
```php

Recupera el componente de fragmento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de fragmento como un `string` si el componente de fragmento existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getFragment

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com#foo");

echo $url->getFragment();
?>

   
```php

El ejemplo anterior mostrará:

    foo

## Véase también

Uri\WhatWg\Url::withFragment

Uri\Rfc3986\Uri::getRawFragment

Uri\Rfc3986\Uri::getFragment
