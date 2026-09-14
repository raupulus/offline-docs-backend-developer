---
title: Uri\WhatWg\Url::equals
description: Verifica si dos URLs son equivalentes
source_url: https://www.php.net/manual/es/uri-whatwg-url.equals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/equals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99840
---

Uri\WhatWg\Url::equals

Verifica si dos URLs son equivalentes

## Descripción

```php
public Uri\WhatWg\Url::equals(Uri\WhatWg\Url $url, [Uri\UriComparisonMode $comparisonMode]): bool
```php

Verifica si dos URLs son equivalentes.

## Parámetros

`url`  
URL con la que comparar la URL actual.

`comparisonMode`  
Indica si el componente de fragmento se tiene en cuenta en la comparación (`Uri\UriComparisonMode::IncludeFragment`) o no (`Uri\UriComparisonMode::ExcludeFragment`). Por defecto, el fragmento se excluye.

## Valores devueltos

Devuelve `true` si las dos URLs son equivalentes, o `false` en caso contrario.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::equals

```
<?php
$url1 = new \Uri\WhatWg\Url("https://example.com");
$url2 = new \Uri\WhatWg\Url("HTTPS://example.com");

var_dump($url1->equals($url2));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

Uri\Rfc3986\Uri::equals
