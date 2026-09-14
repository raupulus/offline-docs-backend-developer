---
title: Uri\WhatWg\Url::withPath
description: Modifica el componente de ruta
source_url: https://www.php.net/manual/es/uri-whatwg-url.withpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100030
---

Uri\WhatWg\Url::withPath

Modifica el componente de ruta

## Descripción

```php
public Uri\WhatWg\Url::withPath(string $path): static
```php

Crea una nueva URL y modifica su componente de ruta.

## Parámetros

`path`  
Nuevo componente de ruta.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withPath

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com/foo/bar");
$url = $url->withPath("/baz");

echo $url->getPath();
?>

   
```php

El ejemplo anterior mostrará:

    /baz

## Véase también

Uri\WhatWg\Url::getPath

Uri\Rfc3986\Uri::withPath
