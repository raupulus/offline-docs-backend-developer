---
title: Dom\CharacterData::remove
source_url: https://www.php.net/manual/es/dom-characterdata.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/characterdata/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 8c0d11185
order: 12170
---

Dom\CharacterData::remove

## Descripción

```php
public Dom\CharacterData::remove(): void
```php

## Ejemplos

Ejemplo de Dom\CharacterData::remove

Elimina los datos de caracteres.

```
<?php
$doc = Dom\XMLDocument::createFromString("<container><![CDATA[hello]]><world/></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->remove();

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><world/></container>

## Véase también

Dom\ChildNode::remove

Dom\CharacterData::after

Dom\CharacterData::before

Dom\CharacterData::replaceWith

Dom\Node::removeChild
