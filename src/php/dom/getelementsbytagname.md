---
title: DOMDocument::getElementsByTagName
description: Busca todos los elementos con el nombre de etiqueta local dado
source_url: https://www.php.net/manual/es/domdocument.getelementsbytagname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/getelementsbytagname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13110
---

DOMDocument::getElementsByTagName

Busca todos los elementos con el nombre de etiqueta local dado

## Descripción

```php
public DOMDocument::getElementsByTagName(string $qualifiedName): DOMNodeList
```php

Esta función devuelve una nueva instancia de la clase `DOMNodeList` que contiene los elementos con el nombre de etiqueta local buscado.

## Parámetros

`qualifiedName`  
El nombre local (sin namespace) de la etiqueta con el cual se hará comparación. El valor especial `*` coincindirá con todas las etiquetas.

## Valores devueltos

Un nuevo objeto `DOMNodeList` que contiene todos los elementos coincidentes.

## Ejemplos

Ejemplo de uso básico

```
<?php
$xml = <<< XML

<books>
 <book>Patrones de Arquitectura de Aplicaciones Empresariales</book>
 <book>Patrones de diseño: elementos de diseño de software reutilizable</book>
 <book>Código limpio</book>
</books>
XML;

$dom = new DOMDocument;
$dom->loadXML($xml);
$books = $dom->getElementsByTagName('book');
foreach ($books as $book) {
    echo $book->nodeValue, PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    Patrones de Arquitectura de Aplicaciones Empresariales
    Patrones de diseño: elementos de diseño de software reutilizable
    Código limpio

## Véase también

DOMDocument::getElementsByTagNameNS
