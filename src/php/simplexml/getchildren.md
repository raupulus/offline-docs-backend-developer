---
title: SimpleXMLElement::getChildren
description: Devuelve los subelementos del elemento actual
source_url: https://www.php.net/manual/es/simplexmlelement.getchildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/getchildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: dcb657b7e
order: 74540
---

SimpleXMLElement::getChildren

Devuelve los subelementos del elemento actual

## Descripción

```php
public SimpleXMLElement::getChildren(): SimpleXMLElement
```php

> [!WARNING]
> Antes de PHP 8.0, SimpleXMLElement::getChildren solo estaba declarada en la subclase `SimpleXMLIterator`.

Este método devuelve un objeto `SimpleXMLElement` que contiene los subelementos del elemento actual `SimpleXMLElement`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `SimpleXMLElement` que contiene los subelementos del objeto actual.

## Ejemplos

Lectura de los subelementos del objeto actual

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
    foreach($xmlElement->getChildren() as $name => $data) {
    echo "The $name is '$data' from the class " . get_class($data) . "\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    The title is 'PHP Basics' from the class SimpleXMLElement
    The author is 'Jim Smith' from the class SimpleXMLElement
