---
title: SimpleXMLElement::valid
description: Verifica si el elemento actual es válido
source_url: https://www.php.net/manual/es/simplexmlelement.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: dcb657b7e
order: 74620
---

SimpleXMLElement::valid

Verifica si el elemento actual es válido

## Descripción

```php
public SimpleXMLElement::valid(): bool
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::valid solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método verifica si el elemento actual es válido, después de una llamada a SimpleXMLElement::rewind o SimpleXMLElement::next.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el elemento actual es válido, `false` en caso contrario.

## Ejemplos

Verifica si un elemento es válido

```
<?php
$xmlElement = new SimpleXMLElement('<books><book>SQL Basics</book></books>');

$xmlElement->rewind(); // Retorno al primer elemento
echo var_dump($xmlElement->valid()); // bool(true)

$xmlElement->next(); // Avance al siguiente elemento
echo var_dump($xmlElement->valid()); // bool(false) ya que solo hay un elemento
?>

    
```php
