---
title: tidy::html
description: Devuelve un objeto tidyNode empezando con la etiqueta <html>
source_url: https://www.php.net/manual/es/tidy.html.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/html.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94100
---

tidy::html

tidy_get_html

Devuelve un objeto

tidyNode

empezando con la etiqueta \<html\>

## Descripción

Estilo orientado a objetos

```php
public tidy::html(): tidyNode
```php

Estilo procedimental

```php
tidy_get_html(tidy $tidy): tidyNode
```

Devuelve un objeto `tidyNode` empezando por la etiqueta \<html\>.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el objeto `tidyNode`.

## Ejemplos

Ejemplo de `tidy::html`

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

$html = $tidy->html();
echo $html->value;
?>

    
```

El ejemplo anterior mostrará:

    <html>
    <head>
    <title>test</title>
    </head>
    <body>
    <p>parrafo</p>
    </body>
    </html>

## Véase también

tidy::body

tidy::head
