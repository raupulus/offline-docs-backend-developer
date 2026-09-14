---
title: SimpleXMLElement::current
description: Retorna la entrada actual
source_url: https://www.php.net/manual/es/simplexmlelement.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 523e43a7d
order: 74500
---

SimpleXMLElement::current

Retorna la entrada actual

## Descripción

```php
public SimpleXMLElement::current(): SimpleXMLElement
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::current solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método retorna el elemento actual como un objeto `SimpleXMLElement`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna el elemento actual como un objeto `SimpleXMLElement`.

## Errores/Excepciones

Se lanza una `Error` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Se lanza una `Error` si SimpleXMLElement::current es llamada sobre un iterador inválido. Anteriormente, se retornaba `null`. |

## Ejemplos

Retorna el elemento actual

```
<?php
$xmlElement = new SimpleXMLElement('<books><book>PHP basics</book><book>XML basics</book></books>');

$xmlElement->rewind(); // Retorno al primer elemento, de lo contrario current() no funciona
var_dump($xmlElement->current());
?>

    
```php

El ejemplo anterior mostrará:

    object(SimpleXMLElement)#2 (1) {
      [0]=>
      string(10) "PHP basics"
    }

## Véase también

SimpleXMLElement::key, SimpleXMLElement::next, SimpleXMLElement::rewind, SimpleXMLElement::valid, `SimpleXMLElement`
