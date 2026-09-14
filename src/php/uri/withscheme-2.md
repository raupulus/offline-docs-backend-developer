---
title: Uri\WhatWg\Url::withScheme
description: Modifica el componente de esquema
source_url: https://www.php.net/manual/es/uri-whatwg-url.withscheme.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withscheme.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100060
---

Uri\WhatWg\Url::withScheme

Modifica el componente de esquema

## Descripción

```php
public Uri\WhatWg\Url::withScheme(string $scheme): static
```php

Crea una nueva URL y modifica su componente de esquema.

## Parámetros

`scheme`  
Nuevo componente de esquema.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withScheme

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com");
$url = $url->withScheme("http");

echo $url->getScheme();
?>

   
```php

El ejemplo anterior mostrará:

    http

## Véase también

Uri\WhatWg\Url::getScheme

Uri\Rfc3986\Uri::withScheme
