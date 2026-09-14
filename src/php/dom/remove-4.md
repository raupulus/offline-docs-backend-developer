---
title: DOMCharacterData::remove
description: Elimina el nodo de datos de carácter
source_url: https://www.php.net/manual/es/domcharacterdata.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 8c0d11185
order: 12850
---

DOMCharacterData::remove

Elimina el nodo de datos de carácter

## Descripción

```php
public DOMCharacterData::remove(): void
```php

Elimina el nodo de datos de carácter.

## Ejemplos

Ejemplo de DOMCharacterData::remove

Elimina los datos.

```
<?php
$doc = new DOMDocument;
$doc->loadXML("<container><![CDATA[hello]]><world/></container>");
$cdata = $doc->documentElement->firstChild;

$cdata->remove();

echo $doc->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><world/></container>

## Véase también

DOMChildNode::remove

DOMCharacterData::after

DOMCharacterData::before

DOMCharacterData::replaceWith

DOMNode::removeChild
