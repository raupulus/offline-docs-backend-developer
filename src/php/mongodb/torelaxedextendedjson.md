---
title: MongoDB\BSON\Document::toRelaxedExtendedJSON
description: Devuelve la representación relajada extendida JSON del documento BSON
source_url: https://www.php.net/manual/es/mongodb-bson-document.torelaxedextendedjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/torelaxedextendedjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47700
---

MongoDB\BSON\Document::toRelaxedExtendedJSON

Devuelve la representación relajada extendida JSON del documento BSON

## Descripción

```php
final public MongoDB\BSON\Document::toRelaxedExtendedJSON(): string
```php

Convierte el documento BSON en su representación [Relajada Extendida JSON](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#relaxed-extended-json-example). El formato relajado prefiere el uso de las primitivas de tipo JSON en detrimento de la fidelidad de los tipos y es el más adecuado para producir una salida que puede ser fácilmente consumida por las API web y los humanos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string que contiene la [representación Relaxed Extended JSON](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#relaxed-extended-json-example) del documento BSON.

## Ejemplos

Ejemplo de MongoDB\BSON\Document::toRelaxedExtendedJSON

```
    
<?php

$documents = [
    [ 'null' => null ],
    [ 'boolean' => true ],
    [ 'string' => 'foo' ],
    [ 'int32' => 123 ],
    [ 'int64' => 4294967295 ],
    [ 'double' => 1.0 ],
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
    $bson = MongoDB\BSON\Document::fromPHP($document);
    echo $bson->toRelaxedExtendedJSON(), "\n";
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

MongoDB\BSON\Document::toCanonicalExtendedJSON

MongoDB\BSON\toRelaxedExtendedJSON

Especificación JSON extendida

Tipos BSON
