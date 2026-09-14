---
title: cubrid_query
description: Enviar una consulta CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8810
---

cubrid_query

Enviar una consulta CUBRID

## Descripción

```php
cubrid_query(string $query, [resource $conn_identifier]): resource
```php

`cubrid_query` envía una consulta única (no están soportadas consultas múltiples) a la base de datos activa actual en el servidor que está asociado con el `conn_identifier` especificado.

## Parámetros

`query`  
Una consulta SQL

La información dentro de la consulta debería estar [adecuadamente escapada](#function.cubrid-real-escape-string).

`conn_identifier`  
La conexión CUBRID. Si el identificador de conexión no se especifica, se asume la última conexión abierta por `cubrid_connect`.

## Valores devueltos

Para SELECT, SHOW, DESCRIBE, EXPLAIN y otras sentencias que devuelven conjuntos de resultadosa, `cubrid_query` devuelve un `resource` en caso de éxito, o `false` en caso de error.

Para otros tipos de sentencias SQL, INSERT, UPDATE, DELETE, DROP, etc, `cubrid_query` devuelve `true` en caso de éxito o `false` en caso de error.

El recurso resultado devuelto debería ser pasado a `cubrid_fetch_array`, y a otras funciones para tratar con las tablas de resultados, para acceder a la información devuelta.

Use `cubrid_num_rows` para averiguar cuántas filas fueron devueltas por una sentencia SELECT o `cubrid_affected_rows` para averiguar cuántas filas fueron afectadas por una sentencia DELETE, INSERT, REPLACE, o UPDATE.

`cubrid_query` también podrá fallar y devolver `false` si el usuario no tiene permiso para acceder a la/s tabla/s referenciada/s por la consulta.

## Ejemplos

Consulta No Válida

La siguiente consulta no es válida sintácticamente, por lo que `cubrid_query` fallará y devolverá `false`.

```
<?php
$conn = cubrid_connect('localhost', 33000, 'demodb');

$result = cubrid_query('SELECT * WHERE 1=1');
if (!$result) {
    die('Consulta inválida: ' . cubrid_error());
}

?>

   
```php

Consulta Válida

La siguiente consulta es válida, por lo que `cubrid_query` devolverá un `resource`.

```
<?php
// Esto podría ser proporcionado por el usuario, por ejemplo
$nombre = 'fred';
$apellido  = 'fox';

cubrid_execute($conn,"DROP TABLE if exists friends");
cubrid_execute($conn,"create table friends(firstname varchar,lastname varchar,address char(24),age int)");
cubrid_execute($conn,"insert into friends values('fred','fox','home-1','20')");
cubrid_execute($conn,"insert into friends values('blue','cat','home-2','21')");
// Formular la Consulta
// Esta es la mejor manera de realizar una consulta SQL
// Para más ejemplos, véase cubrid_real_escape_string()
$consulta = sprintf("SELECT firstname, lastname, address, age FROM friends WHERE firstname='%s' AND lastname='%s'",
cubrid_real_escape_string($nombre),
cubrid_real_escape_string($apellido));

// Realizar la Constulta
$result = cubrid_query($consulta);

// Verificar el resultado
// Esto muestra la consulta real enviada a CUBRID, y el error. Útil para depuración.
if (!$result) {
    $mensaje  = 'Consulta no válida: ' . cubrid_error() . "\n";
    $mensaje .= 'Consulta completa: ' . $consulta;
    die($mensaje);
}

// Usar el resultado
// Intentar imprimir $result no permitirá el acceso a la información en el recurso
// Se debe usar una de las funciones de resultados de cubrid
// Véase también cubrid_result(), cubrid_fetch_array(), cubrid_fetch_row(), etc.
while ($fila = cubrid_fetch_assoc($result)) {
    echo $fila['firstname'];
    echo $fila['lastname'];
    echo $fila['address'];
    echo $fila['age'];
}

// Liberar los recursos asociados con el conjunto de resultados
// Esto se hace automáticamente al final del script
cubrid_free_result($result);
?>

   
```php

## Véase también

cubrid_connect

cubrid_error

cubrid_real_escape_string

cubrid_result

cubrid_fetch_assoc

cubrid_unbuffered_query
