---
title: tidyNode::getNextSibling
description: Devuelve el nodo hermano siguiente del nodo actual
source_url: https://www.php.net/manual/es/tidynode.getnextsibling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/getnextsibling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 43c6d8023
order: 94200
---

tidyNode::getNextSibling

Devuelve el nodo hermano siguiente del nodo actual

## Descripción

```php
public tidyNode::getNextSibling(): tidyNode
```php

Devuelve el nodo hermano siguiente del nodo actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `tidyNode` si el nodo tiene un hermano siguiente, o `null` de lo contrario.

## Ejemplos

Ejemplo de `tidyNode::getNextSibling`

```
<?php

$html = <<< HTML
<html>
 <head>
 </head>
 <body>
  <p>Hello</p><p>World</p>
 </body>
</html>

HTML;

$tidy = tidy_parse_string($html);

$node = $tidy->body();
var_dump($node->child[0]->getNextSibling()->value);

?>

   
```php

El ejemplo anterior mostrará:

    string(13) "<p>World</p>
    "

## Véase también

tidyNode::getParent

tidyNode::getPreviousSibling
