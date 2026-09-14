---
title: DOMDocument::saveHTMLFile
description: Copia el documento interno a un fichero usando el formato HTML
source_url: https://www.php.net/manual/es/domdocument.savehtmlfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/savehtmlfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13260
---

DOMDocument::saveHTMLFile

Copia el documento interno a un fichero usando el formato HTML

## Descripción

```php
public DOMDocument::saveHTMLFile(string $filename): int
```php

Crea un documento HTML desde la representación DOM. Esta función normalmente se llama después de construir un nuevo documento desde cero, como en el ejemplo de abajo.

## Parámetros

`filename`  
La ruta al documento HTML guardado.

## Valores devueltos

Devuelve el número de bytes escritos o `false` si ocurrió un error.

## Ejemplos

Guardar un árbol HTML en un archivo

```
<?php

$doc = new DOMDocument('1.0');
// queremos una impresión buena
$doc->formatOutput = true;

$root = $doc->createElement('html');
$root = $doc->appendChild($root);

$head = $doc->createElement('head');
$head = $root->appendChild($head);

$title = $doc->createElement('title');
$title = $head->appendChild($title);

$text = $doc->createTextNode('Este es el título');
$text = $title->appendChild($text);

echo 'EScrito: ' . $doc->saveHTMLFile("/tmp/test.html") . ' bytes'; // Escrito: 129 bytes

?>

    
```php

## Véase también

DOMDocument::saveHTML, DOMDocument::loadHTML, DOMDocument::loadHTMLFile
