---
title: DOMElement::append
description: Añade nodos después del último hijo
source_url: https://www.php.net/manual/es/domelement.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13410
---

DOMElement::append

Añade nodos después del último hijo

## Descripción

```php
public DOMElement::append(DOMNode ...$nodes): void
```php

Añade uno o varios `nodes` a la lista de hijos después del último nodo hijo.

## Ejemplos

Ejemplo de DOMElement::append

Añade nodos en el elemento contenedor.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container>hello </container>");
$world = $doc->documentElement;

$world->append("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container>hello beautiful<world/></container>

## Véase también

DOMParentNode::append

DOMElement::prepend
