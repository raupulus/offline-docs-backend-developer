---
title: MongoDB\BSON\ObjectId::getTimestamp
description: Devuelve el componente de timestamp de ObjectId
source_url: https://www.php.net/manual/es/mongodb-bson-objectid.gettimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/objectid/gettimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48030
---

MongoDB\BSON\ObjectId::getTimestamp

Devuelve el componente de timestamp de ObjectId

## Descripción

```php
final public MongoDB\BSON\ObjectId::getTimestamp(): int
```php

El componente de timestamp de un ObjectId son sus 32 bits más significativos, que denotan el número de segundos desde el epoch Unix. Este valor se lee como un entero de 32 bits sin signo con un orden de bytes big-endian.

> [!NOTE]
> Dado que el tipo integer de PHP es con signo, algunos de los valores devueltos por este método pueden aparecer como enteros negativos en plataformas de 32 bits. El formateador `"%u"` de `sprintf` se puede utilizar para obtener una representación en forma de string del valor decimal sin signo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de timestamp de ObjectId.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\BSON\ObjectId::getTimestamp`

```
<?php

var_dump((new MongoDB\BSON\ObjectId())->getTimestamp());

var_dump((new MongoDB\BSON\ObjectId('0000002a0000000000000000'))->getTimestamp());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    integer(1484854719)
    integer(42)

## Véase también

Referencia ObjectId

Tipos BSON : ObjectId
