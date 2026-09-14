---
title: cubrid_insert_id
description: Devuelve el ID generado por la última columna actualizada AUTO_INCREMENT
source_url: https://www.php.net/manual/es/function.cubrid-insert-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-insert-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 9130
---

cubrid_insert_id

Devuelve el ID generado por la última columna actualizada

AUTO_INCREMENT

## Descripción

```php
cubrid_insert_id([resource $conn_identifier]): string
```php

La función `cubrid_insert_id` recupera el ID generado para la columna AUTO_INCREMENT que fue actualizada por la consulta INSERT previa. Devuelve 0 si la consulta previa no generó nuevas filas, o FALSE en caso de error.

> [!NOTE]
> CUBRID soporta AUTO_INCREMENT para más de una columna en una tabla. En la mayoría de los casos, habrá una única columna AUTO_INCREMENT en una tabla. Si hay varias columnas AUTO_INCREMENT, esta función no debería ser usada aunque devuelva un valor.

## Parámetros

`conn_identifier`  
El Identificador de conexión previamente obtenido por una llamada a `cubrid_connect`.

## Valores devueltos

Un string representa el ID generado para una columna AUTO:INCREMENT por la consulta previa, en caso de éxito.

0, si la consulta previa no generó nuevas filas.

`false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Cambia el valor devuelto de un array a un string; elimina el primer parámetro class_name. |

## Ejemplos

Ejemplo de `cubrid_insert_id`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

@cubrid_execute($conn, "DROP TABLE cubrid_test");
cubrid_execute($conn, "CREATE TABLE cubrid_test (d int AUTO_INCREMENT(1, 2), t varchar)");

for ($i = 0; $i < 10; $i++) {
    cubrid_execute($conn, "INSERT INTO cubrid_test(t) VALUES('cubrid_test')");
}

$id = cubrid_insert_id();
var_dump($id);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    string(2) "19"
