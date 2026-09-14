---
title: DOMDocumentFragment::appendXML
description: Añade información XML sin formato
source_url: https://www.php.net/manual/es/domdocumentfragment.appendxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocumentfragment/appendxml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13340
---

DOMDocumentFragment::appendXML

Añade información XML sin formato

## Descripción

```php
public DOMDocumentFragment::appendXML(string $data): bool
```php

Añade información XML sin formato a un DOMDocumentFragment.

Este método no es parte del estándar DOM. Fue creado como enfoque más sencillo para añadir un DocumentFragment de XML a un DOMDocument.

Si quiere mantener los estándares, tendrá que crear un DOMDocument temporal con una raíz cualquiera y después ir a través de los nodos hijo de la raíz de su información XML para añadirlos.

## Parámetros

`data`  
XML a añadir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Añadir información XML a su documento

```
<?php
$doc = new DOMDocument();
$doc->loadXML("<root/>");
$f = $doc->createDocumentFragment();
$f->appendXML("<foo>text</foo><bar>text2</bar>");
$doc->documentElement->appendChild($f);
echo $doc->saveXML();
?>

    
```php

El ejemplo anterior mostrará:

```
<root><foo>text</foo><bar>text2</bar></root>

    
```php
