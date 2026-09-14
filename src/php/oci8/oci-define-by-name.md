---
title: oci_define_by_name
description: Asocia una variable PHP con una columna para una consulta de recuperación
  de datos
source_url: https://www.php.net/manual/es/function.oci-define-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-define-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 61374bbe2
order: 57250
---

oci_define_by_name

Asocia una variable PHP con una columna para una consulta de recuperación de datos

## Descripción

```php
oci_define_by_name(resource $statement, string $column, mixed $var, [int $type]): bool
```php

Asocia una variable PHP con una columna para una consulta de recuperación de datos utilizando la función `oci_fetch`.

La llamada a la función `oci_define_by_name` debe realizarse antes de la ejecución de la función `oci_execute`.

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

`column`  
El nombre de la columna utilizado en la consulta.

Utilice un nombre en mayúsculas para los nombres de columna no sensibles a la casilla (por omisión bajo Oracle). Utilice la casilla exacta del nombre de la columna para los nombres de columna sensibles a la casilla.

`var`  
La variable PHP que contendrá el valor devuelto por la columna.

`type`  
El tipo de datos a devolver. En general, este argumento no es necesario. Tenga en cuenta que el estilo Oracle de conversión de datos no se aplica aquí. Por ejemplo, `SQLT_INT` será ignorado y el tipo de datos devuelto será `SQLT_CHR`.

Puede utilizar, opcionalmente, la función `oci_new_descriptor` para asignar descriptores LOB/ROWID/BFILE.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_define_by_name`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$sql = 'SELECT location_id, city FROM locations WHERE location_id < 1200';
$stid = oci_parse($conn, $sql);

// Las definiciones DEBEN realizarse antes de la ejecución de la consulta
oci_define_by_name($stid, 'LOCATION_ID', $locid);
oci_define_by_name($stid, 'CITY', $city);

oci_execute($stid);

// Cada recuperación poblará las variables previamente definidas con los datos de la siguiente línea
while (oci_fetch($stid)) {
    echo "Location id $locid is $city<br>\n";
}

// Muestra:
//   Location id 1000 is Roma
//   Location id 1100 is Venice

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_define_by_name` y nombres de columna sensibles a la casilla

```
<?php

/*
  Antes de la ejecución, cree la tabla siguiente con un nombre de columna sensible a la casilla:
    CREATE TABLE mytab (id NUMBER, "MyDescription" VARCHAR2(30));
    INSERT INTO mytab (id, "MyDescription") values (1, 'Iced Coffee');
    COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM mytab');

// Utilice mayúsculas para los nombres de columna no sensibles a la casilla
oci_define_by_name($stid, 'ID', $id);

// Utilice la casilla exacta para los nombres de columnas sensibles a la casilla
oci_define_by_name($stid, 'MyDescription', $mydesc);

oci_execute($stid);

while (oci_fetch($stid)) {
    echo "id $id is $mydesc<br>\n";
}

// Muestra:
//   id 1 is Iced Coffee

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_define_by_name` y columnas de tipo LOB

```
<?php

/*
  Antes de la ejecución, cree la tabla siguiente:
    CREATE TABLE mytab (id NUMBER, fruit CLOB);
    INSERT INTO mytab (id, fruit) values (1, 'apple');
    INSERT INTO mytab (id, fruit) values (2, 'orange');
    COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM mytab');

// Las definiciones DEBEN realizarse antes de la ejecución
oci_define_by_name($stid, 'ID', $id);
oci_define_by_name($stid, 'FRUIT', $fruit);  // $fruit se convertirá en un descriptor LOB

oci_execute($stid);

while (oci_fetch($stid)) {
    echo $id . " is " . $fruit->load(100) . "<br>\n";
}

// Muestra:
//   1 is apple
//   2 is orange

$fruit->free();
oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_define_by_name` y un tipo explícito

```
<?php

/*
  Antes de la ejecución, cree la tabla siguiente:
    CREATE TABLE mytab (id NUMBER, fruit CLOB);
    INSERT INTO mytab (id, fruit) values (1, 'apple');
    INSERT INTO mytab (id, fruit) values (2, 'orange');
    COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM mytab');

// Las definiciones DEBEN realizarse antes de la ejecución
oci_define_by_name($stid, 'ID', $id);

$fruit = oci_new_descriptor($conn, OCI_D_LOB);
oci_define_by_name($stid, 'FRUIT', $fruit, OCI_D_CLOB);

oci_execute($stid);

while (oci_fetch($stid)) {
    echo $id . " is " . $fruit->load(100) . "<br>\n";
}

// Muestra:
//   1 is apple
//   2 is orange

$fruit->free();
oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Véase también

`oci_fetch`, `oci_new_descriptor`
