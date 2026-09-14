---
title: DOMAttr::isId
description: Verifica si el atributo es un identificador definido
source_url: https://www.php.net/manual/es/domattr.isid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domattr/isid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1f37a6c2
order: 12760
---

DOMAttr::isId

Verifica si el atributo es un identificador definido

## Descripción

```php
public DOMAttr::isId(): bool
```php

Esta función verifica si el atributo es un identificador definido.

De acuerdo con el estándar DOM, esto requiere un DTD que defina el atributo ID que sea del tipo ID. Se debe validar el documento con la función [???](#domdocument.validate) o la propiedad DOMDocument::\$validateOnParse antes de utilizar esta función.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si este atributo es un ID definido, `false` en caso contrario.

## Ejemplos

Ejemplo con DOMAttr::isId()

```
<?php

$doc = new DOMDocument;

// Debemos validar nuestro documento antes de referirnos al ID
$doc->validateOnParse = true;
$doc->load('examples/book-docbook.xml');

// Obtenemos el atributo nombrado id del elemento chapter
$attr = $doc->getElementsByTagName('chapter')->item(0)->getAttributeNode('id');

var_dump($attr->isId()); // bool(true)

?>

    
```php
