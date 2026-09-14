---
title: DOMDocumentFragment::replaceChildren
description: Reemplaza los hijos en el fragmento
source_url: https://www.php.net/manual/es/domdocumentfragment.replacechildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocumentfragment/replacechildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d6f54016d
order: 13370
---

DOMDocumentFragment::replaceChildren

Reemplaza los hijos en el fragmento

## Descripción

```php
public DOMDocumentFragment::replaceChildren(DOMNode ...$nodes): void
```php

Reemplaza los hijos en el fragmento por nuevos `nodes`.

## Ejemplos

Ejemplo de DOMDocumentFragment::replaceChildren

Reemplaza los hijos por nuevos nodos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><hello/></container>");
$fragment = $doc->createDocumentFragment();
$fragment->append("hello");

$fragment->replaceChildren("beautiful", $doc->createElement("world"));

echo $doc->saveXML($fragment);
?>

   
```php

El ejemplo anterior mostrará:

    beautiful
    <world/>

## Véase también

DOMParentNode::replaceChildren

DOMDocumentFragment::append

DOMDocumentFragment::prepend
