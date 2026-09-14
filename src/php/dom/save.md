---
title: DOMDocument::save
description: Copia el árbol XML interno a un archivo
source_url: https://www.php.net/manual/es/domdocument.save.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/save.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13240
---

DOMDocument::save

Copia el árbol XML interno a un archivo

## Descripción

```php
public DOMDocument::save(string $filename, [int $options]): int
```php

Crea un documento XML desde la representación DOM. Esta función normalmente se llama después de construir un nuevo documento desde ceros, como en el ejemplo de abajo.

## Parámetros

`filename`  
La ruta al documento XML guardado.

`options`  
Opciones Adicionales. Actualmente sólo está soportada [LIBXML_NOEMPTYTAG](#libxml.constants).

## Valores devueltos

Devuelve el número de bytes escritos o `false` si ocurrió un error.

## Ejemplos

Guardar un árbol DOM en un fichero

```
<?php

$doc = new DOMDocument('1.0');
// queremos una impresión buena
$doc->formatOutput = true;

$root = $doc->createElement('book');
$root = $doc->appendChild($root);

$title = $doc->createElement('title');
$title = $root->appendChild($title);

$text = $doc->createTextNode('Este es el título');
$text = $title->appendChild($text);

echo 'Escrito: ' . $doc->save("/tmp/test.xml") . ' bytes'; // Escrito: 72 bytes

?>

    
```php

## Véase también

DOMDocument::saveXML, DOMDocument::load, DOMDocument::loadXML
