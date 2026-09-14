---
title: DOMDocument::saveHTML
description: Copia el documento interno a una cadena usando el formato HTML
source_url: https://www.php.net/manual/es/domdocument.savehtml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/savehtml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13250
---

DOMDocument::saveHTML

Copia el documento interno a una cadena usando el formato HTML

## Descripción

```php
public DOMDocument::saveHTML([DOMNode $node]): string
```php

Crea un documento HTML desde la representación DOM. Esta función normalmente se llama después de construir un nuevo documento desde cero, como en el ejemplo de abajo.

## Parámetros

`node`  
Parámetro opcional que devuelve una parte del documento.

## Valores devueltos

Devuelve el HTML, o `false` si ocurrió un error.

## Ejemplos

Salvar un árbol HTML en una cadena

```
<?php

$doc = new DOMDocument('1.0');

$root = $doc->createElement('html');
$root = $doc->appendChild($root);

$head = $doc->createElement('head');
$head = $root->appendChild($head);

$title = $doc->createElement('title');
$title = $head->appendChild($title);

$text = $doc->createTextNode('Este es el título');
$text = $title->appendChild($text);

echo $doc->saveHTML();

?>

    
```php

## Véase también

DOMDocument::saveHTMLFile, DOMDocument::loadHTML, DOMDocument::loadHTMLFile
