---
title: DOMDocument::createElementNS
description: Crea un nuevo nodo elemento con el nombre de espacio asociado
source_url: https://www.php.net/manual/es/domdocument.createelementns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createelementns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13060
---

DOMDocument::createElementNS

Crea un nuevo nodo elemento con el nombre de espacio asociado

## Descripción

```php
public DOMDocument::createElementNS(string $namespace, string $qualifiedName, [string $value]): DOMElement
```php

Esta función crea un nuevo nodo elemento con el nombre de espacio asociado. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`namespace`  
El URI del nombre de espacio.

`qualifiedName`  
Elo nombre cualificado del elemento, como `prefix:tagname`.

`value`  
El valor del elemento. De manera predeterminada se creará un elemento vacio. El valor también puede ser asignado más tarde con [DOMElement::\$nodeValue](#domnode.props.nodevalue).

## Valores devueltos

El nuevo `DOMElement` o `false` si ha ocurrido un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INVALID_CHARACTER_ERR`  
Lanzado si `qualifiedName` contiene un carácter inválido.

`DOM_NAMESPACE_ERR`  
Lanzado si `qualifiedName` es un nombre cualificado mal formado.

## Ejemplos

Crear un nuevo elemento e insertarlo como raíz

```
<?php

$dom = new DOMDocument('1.0', 'utf-8');

$element = $dom->createElementNS('http://www.example.com/XFoo', 'xfoo:test', 'This is the root element!');

// Insertamos el nuevo elemento como raíz (hijo del documento)
$dom->appendChild($element);

echo $dom->saveXML();
?>

    
```php

El ejemplo anterior mostrará:

```
<xfoo:test xmlns:xfoo="http://www.example.com/XFoo">This is the root element!</xfoo:test>

    
```php

Un ejemplo de prefijo de nombre de espacio

```
<?php
$doc  = new DOMDocument('1.0', 'utf-8');
$doc->formatOutput = true;
$root = $doc->createElementNS('http://www.w3.org/2005/Atom', 'element');
$doc->appendChild($root);
$root->setAttributeNS('http://www.w3.org/2000/xmlns/' ,'xmlns:g', 'http://base.google.com/ns/1.0');
$item = $doc->createElementNS('http://base.google.com/ns/1.0', 'g:item_type', 'house');
$root->appendChild($item);

echo $doc->saveXML(), "\n";

echo $item->namespaceURI, "\n"; // Imprime: http://base.google.com/ns/1.0
echo $item->prefix, "\n";       // Imprime: g
echo $item->localName, "\n";    // Imprime: item_type
?>

    
```php

El ejemplo anterior mostrará:

```
<element xmlns="http://www.w3.org/2005/Atom" xmlns:g="http://base.google.com/ns/1.0">
  <g:item_type>house</g:item_type>
</element>

http://base.google.com/ns/1.0
g
item_type

    
```php

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
