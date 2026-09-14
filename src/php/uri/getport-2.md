---
title: Uri\WhatWg\Url::getPort
description: Recupera el componente de puerto
source_url: https://www.php.net/manual/es/uri-whatwg-url.getport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: a00f03a61
order: 99890
---

Uri\WhatWg\Url::getPort

Recupera el componente de puerto

## Descripción

```php
public Uri\WhatWg\Url::getPort(): int
```php

Recupera el componente de puerto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de puerto como un `int` si el componente de puerto existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getPort

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com:443");

echo $url->getPort();
?>

   
```php

El ejemplo anterior mostrará:

    443

## Véase también

Uri\WhatWg\Url::withPort

Uri\Rfc3986\Uri::getPort
