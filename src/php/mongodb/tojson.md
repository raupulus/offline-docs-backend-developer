---
title: MongoDB\BSON\toJSON
description: Devuelve la representación en JSON Extendido Legado de un valor BSON
source_url: https://www.php.net/manual/es/function.mongodb.bson-tojson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/bson/tojson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48780
---

MongoDB\BSON\toJSON

Devuelve la representación en JSON Extendido Legado de un valor BSON

> [!WARNING]
> Esta función ha sido *DEPRECADA* a partir de la versión 1.20.0 de la extensión y fue eliminada en la versión 2.0. Las aplicaciones deben usar en su lugar MongoDB\BSON\Document::toCanonicalExtendedJSON o MongoDB\BSON\Document::toRelaxedExtendedJSON.

## Descripción

```php
MongoDB\BSON\toJSON(string $bson): string
```php

Convierte una cadena BSON a su representación en [JSON Extendido Legado](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/).

> [!NOTE]
> Existen varios formatos JSON para representar BSON. Esta función implementa el "modo estricto" definido en [JSON Extendido de MongoDB](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/), que ha sido reemplazado por los formatos canónico y relajado definidos en la [Especificación de JSON Extendido](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md) e implementados por `MongoDB\BSON\toCanonicalExtendedJSON` y `MongoDB\BSON\toRelaxedExtendedJSON`, respectivamente.

> [!WARNING]
> [JSON](http://www.json.org/) no admite [`NAN`](#language.types.float.nan) ni [`INF`](#function.is-infinite), y el formato de JSON Extendido Legado de MongoDB no define una representación alternativa para estos valores ([libbson](https://github.com/mongodb/mongo-c-driver/tree/master/src/libbson) generará literales `nan` e `inf`, que pueden no ser analizados como JSON válido). Si está trabajando con BSON que puede contener números no finitos, utilice `MongoDB\BSON\toCanonicalExtendedJSON` o `MongoDB\BSON\toRelaxedExtendedJSON`.

## Parámetros

`bson` (`string`)  
Valor BSON a convertir.

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

Ejemplo de `MongoDB\BSON\toJSON`

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
    echo MongoDB\BSON\toJSON($bson), "\n";
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
    { "nan" : nan }
    { "pos_inf" : inf }
    { "neg_inf" : -inf }
    { "array" : [ "foo", "bar" ] }
    { "document" : { "foo" : "bar" } }
    { "oid" : { "$oid" : "56315a7c6118fd1b920270b1" } }
    { "dec128" : { "$numberDecimal" : "1234.5678" } }
    { "binary" : { "$binary" : "Zm9v", "$type" : "00" } }
    { "date" : { "$date" : 1445990400000 } }
    { "timestamp" : { "$timestamp" : { "t" : 5678, "i" : 1234 } } }
    { "regex" : { "$regex" : "pattern", "$options" : "i" } }
    { "code" : { "$code" : "function() { return 1; }" } }
    { "code_ws" : { "$code" : "function() { return a; }", "$scope" : { "a" : 1 } } }
    { "minkey" : { "$minKey" : 1 } }
    { "maxkey" : { "$maxKey" : 1 } }

## Véase también

MongoDB\BSON\fromJSON

MongoDB\BSON\toCanonicalExtendedJSON

MongoDB\BSON\toRelaxedExtendedJSON

JSON Extendido de MongoDB

BSON de MongoDB
