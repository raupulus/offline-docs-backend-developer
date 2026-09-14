---
title: xml_parse_into_struct
description: Analiza una estructura XML
source_url: https://www.php.net/manual/es/function.xml-parse-into-struct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parse-into-struct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: b47e4bea1
order: 102720
---

xml_parse_into_struct

Analiza una estructura XML

## Descripción

```php
xml_parse_into_struct(XMLParser $parser, string $data, array $values, [array $index]): int
```php

Esta función analiza la cadena XML `data` y la coloca en dos arrays: el primero `index` contiene punteros a la posición de los valores correspondientes en el array `values`. Estos dos parámetros se pasan por referencia.

## Parámetros

`parser`  
Una referencia a un analizador XML.

`data`  
Un string que contiene los datos XML.

`values`  
Un array que contiene los valores de los datos XML.

`index`  
Un array que contiene los punteros a los valores apropiados en el parámetro \$values.

## Valores devueltos

`xml_parse_into_struct` retorna 0 si ocurre un error y 1 en caso de éxito. Esto no es lo mismo que `false` y `true`, por lo que se debe tener precaución con los operadores como ===.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Ejemplos

A continuación, se encuentra un ejemplo que ilustra la estructura de los dos arrays generados por la función. Se utiliza una etiqueta simple `note`, colocada dentro de otra etiqueta `para`. Se analiza todo y se muestra la estructura generada:

Ejemplo con `xml_parse_into_struct`

```
<?php
$simple = "<para><note>simple note</note></para>";
$p = xml_parser_create();
xml_parse_into_struct($p, $simple, $vals, $index);
echo "Array Index\n";
print_r($index);
echo "\nArray Vals\n";
print_r($vals);
?>

    
```php

Mostrará:

    Array Index
    Array
    (
        [PARA] => Array
            (
                [0] => 0
                [1] => 2
            )

        [NOTE] => Array
            (
                [0] => 1
            )

    )

    Array Vals
    Array
    (
        [0] => Array
            (
                [tag] => PARA
                [type] => open
                [level] => 1
            )

        [1] => Array
            (
                [tag] => NOTE
                [type] => complete
                [level] => 2
                [value] => simple note
            )

        [2] => Array
            (
                [tag] => PARA
                [type] => close
                [level] => 1
            )

    )

El análisis basado en eventos (como el de expat) puede resultar complejo cuando el documento XML es complejo. `xml_parse_into_struct` no genera objetos de tipo DOM, sino que genera estructuras que pueden ser recorridas de manera similar a un árbol. Consideremos el siguiente fichero, que representa una pequeña base de datos XML:

moldb.xml - Pequeña base de datos molecular

```
<moldb>

  <molecule>
      <name>Alanine</name>
      <symbol>ala</symbol>
      <code>A</code>
      <type>hydrophobic</type>
  </molecule>

  <molecule>
      <name>Lysine</name>
      <symbol>lys</symbol>
      <code>K</code>
      <type>charged</type>
  </molecule>

</moldb>

    
```php

Y ahora, un código que analiza el documento y genera los objetos correspondientes:

parsemoldb.php: Analiza moldb.xml y crea un array de objetos moleculares

```
<?php

class AminoAcid {
    var $name;  // nombre aa
    var $symbol;    // símbolo de tres letras
    var $code;  // código de una letra
    var $type;  // hidrofóbico, cargado o neutro

    function __construct ($aa) {
        foreach ($aa as $k=>$v)
            $this->$k = $aa[$k];
    }
}

function readDatabase($filename)
{
    // lee la base de datos xml de aminoácidos
    $data = file_get_contents($filename);
    $parser = xml_parser_create();
    xml_parser_set_option($parser, XML_OPTION_CASE_FOLDING, 0);
    xml_parser_set_option($parser, XML_OPTION_SKIP_WHITE, 1);
    xml_parse_into_struct($parser, $data, $values, $tags);
    unset($parser);

    // bucle a través de las estructuras
    foreach ($tags as $key=>$val) {
        if ($key == "molecule") {
            $molranges = $val;
            // cada par contiguo de entradas del array son los límites inferior y superior para cada definición de molécula
            for ($i=0; $i < count($molranges); $i+=2) {
                $offset = $molranges[$i] + 1;
                $len = $molranges[$i + 1] - $offset;
                $tdb[] = parseMol(array_slice($values, $offset, $len));
            }
        } else {
            continue;
        }
    }
    return $tdb;
}

function parseMol($mvalues) {
    for ($i=0; $i < count($mvalues); $i++)
        $mol[$mvalues[$i]["tag"]] = $mvalues[$i]["value"];
    return new AminoAcid($mol);
}

$db = readDatabase("moldb.xml");
echo "** Base de objetos AminoAcid:\n";
print_r($db);

?>

    
```php

Tras la ejecución de `parsemoldb.php`, la variable `$db` contiene un array de objetos `AminoAcid`, y la salida lo confirma:

    ** Base de objetos AminoAcid:
    Array
    (
        [0] => aminoacid Object
            (
                [name] => Alanine
                [symbol] => ala
                [code] => A
                [type] => hydrophobic
            )

        [1] => aminoacid Object
            (
                [name] => Lysine
                [symbol] => lys
                [code] => K
                [type] => charged
            )

    )
