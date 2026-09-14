---
title: Uri\WhatWg\Url::withQuery
description: Modifica el componente de consulta
source_url: https://www.php.net/manual/es/uri-whatwg-url.withquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100050
---

Uri\WhatWg\Url::withQuery

Modifica el componente de consulta

## Descripción

```php
public Uri\WhatWg\Url::withQuery(string $query): static
```php

Crea una nueva URL y modifica su componente de consulta.

## Parámetros

`query`  
Nuevo componente de consulta.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withQuery

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com?foo=bar");
$url = $url->withQuery("foo=baz");

echo $url->getQuery();
?>

   
```php

El ejemplo anterior mostrará:

    foo=baz

## Véase también

Uri\WhatWg\Url::getQuery

Uri\Rfc3986\Uri::withQuery
