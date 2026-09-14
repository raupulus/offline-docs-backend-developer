---
title: Dom\import_simplexml
description: Devuelve un objeto Dom\Attr o Dom\Element a partir de un objeto SimpleXMLElement
source_url: https://www.php.net/manual/es/function.dom-ns-import-simplexml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/functions/dom-ns-import-simplexml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c82f29b65
order: 14390
---

Dom\import_simplexml

Devuelve un objeto

Dom\Attr

o

Dom\Element

a partir de un objeto

SimpleXMLElement

## Descripción

```php
Dom\import_simplexml(object $node): Dom\Attr
```php

Esta función toma el atributo o el elemento `node` dado (una instancia de `SimpleXMLElement`) y crea un nodo `Dom\Attr` o `Dom\Element`, respectivamente. El nuevo `Dom\Node` hace referencia al mismo nodo XML subyacente que el `SimpleXMLElement`.

## 

## Valores devueltos

El `Dom\Attr` o `Dom\Element`.

## Ejemplos

Importa SimpleXML en DOM y modifica SimpleXML a través de DOM

La gestión de errores se omite por brevedad.

```
<?php

$sxe = simplexml_load_string('<books><book><title>blah</title></book></books>');
$elt = Dom\import_simplexml($sxe);
$elt->setAttribute("foo", "bar");
echo $sxe->asXML();

?>

   
```php

El ejemplo anterior mostrará:

    <books foo="bar"><book><title>blah</title></book></books>

## Véase también

simplexml_import_dom
