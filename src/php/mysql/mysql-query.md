---
title: mysql_query
description: Enviar una consulta MySQL
source_url: https://www.php.net/manual/es/function.mysql-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52420
---

mysql_query

Enviar una consulta MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_query
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::query
>
> </div>

## Descripción

```php
mysql_query(string $query, [resource $link_identifier]): mixed
```php

`mysql_query` envía una única consulta (no hay soporte para múltiples consultas) a la base de datos actualmente activa en el servidor asociado con el identificador de enlace especificado por `link_identifier`.

## Parámetros

`query`  
Una consulta SQL

El string de la consulta no debería terminar con un punto y coma. Los datos insertados en la consulta deberían estar [correctamente escapados](#function.mysql-real-escape-string).

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Para SELECT, SHOW, DESCRIBE, EXPLAIN y otras sentencias que retornan un conjunto de resultados, `mysql_query` devuelve un `resource` en caso de éxito, o `false` en caso de error.

Para otros tipos de sentencias SQL, tales como INSERT, UPDATE, DELETE, DROP, etc, `mysql_query` devuelve `true` en caso de éxito o `false` en caso de error.

El conjunto de resultados devuelto debería ser pasado a `mysql_fetch_array`, y otras funciones para manejar las tablas del resultado, para acceder a los datos retornados.

Use `mysql_num_rows` para averiguar cuántas filas fueron devueltas por la sentencia SELECT, o `mysql_affected_rows` para averiguar cuántas filas fueron afectadas por las sentencias DELETE, INSERT, REPLACE, o UPDATE.

`mysql_query` también fallará y retornará `false` si el usuario no está autorizado para acceder a la/s tabla/s a la/s que hace referencia la consulta.

## Ejemplos

Consulta inválida

La siguiente consulta no es sintácticamente válida, por lo que `mysql_query` fallará y retornará `false`.

```
<?php
$resultado = mysql_query('SELECT * WHERE 1=1');
if (!$resultado) {
    die('Consulta no válida: ' . mysql_error());
}

?>

   
```php

Consulta válida

La siguiente consulta es válida, por lo que `mysql_query` retornará un `resource`.

```
<?php
// Lo siguiente podría ser proporcionado por un usuario, como por ejemplo
$nombre = 'fred';
$apellido  = 'fox';

// Formular la consulta
// Este es el mejor método para formular una consulta SQL
// Para más ejemplos, consulte mysql_real_escape_string()
$consulta = sprintf("SELECT nombre, apellido, direccion, edad FROM amigos
    WHERE nombre='%s' AND apellido='%s'",
    mysql_real_escape_string($nombre),
    mysql_real_escape_string($apellido));

// Ejecutar la consulta
$resultado = mysql_query($consulta);

// Comprobar el resultado
// Lo siguiente muestra la consulta real enviada a MySQL, y el error ocurrido. Útil para depuración.
if (!$resultado) {
    $mensaje  = 'Consulta no válida: ' . mysql_error() . "\n";
    $mensaje .= 'Consulta completa: ' . $consulta;
    die($mensaje);
}

// Usar el resultado
// Si se intenta imprimir $resultado no será posible acceder a la información del recurso
// Se debe usar una de las funciones de resultados de mysql
// Consulte también mysql_result(), mysql_fetch_array(), mysql_fetch_row(), etc.
while ($fila = mysql_fetch_assoc($resultado)) {
    echo $fila['nombre'];
    echo $fila['apellido'];
    echo $fila['direccion'];
    echo $fila['edad'];
}

// Liberar los recursos asociados con el conjunto de resultados
// Esto se ejecutado automáticamente al finalizar el script.
mysql_free_result($resultado);
?>

   
```php

## Véase también

mysql_connect

mysql_error

mysql_real_escape_string

mysql_result

mysql_fetch_assoc

mysql_unbuffered_query
