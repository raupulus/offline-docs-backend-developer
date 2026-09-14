---
title: DOMElement::insertAdjacentText
description: Inserta un texto adyacente
source_url: https://www.php.net/manual/es/domelement.insertadjacenttext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/insertadjacenttext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: cdbee08c7
order: 13540
---

DOMElement::insertAdjacentText

Inserta un texto adyacente

## Descripción

```php
public DOMElement::insertAdjacentText(string $where, string $data): void
```php

Inserta un texto en una posición relativa dada por `where`.

## Parámetros

`where`  
`beforebegin` - Inserta antes del elemento objetivo., `afterbegin` - Inserta como primer hijo del elemento objetivo., `beforeend` - Inserta como último hijo del elemento objetivo., `afterend` - Inserta después del elemento objetivo.

`data`  
El string a insertar.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de DOMElement::insertAdjacentText

```
<?php

$dom = new DOMDocument();
$dom->loadXML('<container><p>H</p></container>');

$container = $dom->documentElement;
$p = $container->firstElementChild;

$p->insertAdjacentText("afterbegin", "P");
$p->insertAdjacentText("beforeend", "P");

echo $dom->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container><p>PHP</p></container>

## Véase también

DOMElement::insertAdjacentElement
