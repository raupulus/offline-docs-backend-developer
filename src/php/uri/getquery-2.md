---
title: Uri\WhatWg\Url::getQuery
description: Recupera el componente de consulta
source_url: https://www.php.net/manual/es/uri-whatwg-url.getquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: df78bd1d2
order: 99900
---

Uri\WhatWg\Url::getQuery

Recupera el componente de consulta

## Descripción

```php
public Uri\WhatWg\Url::getQuery(): string
```php

Recupera el componente de consulta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de consulta como un `string` si el componente de consulta existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getQuery

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com?foo/bar");

echo $url->getQuery();
?>

   
```php

El ejemplo anterior mostrará:

    foo/bar

## Véase también

Uri\WhatWg\Url::withQuery

Uri\Rfc3986\Uri::getRawQuery

Uri\Rfc3986\Uri::getQuery
