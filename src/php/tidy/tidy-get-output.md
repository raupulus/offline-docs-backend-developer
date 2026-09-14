---
title: tidy_get_output
description: Devuelve una cadena que contiene las etiquetas analizadas por Tidy
source_url: https://www.php.net/manual/es/function.tidy-get-output.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/functions/tidy-get-output.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 04f10f9f8
order: 93940
---

tidy_get_output

Devuelve una cadena que contiene las etiquetas analizadas por Tidy

## Descripción

```php
tidy_get_output(tidy $tidy): string
```php

Devuelve una cadena con el HTML reparado.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve las etiquetas analizadas por tidy

## Ejemplos

Ejemplo de la función `tidy_get_output`

```
<?php

$html = '<p>paragraph</i>';
$tidy = tidy_parse_string($html);

$tidy->cleanRepair();

echo tidy_get_output($tidy);
?>

    
```php

El ejemplo anterior mostrará:

    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
    <html>
    <head>
    <title></title>
    </head>
    <body>
    <p>paragraph</p>
    </body>
    </html>
