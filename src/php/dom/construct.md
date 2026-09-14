---
title: DOMAttr::__construct
description: Crea un nuevo objeto DOMAttr
source_url: https://www.php.net/manual/es/domattr.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domattr/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d6f54016d
order: 12750
---

DOMAttr::\_\_construct

Crea un nuevo objeto

DOMAttr

## Descripción

```php
public DOMAttr::__construct(string $name, [string $value])
```php

Crea un nuevo objeto DOMAttr. Este objeto es de solo lectura. Puede ser añadido a un documento, pero los nodos adicionales no pueden ser añadidos a este nodo mientras este nodo esté asociado a un documento. Para crear un nodo accesible en escritura, utilice [???](#domdocument.createattribute).

## Parámetros

`name`  
El nombre del atributo.

`value`  
El valor del atributo.

## Ejemplos

Creación de un nuevo objeto `DOMAttr`

```
<?php

$dom = new DOMDocument('1.0', 'utf-8');
$element = $dom->appendChild(new DOMElement('root'));
$attr = $element->setAttributeNode(new DOMAttr('attr', 'attrvalue'));
echo $dom->saveXML();

?>

    
```php

El ejemplo anterior mostrará:

    <root attr="attrvalue"/>

## Véase también

DOMDocument::createAttribute
