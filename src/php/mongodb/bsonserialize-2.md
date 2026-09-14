---
title: MongoDB\BSON\Serializable::bsonSerialize
description: Proporciona un array o documento para serializar como BSON
source_url: https://www.php.net/manual/es/mongodb-bson-serializable.bsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/serializable/bsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48370
---

MongoDB\BSON\Serializable::bsonSerialize

Proporciona un array o documento para serializar como BSON

## Descripción

```php
abstract public MongoDB\BSON\Serializable::bsonSerialize(): array
```php

Se invoca durante la serialización del objeto a BSON. El método debe devolver un `array`, `stdClass`, `MongoDB\BSON\Document`, o `MongoDB\BSON\PackedArray`.

Los documentos raíz (por ejemplo, un MongoDB\BSON\Serializable pasado a MongoDB\BSON\Document::fromPHP) siempre se serializarán como un documento BSON. Para los valores de campo, los arrays asociativos y las instancias de `stdClass` se serializarán como un documento BSON y los arrays secuenciales (es decir, índices numéricos secuenciales que comienzan en `0`) se serializarán como un array BSON.

Se recomienda a los usuarios incluir una propiedad \_id (por ejemplo, un `MongoDB\BSON\ObjectId` inicializado en el constructor) al devolver datos para un documento raíz BSON. En ausencia de una propiedad \_id, la extensión o el servidor generará un `MongoDB\BSON\ObjectId` para operaciones de inserción o actualización (upsert), respectivamente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array`, `stdClass`, `MongoDB\BSON\Document`, o `MongoDB\BSON\PackedArray` que se serializará como un array o documento BSON.

## Historial de cambios

<table>
<thead>
<tr>
<th>Versión</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PECL mongodb 2.0.0</td>
<td>Los tipos de retorno previamente declarados como provisionales ahora son aplicados.</td>
</tr>
<tr>
<td>PECL mongodb 1.17.0</td>
<td><p>El tipo de retorno se cambió de <code>arrayobject</code>. En lugar de <code>object</code>, el tipo de retorno ahora especifica <code>stdClass</code>. Las clases que implementan esta interfaz deben modificarse para dejar de declarar un tipo de retorno <code>object</code>. Como el tipo de retorno es tentativo, se emite una advertencia de obsolescencia en PHP 8.1 y versiones posteriores.</p>
<p>Además de los cambios anteriores, la extensión ahora también admite devolver instancias de <code>MongoDB\BSON\Document</code> y <code>MongoDB\BSON\PackedArray</code>. Tenga en cuenta que cualquier instancia de <code>MongoDB\BSON\PackedArray</code> devuelta se convierte silenciosamente en objetos cuando se almacenan como documentos raíz. Se almacenan como arrays cuando se utilizan como valor de campo incrustado.</p></td>
</tr>
</tbody>
</table>

## Ejemplos

`MongoDB\BSON\Serializable::bsonSerialize` que devuelve un array asociativo para documento raíz

```
<?php

class MyDocument implements MongoDB\BSON\Serializable
{
    private $id;

    function __construct()
    {
        $this->id = new MongoDB\BSON\ObjectId;
    }

    function bsonSerialize(): array
    {
        return ['_id' => $this->id, 'foo' => 'bar'];
    }
}

echo MongoDB\BSON\Document::fromPHP(new MyDocument)->toRelaxedExtendedJSON(), "\n";

?>

   
```php

Resultado del ejemplo anterior es similar a:

    { "_id" : { "$oid" : "56cccdcada14d8755a58c591" }, "foo" : "bar" }

`MongoDB\BSON\Serializable::bsonSerialize` que devuelve un array secuencial para documento raíz

```
<?php

class MyArray implements MongoDB\BSON\Serializable
{
    function bsonSerialize(): array
    {
        return [1, 2, 3];
    }
}

echo MongoDB\BSON\Document::fromPHP(new MyArray)->toRelaxedExtendedJSON(), "\n";

?>

   
```php

El ejemplo anterior mostrará:

    { "0" : 1, "1" : 2, "2" : 3 }

`MongoDB\BSON\Serializable::bsonSerialize` que devuelve un array asociativo para campo de documento

```
<?php

class MyDocument implements MongoDB\BSON\Serializable
{
    function bsonSerialize(): array
    {
        return ['foo' => 'bar'];
    }
}

$value = ['document' => new MyDocument];

echo MongoDB\BSON\Document::fromPHP($value)->toRelaxedExtendedJSON(), "\n";

?>

   
```php

El ejemplo anterior mostrará:

    { "document" : { "foo" : "bar" } }

`MongoDB\BSON\Serializable::bsonSerialize` que devuelve un array secuencial para campo de documento

```
<?php

class MyArray implements MongoDB\BSON\Serializable
{
    function bsonSerialize(): array
    {
        return [1, 2, 3];
    }
}

$value = ['array' => new MyArray];

echo MongoDB\BSON\Document::fromPHP($value)->toRelaxedExtendedJSON(), "\n";

?>

   
```php

El ejemplo anterior mostrará:

    { "array" : [ 1, 2, 3 ] }

## Véase también

MongoDB\BSON\Unserializable::bsonUnserialize

MongoDB\BSON\Persistable
