---
title: cubrid_get_class_name
description: Obtener el nombre de la clase usando OID
source_url: https://www.php.net/manual/es/function.cubrid-get-class-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get-class-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9070
---

cubrid_get_class_name

Obtener el nombre de la clase usando OID

## Descripción

```php
cubrid_get_class_name(resource $conn_identifier, string $oid): string
```php

La función `cubrid_get_class_name` se usa para obtener el nombre de la clase del `oid`. No funciona al seleccionar datos desde las tablas del sistema, por ejemplo db_class.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
Oid de la instancia de la que se quiere comprobar su existencia.

## Valores devueltos

El nombre de la clase cuando el proceso tiene éxito, o `false` si ocurre un error.

`false`, cuando el proceso no tiene éxito.

## Ejemplos

Ejemplo de `cubrid_get_class_name`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

$req = cubrid_execute($conn, "SELECT * FROM code", CUBRID_INCLUDE_OID);
$oid = cubrid_current_oid($req);
$class_name = cubrid_get_class_name($conn, $oid);

print_r($class_name);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    code

## Véase también

cubrid_is_instance

cubrid_drop
