---
title: ob_tidyhandler
description: Función callback de ob_start para reparar el buffer
source_url: https://www.php.net/manual/es/function.ob-tidyhandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/functions/ob-tidyhandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 14af302c9
order: 93900
---

ob_tidyhandler

Función callback de ob_start para reparar el buffer

## Descripción

```php
ob_tidyhandler(string $input, [int $mode]): string
```php

Función callback para la función `ob_start` con el fin de reparar el buffer.

## Parámetros

`input`  
EL buffer.

`mode`  
El modo del buffer.

## Valores devueltos

Devuelve el buffer modificado.

## Ejemplos

Ejemplo de `ob_tidyhandler`

```
<?php
ob_start('ob_tidyhandler');

echo '<p>test</i>';
?>

    
```php

El ejemplo anterior mostrará:

    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
    <html>
    <head>
    <title></title>
    </head>
    <body>
    <p>test</p>
    </body>
    </html>

## Véase también

`ob_start`
