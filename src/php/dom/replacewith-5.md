---
title: DOMElement::replaceWith
description: Reemplaza el elemento por nuevos nodos
source_url: https://www.php.net/manual/es/domelement.replacewith.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/replacewith.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13610
---

DOMElement::replaceWith

Reemplaza el elemento por nuevos nodos

## Descripción

```php
public DOMElement::replaceWith(DOMNode ...$nodes): void
```php

Reemplaza el elemento por nuevos `nodes`.

## Ejemplos

Ejemplo de DOMElement::replaceWith

Reemplaza el elemento por nuevos nodos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><hello/></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->replaceWith("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container>beautiful<world/></container>

## Véase también

DOMChildNode::replaceWith

DOMElement::replaceChildren

DOMElement::after

DOMElement::before

DOMElement::remove
