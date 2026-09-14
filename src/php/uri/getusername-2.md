---
title: Uri\WhatWg\Url::getUsername
description: Recupera el componente de nombre de usuario
source_url: https://www.php.net/manual/es/uri-whatwg-url.getusername.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getusername.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99930
---

Uri\WhatWg\Url::getUsername

Recupera el componente de nombre de usuario

## Descripción

```php
public Uri\WhatWg\Url::getUsername(): string
```php

Recupera el componente de nombre de usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de nombre de usuario como un `string` si el componente de nombre de usuario existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getUsername

```
<?php
$url = new \Uri\WhatWg\Url("https://username:password@example.com");

echo $url->getUsername();
?>

   
```php

El ejemplo anterior mostrará:

    username

## Véase también

Uri\WhatWg\Url::withUsername

Uri\Rfc3986\Uri::getRawUsername

Uri\Rfc3986\Uri::getUsername
