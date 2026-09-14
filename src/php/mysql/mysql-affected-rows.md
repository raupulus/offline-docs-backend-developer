---
title: mysql_affected_rows
description: Obtiene el número de filas afectadas en la anterior operación de MySQL
source_url: https://www.php.net/manual/es/function.mysql-affected-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-affected-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52030
---

mysql_affected_rows

Obtiene el número de filas afectadas en la anterior operación de MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_affected_rows
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::rowCount
>
> </div>

## Descripción

```php
mysql_affected_rows([resource $link_identifier]): int
```php

Obtiene el número de filas afectadas por la última consulta INSERT, UPDATE, REPLACE o DELETE asociada con `link_identifier`.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve el número de filas afectadas en caso de éxito, y -1 si la última consulta falló.

Si la consulta anterior fue DELETE con ninguna cláusula WHERE, todos los registros habrán sido borrados de la tabla, aunque ésta función devolverá cero con una versión anterior a MySQL 4.1.2.

Al utilizar UPDATE, MySQL no actualiza las columnas donde el nuevo valor es el mismo que el anterior. Esto crea la posibilidad de que `mysql_affected_rows` no pueda equivaler en realidad al número de filas encontradas, solamente el número de filas que estuvieron literalmente afectadas por la consulta.

La sentencia REPLACE primero borra el registro con la misma clave primaria y luego inserta el nuevo registro. Esta función devuelve el número de registros borrados más el número de registros insertados.

En el caso de consultas "INSERT ... ON DUPLICATE KEY UPDATE", el valor devuelto será `1` si se realizó una inserción, o `2` para una actualización de una fila existente.

## Ejemplos

Ejemplo de `mysql_affected_rows`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No se pudo conectar: ' . mysql_error());
}
mysql_select_db('mibd');

/* Esto debería devolver el número correcto de registros borrados */
mysql_query('DELETE FROM mitabla WHERE id < 10');
printf("Registros borrados: %d\n", mysql_affected_rows());

/* con una clausula WHERE que nunca es verdad, debería devolver 0 */
mysql_query('DELETE FROM mitabla WHERE 0');
printf("Registros borrados: %d\n", mysql_affected_rows());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Registros borrados: 10
    Registros borrados: 0

Ejemplo de `mysql_affected_rows` al utilizar transacciones

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No se pudo conectar: ' . mysql_error());
}
mysql_select_db('mibd');

/* Actualizar registros */
mysql_query("UPDATE mitabla SET usado=1 WHERE id < 10");
printf ("Registros actualizados: %d\n", mysql_affected_rows());
mysql_query("COMMIT");
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Registros actualizados: 10

## Notas

> [!NOTE]
> Si se usan transacciones, es necesario llamar a `mysql_affected_rows` después de una consulta INSERT, UPDATE, o DELETE, no después del COMMIT.

> [!NOTE]
> Para conocer el número de filas devueltas por un SELECT, es posible usar `mysql_num_rows`.

> [!NOTE]
> `mysql_affected_rows` no cuenta la filas afectadas implícitamente a través del uso de ON DELETE CASCADE y/o ON UPDATE CASCADE en las restricciones de las claves foráneas.

## Véase también

mysql_num_rows

mysql_info
