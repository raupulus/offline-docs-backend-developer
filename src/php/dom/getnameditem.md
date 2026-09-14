---
title: DOMNamedNodeMap::getNamedItem
description: Devuelve un nodo especificado por su nombre
source_url: https://www.php.net/manual/es/domnamednodemap.getnameditem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnamednodemap/getnameditem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1f37a6c2
order: 13820
---

DOMNamedNodeMap::getNamedItem

Devuelve un nodo especificado por su nombre

## Descripción

```php
public DOMNamedNodeMap::getNamedItem(string $qualifiedName): DOMNode
```php

Obtiene un nodo especificado por su `nodeName`.

## Parámetros

`qualifiedName`  
El `nodeName` del nodo a recuperar.

## Valores devueltos

Un nodo (de cualquier tipo) con un `nodeName` especificado, o `null` si no se encuentra ningún nodo.

## Ejemplos

Recuperar un atributo en un nodo

```
<?php

$doc = new DOMDocument;
$doc->load('examples/book.xml');

$id = $doc->firstChild->nextSibling->nextSibling->firstChild->nextSibling->attributes->getNamedItem('id');
?>

   
```php

Acceder a un elemento con la sintaxis de array

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book.xml');

$id = $doc->firstChild->nextSibling->nextSibling->firstChild->nextSibling->attributes['id'];
?>

   
```php

## Véase también

DOMNamedNodeMap::getNamedItemNS
