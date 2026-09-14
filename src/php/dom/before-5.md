---
title: DOMElement::before
description: Añade nodos antes del elemento
source_url: https://www.php.net/manual/es/domelement.before.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/before.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13420
---

DOMElement::before

Añade nodos antes del elemento

## Descripción

```php
public DOMElement::before(DOMNode ...$nodes): void
```php

Añade los `nodes` pasados antes del elemento.

## Ejemplos

Ejemplo de DOMElement::before

Añade los nodos antes del elemento hello.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<world/>");
$world = $doc->documentElement;

$world->before("hello", $doc->createElement("beautiful"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    hello
    <beautiful/>
    <world/>

## Véase también

DOMChildNode::before

DOMElement::after
