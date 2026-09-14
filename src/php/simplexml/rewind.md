---
title: SimpleXMLElement::rewind
description: Reemplaza el puntero al inicio
source_url: https://www.php.net/manual/es/simplexmlelement.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: dcb657b7e
order: 74590
---

SimpleXMLElement::rewind

Reemplaza el puntero al inicio

## Descripción

```php
public SimpleXMLElement::rewind(): void
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::rewind solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método reinicia el iterador `SimpleXMLElement` al primer elemento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Retorno al primer elemento

```
<?php
$xmlElement = new SimpleXMLElement('<books><book>PHP Basics</book><book>XML Basics</book></books>');
$xmlElement->rewind();

var_dump($xmlElement->current());
?>

    
```php

El ejemplo anterior mostrará:

    object(SimpleXMLElement)#2 (1) {
      [0]=>
      string(10) "PHP Basics"
    }
