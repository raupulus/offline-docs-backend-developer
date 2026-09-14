---
title: DOMDocument::replaceChildren
description: Reemplaza los hijos en el documento
source_url: https://www.php.net/manual/es/domdocument.replacechildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/replacechildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: d6f54016d
order: 13230
---

DOMDocument::replaceChildren

Reemplaza los hijos en el documento

## Descripción

```php
public DOMDocument::replaceChildren(DOMNode ...$nodes): void
```php

Reemplaza los hijos en el documento por nuevos `nodes`.

## Ejemplos

Ejemplo de DOMDocument::replaceChildren

Reemplaza los hijos por nuevos nodos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><hello/></container>");

$doc->replaceChildren("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    beautiful
    <world/>

## Véase también

DOMParentNode::replaceChildren

DOMDocument::append

DOMDocument::prepend
