---
title: SimpleXMLElement::asXML
description: Devuelve un string basado en un elemento SimpleXML
source_url: https://www.php.net/manual/es/simplexmlelement.asxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/asXML.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: d6f54016d
order: 74450
---

SimpleXMLElement::asXML

Devuelve un string basado en un elemento SimpleXML

## Descripción

```php
public SimpleXMLElement::asXML([string $filename]): string
```php

Formatea los datos del objeto padre en XML 1.0.

## Parámetros

`filename`  
Si se especifica un string, la función escribe los datos al fichero en lugar de devolverlos.

## Valores devueltos

Si el parámetro `filename` no está especificado, la función devuelve un string en caso de éxito y false en caso de error. Si el parámetro está especificado, devuelve true si el fichero ha sido escrito correctamente y false en otro caso.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `filename` ahora es nullable. |

## Ejemplos

Obtener XML con SimpleXML

```
<?php
$string = <<<XML
<a>
 <b>
  <c>text</c>
  <c>stuff</c>
 </b>
 <d>
  <c>code</c>
 </d>
</a>
XML;

$xml = new SimpleXMLElement($string);

echo $xml->asXML();

?>

    
```php

El ejemplo anterior mostrará:

    <a>
     <b>
      <c>text</c>
      <c>stuff</c>
     </b>
     <d>
      <c>code</c>
     </d>
    </a>

`SimpleXMLElement::asXML` también funciona con los resultados Xpath:

Uso de `SimpleXMLElement::asXML` con los resultados de `SimpleXMLElement::xpath`

```
<?php
$string = <<<XML
<a>
 <b>
  <c>text</c>
  <c>stuff</c>
 </b>
 <d>
  <c>code</c>
 </d>
</a>
XML;

$xml = new SimpleXMLElement($string);

/* Se busca <a><b><c> */
$result = $xml->xpath('/a/b/c');

foreach ($result as $node) {
    echo $node->asXML();
}
?>

    
```php

El ejemplo anterior mostrará:

    <c>text</c><c>stuff</c>

## Véase también

SimpleXMLElement::\_\_toString, [???](#simplexml.examples-basic)
