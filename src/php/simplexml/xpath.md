---
title: SimpleXMLElement::xpath
description: Ejecuta una consulta XPath sobre datos XML
source_url: https://www.php.net/manual/es/simplexmlelement.xpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/xpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74630
---

SimpleXMLElement::xpath

Ejecuta una consulta XPath sobre datos XML

## Descripción

```php
public SimpleXMLElement::xpath(string $expression): array
```php

El método `xpath` busca en el nodo SimpleXML hijos que correspondan al `expression` Xpath.

## Parámetros

`expression`  
Una ruta XPath

## Valores devueltos

Devuelve un array de objetos SimpleXMLElement en caso de éxito o `null` o `false` si ocurre un error.

## Ejemplos

Xpath

```
<?php
$string = <<<XML
<a>
 <b>
  <c>text</c>
  <c>stuff</c>
 </b>
 <d>
  <c>code</c>
 </d>
</a>
XML;

$xml = new SimpleXMLElement($string);

/* Se busca <a><b><c> */
$result = $xml->xpath('/a/b/c');

foreach ($result as $node) {
    echo '/a/b/c: ',$node,"\n";
}

/* Las rutas relativas también funcionan... */
$result = $xml->xpath('b/c');

foreach ($result as $node) {
    echo 'b/c: ',$node,"\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    /a/b/c: text
    /a/b/c: stuff
    b/c: text
    b/c: stuff

        

Observe que los dos resultados son iguales.

## Véase también

SimpleXMLElement::registerXPathNamespace, SimpleXMLElement::getDocNamespaces, SimpleXMLElement::getNamespaces, [???](#simplexml.examples-basic)
