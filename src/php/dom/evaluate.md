---
title: DOMXPath::evaluate
description: Evalúa una expresión XPath dada y devuelve un resultado tipado si es
  posible
source_url: https://www.php.net/manual/es/domxpath.evaluate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/evaluate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: c1f37a6c2
order: 14300
---

DOMXPath::evaluate

Evalúa una expresión XPath dada y devuelve un resultado tipado si es posible

## Descripción

```php
public DOMXPath::evaluate(string $expression, [DOMNode $contextNode], [bool $registerNodeNS]): mixed
```php

Ejecuta la expresión XPath `expression` y devuelve un resultado tipado si es posible.

## Parámetros

`expression`  
La expresión XPath a ejecutar.

`contextNode`  
El argumento opcional `contextNode` puede ser especificado para realizar consultas XPath relativas. Por omisión, las consultas son relativas al elemento root.

`registerNodeNS`  
Indica si se deben registrar automáticamente los prefijos de espacio de nombres en vigor del nodo de contexto en el objeto `DOMXPath`. Esto puede ser utilizado para evitar tener que llamar manualmente a DOMXPath::registerNamespace para cada espacio de nombres en vigor. En caso de conflicto de prefijos de espacio de nombres, solo se registra el prefijo de espacio de nombres descendiente más cercano.

## Valores devueltos

Devuelve un resultado tipado si es posible o un `DOMNodeList` que contiene todos los nodos que coinciden con la expresión XPath `expression`.

Si el argumento `expression` está mal formado o bien si el argumento `contextNode` es inválido, el método DOMXPath::evaluate devolverá `false`.

## Ejemplos

Recuperación del número total de libros en inglés

```
<?php

$doc = new DOMDocument;

$doc->load('examples/book-dcobook.xml');

$xpath = new DOMXPath($doc);

$tbody = $doc->getElementsByTagName('tbody')->item(0);

// nuestra consulta es relativa al nodo tbody
$query = 'count(row/entry[. = "en"])';

$entries = $xpath->evaluate($query, $tbody);
echo "Hay $entries libros en inglés\n";

?>

    
```php

El ejemplo anterior mostrará:

    Hay 2 libros en inglés

## Véase también

DOMXPath::query
