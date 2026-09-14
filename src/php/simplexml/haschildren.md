---
title: SimpleXMLElement::hasChildren
description: Verifica si el elemento actual tiene subelementos
source_url: https://www.php.net/manual/es/simplexmlelement.haschildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/haschildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: dcb657b7e
order: 74550
---

SimpleXMLElement::hasChildren

Verifica si el elemento actual tiene subelementos

## Descripción

```php
public SimpleXMLElement::hasChildren(): bool
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::hasChildren solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método verifica si el objeto actual `SimpleXMLElement` tiene subelementos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la entrada actual tiene subelementos, `false` en caso contrario.

## Ejemplos

Verifica si un elemento tiene subelementos

```
<?php
$xml = <<<XML
<books>
    <book>
        <title>PHP Basics</title>
        <author>Jim Smith</author>
    </book>
    <book>XML basics</book>
</books>
XML;

$xmlElement = new SimpleXMLElement($xml);
for ($xmlElement->rewind(); $xmlElement->valid(); $xmlElement->next()) {
    if ($xmlElement->hasChildren()) {
        var_dump($xmlElement->current());
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    object(SimpleXMLElement)#2 (2) {
      ["title"]=>
      string(10) "PHP Basics"
      ["author"]=>
      string(9) "Jim Smith"
    }
