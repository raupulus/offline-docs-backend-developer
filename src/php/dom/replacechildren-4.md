---
title: DOMElement::replaceChildren
description: Reemplaza los hijos en el elemento
source_url: https://www.php.net/manual/es/domelement.replacechildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/replacechildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13600
---

DOMElement::replaceChildren

Reemplaza los hijos en el elemento

## Descripción

```php
public DOMElement::replaceChildren(DOMNode ...$nodes): void
```php

Reemplaza los hijos en el elemento por nuevos `nodes`.

## Ejemplos

Ejemplo de DOMElement::replaceChildren

Reemplaza los hijos por nuevos nodos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><hello/></container>");
$container = $doc->documentElement;

$container->replaceWith("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    beautiful
    <world/>

## Véase también

DOMParentNode::replaceChildren

DOMElement::replaceWith

DOMElement::after

DOMElement::before

DOMElement::remove
