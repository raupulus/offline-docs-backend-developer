---
title: SimpleXMLElement::getDocNamespaces
description: Devuelve los espacios de nombres declarados en un documento
source_url: https://www.php.net/manual/es/simplexmlelement.getdocnamespaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/getDocNamespaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74510
---

SimpleXMLElement::getDocNamespaces

Devuelve los espacios de nombres declarados en un documento

## Descripción

```php
public SimpleXMLElement::getDocNamespaces([bool $recursive], [bool $fromRoot]): array
```php

Devuelve los espacios de nombres declarados en un documento.

## Parámetros

`recursive`  
Si se especifica, devuelve todos los espacios de nombres declarados en los nodos padres e hijos. De lo contrario, devuelve únicamente los espacios de nombres declarados en el nodo raíz.

`fromRoot`  
Permite verificar recursivamente los espacios de nombres bajo un nodo hijo en lugar de realizar esta verificación desde la raíz del documento XML.

## Valores devueltos

El método `getDocNamespaces` devuelve un array de espacios de nombres con sus URL asociadas.

## Ejemplos

Obtiene los espacios de nombres del documento

```
<?php

$xml = <<<XML

<people xmlns:p="http://example.org/ns">
    <p:person id="1">John Doe</p:person>
    <p:person id="2">Susie Q. Public</p:person>
</people>
XML;

$sxe = new SimpleXMLElement($xml);

$namespaces = $sxe->getDocNamespaces();
var_dump($namespaces);

?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
       ["p"]=>
       string(21) "http://example.org/ns"
    }

Trabajo con múltiples espacios de nombres

```
<?php

$xml = <<<XML

<people xmlns:p="http://example.org/ns" xmlns:t="http://example.org/test">
    <p:person t:id="1">John Doe</p:person>
    <p:person t:id="2" a:addr="123 Street" xmlns:a="http://example.org/addr">
        Susie Q. Public
    </p:person>
</people>
XML;

$sxe = new SimpleXMLElement($xml);

$namespaces = $sxe->getDocNamespaces(TRUE);
var_dump($namespaces);

?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      ["p"]=>
      string(21) "http://example.org/ns"
      ["t"]=>
      string(23) "http://example.org/test"
      ["a"]=>
      string(23) "http://example.org/addr"
    }

## Véase también

SimpleXMLElement::getNamespaces, SimpleXMLElement::registerXPathNamespace
