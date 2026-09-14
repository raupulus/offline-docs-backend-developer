---
title: SimpleXMLElement::next
description: Se desplaza al elemento siguiente
source_url: https://www.php.net/manual/es/simplexmlelement.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: dcb657b7e
order: 74570
---

SimpleXMLElement::next

Se desplaza al elemento siguiente

## Descripción

```php
public SimpleXMLElement::next(): void
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::next solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método desplaza el iterador `SimpleXMLElement` al elemento siguiente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Pasa al elemento siguiente

```
<?php
$xmlElement = new SimpleXMLElement('<books><book>PHP Basics</book><book>XML basics</book></books>');
$xmlElement->rewind(); // rewind al primer elemento
$xmlElement->next();

var_dump($xmlElement->current());
?>

    
```php

El ejemplo anterior mostrará:

    object(SimpleXMLElement)#2 (1) {
      [0]=>
      string(10) "XML basics"
    }
