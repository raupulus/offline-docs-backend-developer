---
title: DOMNode::getNodePath
description: Obtener un XPath de un nodo
source_url: https://www.php.net/manual/es/domnode.getnodepath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/getnodepath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13960
---

DOMNode::getNodePath

Obtener un XPath de un nodo

## Descripción

```php
public DOMNode::getNodePath(): string
```php

Obtiene una ruta de ubicación XPath del nodo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` que contiene el XPath, o `null` en caso de error.

## Ejemplos

Ejemplo de DOMNode::getNodePath

```
<?php
// Crear una nueva instancia de DOMDocument
$dom = new DOMDocument;

// Cargar el XML
$dom->loadXML('
<frutas>
 <manzanas>
  <manzana>braeburn</manzana>
  <manzana>granny smith</manzana>
 </manzanas>
 <peras>
  <pera>conference</pera>
 </peras>
</frutas>
');

// Imprimir el XPath para cada elemento
foreach ($dom->getElementsByTagName('*') as $nodo) {
    echo $nodo->getNodePath() . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    /frutas
    /frutas/manzanas
    /frutas/manzanas/manzana[1]
    /frutas/manzanas/manzana[2]
    /frutas/peras
    /frutas/peras/pera

## Véase también

`DOMXPath`
