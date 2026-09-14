---
title: DOMDocumentFragment::append
description: Añade nodos después del último nodo hijo
source_url: https://www.php.net/manual/es/domdocumentfragment.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocumentfragment/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1349f957
order: 13330
---

DOMDocumentFragment::append

Añade nodos después del último nodo hijo

## Descripción

```php
public DOMDocumentFragment::append(DOMNode ...$nodes): void
```php

Añade uno o varios `nodes` a la lista de hijos después del último nodo hijo.

## Ejemplos

Ejemplo de DOMDocumentFragment::append

Añade nodos en el fragmento.

```
<?php
$doc = new DOMDocument;
$fragment = $doc->createDocumentFragment();
$fragment->appendChild($doc->createElement("hello"));

$fragment->append("beautiful", $doc->createElement("world"));

echo $doc->saveXML($fragment);
?>

   
```php

El ejemplo anterior mostrará:

    <hello/>beautiful<world/>

## Véase también

DOMParentNode::append

DOMDocumentFragment::prepend
