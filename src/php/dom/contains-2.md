---
title: DOMNode::contains
description: Verifica si un nodo contiene otro nodo
source_url: https://www.php.net/manual/es/domnode.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: cdbee08c7
order: 13940
---

DOMNode::contains

Verifica si un nodo contiene otro nodo

## Descripción

```php
public DOMNode::contains(DOMNode $other): bool
```php

Verifica si el nodo contiene el otro nodo `other`.

## Parámetros

`other`  
El nodo a verificar.

## Valores devueltos

Devuelve `true` si el nodo contiene el nodo `other`, en caso contrario `false`.

## Ejemplos

Ejemplo de DOMNode::contains

```
<?php

$dom = new DOMDocument();
$dom->loadXML(<<<XML
<!DOCTYPE HTML>
<html>
   <body>
       <main>
           <p>Hello, world!</p>
       </main>
   </body>
</html>
XML);

$xpath = new DOMXPath($dom);
$main = $xpath->query("//main")[0];

var_dump($dom->documentElement->contains($main));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
