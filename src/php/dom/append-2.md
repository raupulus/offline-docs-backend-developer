---
title: DOMDocument::append
description: Añade nodos después del último nodo hijo
source_url: https://www.php.net/manual/es/domdocument.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1349f957
order: 12980
---

DOMDocument::append

Añade nodos después del último nodo hijo

## Descripción

```php
public DOMDocument::append(DOMNode ...$nodes): void
```php

Añade uno o varios `nodes` a la lista de hijos después del último nodo hijo.

## Ejemplos

Ejemplo de DOMDocument::append

Añade nodos después del nodo raíz del documento.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<hello/>");

$doc->append("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <hello/>
    beautiful
    <world/>

## Véase también

DOMParentNode::append

DOMDocument::prepend
