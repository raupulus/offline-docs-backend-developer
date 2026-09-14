---
title: Dom\CharacterData::replaceWith
source_url: https://www.php.net/manual/es/dom-characterdata.replacewith.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/characterdata/replacewith.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 8c0d11185
order: 12190
---

Dom\CharacterData::replaceWith

## Descripción

```php
public Dom\CharacterData::replaceWith(Dom\Node ...$nodes): void
```php

## Ejemplos

Ejemplo de Dom\CharacterData::replaceWith

Reemplaza los datos de caracteres por nuevos nodos.

```
<?php
$doc = Dom\XMLDocument::createFromString("<container><![CDATA[hello]]></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->replaceWith("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container>beautiful<world/></container>

## Véase también

Dom\ChildNode::replaceWith

Dom\CharacterData::after

Dom\CharacterData::before

Dom\CharacterData::remove
