---
title: cubrid_list_dbs
description: Devuelve una matriz con la lista de todas las bases de datos Cubrid existentes
source_url: https://www.php.net/manual/es/function.cubrid-list-dbs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-list-dbs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8780
---

cubrid_list_dbs

Devuelve una matriz con la lista de todas las bases de datos Cubrid existentes

## Descripción

```php
cubrid_list_dbs([resource $conn_identifier]): array
```php

Esta función devuelve una matriz con la lista de todas las bases de datos Cubrid existentes.

## Parámetros

`conn_identifier`  
La conexión CUBRID.

## Valores devueltos

Una matriz numérica con todas las bases de datos Cubrid existentes; en caso de éxito.

`false` en caso de fallo.

## Ejemplos

Ejemplo de `cubrid_list_dbs`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$db_list = cubrid_list_dbs($conn);
var_dump($db_list);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      string(6) "demodb"
    }
