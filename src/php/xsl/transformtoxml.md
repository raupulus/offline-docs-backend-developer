---
title: XSLTProcessor::transformToXml
description: Transformar en XML
source_url: https://www.php.net/manual/es/xsltprocessor.transformtoxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/transformtoxml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 01904e809
order: 104230
---

XSLTProcessor::transformToXml

Transformar en XML

## Descripción

```php
public XSLTProcessor::transformToXml(object $document): string
```php

Transforma el nodo fuente en una cadena aplicando una hoja de estilo dada por el método `xsltprocessor::importStylesheet`.

## 

## Valores devueltos

El resultado de la transformación como una cadena de caracteres o `false` si ocurre un error.

## Ejemplos

Transformación en una cadena

```
<?php

// Cargar la fuente XML
$xml = new DOMDocument;
$xml->load('collection.xml');

$xsl = new DOMDocument;
$xsl->load('collection.xsl');

// Configurar el transformador
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl); // adjuntar las reglas XSL

echo $proc->transformToXML($xml);

?>

      
```php

El ejemplo anterior mostrará:

    ¡Hola! Bienvenido a la increíble colección de CD de Nicolas Eliaszewicz !

    <h1>Fight for your mind</h1><h2>por Ben Harper - 1995</h2><hr>
    <h1>Electric Ladyland</h1><h2>por Jimi Hendrix - 1997</h2><hr>

Transformación en una cadena utilizando `Dom\Document`

```
<?php

$xml = Dom\XMLDocument::createFromFile('collection.xml');
$xsl = Dom\XMLDocument::createFromFile('collection.xsl');

// Configurar el transformador
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl); // adjuntar las reglas XSL

echo $proc->transformToXML($xml);

?>

      
```php

El ejemplo anterior mostrará:

    ¡Hola! Bienvenido a la increíble colección de CD de Nicolas Eliaszewicz !

    <h1>Fight for your mind</h1><h2>por Ben Harper - 1995</h2><hr>
    <h1>Electric Ladyland</h1><h2>por Jimi Hendrix - 1997</h2><hr>

## Véase también

`XSLTProcessor::transformToDoc`, `XSLTProcessor::transformToUri`
