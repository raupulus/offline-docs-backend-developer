---
title: tidyNode::getParent
description: Devuelve el nodo padre del nodo actual
source_url: https://www.php.net/manual/es/tidynode.getparent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode/getparent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: true
translation_revision: 43c6d8023
order: 94210
---

tidyNode::getParent

Devuelve el nodo padre del nodo actual

## Descripción

```php
public tidyNode::getParent(): tidyNode
```php

Devuelve el nodo padre del nodo actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `tidyNode` si el nodo tiene un padre, o `null` en caso contrario.

## Ejemplos

Ejemplo con `tidyNode::getParent`

```
<?php

$html = <<< HTML
<html><head>
<?php echo '<title>title</title>'; ?>
<#
  /* JSTE code */
  alert('Hello World');
#>
 </head>
 <body>
 Hello World
 </body>
</html>

HTML;

$tidy = tidy_parse_string($html);
$num = 0;

$node = $tidy->html()->child[0]->child[0];

var_dump($node->getParent()->name);
?>

    
```php

El ejemplo anterior mostrará:

    string(4) "head"

## Véase también

tidyNode::getPreviousSibling

tidyNode::getNextSibling
