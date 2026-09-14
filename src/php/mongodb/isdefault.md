---
title: MongoDB\Driver\ReadConcern::isDefault
description: Verifica si es el read concern por omisión
source_url: https://www.php.net/manual/es/mongodb-driver-readconcern.isdefault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readconcern/isdefault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 50840
---

MongoDB\Driver\ReadConcern::isDefault

Verifica si es el read concern por omisión

## Descripción

```php
final public MongoDB\Driver\ReadConcern::isDefault(): bool
```php

Devuelve si es el read concern por omisión (es decir, sin opciones especificadas). Este método está principalmente destinado a ser utilizado en conjunción con MongoDB\Driver\Manager::getReadConcern para determinar si el Manager ha sido construido sin ninguna opción de read concern.

El controlador no incluirá un read concern por omisión en sus operaciones de lectura (por ejemplo MongoDB\Driver\Manager::executeQuery) para permitir que el servidor aplique su propio valor por omisión. Las bibliotecas que acceden al read concern del Manager para incluirlo en sus propios comandos de lectura deberían utilizar este método para asegurarse de que los read concerns por omisión se dejan sin definir.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si es el read concern por omisión y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadConcern::isDefault`

```
<?php

$rc = new MongoDB\Driver\ReadConcern(null);
var_dump($rc->isDefault());

$rc = new MongoDB\Driver\ReadConcern(MongoDB\Driver\ReadConcern::MAJORITY);
var_dump($rc->isDefault());

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1/?readConcernLevel=majority');
$rc = $manager->getReadConcern();
var_dump($rc->isDefault());

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1/');
$rc = $manager->getReadConcern();
var_dump($rc->isDefault());

?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(false)
    bool(true)

## Véase también

MongoDB\Driver\Manager::getReadConcern

Referencia de Read Concern
