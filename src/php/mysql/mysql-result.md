---
title: mysql_result
description: Obtener datos de resultado
source_url: https://www.php.net/manual/es/function.mysql-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52440
---

mysql_result

Obtener datos de resultado

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_data_seek
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> junto con
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_field_seek
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> y
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_field
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::fetchColumn
>
> </div>

## Descripción

```php
mysql_result(resource $result, int $row, [mixed $field]): string
```php

Recupera el contenido de una celda de un conjunto de resultados de MySQL.

Cuando se esté trabajando con conjuntos de resultados grandes, se debería considerar usar una de las funciones que obtienen una fila completa (especificadas más abajo). Debido a que estas funciones retornan el contenido de múltiples celdas en una única llamada a función, son MUCHO MÁS rápidas que `mysql_result`. Además, se ha de tener en cuenta que la especificación de un índice numérico para el campo pasado como argumento es mucho más rápido que especificar un nombre de campo o el argumento nombre_tabla.nombre_campo.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`row`  
El número de fila del conjunto de resultados que está siendo recuperado. El número de filas empieza a partir de `0`.

`field`  
El nombre o el índice del campo que está siendo recuperado.

Puede ser el índice del campo, el nombre del campo, o el nombre de la tabla punto nombre del campo (nombre_tabla.nombre_campo). Si se ha utilizado un alias para el nombre de la columna ('select foo as bar from...'), utilice el alias en lugar del nombre del campo. Si no está definido, se recuperará el primer campo.

## Valores devueltos

El contenido de una celda de un conjunto de resultados de MySQL en caso de éxito, o `false` en caso de fallo.

## Ejemplos

Ejemplo de `mysql_result`

```
<?php
$enlace = mysql_connect('anfitrión_mysql', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No se pudo conectar: ' . mysql_error());
}
if (!mysql_select_db('nombre_base_datos')) {
    die('No se pudo seleccionar la base de datos: ' . mysql_error());
}
$resultado = mysql_query('SELECT name FROM work.employee');
if (!$resultado) {
    die('No se pudo consultar:' . mysql_error());
}
echo mysql_result($resultado, 2); // imprime el nombre del tercer empleado

mysql_close($enlace);
?>

   
```php

## Notas

> [!NOTE]
> Las llamadas a `mysql_result` no deberían ser mezcladas con llamadas a otras funciones que manejen conjuntos de resultados.

## Véase también

mysql_fetch_row

mysql_fetch_array

mysql_fetch_assoc

mysql_fetch_object
