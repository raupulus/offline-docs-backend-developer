---
title: tidy::body
description: Devuelve un objeto tidyNode empezando con la etiqueta <body>
source_url: https://www.php.net/manual/es/tidy.body.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/body.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 2b84fa46e
order: 93980
---

tidy::body

tidy_get_body

Devuelve un objeto

tidyNode

empezando con la etiqueta \<body\>

## Descripción

Estilo orientado a objetos

```php
public tidy::body(): tidyNode
```php

Estilo procedimental

```php
tidy_get_body(tidy $tidy): tidyNode
```

Devuelve un objeto `tidyNode` empezando por la etiqueta \<body\>.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve un objeto `tidyNode` empezando por la etiqueta \<body\> del árbol analizado por tidy.

## Ejemplos

Ejemplo de `tidy::getBody`

```php
<?php
$html = '
<html>
  <head>
    <title>test</title>
  </head>
  <body>
    <p>paragraph</p>
  </body>
</html>';

$tidy = tidy_parse_string($html);

$body = $tidy->Body();
echo $body->value;
?>

    
```

El ejemplo anterior mostrará:

    <body>
    <p>paragraph</p>
    </body>

## Véase también

tidy::head

tidy::html
