---
title: DOMElement::after
description: Añade nodos después del elemento
source_url: https://www.php.net/manual/es/domelement.after.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/after.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13400
---

DOMElement::after

Añade nodos después del elemento

## Descripción

```php
public DOMElement::after(DOMNode ...$nodes): void
```php

Añade los `nodes` pasados después del elemento.

## Ejemplos

Ejemplo de DOMElement::after

Añade los nodos después del elemento hello.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<hello/>");
$container = $doc->documentElement;

$container->after("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <hello/>
    beautiful
    <world/>

## Véase también

DOMChildNode::after

DOMElement::before
