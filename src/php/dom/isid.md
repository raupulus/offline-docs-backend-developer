---
title: Dom\Attr::isId
source_url: https://www.php.net/manual/es/dom-attr.isid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/attr/isid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 12100
---

Dom\Attr::isId

## Descripción

```php
public Dom\Attr::isId(): bool
```php

Según la norma DOM esto requiere un DTD que defina el atributo ID como de tipo ID. Para utilizar este método, el documento debe ser validado en el momento del análisis pasando `LIBXML_DTDVALID` como opción.

## Parámetros

Esta función no contiene ningún parámetro.

## 

## Ejemplos

Ejemplo de Dom\Attr::isId()

```
<?php

// Se debe validar el documento antes de referirse al id
$doc = Dom\XMLDocument::createFromFile('examples/book-docbook.xml', LIBXML_DTDVALID);

// Se obtiene el atributo llamado id del elemento chapter
$attr = $doc->getElementsByTagName('chapter')->item(0)->getAttributeNode('id');

var_dump($attr->isId()); // bool(true)

?>

   
```php
