---
title: MongoDB\Driver\Manager::getReadPreference
description: Devuelve el ReadPreference para el Manager
source_url: https://www.php.net/manual/es/mongodb-driver-manager.getreadpreference.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/getreadpreference.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49810
---

MongoDB\Driver\Manager::getReadPreference

Devuelve el ReadPreference para el Manager

## Descripción

```php
final public MongoDB\Driver\Manager::getReadPreference(): MongoDB\Driver\ReadPreference
```php

Devuelve el `MongoDB\Driver\ReadPreference` para el Manager, que se deriva de sus opciones URI. Es el ReadPreference por omisión para las peticiones y comandos ejecutados en el Manager.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El `MongoDB\Driver\ReadPreference` para el Manager.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\Manager::getReadPreference`

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
var_dump($manager->getReadPreference());

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017/?readPreference=secondaryPreferred&readPreferenceTags=dc:ny,rack:1&readPreferenceTags=dc:ny&readPreferenceTags=');
var_dump($manager->getReadPreference());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\ReadPreference)#2 (1) {
      ["mode"]=>
      string(7) "primary"
    }
    object(MongoDB\Driver\ReadPreference)#1 (2) {
      ["mode"]=>
      string(18) "secondaryPreferred"
      ["tags"]=>
      array(3) {
        [0]=>
        object(stdClass)#3 (2) {
          ["dc"]=>
          string(2) "ny"
          ["rack"]=>
          string(1) "1"
        }
        [1]=>
        object(stdClass)#4 (1) {
          ["dc"]=>
          string(2) "ny"
        }
        [2]=>
        object(stdClass)#5 (0) {
        }
      }
    }

## Véase también

MongoDB\Driver\ReadPreference

MongoDB\Driver\Manager::\_\_construct
