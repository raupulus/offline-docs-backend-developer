---
title: DOMNode::removeChild
description: Elimina un hijo de la lista de hijos
source_url: https://www.php.net/manual/es/domnode.removechild.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/removechild.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 14080
---

DOMNode::removeChild

Elimina un hijo de la lista de hijos

## Descripción

```php
public DOMNode::removeChild(DOMNode $child): DOMNode
```php

Esta función elimina un hijo de la lista de hijos.

## Parámetros

`child`  
El hijo a eliminar.

## Valores devueltos

Si el hijo no puede ser eliminado, la función devuelve el antiguo hijo o `false` en caso de error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de solo lectura.

`DOM_NOT_FOUND_ERR`  
Lanzado si `child` no es un hijo de este nodo.

## Ejemplos

El siguiente ejemplo elimina el elemento `chapter` de nuestro documento XML.

Eliminación de un hijo

```
<?php

$doc = new DOMDocument;
$doc->load('examples/book-docbook.xml');

$book = $doc->documentElement;

// Se recupera el capítulo y se elimina del libro
$chapter = $book->getElementsByTagName('chapter')->item(0);
$oldchapter = $book->removeChild($chapter);

echo $doc->saveXML();
?>
    
```php

El ejemplo anterior mostrará:

```
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.1.2//EN"
          "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd">
<book id="listing">
 <title>My lists</title>

</book>

    
```php

## Véase también

DOMChildNode::remove, DOMNode::appendChild, DOMNode::replaceChild
