---
title: xml_set_object
description: Configura un objeto como analizador XML
source_url: https://www.php.net/manual/es/function.xml-set-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-set-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 102850
---

xml_set_object

Configura un objeto como analizador XML

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.4.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] xml_set_object(XMLParser $parser, object $object): true
```php

Permite utilizar `parser` dentro de `object`. Todas las funciones de retrollamada podrán ser definidas con `xml_set_element_handler`, etc., y se considerarán métodos de `object`.

## Parámetros

`parser`  
Una referencia de analizador XML para usar en el objeto.

`object`  
El objeto en el que se debe usar el analizador XML.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esta función está ahora deprecada, pase en su lugar valores `callable` apropiados a `xml_set_` |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `xml_set_object`

```
<?php
class CustomXMLParser
{
    private $parser;

    function __construct()
    {
        $this->parser = xml_parser_create();

        xml_set_object($this->parser, $this);
        xml_set_element_handler($this->parser, "tag_open", "tag_close");
        xml_set_character_data_handler($this->parser, "cdata");
    }

    function parse($data)
    {
        xml_parse($this->parser, $data);
    }

    function tag_open($parser, $tag, $attributes)
    {
        var_dump($tag, $attributes);
    }

    function cdata($parser, $cdata)
    {
        var_dump($cdata);
    }

    function tag_close($parser, $tag)
    {
        var_dump($tag);
    }
}

$xml_parser = new CustomXMLParser();
$xml_parser->parse("<A ID='hallo'>PHP</A>");
?>

    
```php

El ejemplo anterior mostrará:

    string(1) "A"
    array(1) {
      ["ID"]=>
      string(5) "hallo"
    }
    string(3) "PHP"
    string(1) "A"
