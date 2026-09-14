---
title: SimpleXMLElement::addAttribute
description: Añade un atributo al elemento SimpleXML
source_url: https://www.php.net/manual/es/simplexmlelement.addattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/addAttribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 74430
---

SimpleXMLElement::addAttribute

Añade un atributo al elemento SimpleXML

## Descripción

```php
public SimpleXMLElement::addAttribute(string $qualifiedName, string $value, [string $namespace]): void
```php

Añade un atributo al elemento SimpleXML.

## Parámetros

`qualifiedName`  
El nombre del atributo a añadir.

`value`  
El valor del atributo.

`namespace`  
Si se especifica, el espacio de nombres al que pertenece el atributo.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

> [!NOTE]
> Los ejemplos listados incluyen a veces `example/simplexml-data.php`, esto hace referencia a la cadena XML del primer ejemplo de [uso básico](#simplexml.examples-basic).

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

SimpleXMLElement::addChild, [???](#simplexml.examples-basic)
