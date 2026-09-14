---
title: DOMDocumentFragment::prepend
description: Añade nodos antes del primer nodo hijo
source_url: https://www.php.net/manual/es/domdocumentfragment.prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocumentfragment/prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13360
---

DOMDocumentFragment::prepend

Añade nodos antes del primer nodo hijo

## Descripción

```php
public DOMDocumentFragment::prepend(DOMNode ...$nodes): void
```php

Añade uno o varios `nodes` a la lista de hijos antes del primer nodo hijo.

## Ejemplos

Ejemplo de DOMDocumentFragment::prepend

Añade nodos antes del fragmento raíz.

```
<?php
$doc = new DOMDocument;
$fragment = $doc->createDocumentFragment();
$fragment->appendChild($doc->createElement("world"));

$fragment->prepend($doc->createElement("hello"), "beautiful");

echo $doc->saveXML($fragment);
?>

   
```php

El ejemplo anterior mostrará:

    <hello/>beautiful<world/>

## Véase también

DOMParentNode::prepend

DOMDocumentFragment::append
