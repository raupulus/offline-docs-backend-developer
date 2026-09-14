---
title: DOMDocument::saveXML
description: Guarda el árbol interno XML en una cadena de caracteres
source_url: https://www.php.net/manual/es/domdocument.savexml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/savexml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 13270
---

DOMDocument::saveXML

Guarda el árbol interno XML en una cadena de caracteres

## Descripción

```php
public DOMDocument::saveXML([DOMNode $node], [int $options]): string
```php

Crea un documento XML desde la representación DOM. Esta función es habitualmente llamada después de la creación de un nuevo documento DOM, como en el ejemplo que se muestra a continuación.

## Parámetros

`node`  
Utilice este argumento para mostrar únicamente un nodo específico sin declaración XML en lugar de todo el documento.

`options`  
Opciones adicionales. Las opciones `LIBXML_NOEMPTYTAG` y `LIBXML_NOXMLDECL` son soportadas. Antes de PHP 8.3.0, solo la opción `LIBXML_NOEMPTYTAG` era soportada.

## Valores devueltos

Devuelve el XML o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_WRONG_DOCUMENT_ERR`  
Lanzado si `node` proviene de otro documento.

## Historial de cambios

| Versión | Descripción                                               |
|---------|-----------------------------------------------------------|
| 8.3.0   | [LIBXML_NOXMLDECL](#libxml.constants) es ahora soportado. |

## Ejemplos

Guardar el árbol DOM en una cadena de caracteres

```
<?php

$doc = new DOMDocument('1.0');
// queremos un formato de salida bonito
$doc->formatOutput = true;

$root = $doc->createElement('book');
$root = $doc->appendChild($root);

$title = $doc->createElement('title');
$title = $root->appendChild($title);

$text = $doc->createTextNode('Este es el título');
$text = $title->appendChild($text);

echo "Obtención de todo el documento :\n";
echo $doc->saveXML() . "\n";

echo "Obtención del título, únicamente :\n";
echo $doc->saveXML($title);

?>

    
```php

El ejemplo anterior mostrará:

    Obtención de todo el documento :

    <book>
      <title>Este es el título</title>
    </book>

    Obtención del título, únicamente :
    <title>Este es el título</title>

## Véase también

DOMDocument::save, DOMDocument::load, DOMDocument::loadXML
