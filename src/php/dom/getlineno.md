---
title: DOMNode::getLineNo
description: Obtiene el número de línea de un nodo
source_url: https://www.php.net/manual/es/domnode.getlineno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/getlineno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: eaf26c34f
order: 13950
---

DOMNode::getLineNo

Obtiene el número de línea de un nodo

## Descripción

```php
public DOMNode::getLineNo(): int
```php

Obtiene el número de línea en el que el nodo fue definido durante el análisis.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de línea en el que el nodo fue definido durante el análisis. Si el nodo fue creado manualmente, el valor devuelto será `0`.

## Ejemplos

Ejemplo con DOMNode::getLineNo

```
<?php
// XML de ejemplo
$xml = <<<XML

<root>
    <node />
</root>
XML;

// Creación de un objeto DOMDocument
$dom = new DOMDocument;

// Carga del XML
$dom->loadXML($xml);

// Muestra el número de línea del nodo.
printf('El nodo <node> está definido en la línea %d', $dom->getElementsByTagName('node')->item(0)->getLineNo());
?>

    
```php

El ejemplo anterior mostrará:

    El nodo <node> está definido en la línea 3
