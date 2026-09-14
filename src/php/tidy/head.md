---
title: tidy::head
description: Devuelve un objeto tidyNode empezando con la etiqueta <head>
source_url: https://www.php.net/manual/es/tidy.head.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/head.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94090
---

tidy::head

tidy_get_head

Devuelve un objeto

tidyNode

empezando con la etiqueta \<head\>

## Descripción

Estilo orientado a objetos

```php
public tidy::head(): tidyNode
```php

Estilo procedimental

```php
tidy_get_head(tidy $tidy): tidyNode
```

Devuelve un objeto `tidyNode` empezando por la etiqueta \<head\>.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el objeto `tidyNode`.

## Ejemplos

Ejemplo de `tidy::head`

```php
<?php
$html = '
<html>
  <head>
    <title>test</title>
  </head>
  <body>
    <p>parrafo</p>
  </body>
</html>';

$tidy = tidy_parse_string($html);

$head = $tidy->head();
echo $head->value;
?>

    
```

El ejemplo anterior mostrará:

    <head>
    <title>test</title>
    </head>

## Véase también

tidy::body

tidy::html
