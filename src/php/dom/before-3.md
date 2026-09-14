---
title: DOMCharacterData::before
description: Añade nodos antes de los datos de carácter
source_url: https://www.php.net/manual/es/domcharacterdata.before.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/before.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 8c0d11185
order: 12820
---

DOMCharacterData::before

Añade nodos antes de los datos de carácter

## Descripción

```php
public DOMCharacterData::before(DOMNode ...$nodes): void
```php

Añade los `nodes` pasados antes de los datos de carácter.

## Ejemplos

Ejemplo de DOMCharacterData::before

Añade los nodos antes de los datos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><![CDATA[world]]></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->before("hello", $doc->createElement("beautiful"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container>hello<beautiful/><![CDATA[world]]></container>

## Véase también

DOMChildNode::before

DOMCharacterData::after
