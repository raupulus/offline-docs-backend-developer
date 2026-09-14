---
title: DOMCharacterData::after
description: Añade nodos después de los datos
source_url: https://www.php.net/manual/es/domcharacterdata.after.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/after.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 8c0d11185
order: 12800
---

DOMCharacterData::after

Añade nodos después de los datos

## Descripción

```php
public DOMCharacterData::after(DOMNode ...$nodes): void
```php

Añade los `nodes` pasados después de los datos de carácter.

## Ejemplos

Ejemplo de DOMCharacterData::after

Añade nodos después de los datos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><![CDATA[hello]]></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->after("beautiful", $doc->createElement("world"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><![CDATA[hello]]>beautiful<world/></container>

## Véase también

DOMChildNode::after

DOMCharacterData::before
