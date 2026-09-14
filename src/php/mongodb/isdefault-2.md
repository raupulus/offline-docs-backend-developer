---
title: MongoDB\Driver\WriteConcern::isDefault
description: Verifica si es el WriteConcern por omisión
source_url: https://www.php.net/manual/es/mongodb-driver-writeconcern.isdefault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcern/isdefault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51510
---

MongoDB\Driver\WriteConcern::isDefault

Verifica si es el WriteConcern por omisión

## Descripción

```php
final public MongoDB\Driver\WriteConcern::isDefault(): bool
```php

Devuelve si es el WriteConcern por omisión (es decir, sin opciones especificadas). Este método está principalmente destinado a ser utilizado en conjunción con MongoDB\Driver\Manager::getWriteConcern para determinar si el Manager ha sido construido sin ninguna opción de WriteConcern.

El controlador no incluirá un WriteConcern por omisión en sus operaciones de escritura (por ejemplo MongoDB\Driver\Manager::executeBulkWrite) para permitir que el servidor aplique su propio WriteConcern por omisión, que puede haber sido [modificado](https://www.mongodb.com/docs/manual/core/replica-set-write-concern/#modify-default-write-concern). Las bibliotecas que acceden al WriteConcern del Manager para incluirlo en sus propios comandos de escritura deberían utilizar este método para asegurarse de que los WriteConcern por omisión no están definidos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si es el WriteConcern por omisión y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\WriteConcern::isDefault`

```
<?php

$wc = new MongoDB\Driver\WriteConcern(1);
var_dump($wc->isDefault());

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1/?w=majority');
$wc = $manager->getWriteConcern();
var_dump($wc->isDefault());

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1/');
$wc = $manager->getWriteConcern();
var_dump($wc->isDefault());

?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    bool(true)

## Véase también

MongoDB\Driver\Manager::getWriteConcern

Modificar el Write Concern por omisión

en el manual de MongoDB

Referencia de Write Concern
