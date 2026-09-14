---
title: DOMNode::isEqualNode
description: Comprueba si los dos nodos son iguales
source_url: https://www.php.net/manual/es/domnode.isequalnode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/isequalnode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: cdbee08c7
order: 14020
---

DOMNode::isEqualNode

Comprueba si los dos nodos son iguales

## Descripción

```php
public DOMNode::isEqualNode(DOMNode $otherNode): bool
```php

Comprueba si los dos nodos son iguales.

## Parámetros

`otherNode`  
El nodo.

## Valores devueltos

Devuelve `true` si los dos nodos son iguales, en caso contrario `false`.

## Ejemplos

Ejemplo de DOMNode::isEqualNode

```
<?php

$dom1 = (new DOMDocument())->createElement('h1', 'Hello World!');
$dom2 = (new DOMDocument())->createElement('h1', 'Hello World!');

var_dump($dom1->isEqualNode($dom2));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
