---
title: DOMElement::remove
description: Elimina el elemento
source_url: https://www.php.net/manual/es/domelement.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7b1704c9a
order: 13560
---

DOMElement::remove

Elimina el elemento

## Descripción

```php
public DOMElement::remove(): void
```php

Elimina el elemento.

## Ejemplos

Ejemplo de DOMElement::remove

Elimina el elemento.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><hello/><world/></container>");
$hello = $doc->documentElement->firstChild;

$hello->remove();

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><world/></container>

## Véase también

DOMElement::after

DOMElement::before

DOMElement::replaceWith

DOMNode::removeChild
