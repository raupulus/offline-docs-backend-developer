---
title: MongoDB\BSON\Unserializable::bsonUnserialize
description: Construye el objeto a partir de un array o documento BSON
source_url: https://www.php.net/manual/es/mongodb-bson-unserializable.bsonunserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/unserializable/bsonunserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48580
---

MongoDB\BSON\Unserializable::bsonUnserialize

Construye el objeto a partir de un array o documento BSON

## Descripción

```php
abstract public MongoDB\BSON\Unserializable::bsonUnserialize(array $data): void
```php

Se invoca durante la deserialización del objeto desde BSON. Las propiedades del array o documento BSON se pasarán a este método como un `array`.

Recuerde verificar la existencia de una propiedad \_id al procesar datos de un documento BSON.

> [!NOTE]
> Este método actúa como el [constructor](#language.oop5.decon.constructor) del objeto. El método [\_\_construct()](#object.construct) no será llamado después de este método.

## Parámetros

`data` (`array`)  
Propiedades dentro del array o documento BSON.

## Valores devueltos

El valor de retorno de este método se ignora.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Los tipos de retorno previamente declarados como provisionales ahora son aplicados. |

## Ejemplos

Ejemplo de `MongoDB\BSON\Unserializable::bsonUnserialize`

```
<?php

class MyDocument implements MongoDB\BSON\Unserializable
{
    private $data = [];

    function bsonUnserialize(array $data): void
    {
        $this->data = $data;
    }
}

$bson = MongoDB\BSON\Document::fromJSON('{ "foo": "bar" }');

var_dump($bson->toPHP(['root' => 'MyDocument']));

?>

   
```php

El ejemplo anterior mostrará:

    object(MyDocument)#1 (1) {
      ["data":"MyDocument":private]=>
      array(1) {
        ["foo"]=>
        string(3) "bar"
      }
    }

## Véase también

MongoDB\BSON\Serializable::bsonSerialize

MongoDB\BSON\Persistable
