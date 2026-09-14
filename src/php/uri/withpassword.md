---
title: Uri\WhatWg\Url::withPassword
description: Modifica el componente de contraseña
source_url: https://www.php.net/manual/es/uri-whatwg-url.withpassword.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/withpassword.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 100020
---

Uri\WhatWg\Url::withPassword

Modifica el componente de contraseña

## Descripción

```php
public #[\SensitiveParameter] Uri\WhatWg\Url::withPassword(string $password): static
```php

Crea una nueva URL y modifica su componente de contraseña.

## Parámetros

`password`  
Nuevo componente de contraseña.

## Valores devueltos

La instancia de `Uri\WhatWg\Url` modificada.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::withPassword

```
<?php
$url = new \Uri\WhatWg\Url("https://user:password@example.com");
$url = $url->withPassword("pass");

echo $url->getPassword();
?>

   
```php

El ejemplo anterior mostrará:

    pass

## Véase también

Uri\WhatWg\Url::getPassword

Uri\WhatWg\Url::getUsername

Uri\Rfc3986\Uri::withUserInfo
