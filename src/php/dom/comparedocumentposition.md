---
title: DOMNode::compareDocumentPosition
description: Comparar la posición de dos nodos
source_url: https://www.php.net/manual/es/domnode.comparedocumentposition.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/compareDocumentPosition.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: f1516b33a
order: 13930
---

DOMNode::compareDocumentPosition

Comparar la posición de dos nodos

## Descripción

```php
public DOMNode::compareDocumentPosition(DOMNode $other): int
```php

Compara la posición del otro nodo con respecto a este nodo.

## Parámetros

`other`  
El nodo cuya posición debe ser comparada, con respecto a este nodo.

## Valores devueltos

Una máscara de bits de las constantes `DOMNode::DOCUMENT_POSITION_*`.

## Ejemplos

Ejemplo de DOMNode::compareDocumentPosition

```
<?php
$xml = <<<XML
<root>
    <child1/>
    <child2/>
</root>
XML;

$dom = new DOMDocument();
$dom->loadXML($xml);

$root = $dom->documentElement;
$child1 = $root->firstElementChild;
$child2 = $child1->nextElementSibling;

var_dump($root->compareDocumentPosition($child1));
var_dump($child2->compareDocumentPosition($child1));
?>

   
```php

El ejemplo anterior mostrará:

    int(20) // Esto es DOMNode::DOCUMENT_POSITION_CONTAINED_BY | DOMNode::DOCUMENT_POSITION_FOLLOWING
    int(2)  // Esto es DOMNode::DOCUMENT_POSITION_PRECEDING
