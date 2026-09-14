---
title: XSLTProcessor::transformToUri
description: Transforma en URI
source_url: https://www.php.net/manual/es/xsltprocessor.transformtouri.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/transformtouri.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 01904e809
order: 104220
---

XSLTProcessor::transformToUri

Transforma en URI

## Descripción

```php
public XSLTProcessor::transformToUri(object $document, string $uri): int
```php

Transforma el nodo fuente en una URI aplicando la hoja de estilo dada por el método `XSLTProcessor::importStylesheet`.

## Parámetros

`document`  
El `Dom\Document`, `DOMDocument`, `SimpleXMLElement` u objeto compatible con libxml a transformar.

`uri`  
La URL para la transformación.

## Valores devueltos

Devuelve el número de bytes escritos o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora lanza una Error si la retrollamada no puede ser invocada, en lugar de emitir una advertencia. |
| 8.4.0 | Añade soporte para `Dom\Document`. |

## Ejemplos

Transformación en un fichero HTML

```
<?php

// Carga del fuente XML
$xml = new DOMDocument;
$xml->load('collection.xml');

$xsl = new DOMDocument;
$xsl->load('collection.xsl');

// Configuración del transformador
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl); // adjuntar las reglas xsl

$proc->transformToURI($xml, 'file:///tmp/out.html');

?>

    
```php

Transformación en un fichero HTML utilizando `Dom\Document`

```
    <?php

    $xml = Dom\XMLDocument::createFromFile('collection.xml');
    $xsl = Dom\XMLDocument::createFromFile('collection.xsl');

    // Configura el transformador
    $proc = new XSLTProcessor;
    $proc->importStyleSheet($xsl); // adjuntar las reglas XSL

    $proc->transformToURI($xml, 'file:///tmp/out.html');

?>

    
```php

## Véase también

`XSLTProcessor::transformToDoc`, `XSLTProcessor::transformToXml`
