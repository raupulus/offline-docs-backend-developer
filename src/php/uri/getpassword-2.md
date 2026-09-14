---
title: Uri\WhatWg\Url::getPassword
description: Recupera el componente de contraseña
source_url: https://www.php.net/manual/es/uri-whatwg-url.getpassword.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getpassword.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99870
---

Uri\WhatWg\Url::getPassword

Recupera el componente de contraseña

## Descripción

```php
public Uri\WhatWg\Url::getPassword(): string
```php

Recupera el componente de contraseña.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de contraseña como un `string` si el componente de contraseña existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getPassword

```
<?php
$url = new \Uri\WhatWg\Url("https://user:password@example.com");

echo $url->getPassword();
?>

   
```php

El ejemplo anterior mostrará:

    password

## Véase también

Uri\WhatWg\Url::withPassword

Uri\Rfc3986\Uri::getRawPassword

Uri\Rfc3986\Uri::getPassword
