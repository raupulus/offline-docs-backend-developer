---
title: DOMNodeList::item
description: Devuelve un nodo especificado por su índice
source_url: https://www.php.net/manual/es/domnodelist.item.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnodelist/item.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1f37a6c2
order: 14150
---

DOMNodeList::item

Devuelve un nodo especificado por su índice

## Descripción

```php
public DOMNodeList::item(int $index): DOMElement
```php

Devuelve un nodo especificado por su `index` en el objeto `DOMNodeList`.

> [!TIP]
> Si se necesita conocer el número de nodos en la colección, utilice la propiedad `length` del objeto `DOMNodeList`.

## Parámetros

`index`  
El índice del nodo en la colección.

## Valores devueltos

El nodo en la posición `index` en la `DOMNodeList`, o `null` si no es un índice válido.

## Ejemplos

Recorrido de todas las entradas de la tabla

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book-docbook.xml');

$items = $doc->getElementsByTagName('entry');

for ($i = 0; $i < $items->length; $i++) {
    echo $items->item($i)->nodeValue . "\n";
}
?>

    
```php

Acceder a un elemento con la sintaxis de array

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book-docbook.xml');

$items = $doc->getElementsByTagName('entry');

for ($i = 0; $i < $items->length; $i++) {
    echo $items[$i]->nodeValue . "\n";
}

?>

    
```php

Recorrer los elementos con [`foreach`](#control-structures.foreach)

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book-docbook.xml');

$items = $doc->getElementsByTagName('entry');

foreach ($items as $item) {
    echo $item->nodeValue . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Title
    Author
    Language
    ISBN
    The Grapes of Wrath
    John Steinbeck
    en
    0140186409
    The Pearl
    John Steinbeck
    en
    014017737X
    Samarcande
    Amine Maalouf
    fr
    2253051209
