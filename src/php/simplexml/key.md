---
title: SimpleXMLElement::key
description: Devuelve la clave actual
source_url: https://www.php.net/manual/es/simplexmlelement.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: d6f54016d
order: 74560
---

SimpleXMLElement::key

Devuelve la clave actual

## Descripción

```php
public SimpleXMLElement::key(): string
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::key solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método lee el nombre de la etiqueta XML actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de la etiqueta XML en el objeto actual del iterador `SimpleXMLElement`.

## Errores/Excepciones

Se lanza una `Error` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora se lanza una `Error` si SimpleXMLElement::key se llama sobre un iterador no válido. Anteriormente, se devolvía `false`. |

## Ejemplos

El nombre de la etiqueta XML actual

```
<?php
$xmlElement = new SimpleXMLElement('<books><book>PHP basics</book><book>XML basics</book></books>');

try {
    echo var_dump($xmlElement->key());
} catch (Error $e) {
    echo $e->getMessage(), "\n";
}

$xmlElement->rewind(); // retorno al primer elemento
echo var_dump($xmlElement->key());

?>

    
```php

El ejemplo anterior mostrará:

    Iterator not initialized or already consumed
    string(4) "book"
