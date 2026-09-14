---
title: Dom\CharacterData::before
source_url: https://www.php.net/manual/es/dom-characterdata.before.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/characterdata/before.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 8c0d11185
order: 12140
---

Dom\CharacterData::before

## Descripción

```php
public Dom\CharacterData::before(Dom\Node ...$nodes): void
```php

## Ejemplos

Ejemplo de Dom\CharacterData::before

Añade nodos antes de los datos de caracteres.

```
<?php
$doc = Dom\XMLDocument::createFromString("<container><![CDATA[world]]></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->before("hello", $doc->createElement("beautiful"));

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container>hello<beautiful/><![CDATA[world]]></container>

## Véase también

Dom\ChildNode::before

Dom\CharacterData::after
