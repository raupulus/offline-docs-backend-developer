---
title: DOMDocument::prepend
description: Añade nodos antes del primer nodo hijo
source_url: https://www.php.net/manual/es/domdocument.prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1349f957
order: 13190
---

DOMDocument::prepend

Añade nodos antes del primer nodo hijo

## Descripción

```php
public DOMDocument::prepend(DOMNode ...$nodes): void
```php

Añade uno o varios `nodes` a la lista de hijos antes del primer nodo hijo.

## Ejemplos

Ejemplo de DOMDocument::prepend

Añade nodos antes del nodo raíz del documento.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<world/>");

$doc->prepend($doc->createElement("hello"), "beautiful");

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <hello/>
    beautiful
    <world/>

## Véase también

DOMParentNode::prepend

DOMDocument::append
