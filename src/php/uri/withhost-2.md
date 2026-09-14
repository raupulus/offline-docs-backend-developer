---
title: Uri\WhatWg\Url::withHost
description: Modifica el componente de host
source_url: https://www.php.net/manual/es/uri-whatwg-url.withhost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withhost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100010
---

Uri\WhatWg\Url::withHost

Modifica el componente de host

## Descripción

```php
public Uri\WhatWg\Url::withHost(string $host): static
```php

Crea una nueva URL y modifica su componente de host.

## Parámetros

`host`  
Nuevo componente de host.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withHost

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com");
$url = $url->withHost("example.net");

echo $url->getAsciiHost();
?>

   
```php

El ejemplo anterior mostrará:

    example.net

## Véase también

Uri\WhatWg\Url::getAsciiHost

Uri\WhatWg\Url::getUnicodeHost

Uri\Rfc3986\Uri::withHost
