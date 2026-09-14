---
title: DOMDocument::adoptNode
description: Transfiere un nodo de otro documento
source_url: https://www.php.net/manual/es/domdocument.adoptnode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/adoptnode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 12970
---

DOMDocument::adoptNode

Transfiere un nodo de otro documento

## Descripción

```php
public DOMDocument::adoptNode(DOMNode $node): DOMNode
```php

Transfiere un nodo de otro documento al documento actual.

## Parámetros

`node`  
El nodo a transferir.

## Valores devueltos

El nodo que ha sido transferido, o `false` en caso de error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NOT_SUPPORTED_ERR`  
Lanzada si el tipo de nodo no es compatible con las transferencias de documento.

## Ejemplos

Ejemplo de DOMDocument::adoptNode

Transfiere el elemento hello del primer documento al segundo.

```
<?php
$doc1 = new DOMDocument;
$doc1->loadXML("<container><hello><world/></hello></container>");
$hello = $doc1->documentElement->firstChild;

$doc2 = new DOMDocument;
$doc2->loadXML("<root/>");
$doc2->documentElement->appendChild($doc2->adoptNode($hello));

echo $doc1->saveXML() . PHP_EOL . PHP_EOL;
echo $doc2->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <container/>

    <root><hello><world/></hello></root>

## Véase también

DOMDocument::importNode
