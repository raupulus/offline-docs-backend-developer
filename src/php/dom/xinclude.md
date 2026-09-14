---
title: DOMDocument::xinclude
description: Reemplaza los XIncludes en un objeto DOMDocument
source_url: https://www.php.net/manual/es/domdocument.xinclude.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/xinclude.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1f37a6c2
order: 13310
---

DOMDocument::xinclude

Reemplaza los XIncludes en un objeto DOMDocument

## Descripción

```php
public DOMDocument::xinclude([int $options]): int
```php

Este método reemplaza los [XIncludes](http://www.w3.org/TR/xinclude/) en un objeto DOMDocument.

> [!NOTE]
> Dado que la biblioteca libxml2 resuelve automáticamente las entidades, este método puede producir resultados no esperados si el fichero XML incluido tiene una DTD adjunta.

## Parámetros

`options`  
[Operación a nivel de bits `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

## Valores devueltos

Devuelve el número de XIncludes del documento, -1 si ocurre un error durante el proceso, o `false` si no hay sustitución.

## Ejemplos

Ejemplo con DOMDocument::xinclude()

```
<?php

$xml = <<<EOD

<chapter xmlns:xi="http://www.w3.org/2001/XInclude">
 <title>Los libros de otra persona</title>
 <para>
  <xi:include href="examples/book.xml">
   <xi:fallback>
    <error>xinclude: book.xml no ha sido encontrado</error>
   </xi:fallback>
  </xi:include>
 </para>
</chapter>
EOD;

$dom = new DOMDocument;

// Se desea un bonito formato de salida
$dom->preserveWhiteSpace = false;
$dom->formatOutput = true;

// carga del string XML definido anteriormente
$dom->loadXML($xml);

// reemplazo de los xincludes
$dom->xinclude();

echo $dom->saveXML();

?>

    
```php

Resultado del ejemplo anterior es similar a:

```
<chapter xmlns:xi="http://www.w3.org/2001/XInclude">
  <title>Los libros de otra persona</title>
  <para>
    <row xml:base="/home/didou/book.xml">
       <entry>The Grapes of Wrath</entry>
       <entry>John Steinbeck</entry>
       <entry>en</entry>
       <entry>0140186409</entry>
      </row>
    <row xml:base="/home/didou/book.xml">
       <entry>The Pearl</entry>
       <entry>John Steinbeck</entry>
       <entry>en</entry>
       <entry>014017737X</entry>
      </row>
    <row xml:base="/home/didou/book.xml">
       <entry>Samarcande</entry>
       <entry>Amine Maalouf</entry>
       <entry>fr</entry>
       <entry>2253051209</entry>
      </row>
  </para>
</chapter>

    
```php
