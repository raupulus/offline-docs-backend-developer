---
title: DOMCharacterData::replaceWith
description: Reemplaza los datos por nuevos nodos
source_url: https://www.php.net/manual/es/domcharacterdata.replacewith.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/replacewith.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1349f957
order: 12870
---

DOMCharacterData::replaceWith

Reemplaza los datos por nuevos nodos

## Descripción

```php
public DOMCharacterData::replaceWith(DOMNode ...$nodes): void
```php

Reemplaza los datos por nuevos `nodes`.

## Ejemplos

Ejemplo de DOMCharacterData::replaceWith

Reemplaza los datos por nuevos nodos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><![CDATA[hello]]></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->replaceWith("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container>beautiful<world/></container>

## Véase también

DOMChildNode::replaceWith

DOMCharacterData::after

DOMCharacterData::before

DOMCharacterData::remove
