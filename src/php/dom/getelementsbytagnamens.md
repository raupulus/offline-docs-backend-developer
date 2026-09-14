---
title: DOMDocument::getElementsByTagNameNS
description: Búsqueda de todos los elementos con un nombre de etiqueta dado en un
  espacio de nombres especificado
source_url: https://www.php.net/manual/es/domdocument.getelementsbytagnamens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/getelementsbytagnamens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 842bbe35c
order: 13120
---

DOMDocument::getElementsByTagNameNS

Búsqueda de todos los elementos con un nombre de etiqueta dado en un espacio de nombres especificado

## Descripción

```php
public DOMDocument::getElementsByTagNameNS(string $namespace, string $localName): DOMNodeList
```php

Devuelve un `DOMNodeList` de todos los elementos con un nombre local dado y una URI de espacio de nombres.

## Parámetros

`namespace`  
La URI del espacio de nombres de los elementos a buscar. El valor especial `"*"` representa todos los espacios de nombres. Pasar `null` representa el espacio de nombres vacío.

`localName`  
El nombre local de los elementos a buscar. El valor especial `"*"` representa todos los nombres locales.

## Valores devueltos

Un nuevo objeto `DOMNodeList` que contiene todos los elementos encontrados.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.3   | `namespace` ahora es nullable. |

## Ejemplos

Recuperación de todos los elementos XInclude

```
<?php

$xml = <<<EOD

<chapter xmlns:xi="http://www.w3.org/2001/XInclude">
<title>Books of the other guy..</title>
<para>
 <xi:include href="book.xml">
  <xi:fallback>
   <error>xinclude: book.xml not found</error>
  </xi:fallback>
 </xi:include>
 <include>
  This is another namespace
 </include>
</para>
</chapter>
EOD;
$dom = new DOMDocument;

// load the XML string defined above
$dom->loadXML($xml);

foreach ($dom->getElementsByTagNameNS('http://www.w3.org/2001/XInclude', '*') as $element) {
    echo 'local name: ', $element->localName, ', prefix: ', $element->prefix, "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    local name: include, prefix: xi
    local name: fallback, prefix: xi

## Véase también

DOMDocument::getElementsByTagName
