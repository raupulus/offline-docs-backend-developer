---
title: DOMNode::appendChild
description: Añade un nuevo hijo al final de los hijos
source_url: https://www.php.net/manual/es/domnode.appendchild.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/appendchild.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13890
---

DOMNode::appendChild

Añade un nuevo hijo al final de los hijos

## Descripción

```php
public DOMNode::appendChild(DOMNode $node): DOMNode
```php

Esta función agrega un hijo a una lista existente de hijos o crea una nueva lista de hijos. El hijo se puede crear con, p.ej., DOMDocument::createElement, DOMDocument::createTextNode etc. o simplemente usando cualquier otro nodo.

Si se utiliza un nodo existente, éste se desplazará.

## Parámetros

`node`  
El hijo añadido.

## Valores devueltos

El nodo añadido o `false` en caso de error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si este nodo es de sólo lectura o si el padre previo del nodo a ser insertado es de sólo lectura.

`DOM_HIERARCHY_REQUEST_ERR`  
Lanzado si este nodo es de un tipo de no permite hijos del tipo del nodo `node`, o si el nodo a añadir es uno de los progenitores del nodo o si es el nodo en sí.

`DOM_WRONG_DOCUMENT_ERR`  
Lanzado si `node` fue creado desde un documento diferente del que creó este nodo.

## Ejemplos

El siguiente ejemplo añadirá un nuevo nodo elemento a un nuevo documento.

Añadiendo un hijo

```
<?php

$doc = new DOMDocument;

$nodo = $doc->createElement("para");
$nuevo_nodo = $doc->appendChild($nodo);

echo $doc->saveXML();
?>

    
```php

Hijos anidados

```
<?php

$doc = new DOMDocument;

$headNode = $doc->createElement("head");
$doc->appendChild($headNode);

$titleNode = $doc->createElement("title");
$headNode->appendChild($titleNode);

echo $doc->saveXML();
?>

    
```php

## Véase también

DOMChildNode::after, DOMNode::insertBefore, DOMNode::removeChild, DOMNode::replaceChild
