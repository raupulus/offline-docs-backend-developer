---
title: MongoDB\BSON\fromPHP
description: Devuelve la representación BSON de un valor PHP
source_url: https://www.php.net/manual/es/function.mongodb.bson-fromphp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/bson/fromphp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 48760
---

MongoDB\BSON\fromPHP

Devuelve la representación BSON de un valor PHP

> [!WARNING]
> Esta función ha sido *DEPRECADA* a partir de la versión 1.20.0 de la extensión y fue eliminada en la versión 2.0. Las aplicaciones deben usar MongoDB\BSON\Document::fromPHP en su lugar.

## Descripción

```php
MongoDB\BSON\fromPHP(array $valor): string
```php

Serializa un array o objeto PHP (por ejemplo, un documento) a su representación [BSON](https://www.mongodb.com/docs/manual/reference/bson-types/). La cadena binaria devuelta describirá un documento BSON.

## Parámetros

`valor` (`arrayobject`)  
Valor PHP que se serializará.

## Valores devueltos

El documento BSON serializado como una cadena binaria.

## Errores/Excepciones

Lanza

MongoDB\Driver\Exception\UnexpectedValueException

si el valor PHP no puede convertirse a BSON. Las razones posibles incluyen, entre otras, encontrar una instancia inesperada de

MongoDB\BSON\Type

o que

MongoDB\BSON\Serializable::bsonSerialize

no devuelva un

array

o un

stdClass

.

## Historial de cambios

| Versión            | Descripción                     |
|--------------------|---------------------------------|
| PECL mongodb 2.0.0 | Esta función ha sido eliminada. |

## Ejemplos

Ejemplo de `MongoDB\BSON\fromPHP`

```
<?php

$bson = MongoDB\BSON\fromPHP(['foo' => 1]);
echo bin2hex($bson), "\n";

?>

   
```php

El ejemplo anterior mostrará:

    0e00000010666f6f000100000000

## Véase también

MongoDB\BSON\Document::fromPHP

MongoDB\BSON\toPHP

MongoDB BSON
