---
title: DOMXPath::quote
description: Cita un string para su uso en una expresión XPath
source_url: https://www.php.net/manual/es/domxpath.quote.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/quote.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: bac9d6a54
order: 14320
---

DOMXPath::quote

Cita un string para su uso en una expresión XPath

## Descripción

```php
public static DOMXPath::quote(string $str): string
```php

Cita `str` para su uso en una expresión XPath.

## Parámetros

`str`  
El string a citar.

## Valores devueltos

Devuelve un string citado para su uso en una expresión XPath.

## Ejemplos

Correspondencia del valor de un atributo con comillas

```
<?php
$doc = new DOMDocument;
$doc->loadXML(<<<XML
<books>
    <book name="'quoted' name">Book title</book>
</books>
XML);

$xpath = new DOMXPath($doc);

$query = "//book[@name=" . DOMXPath::quote("'quoted' name") . "]";
echo $query, "\n";

$entries = $xpath->query($query);

foreach ($entries as $entry) {
    echo "Found ", $entry->textContent, "\n";
}
?>

   
```php

El ejemplo anterior mostrará:

    //book[@name="'quoted' name"]
    Found Book title

       

Las citas mixtas también son admitidas:

```
<?php
echo DOMXPath::quote("'different' \"quote\" styles");
?>

   
```php

El ejemplo anterior mostrará:

    concat("'different' ",'"quote" styles')

## Véase también

DOMXPath::evaluate, DOMXPath::query
