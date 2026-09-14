---
title: DOMElement::getAttributeNames
description: Devuelve los nombres de los atributos
source_url: https://www.php.net/manual/es/domelement.getattributenames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getattributenames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: cdbee08c7
order: 13450
---

DOMElement::getAttributeNames

Devuelve los nombres de los atributos

## Descripción

```php
public DOMElement::getAttributeNames(): array
```php

Obtener los nombres de los atributos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los nombres de los atributos.

## Ejemplos

Ejemplo de DOMElement::getAttributeNames

```
<?php

$dom = new DOMDocument();
$dom->loadXML('<html xmlns:some="some:ns" some:test="a" test2="b"/>');
var_dump($dom->documentElement->getAttributeNames());
?>

   
```php

El ejemplo anterior mostrará:

    array(3) {
     [0]=>
     string(10) "xmlns:some"
     [1]=>
     string(9) "some:test"
     [2]=>
     string(5) "test2"
    }
