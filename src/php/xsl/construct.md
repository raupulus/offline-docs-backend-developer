---
title: XSLTProcessor::__construct
description: Crea un nuevo objeto XSLTProcessor
source_url: https://www.php.net/manual/es/xsltprocessor.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: false
translation_revision: adf11d8d6
order: 104100
---

XSLTProcessor::\_\_construct

Crea un nuevo objeto XSLTProcessor

## Descripción

```php
XSLTProcessor::__construct()
```php

Crea un nuevo objeto `XSLTProcessor`.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Creando un `XSLTProcessor`

```
<?php

$xsldoc = new DOMDocument();
$xsldoc->load($xsl_filename);

$xmldoc = new DOMDocument();
$xmldoc->load($xml_filename);

$xsl = new XSLTProcessor();
$xsl->importStyleSheet($xsldoc);
echo $xsl->transformToXML($xmldoc);

?>

    
```php
