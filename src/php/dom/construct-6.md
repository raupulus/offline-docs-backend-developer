---
title: DOMElement::__construct
description: Crea un nuevo objeto DOMElement
source_url: https://www.php.net/manual/es/domelement.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 13430
---

DOMElement::\_\_construct

Crea un nuevo objeto DOMElement

## Descripción

```php
public DOMElement::__construct(string $qualifiedName, [string $value], [string $namespace])
```php

Crea un nuevo objeto `DOMElement`. Este objeto es de sólo lectura. Puede ser añadido a un documento, pero no se pueden añadir nodos adicionales a este nodo hasta que el nodo esté asociado con un documento. Para crear un nodo modificable, use [???](#domdocument.createelement) o [???](#domdocument.createelementns).

## Parámetros

`qualifiedName`  
El nombre de la etiqueta del elemento. Cuando también se pasa en namespaceURI, el nombre del elemento puede tomar un prefijo para asociarlo con la URI.

`value`  
El valor del elemento.

`namespace`  
Una URI del espacio de nombres para crear el elemento dentro de un espacio de nombres especificado.

## Ejemplos

Crear un nuevo objeto DOMElement

```
<?php

$dom = new DOMDocument('1.0', 'iso-8859-1');
$element = $dom->appendChild(new DOMElement('root'));
$element_ns = new DOMElement('pr:node1', 'thisvalue', 'http://xyz');
$element->appendChild($element_ns);
echo $dom->saveXML(); /* 
<root><pr:node1 xmlns:pr="http://xyz">thisvalue</pr:node1></root> */

?>

    
```php

## Véase también

DOMDocument::createElement, DOMDocument::createElementNS
