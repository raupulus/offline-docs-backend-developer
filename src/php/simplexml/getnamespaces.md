---
title: SimpleXMLElement::getNamespaces
description: Devuelve los espacios de nombres utilizados en un documento
source_url: https://www.php.net/manual/es/simplexmlelement.getnamespaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/getNamespaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74530
---

SimpleXMLElement::getNamespaces

Devuelve los espacios de nombres utilizados en un documento

## Descripción

```php
public SimpleXMLElement::getNamespaces([bool $recursive]): array
```php

Devuelve los espacios de nombres utilizados en un documento.

## Parámetros

`recursive`  
Si se especifica, devuelve todos los espacios de nombres utilizados en los nodos padres e hijos. De lo contrario, devuelve únicamente los espacios de nombres utilizados en el nodo raíz.

## Valores devueltos

El método `getNamespaces` devuelve un array de espacios de nombres con sus URL asociadas.

## Ejemplos

Obtiene los espacios de nombres utilizados en un documento

```
<?php

$xml = <<<XML

<people xmlns:p="http://example.org/ns" xmlns:t="http://example.org/test">
    <p:person id="1">John Doe</p:person>
    <p:person id="2">Susie Q. Public</p:person>
</people>
XML;

$sxe = new SimpleXMLElement($xml);

$namespaces = $sxe->getNamespaces(true);
var_dump($namespaces);

?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["p"]=>
      string(21) "http://example.org/ns"
    }

## Véase también

SimpleXMLElement::getDocNamespaces, SimpleXMLElement::registerXPathNamespace
