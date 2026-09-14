---
title: MongoDB\BSON\toRelaxedExtendedJSON
description: Devuelve la representación en Relaxed Extended JSON de un valor BSON
source_url: https://www.php.net/manual/es/function.mongodb.bson-torelaxedextendedjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/bson/torelaxedextendedjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48800
---

MongoDB\BSON\toRelaxedExtendedJSON

Devuelve la representación en Relaxed Extended JSON de un valor BSON

> [!WARNING]
> Esta función ha sido *DEPRECADA* a partir de la versión 1.20.0 de la extensión y fue eliminada en la versión 2.0. Las aplicaciones deben usar MongoDB\BSON\Document::toRelaxedExtendedJSON en su lugar.

## Descripción

```php
MongoDB\BSON\toRelaxedExtendedJSON(string $bson): string
```php

Convierte una cadena BSON a su representación en [Relaxed Extended JSON](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#relaxed-extended-json-example). El formato relajado prefiere el uso de primitivas de tipo JSON a costa de la fidelidad de tipos y es más adecuado para producir salidas que puedan ser consumidas fácilmente por APIs web y humanos.

## Parámetros

`bson` (`string`)  
Valor BSON que se convertirá.

## Valores devueltos

El valor JSON convertido.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\UnexpectedValueException

si la entrada no contiene exactamente un documento BSON. Las razones posibles incluyen, pero no se limitan a, BSON inválido, datos adicionales (después de leer un documento BSON), o un error inesperado de

libbson

.

## Historial de cambios

| Versión            | Descripción                     |
|--------------------|---------------------------------|
| PECL mongodb 2.0.0 | Esta función ha sido eliminada. |

## Ejemplos

Ejemplo de `MongoDB\BSON\toRelaxedExtendedJSON`

```
<?php

$documents = [
    [ 'null' => null ],
    [ 'boolean' => true ],
    [ 'string' => 'foo' ],
    [ 'int32' => 123 ],
    [ 'int64' => 4294967295 ],
    [ 'double' => 1.0, ],
    [ 'nan' => NAN ],
    [ 'pos_inf' => INF ],
    [ 'neg_inf' => -INF ],
    [ 'array' => [ 'foo', 'bar' ]],
    [ 'document' => [ 'foo' => 'bar' ]],
    [ 'oid' => new MongoDB\BSON\ObjectId('56315a7c6118fd1b920270b1') ],
    [ 'dec128' => new MongoDB\BSON\Decimal128('1234.5678') ],
    [ 'binary' => new MongoDB\BSON\Binary('foo', MongoDB\BSON\Binary::TYPE_GENERIC) ],
    [ 'date' => new MongoDB\BSON\UTCDateTime(1445990400000) ],
    [ 'timestamp' => new MongoDB\BSON\Timestamp(1234, 5678) ],
    [ 'regex' => new MongoDB\BSON\Regex('pattern', 'i') ],
    [ 'code' => new MongoDB\BSON\Javascript('function() { return 1; }') ],
    [ 'code_ws' => new MongoDB\BSON\Javascript('function() { return a; }', ['a' => 1]) ],
    [ 'minkey' => new MongoDB\BSON\MinKey ],
    [ 'maxkey' => new MongoDB\BSON\MaxKey ],
];

foreach ($documents as $document) {
    $bson = MongoDB\BSON\fromPHP($document);
    echo MongoDB\BSON\toRelaxedExtendedJSON($bson), "\n";
}

?>

   
```php

El ejemplo anterior mostrará:

    { "null" : null }
    { "boolean" : true }
    { "string" : "foo" }
    { "int32" : 123 }
    { "int64" : 4294967295 }
    { "double" : 1.0 }
    { "nan" : { "$numberDouble" : "NaN" } }
    { "pos_inf" : { "$numberDouble" : "Infinity" } }
    { "neg_inf" : { "$numberDouble" : "-Infinity" } }
    { "array" : [ "foo", "bar" ] }
    { "document" : { "foo" : "bar" } }
    { "oid" : { "$oid" : "56315a7c6118fd1b920270b1" } }
    { "dec128" : { "$numberDecimal" : "1234.5678" } }
    { "binary" : { "$binary" : { "base64": "Zm9v", "subType" : "00" } } }
    { "date" : { "$date" : "2015-10-28T00:00:00Z" } }
    { "timestamp" : { "$timestamp" : { "t" : 5678, "i" : 1234 } } }
    { "regex" : { "$regularExpression" : { "pattern" : "pattern", "options" : "i" } } }
    { "code" : { "$code" : "function() { return 1; }" } }
    { "code_ws" : { "$code" : "function() { return a; }", "$scope" : { "a" : 1 } } }
    { "minkey" : { "$minKey" : 1 } }
    { "maxkey" : { "$maxKey" : 1 } }

## Véase también

MongoDB\BSON\Document::fromJSON

MongoDB\BSON\Document::toRelaxedExtendedJSON

MongoDB\BSON\fromJSON

MongoDB\BSON\toCanonicalExtendedJSON

JSON Extendido

MongoDB BSON
