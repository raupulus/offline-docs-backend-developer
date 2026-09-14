---
title: SimpleXMLElement::getName
description: Obtiene el nombre de un elemento XML
source_url: https://www.php.net/manual/es/simplexmlelement.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/getName.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 74520
---

SimpleXMLElement::getName

Obtiene el nombre de un elemento XML

## Descripción

```php
public SimpleXMLElement::getName(): string
```php

Obtiene el nombre de un elemento XML.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El método `getName` devuelve un nombre en forma de string de una etiqueta XML referenciada por el objeto SimpleXMLElement.

## Ejemplos

> [!NOTE]
> Los ejemplos listados incluyen a veces `examples/simplexml-data.php`, esto hace referencia a la cadena XML del primer ejemplo de [el uso básico](#simplexml.examples-basic).

Obtiene los nombres de los elementos XML

```
<?php
include 'examples/simplexml-data.php';
$sxe = new SimpleXMLElement($xmlstr);

echo $sxe->getName() . "\n";

foreach ($sxe->children() as $child)
{
    echo $child->getName() . "\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    movies
    movie
