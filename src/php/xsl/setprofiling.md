---
title: XSLTProcessor::setProfiling
description: Establece el fichero de salida para la información resultado del proceso
source_url: https://www.php.net/manual/es/xsltprocessor.setprofiling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/setprofiling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: false
translation_revision: bad9acb50
order: 104190
---

XSLTProcessor::setProfiling

Establece el fichero de salida para la información resultado del proceso

## Descripción

```php
public XSLTProcessor::setProfiling(string $filename): true
```php

Establece el nombre del fichero de salida para la información generada del propio procesado de la hoja de estilos.

## Parámetros

`filename`  
Ruta al fichero donde volcar la información.

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo de salida de información

```
<?php
// Load the XML source
$xml = new DOMDocument;
$xml->load('collection.xml');

$xsl = new DOMDocument;
$xsl->load('collection.xsl');

// Configuración del procesador
$proc = new XSLTProcessor;
$proc->setProfiling('profiling.txt');
$proc->importStyleSheet($xsl); // adjunta las reglas xsl

echo trim($proc->transformToDoc($xml)->firstChild->wholeText);
?>

    
```php

Este código generará la siguiente información en el fichero profiling.txt:

    number               match                name      mode  Calls Tot 100us Avg

        0                   cd                                    2      3      1
        1           collection                                    1      1      1

                             Total                                3      4
