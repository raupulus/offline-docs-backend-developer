---
title: DOMXPath::query
description: Evalúa la expresión XPath dada
source_url: https://www.php.net/manual/es/domxpath.query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: c1f37a6c2
order: 14310
---

DOMXPath::query

Evalúa la expresión XPath dada

## Descripción

```php
public DOMXPath::query(string $expression, [DOMNode $contextNode], [bool $registerNodeNS]): mixed
```php

Evalúa la expresión `expression` XPath dada.

## Parámetros

`expression`  
La expresión XPath a ejecutar.

`contextNode`  
El argumento opcional `contextNode` puede ser especificado para realizar consultas XPath relativas. Por omisión, las consultas son relativas al elemento raíz.

`registerNodeNS`  
Indica si se deben registrar automáticamente los prefijos de espacio de nombres en vigor del nodo de contexto en el objeto `DOMXPath`. Esto puede ser utilizado para evitar tener que llamar manualmente a DOMXPath::registerNamespace para cada espacio de nombres en vigor. En caso de conflicto de prefijos de espacio de nombres, solo se registra el prefijo de espacio de nombres descendiente más cercano.

## Valores devueltos

Devuelve un `DOMNodeList` que contiene todos los nodos que coinciden con la expresión `expression` XPath dada. Todas las expresiones que no devuelvan ningún nodo devolverán un `DOMNodeList` vacío.

Si el argumento `expression` está malformado o el argumento `contextNode` es inválido, DOMXPath::query devolverá `false`.

## Errores/Excepciones

Los siguientes errores pueden ocurrir al utilizar una expresión que invoca retrollamadas PHP.

- Lanza una Error si una retrollamada PHP es invocada pero ninguna retrollamada está registrada, o si la retrollamada nombrada no está registrada.

- Lanza una TypeError si la sintaxis `php:function` es utilizada y el nombre del gestor no es un string.

- Lanza una Error si un objeto no-DOM es devuelto por una retrollamada.

## Ejemplos

Recuperación de todos los libros en inglés

```
<?php

$doc = new DOMDocument;

// No queremos preocuparnos por los espacios en blanco
$doc->preserveWhiteSpace = false;

$doc->load('examples/book-docbook.xml');

$xpath = new DOMXPath($doc);

// Comenzamos en el elemento raíz
$query = '//book/chapter/para/informaltable/tgroup/tbody/row/entry[. = "en"]';

$entries = $xpath->query($query);

foreach ($entries as $entry) {
    echo "Libro encontrado {$entry->previousSibling->previousSibling->nodeValue}," .
         " por {$entry->previousSibling->nodeValue}\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Libro encontrado : The Grapes of Wrath, por John Steinbeck
    Libro encontrado : The Pearl, por John Steinbeck

        

También podemos utilizar el argumento `contextNode` para acortar nuestra expresión :

```
<?php

$doc = new DOMDocument;
$doc->preserveWhiteSpace = false;

$doc->load('examples/book-docbook.xml');

$xpath = new DOMXPath($doc);

$tbody = $doc->getElementsByTagName('tbody')->item(0);

// nuestra consulta es relativa al nodo tbody
$query = 'row/entry[. = "en"]';

$entries = $xpath->query($query, $tbody);

foreach ($entries as $entry) {
    echo "Libro encontrado : {$entry->previousSibling->previousSibling->nodeValue}," .
         " por {$entry->previousSibling->nodeValue}\n";
}
?>

    
```php

## Véase también

DOMXPath::query
