---
title: DOMDocument::getElementById
description: Busca un elemento con un cierto identificador
source_url: https://www.php.net/manual/es/domdocument.getelementbyid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/getelementbyid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 13100
---

DOMDocument::getElementById

Busca un elemento con un cierto identificador

## Descripción

```php
public DOMDocument::getElementById(string $elementId): DOMElement
```php

Esta función es similar a la función [???](#domdocument.getelementsbytagname) pero busca un elemento con un identificador dado.

Para que esta función funcione, es necesario definir los atributos ID con [???](#domelement.setidattribute) o definir una DTD que defina un atributo que debe ser de tipo ID. En el último caso, es necesario validar el documento con [???](#domdocument.validate) o [DOMDocument::\$validateOnParse](#domdocument.props.validateonparse) antes de utilizar esta función.

## Parámetros

`elementId`  
El valor del identificador único para un elemento.

## Valores devueltos

Devuelve un `DOMElement` o `null` si el elemento no es encontrado.

## Ejemplos

Ejemplo con DOMDocument::getElementById()

El siguiente ejemplo utiliza el archivo `book.xml`, cuyo contenido es:

```
<!DOCTYPE books [
  <!ELEMENT books   (book+)>
  <!ELEMENT book    (title, author+, xhtml:blurb?)>
  <!ELEMENT title   (#PCDATA)>
  <!ELEMENT blurb   (#PCDATA)>
  <!ELEMENT author  (#PCDATA)>
  <!ATTLIST books   xmlns        CDATA  #IMPLIED>
  <!ATTLIST books   xmlns:xhtml  CDATA  #IMPLIED>
  <!ATTLIST book    id           ID     #IMPLIED>
  <!ATTLIST author  email        CDATA  #IMPLIED>
]>

<books xmlns="http://books.php/" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <book id="php-basics">
    <title>PHP Basics</title>
    <author email="jim.smith@basics.php">Jim Smith</author>
    <author email="jane.smith@basics.php">Jane Smith</author>
    <xhtml:blurb><![CDATA[
<p><em>PHP Basics</em> provides an introduction to PHP.</p>
]]></xhtml:blurb>
  </book>
  <book id="php-advanced">
    <title>PHP Advanced Programming</title>
    <author email="jon.doe@advanced.php">Jon Doe</author>
  </book>
</books>
```php

```
<?php

$doc = new DomDocument;

// Es necesario validar el documento antes de referirse al ID
$doc->validateOnParse = true;
$doc->load('examples/book.xml');

echo "El elemento cuyo ID es 'php-basics' es: " . $doc->getElementById('php-basics')->tagName . "\n";

?>

   
```php

El ejemplo anterior mostrará:

    El elemento cuyo ID es 'php-basics' es: chapter

## Véase también

DOMDocument::getElementsByTagName
