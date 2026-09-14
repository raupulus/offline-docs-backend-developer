---
title: DOMElement::insertAdjacentElement
description: Inserta un elemento adyacente
source_url: https://www.php.net/manual/es/domelement.insertadjacentelement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/insertadjacentelement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: cdbee08c7
order: 13530
---

DOMElement::insertAdjacentElement

Inserta un elemento adyacente

## Descripción

```php
public DOMElement::insertAdjacentElement(string $where, DOMElement $element): DOMElement
```php

Inserta un elemento en una posición relativa dada por `where`.

## Parámetros

`where`  
`beforebegin` - Inserta antes del elemento objetivo., `afterbegin` - Inserta como primer hijo del elemento objetivo., `beforeend` - Inserta como último hijo del elemento objetivo., `afterend` - Inserta después del elemento objetivo.

`element`  
El elemento a insertar.

## Valores devueltos

Devuelve `DOMElement` o `null` en caso de fallo.

## Ejemplos

Ejemplo de DOMElement::insertAdjacentElement

```
<?php

$dom = new DOMDocument();
$dom->loadXML('<container><p>foo</p></container>');
$container = $dom->documentElement;
$p = $container->firstElementChild;

$p->insertAdjacentElement('beforebegin', $dom->createElement('A'));
echo $dom->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><A/><p>foo</p></container>

## Véase también

DOMElement::insertAdjacentText
