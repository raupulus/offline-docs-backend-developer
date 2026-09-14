---
title: DOMElement::prepend
description: Añade nodos antes del primer hijo
source_url: https://www.php.net/manual/es/domelement.prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13550
---

DOMElement::prepend

Añade nodos antes del primer hijo

## Descripción

```php
public DOMElement::prepend(DOMNode ...$nodes): void
```php

Añade uno o varios `nodes` a la lista de hijos antes del primer nodo hijo.

## Ejemplos

Ejemplo de DOMElement::prepend

Añade los nodos antes del elemento contenedor.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container> world</container>");
$world = $doc->documentElement;

$world->prepend($doc->createElement("hello"), "beautiful");

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><hello/>beautiful world</container>

## Véase también

DOMParentNode::prepend

DOMElement::append
