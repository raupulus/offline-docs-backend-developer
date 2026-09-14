---
title: cubrid_bind
description: Vincular variables para una sentencia preparada como parámetros
source_url: https://www.php.net/manual/es/function.cubrid-bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 8860
---

cubrid_bind

Vincular variables para una sentencia preparada como parámetros

## Descripción

```php
cubrid_bind(resource $req_identifier, int $bind_index, mixed $bind_value, [string $bind_value_type]): bool
```php

La función `cubrid_bind` se usa para vincular valores a un marcador de posición nominado o signo de interrogación correspondiente en la sentencia SQL que fue pasada a `cubrid_prepare`. Si no se da `bind_value_type`, string será lo predeterminado.

> [!NOTE]
> Si el tipo de datos a ser vinculados es BLOB/CLOB, CUBRID intentará mapear la información como un flujo de PHP. Si el tipo real de valor vinculado no es un flujo, CUBRID intentará convertirlo a cadena, y usarlo como la ruta completa y el nombre de fichero de un fichero del sistema de ficheros cliente.
>
> Si el tipo de datos a ser vinculados explícitamente es ENUM, el argumento `bind_value` debería ser el elemento enum que esté en formato string.
>
> En un entorno fragmentado de CUBRID, se debe incluir de `bind_value_type` en la función `cubrid_bind`

La siguiente tabla muestra los tipos de los valores sustitutos.

| Soporte      | Tipo de Vinculación | Tipo SQL Correspondiente |
|--------------|---------------------|--------------------------|
| Soportado    | STRING              | CHAR, VARCHAR            |
|              | NCHAR               | NCHAR, NVARCHAR          |
|              | BIT                 | BIT, VARBIT              |
|              | NUMERIC or NUMBER   | SHORT, INT, NUMERIC      |
|              | FLOAT               | FLOAT                    |
|              | DOUBLE              | DOUBLE                   |
|              | TIME                | TIME                     |
|              | DATE                | DATE                     |
|              | TIMESTAMP           | TIMESTAMP                |
|              | OBJECT              | OBJECT                   |
|              | ENUM                | ENUM                     |
|              | BLOB                | BLOB                     |
|              | CLOB                | CLOB                     |
|              | NULL                | NULL                     |
| No soportado | SET                 | SET                      |
|              | MULTISET            | MULTISET                 |
|              | SEQUENCE            | SEQUENCE                 |

Tipos de Datos de Vinculación de CUBRID

## Parámetros

`req_identifier`  
Identificador de solicitud como resultado de `cubrid_prepare`

`bind_index`  
Índice de ubicación de los parámetros de vinculación. Comienza con 1.

`bind_value`  
Valor actual para el vínculo.

`bind_index`  
Un tipo de valor a vincular. (Es omitido por defecto. Así, el sistema internamente usa una cadena por omisión. Sin embargo, se necesita especificar el tipo exacto del valor como argumento cuando son de tipo NCHAR, BIT, o BLOB/CLOB).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                       |
|---------|---------------------------------------------------|
| 8.3.1   | Añadido el soporte para tipos de datos BLOB/CLOB. |

## Ejemplos

Ejemplo de `cubrid_bind`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

$result = cubrid_execute($conn, "SELECT code FROM event WHERE sports='Basketball' and gender='M'");
$row = cubrid_fetch_array($result, CUBRID_ASSOC);
$event_code = $row["code"];

cubrid_close_request($result);

$game_req = cubrid_prepare($conn, "SELECT athlete_code FROM game WHERE host_year=1992 and event_code=? and nation_code='USA'");
cubrid_bind($game_req, 1, $event_code, "number");
cubrid_execute($game_req);

printf("--- Dream Team (1992 United States men's Olympic basketball team) ---\n");
while ($athlete_code = cubrid_fetch_array($game_req, CUBRID_NUM)) {
    $athlete_req  = cubrid_prepare($conn, "SELECT name FROM athlete WHERE code=? AND  nation_code='USA' AND event='Basketball' AND gender='M'");
    cubrid_bind($athlete_req, 1, $athlete_code[0], "number");
    cubrid_execute($athlete_req);
    $row = cubrid_fetch_assoc($athlete_req);
    printf("%s\n", $row["name"]);
}

cubrid_close_request($game_req);
cubrid_close_request($athlete_req);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    --- Dream Team (1992 United States men's Olympic basketball team) ---
    Stockton John
    Robinson David
    Pippen Scottie
    Mullin C.
    Malone Karl
    Laettner C.
    Jordan Michael
    Johnson Earvin
    Ewing Patrick
    Drexler Clyde
    Bird Larry
    Barkley Charles

Ejemplo de BLOB/CLOB de `cubrid_bind`

```
<?php
$con = cubrid_connect("localhost", 33000, "demodb", "dba", "");
if ($con) {
    cubrid_execute($con,"DROP TABLE if exists php_cubrid_lob_test");
    cubrid_execute($con,"CREATE TABLE php_cubrid_lob_test (doc_content CLOB)");
    $sql = "INSERT INTO php_cubrid_lob_test(doc_content) VALUES(?)";
    $req = cubrid_prepare($con, $sql);

    $fp = fopen("book.txt", "rb");

    cubrid_bind($req, 1, $fp, "clob");
    cubrid_execute($req);
}
?>

   
```php

Ejemplo de BLOB/CLOB de `cubrid_bind`

```
<?php
$con = cubrid_connect("localhost", 33000, "foo");
if ($con) {
    cubrid_execute($con,"DROP TABLE if exists php_cubrid_lob_test");
    cubrid_execute($con,"CREATE TABLE php_cubrid_lob_test (image BLOB)");
    $sql = "INSERT INTO php_cubrid_lob_test(image) VALUES(?)";
    $req = cubrid_prepare($con, $sql);

    cubrid_bind($req, 1, "cubrid_logo.png", "blob");
    cubrid_execute($req);
}
?>

   
```php

## Véase también

cubrid_execute

cubrid_prepare
