---
title: ob_get_contents
description: Devuelve el contenido del búfer de salida
source_url: https://www.php.net/manual/es/function.ob-get-contents.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-get-contents.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: false
translation_revision: 6ab6ea465
order: 59790
---

ob_get_contents

Devuelve el contenido del búfer de salida

## Descripción

```php
ob_get_contents(): string
```php

Devuelve el contenido del búfer de salida sin borrarlo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del búfer de salida sin borrarlo o `false`, si la temporización de salida no está activada.

## Ejemplos

Ejemplo con `ob_get_contents`

```
<?php

ob_start();

echo "Bonjour ";

$out1 = ob_get_contents();

echo "le monde !";

$out2 = ob_get_contents();

ob_end_clean();

var_dump($out1, $out2);
?>

    
```php

El ejemplo anterior mostrará:

    string(8) "Bonjour "
    string(18) "Bonjour le monde !"

## Véase también

`ob_start`, `ob_get_length`
