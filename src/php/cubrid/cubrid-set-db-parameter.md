---
title: cubrid_set_db_parameter
description: Define los parámetros de la base de datos CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-set-db-parameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-set-db-parameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9500
---

cubrid_set_db_parameter

Define los parámetros de la base de datos CUBRID

## Descripción

```php
cubrid_set_db_parameter(resource $conn_identifier, int $param_type, int $param_value): bool
```php

La función `cubrid_set_db_parameter` se utiliza para definir los parámetros de la base de datos CUBRID. Puede definir los siguientes parámetros de la base de datos CUBRID:

PARAM_ISOLATION_LEVEL

PARAM_LOCK_TIMEOUT

> [!NOTE]
> El modo auto-commit puede ser definido utilizando la función `cubrid_set_autocommit`.

## Parámetros

`conn_identifier`  
La conexión CUBRID. Si el identificador de conexión no es especificado, se utilizará el último enlace abierto por la función `cubrid_connect`.

`param_type`  
Tipo de parámetro de la base de datos.

`param_value`  
Nivel de aislamiento (1-6) o el valor del tiempo de espera (en segundos).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_get_db_parameter`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

$params = cubrid_get_db_parameter($conn);
var_dump($params);

cubrid_set_autocommit($conn, CUBRID_AUTOCOMMIT_TRUE);
cubrid_set_db_parameter($conn, CUBRID_PARAM_ISOLATION_LEVEL, 2);

$params_new = cubrid_get_db_parameter($conn);
var_dump($params_new);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(4) {
      ["PARAM_ISOLATION_LEVEL"]=>
      int(3)
      ["PARAM_LOCK_TIMEOUT"]=>
      int(-1)
      ["PARAM_MAX_STRING_LENGTH"]=>
      int(1073741823)
      ["PARAM_AUTO_COMMIT"]=>
      int(0)
    }
    array(4) {
      ["PARAM_ISOLATION_LEVEL"]=>
      int(2)
      ["PARAM_LOCK_TIMEOUT"]=>
      int(-1)
      ["PARAM_MAX_STRING_LENGTH"]=>
      int(1073741823)
      ["PARAM_AUTO_COMMIT"]=>
      int(1)
    }

## Véase también

cubrid_get_db_parameter

cubrid_set_autocommit
