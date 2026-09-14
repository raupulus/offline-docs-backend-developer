---
title: simplexml_import_dom
description: Construye un objeto SimpleXMLElement a partir de un objeto XML o HTML
source_url: https://www.php.net/manual/es/function.simplexml-import-dom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/functions/simplexml-import-dom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_revision: c142be811
order: 74390
---

simplexml_import_dom

Construye un objeto

SimpleXMLElement

a partir de un objeto XML o HTML

## Descripción

```php
simplexml_import_dom(object $node, [string $class_name]): SimpleXMLElement
```php

`simplexml_import_dom` toma un nodo de un documento [DOM](#book.dom) y lo transforma en nodo `SimpleXML`. Este nuevo objeto puede entonces ser utilizado como un objeto nativo `SimpleXML`.

## Parámetros

`node`  
Un elemento [DOM](#book.dom)

`class_name`  
Este parámetro opcional permite que `simplexml_load_string` retorne un objeto de la clase especificada. Esta clase debe extender la clase `SimpleXMLElement`.

## Valores devueltos

Retorna un objeto `SimpleXMLElement` o `null` en caso de fallo.

## Errores/Excepciones

Lanza una `TypeError` cuando un `node` no-XML o no-HTML es pasado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añade soporte para `Dom\Document`. |
| 8.4.0 | Esta función ahora lanza una `TypeError` en lugar de una `ValueError` cuando un `node` no-XML o no-HTML es pasado. |

## Ejemplos

Importar un `DOMDocument`

```
<?php
$dom = new DOMDocument;
$dom->loadXML('<books><book><title>blah</title></book></books>');
if (!$dom) {
    echo 'Error durante el análisis del documento';
    exit;
}

$s = simplexml_import_dom($dom);

echo $s->book[0]->title;
?>

    
```php

El ejemplo anterior mostrará:

    blah

Importar un `Dom\Document`

```
<?php
$dom = Dom\XMLDocument::createFromString('<books><book><title>blah</title></book></books>');

$s = simplexml_import_dom($dom);

echo $s->book[0]->title;
?>

    
```php

El ejemplo anterior mostrará:

    blah

## Véase también

`dom_import_simplexml`, [???](#simplexml.examples-basic)
