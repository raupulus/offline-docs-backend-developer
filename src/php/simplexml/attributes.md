---
title: SimpleXMLElement::attributes
description: Identifica los atributos de un elemento
source_url: https://www.php.net/manual/es/simplexmlelement.attributes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/attributes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74460
---

SimpleXMLElement::attributes

Identifica los atributos de un elemento

## Descripción

```php
public SimpleXMLElement::attributes([string $namespaceOrPrefix], [bool $isPrefix]): SimpleXMLElement
```php

Proporciona los atributos y los valores definidos en una etiqueta XML.

> [!NOTE]
> SimpleXML añade propiedades iterativas para casi todos sus métodos. Estas no pueden ser vistas utilizando `var_dump` o cualquier otra función que examine los objetos.

## Parámetros

`namespaceOrPrefix`  
Un espacio de nombres opcional para los atributos recuperados

`isPrefix`  
Por omisión, vale `false`

## Valores devueltos

Devuelve un objeto `SimpleXMLElement` que permite recuperar todos los atributos de una etiqueta.

Devuelve `null` si se invoca sobre un objeto `SimpleXMLElement` que representa ya un atributo y no una etiqueta.

## Ejemplos

Interpretación de una cadena XML

```
<?php
$string = <<<XML
<a>
 <foo name="one" game="lonely">1</foo>
</a>
XML;

$xml = simplexml_load_string($string);
foreach($xml->foo[0]->attributes() as $a => $b) {
    echo $a,'="',$b,"\"\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    name="one"
    game="lonely"

## Véase también

[???](#simplexml.examples-basic)
