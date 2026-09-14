---
title: Dom\CharacterData::after
source_url: https://www.php.net/manual/es/dom-characterdata.after.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/characterdata/after.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 8c0d11185
order: 12120
---

Dom\CharacterData::after

## Descripción

```php
public Dom\CharacterData::after(Dom\Node ...$nodes): void
```php

## Ejemplos

Ejemplo de Dom\CharacterData::after

Añade nodos después de los datos de caracteres.

```
<?php
$doc = Dom\XMLDocument::createFromString("<container><![CDATA[hello]]></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->after("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><![CDATA[hello]]>beautiful<world/></container>

## Véase también

Dom\ChildNode::after

Dom\CharacterData::before
