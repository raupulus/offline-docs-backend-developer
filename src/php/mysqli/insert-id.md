---
title: mysqli::$insert_id
description: Devuelve el valor generado para una columna AUTO_INCREMENT por la última
  consulta
source_url: https://www.php.net/manual/es/mysqli.insert-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/insert-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: c85c9d1d4
order: 55170
---

mysqli::\$insert_id

mysqli_insert_id

Devuelve el valor generado para una columna AUTO_INCREMENT por la última consulta

## Descripción

Estilo orientado a objetos

int

string

mysqli-\>insert_id

Estilo procedimental

```php
mysqli_insert_id(mysqli $mysql): int
```php

Devuelve el ID generado por una consulta `INSERT` o `UPDATE` en una tabla con una columna que tiene el atributo `AUTO_INCREMENT`. En el caso de consultas multilínea `INSERT`, esto devuelve el primer valor generado automáticamente que fue insertado con éxito.

Ejecutar una consulta `INSERT` o `UPDATE` utilizando la función MySQL `LAST_INSERT_ID()` modificará también el valor devuelto por `mysqli_insert_id`. Si `LAST_INSERT_ID(expr)` se ha utilizado para generar el valor de `AUTO_INCREMENT`, esto devuelve el valor de la última `expr` en lugar del valor generado de `AUTO_INCREMENT`.

Devuelve `0` si la consulta anterior no ha cambiado el valor de `AUTO_INCREMENT`. `mysqli_insert_id` debe ser llamado inmediatamente después de que la consulta haya generado el valor.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

El valor del campo `AUTO_INCREMENT` modificado por la última consulta. Devuelve cero si no ha habido consulta en la conexión o si la última consulta no ha modificado el valor del `AUTO_INCREMENT`.

Solo las consultas emitidas por la conexión actual afectan el valor de retorno. El valor no se ve afectado por las consultas que utilizan otras conexiones o clientes.

> [!NOTE]
> Si el número es mayor que el valor máximo de un integer, será devuelto como un `string`

## Ejemplos

Ejemplo con `$mysqli->insert_id`

Estilo orientado a objetos

```
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$mysqli->query("CREATE TABLE myCity LIKE City");

$query = "INSERT INTO myCity VALUES (NULL, 'Stuttgart', 'DEU', 'Stuttgart', 617000)";
$mysqli->query($query);

printf("El nuevo registro tiene ID %d.\n", $mysqli->insert_id);

/* eliminar tabla */
$mysqli->query("DROP TABLE myCity");
?>

   
```php

Estilo procedimental

```
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

mysqli_query($link, "CREATE TABLE myCity LIKE City");

$query = "INSERT INTO myCity VALUES (NULL, 'Stuttgart', 'DEU', 'Stuttgart', 617000)";
mysqli_query($link, $query);

printf("El nuevo registro tiene ID %d.\n", mysqli_insert_id($link));

/* eliminar tabla */
mysqli_query($link, "DROP TABLE myCity");
?>

   
```php

Los ejemplos anteriores mostrarán:

    El nuevo registro tiene ID 1.
