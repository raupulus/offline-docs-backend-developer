---
title: SimpleXMLElement::__toString
description: Devuelve el contenido como string
source_url: https://www.php.net/manual/es/simplexmlelement.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/toString.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: true
translation_revision: 770c6faca
order: 74610
---

SimpleXMLElement::\_\_toString

Devuelve el contenido como string

## Descripción

```php
public SimpleXMLElement::__toString(): string
```php

Devuelve el contenido de texto almacenado directamente en el elemento. No devuelve el contenido de texto almacenado en los elementos hijos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido como string, o un string vacío en caso de error.

## Ejemplos

Obtener el contenido como string

```
<?php
$xml = new SimpleXMLElement('<a>1 <b>2 </b>3</a>');
echo $xml;
?>

    
```php

El ejemplo anterior mostrará:

    1 3

## Véase también

SimpleXMLElement::asXML
