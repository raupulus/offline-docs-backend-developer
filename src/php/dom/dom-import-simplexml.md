---
title: dom_import_simplexml
description: Obtiene un objeto DOMAttr o DOMElement desde un objeto SimpleXMLElement
source_url: https://www.php.net/manual/es/function.dom-import-simplexml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/functions/dom-import-simplexml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 940ea8c1b
order: 14380
---

dom_import_simplexml

Obtiene un objeto

DOMAttr

o

DOMElement

desde un objeto

SimpleXMLElement

## Descripción

```php
dom_import_simplexml(object $node): DOMAttr
```php

Esta función toma el atributo o el elemento dado `node` (una instancia de `SimpleXMLElement`) y crea respectivamente un nodo `DOMAttr` o `DOMElement`. El nuevo `DOMNode` hace referencia al mismo nodo XML subyacente que el `SimpleXMLElement`.

## Parámetros

`node`  
El atributo o el elemento nodo a importar (una instancia de `SimpleXMLElement`).

## Valores devueltos

El `DOMAttr` o `DOMElement`.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.0.0   | Esta función ya no devuelve `null` en caso de error. |

## Ejemplos

Importación de un objeto SimpleXML en DOM con `dom_import_simplexml`

```
<?php

$sxe = simplexml_load_string('<books><book><title>blah</title></book></books>');

if ($sxe === false) {
    echo 'Error al analizar el documento';
    exit;
}

$dom_sxe = dom_import_simplexml($sxe);
if (!$dom_sxe) {
    echo 'Error al convertir el XML';
    exit;
}

$dom = new DOMDocument('1.0');
$dom_sxe = $dom->importNode($dom_sxe, true);
$dom_sxe = $dom->appendChild($dom_sxe);

echo $dom->saveXML();

?>

   
```php

El ejemplo anterior mostrará:

    <books><book><title>blah</title></book></books>

Importar SimpleXML en DOM y modificar SimpleXML mediante DOM

La gestión de errores se omite por razones de concisión.

```
<?php

$sxe = simplexml_load_string('<books><book><title>blah</title></book></books>');
$elt = dom_import_simplexml($sxe);
$elt->setAttribute("foo", "bar");
echo $sxe->asXML();

?>

   
```php

El ejemplo anterior mostrará:

    <books foo="bar"><book><title>blah</title></book></books>

## Véase también

`simplexml_import_dom`
