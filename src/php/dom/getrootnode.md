---
title: DOMNode::getRootNode
description: Devuelve el nodo raíz
source_url: https://www.php.net/manual/es/domnode.getrootnode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/getrootnode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: d715365c0
order: 13970
---

DOMNode::getRootNode

Devuelve el nodo raíz

## Descripción

```php
public DOMNode::getRootNode([array $options]): DOMNode
```php

Devuelve el nodo raíz.

## Parámetros

`options`  
Este argumento no tiene efecto aún.

## Valores devueltos

Devuelve el nodo raíz.

## Ejemplos

Ejemplo de DOMNode::getRootNode

```
<?php

$dom = new DOMDocument();
$dom->loadXML('<html><body/></html>');

var_dump($dom->documentElement->firstElementChild->getRootNode() === $dom);
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
