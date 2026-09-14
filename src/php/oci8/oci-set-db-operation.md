---
title: oci_set_db_operation
description: Establece la operación de base de datos
source_url: https://www.php.net/manual/es/function.oci-set-db-operation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-db-operation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: ed6de1ae2
order: 57630
---

oci_set_db_operation

Establece la operación de base de datos

## Descripción

```php
oci_set_db_operation(resource $connection, string $action): bool
```php

Establece el DBOP para el seguimiento de Oracle.

El nombre de la operación de la base de datos se registra en la base de datos cuando se produce el siguiente "ida y vuelta" de PHP a la base de datos, normalmente cuando se ejecuta una instrucción SQL.

La operación de la base de datos puede consultarse posteriormente desde las vistas de administración de la base de datos como `V$SQL_MONITOR`.

La función `oci_set_db_operation` está disponible cuando OCI8 utiliza la biblioteca cliente de Oracle 12 (o posterior) y Oracle Database 12 (o posterior).

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o la función `oci_new_connect`.

`action`  
El string elegida por el usuario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ajuste del DBOP

```
<?php

$c = oci_connect('hr', 'welcome', 'localhost/XE');

// Record the operation
oci_set_db_operation($c, 'main query');

// Code that causes a round-trip, for example a query:
$s = oci_parse($c, 'select * from dual');
oci_execute($s);
oci_fetch_all($s, $res);

sleep(30);

?>

    
```php

    // While the script is running, the administrator can see the database operations
    // being performed:

    sqlplus system/welcome
    SQL> select dbop_name from v$sql_monitor;

## Notas

> [!CAUTION]
> Algunas funciones OCI8 requieren ida y vuelta con la base de datos. Estas ida y vuelta pueden ser evitadas al usar consultas cuyo resultado es almacenado en caché.

## Véase también

`oci_set_action`, `oci_set_module_name`, `oci_set_client_info`, `oci_set_client_identifier`
