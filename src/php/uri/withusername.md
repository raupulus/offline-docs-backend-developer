---
title: Uri\WhatWg\Url::withUsername
description: Modifica el componente de nombre de usuario
source_url: https://www.php.net/manual/es/uri-whatwg-url.withusername.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withusername.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100070
---

Uri\WhatWg\Url::withUsername

Modifica el componente de nombre de usuario

## Descripción

```php
public Uri\WhatWg\Url::withUsername(string $username): static
```php

Crea una nueva URL y modifica su componente de nombre de usuario.

## Parámetros

`username`  
Nuevo componente de nombre de usuario.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withUsername

```
<?php
$url = new \Uri\WhatWg\Url("https://user:password@example.com");
$url = $url->withUsername("usr");

echo $url->getUsername();
?>

   
```php

El ejemplo anterior mostrará:

    usr

## Véase también

Uri\WhatWg\Url::getUsername

Uri\WhatWg\Url::getPassword

Uri\Rfc3986\Uri::withUserInfo
