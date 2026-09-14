---
title: SimpleXMLElement::addChild
description: Añade un elemento hijo al nodo XML
source_url: https://www.php.net/manual/es/simplexmlelement.addchild.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/addChild.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: dca2a8354
order: 74440
---

SimpleXMLElement::addChild

Añade un elemento hijo al nodo XML

## Descripción

```php
public SimpleXMLElement::addChild(string $qualifiedName, [string $value], [string $namespace]): SimpleXMLElement
```php

Añade un elemento hijo al nodo y devuelve un SimpleXMLElement del hijo.

## Parámetros

`qualifiedName`  
El nombre del elemento hijo a añadir.

`value`  
Si se especifica, el valor del elemento hijo.

Los caracteres especiales `<` y `>` se escapan automáticamente, `&` debe escaparse manualmente.

`namespace`  
Si se especifica, el espacio de nombres al que pertenece el elemento hijo.

## Valores devueltos

El método `addChild` devuelve un objeto `SimpleXMLElement` que representa al hijo a añadir al nodo XML en caso de éxito; `null` en caso de fallo.

## Ejemplos

> [!NOTE]
> Los ejemplos listados incluyen a veces `examples/simplexml-data.php`, esto hace referencia a la cadena XML del primer ejemplo de [el uso básico](#simplexml.examples-basic).

Añade atributos y elementos hijos a un elemento SimpleXML

```
<?php

include 'examples/simplexml-data.php';

$sxe = new SimpleXMLElement($xmlstr);
$sxe->addAttribute('type', 'documentary');

$movie = $sxe->addChild('movie');
$movie->addChild('title', 'PHP2: More Parser Stories');
$movie->addChild('plot', 'This is all about the people who make it work.');

$characters = $movie->addChild('characters');
$character  = $characters->addChild('character');
$character->addChild('name', 'Mr. Parser');
$character->addChild('actor', 'John Doe');

$rating = $movie->addChild('rating', '5');
$rating->addAttribute('type', 'stars');

echo $sxe->asXML();

?>

    
```php

Resultado del ejemplo anterior es similar a:

    <movies type="documentary">
     <movie>
      <title>PHP: Behind the Parser</title>
      <characters>
       <character>
        <name>Ms. Coder</name>
        <actor>Onlivia Actora</actor>
       </character>
       <character>
        <name>Mr. Coder</name>
        <actor>El Act&#xD3;r</actor>
       </character>
      </characters>
      <plot>
       So, this language. It's like, a programming language. Or is it a
       scripting language? All is revealed in this thrilling horror spoof
       of a documentary.
      </plot>
      <great-lines>
       <line>PHP solves all my web problems</line>
      </great-lines>
      <rating type="thumbs">7</rating>
      <rating type="stars">5</rating>
     </movie>
     <movie>
      <title>PHP2: More Parser Stories</title>
      <plot>This is all about the people who make it work.</plot>
      <characters>
       <character>
        <name>Mr. Parser</name>
        <actor>John Doe</actor>
       </character>
      </characters>
      <rating type="stars">5</rating>
     </movie>
    </movies>

## Véase también

SimpleXMLElement::addAttribute, [???](#simplexml.examples-basic)
