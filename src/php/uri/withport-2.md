---
title: Uri\WhatWg\Url::withPort
description: Modifica el componente de puerto
source_url: https://www.php.net/manual/es/uri-whatwg-url.withport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100040
---

Uri\WhatWg\Url::withPort

Modifica el componente de puerto

## Descripción

```php
public Uri\WhatWg\Url::withPort(int $port): static
```php

Crea una nueva URL y modifica su componente de puerto.

## Parámetros

`port`  
Nuevo componente de puerto.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withPort

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com:8080");
$url = $url->withPort(443);

echo $url->getPort();
?>

   
```php

El ejemplo anterior mostrará:

    443

## Véase también

Uri\WhatWg\Url::getPort

Uri\Rfc3986\Uri::withPort
