---
title: XSLTProcessor::transformToDoc
description: Transforma en un documento
source_url: https://www.php.net/manual/es/xsltprocessor.transformtodoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/transformtodoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: true
translation_revision: 01904e809
order: 104210
---

XSLTProcessor::transformToDoc

Transforma en un documento

## Descripción

```php
public XSLTProcessor::transformToDoc(object $document, [string $returnClass]): object
```php

Transforma el nodo fuente en un documento (por ejemplo, `DOMDocument`) aplicando la hoja de estilo dada por el método `XSLTProcessor::importStylesheet`.

## Parámetros

`document`  
El `Dom\Document`, `DOMDocument`, `SimpleXMLElement` o un objeto compatible con libxml a transformar.

`returnClass`  
Este parámetro opcional puede ser utilizado para que XSLTProcessor::transformToDoc devuelva un objeto de la clase especificada. Esta clase debe extender o ser la misma clase que la de `document`.

## Valores devueltos

El documento resultante o `false` si ocurre un error.

## Ejemplos

Transformación en `DOMDocument`

```
<?php

// Carga de la fuente XML
$xml = new DOMDocument;
$xml->load('collection.xml');

$xsl = new DOMDocument;
$xsl->load('collection.xsl');

// Configuración del transformador
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl); // adjuntar las reglas xsl

echo trim($proc->transformToDoc($xml)->firstChild->wholeText);

?>

    
```php

El ejemplo anterior mostrará:

    ¡Hola! Bienvenido a la increíble colección de CD de Nicolas Eliaszewicz.

Transformación en `Dom\Document`

```
<?php

$xml = Dom\XMLDocument::createFromFile('collection.xml');
$xsl = Dom\XMLDocument::createFromFile('collection.xsl');

// Configuración del transformador
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl); // adjuntar las reglas xsl

echo trim($proc->transformToDoc($xml)->firstChild->wholeText);

?>

    
```php

El ejemplo anterior mostrará:

    ¡Hola! Bienvenido a la increíble colección de CD de Nicolas Eliaszewicz.

## Véase también

`XSLTProcessor::transformToUri`, `XSLTProcessor::transformToXml`
