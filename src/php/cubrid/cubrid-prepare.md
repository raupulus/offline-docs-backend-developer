---
title: cubrid_prepare
description: Prepara una consulta SQL para su ejecución
source_url: https://www.php.net/manual/es/function.cubrid-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 5acad2fc9
order: 9410
---

cubrid_prepare

Prepara una consulta SQL para su ejecución

## Descripción

```php
cubrid_prepare(resource $conn_identifier, string $prepare_stmt, [int $option]): resource
```php

La función `cubrid_prepare` compila una consulta SQL para un gestor de conexión dado y devuelve un gestor que representa la consulta precompilada.

Una consulta preparada puede ser ejecutada varias veces, lo cual resulta eficiente para la ejecución repetida o para el procesamiento de grandes volúmenes de datos. Solo se puede utilizar una única consulta, y un parámetro puede marcarse con un signo de interrogación (`?`) en el lugar apropiado de la consulta SQL. Se añade un parámetro al vincular un valor en la cláusula `VALUES` de una sentencia `INSERT` o en la cláusula `WHERE`. Tenga en cuenta que un valor solo puede ser vinculado a un parámetro utilizando la función `cubrid_bind`.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`prepare_stmt`  
Consulta preparada.

`option`  
OID devuelto por la opción `CUBRID_INCLUDE_OID`.

## Valores devueltos

Identificador de consulta en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_prepare`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$sql = <<<EOD
SELECT g.event_code, e.name
FROM game g
JOIN event e ON g.event_code=e.code
WHERE host_year = ? AND event_code NOT IN (SELECT event_code FROM game WHERE host_year=?) GROUP BY event_code;
EOD;

$req = cubrid_prepare($conn, $sql);

cubrid_bind($req, 1, 2004);
cubrid_bind($req, 2, 2000);
cubrid_execute($req);

$row_num = cubrid_num_rows($req);
printf("There are %d event that exits in 2004 olympic but not in 2000. For example:\n\n", $row_num);

printf("%-15s %s\n", "Event_code", "Event_name");
printf("----------------------------\n");

$row = cubrid_fetch_assoc($req);
printf("%-15d %s\n", $row["event_code"], $row["name"]);
$row = cubrid_fetch_assoc($req);
printf("%-15d %s\n", $row["event_code"], $row["name"]);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    There are 27 event that exits in 2004 olympic but not in 2000. For example:

    Event_code      Event_name
    ----------------------------
    20063           +91kg
    20070           64kg

## Véase también

cubrid_execute

cubrid_bind
