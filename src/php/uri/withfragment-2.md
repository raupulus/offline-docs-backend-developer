---
title: Uri\WhatWg\Url::withFragment
description: Modifica el componente de fragmento
source_url: https://www.php.net/manual/es/uri-whatwg-url.withfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100000
---

Uri\WhatWg\Url::withFragment

Modifica el componente de fragmento

## Descripción

```php
public Uri\WhatWg\Url::withFragment(string $fragment): static
```php

Crea una nueva URL y modifica su componente de fragmento.

## Parámetros

`fragment`  
Nuevo componente de fragmento.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withFragment

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com/#foo");
$url = $url->withFragment("bar");

echo $url->getFragment();
?>

   
```php

El ejemplo anterior mostrará:

    bar

## Véase también

Uri\WhatWg\Url::getFragment

Uri\Rfc3986\Uri::withFragment
