---
title: MongoDB\Driver\ReadPreference::getTagSets
description: Devuelve la opción "tagSets" de ReadPreference
source_url: https://www.php.net/manual/es/mongodb-driver-readpreference.gettagsets.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference/gettagsets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50920
---

MongoDB\Driver\ReadPreference::getTagSets

Devuelve la opción "tagSets" de ReadPreference

## Descripción

```php
final public MongoDB\Driver\ReadPreference::getTagSets(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "tagSets" de ReadPreference.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadPreference::getTagSets`

```
<?php

$mode = MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED;

/* Null y un array vacío indican ambos la ausencia de preferencia de conjunto de etiquetas. */
$rp = new MongoDB\Driver\ReadPreference($mode, null);
var_dump($rp->getTagSets());

$rp = new MongoDB\Driver\ReadPreference($mode, []);
var_dump($rp->getTagSets());

/* Preferir un nodo en Nueva York, pero volver a cualquier nodo disponible. */
$rp = new MongoDB\Driver\ReadPreference($mode, [['dc' => 'ny']]);
var_dump($rp->getTagSets());

/* Preferir un nodo en Nueva York, seguido de un nodo en San Francisco
   etiquetado para el reporting, y finalmente volver a cualquier nodo disponible. */
$rp = new MongoDB\Driver\ReadPreference($mode, [
  ['dc' => 'ny'],
  ['dc' => 'sf', 'use' => 'reporting'],
  [],
]);
var_dump($rp->getTagSets());

?>

   
```php

El ejemplo anterior mostrará:

    array(0) {
    }
    array(0) {
    }
    array(2) {
      [0]=>
      array(1) {
        ["dc"]=>
        string(2) "ny"
      }
      [1]=>
      array(0) {
      }
    }
    array(3) {
      [0]=>
      array(1) {
        ["dc"]=>
        string(2) "ny"
      }
      [1]=>
      array(2) {
        ["dc"]=>
        string(2) "sf"
        ["use"]=>
        string(9) "reporting"
      }
      [2]=>
      array(0) {
      }
    }

## Véase también

Referencia de Read Preference
