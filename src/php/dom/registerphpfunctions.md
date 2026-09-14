---
title: DOMXPath::registerPhpFunctions
description: Registra una función PHP como función XPath
source_url: https://www.php.net/manual/es/domxpath.registerphpfunctions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/registerphpfunctions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: c1f37a6c2
order: 14350
---

DOMXPath::registerPhpFunctions

Registra una función PHP como función XPath

## Descripción

```php
public DOMXPath::registerPhpFunctions([string $restrict]): void
```php

Este método activa la posibilidad de utilizar funciones PHP en expresiones XPath.

## Parámetros

`restrict`  
Utilice este parámetro únicamente para autorizar ciertas funciones a ser llamadas desde XPath.

Este parámetro puede ser uno de los siguientes elementos: un `string` (nombre de función), un `array` indexado conteniendo nombres de funciones, o un `array` asociativo con claves correspondientes a nombres de funciones y valores asociados correspondientes a `callable`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

- Lanza una ValueError si el nombre de un callback no es válido.

- Levanta una excepción ValueError si `options` contiene una opción inválida.

- Levanta una excepción ValueError si `overrideEncoding` utiliza un codificado desconocido.

- Lanza una TypeError si un callback dado no es llamable.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Los nombres de callback inválidos ahora lanzan una ValueError. Pasar una entrada no llamable ahora lanza una TypeError. |
| 8.4.0 | Ahora es posible utilizar `callable`s para callbacks al utilizar `restrict` con entradas de tipo `array`. |

## Ejemplos

Los siguientes ejemplos utilizan el fichero `book.xml` que contiene los siguientes datos:

book.xml

```
<books>
 <book>
  <title>PHP Basics</title>
  <author>Jim Smith</author>
  <author>Jane Smith</author>
 </book>
 <book>
  <title>PHP Secrets</title>
  <author>Jenny Smythe</author>
 </book>
 <book>
  <title>XML basics</title>
  <author>Joe Black</author>
 </book>
</books>

    
```php

DOMXPath::registerPhpFunctions con `php:function`

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book-simple.xml');

$xpath = new DOMXPath($doc);

// Registra el espacio de nombres php (necesario)
$xpath->registerNamespace("php", "http://php.net/xpath");

// Registra las funciones PHP (Sin restricciones)
$xpath->registerPhpFunctions();

// Llama a la función substr en el título del libro
$nodes = $xpath->query('//book[php:functionString("substr", title, 0, 3) = "PHP"]');

echo "{$nodes->length} libros encontrados cuyo título comienza con 'PHP':\n";
foreach ($nodes as $node) {
    $title  = $node->getElementsByTagName("title")->item(0)->nodeValue;
    $author = $node->getElementsByTagName("author")->item(0)->nodeValue;
    echo "$title por $author\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    2 libros encontrados cuyo título comienza con 'PHP':
    PHP Basics por Jim Smith
    PHP Secrets por Jenny Smythe

Ejemplo con DOMXPath::registerPhpFunctions y `php:function`

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book-simple.xml');

$xpath = new DOMXPath($doc);

// Registra el espacio de nombres php (necesario)
$xpath->registerNamespace("php", "http://php.net/xpath");

// Registra funciones PHP (solo has_multiple)
$xpath->registerPhpFunctions("has_multiple");

function has_multiple($nodes) {
    // Retorna true si hay más de un autor
    return count($nodes) > 1;
}
// Filtra los libros cuyos autores son múltiples
$books = $xpath->query('//book[php:function("has_multiple", author)]');

echo "Libros con múltiples autores :\n";
foreach ($books as $book) {
    echo $book->getElementsByTagName("title")->item(0)->nodeValue . "\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Libros con múltiples autores :
    PHP Basics

DOMXPath::registerPhpFunctions con un `callable`

```
<?php
$doc = new DOMDocument;
$doc->load('examples/book-simple.xml');

$xpath = new DOMXPath($doc);

// Registrar el namespace php: (necesario)
$xpath->registerNamespace("php", "http://php.net/xpath");

// Registrar las funciones PHP (solo has_multiple)
$xpath->registerPhpFunctions(["has_multiple" => fn ($nodes) => count($nodes) > 1]);

// Filtrar los libros con múltiples autores
$books = $xpath->query('//book[php:function("has_multiple", author)]');

echo "Libros con múltiples autores :\n";
foreach ($books as $book) {
    echo $book->getElementsByTagName("title")->item(0)->nodeValue . "\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Libros con múltiples autores :
    PHP Basics

## Véase también

DOMXPath::registerNamespace, DOMXPath::query, DOMXPath::evaluate, XSLTProcessor::registerPHPFunctions
