---
title: oci_fetch_object
description: Lee una línea de un resultado en forma de objeto
source_url: https://www.php.net/manual/es/function.oci-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57310
---

oci_fetch_object

Lee una línea de un resultado en forma de objeto

## Descripción

```php
oci_fetch_object(resource $statement, [int $mode]): stdClass
```php

Devuelve un objeto que contiene la siguiente línea de resultado de una consulta. Cada atributo de este objeto corresponde a una columna de la línea. Esta función se utiliza típicamente en un ciclo mientras no devuelva `false`, lo que indica que no hay más líneas disponibles.

Para más detalles sobre el mapeo de tipos de datos realizado por la extensión OCI8, lea los [tipos de datos soportados por el driver](#oci8.datatypes).

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

## Valores devueltos

Devuelve un objeto. Cada atributo de este objeto corresponde a una columna de la línea. Si no hay más líneas disponibles en la consulta `statement` entonces se devuelve `false`.

Todas las columnas `LOB` son devueltas en forma de descriptores LOB.

Las columnas `DATE` son devueltas en forma de strings formateados con el formato de fecha actual. El formato por omisión puede ser cambiado mediante las variables de entorno Oracle, como `NLS_LANG` o ejecutando el comando `ALTER SESSION SET NLS_DATE_FORMAT`.

Los nombres de columnas que no son sensibles a la casse (por omisión en Oracle), tendrán nombres de atributos en mayúsculas. Los nombres de columnas que son sensibles a la casse, tendrán nombres de atributos utilizando exactamente la misma casse de la columna. Utilice la función `var_dump` sobre el objeto de resultado para verificar la casse apropiada para el acceso a los atributos.

Los valores de atributo serán `null` para cada campo de datos `NULL`.

## Ejemplos

Ejemplo con `oci_fetch_object`

```
<?php

/*
  Antes de la ejecución, cree la tabla:
    CREATE TABLE mytab (id NUMBER, description VARCHAR2(30));
    INSERT INTO mytab (id, description) values (1, 'Fish and Chips');
    COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT id, description FROM mytab');
oci_execute($stid);

while (($row = oci_fetch_object($stid)) != false) {
    // Utilice nombres de atributos sensibles a la casse para cada columna estándar de Oracle
    echo $row->ID . "<br>\n";
    echo $row->DESCRIPTION . "<br>\n";
}

// Muestra:
//    1
//    Fish and Chips

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_object` con nombres de columna sensibles a la casse

```
<?php

/*
  Antes de la ejecución, cree la tabla con una columna cuyo nombre es sensible a la casse:
    CREATE TABLE mytab (id NUMBER, "MyDescription" VARCHAR2(30));
    INSERT INTO mytab (id, "MyDescription") values (1, 'Iced Coffee');
    COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT id, "MyDescription" FROM mytab');
oci_execute($stid);

while (($row = oci_fetch_object($stid)) != false) {
    // Utilice nombres de atributos en mayúsculas para cada columna estándar de Oracle
    echo $row->ID . "<br>\n";
    // Utilice la casse exacta para los nombres de columnas sensibles a la casse
    echo $row->MyDescription . "<br>\n";
}

// Muestra:
//    1
//    Iced Coffee

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_object` con LOBs

```
<?php

/*
  Antes de la ejecución, cree la tabla:
    CREATE TABLE mytab (id NUMBER, description CLOB);
    INSERT INTO mytab (id, description) values (1, 'A very long string');
    COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT id, description FROM mytab');
oci_execute($stid);

while (($row = oci_fetch_object($stid)) != false) {
    echo $row->ID . "<br>\n";
    // Lo siguiente mostrará los 11 primeros bytes desde DESCRIPTION
    echo $row->DESCRIPTION->read(11) . "<br>\n";
}

// Muestra:
//    1
//    A very long

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Véase también

`oci_fetch`, `oci_fetch_all`, `oci_fetch_assoc`, `oci_fetch_array`, `oci_fetch_row`
