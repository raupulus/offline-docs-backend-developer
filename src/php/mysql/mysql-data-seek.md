---
title: mysql_data_seek
description: Mueve el puntero de resultados interno
source_url: https://www.php.net/manual/es/function.mysql-data-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-data-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52080
---

mysql_data_seek

Mueve el puntero de resultados interno

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
> PDO::FETCH_ORI_ABS
>
> </div>

## Descripción

```php
mysql_data_seek(resource $result, int $row_number): bool
```php

`mysql_data_seek` mueve el puntero de filas interno del resultado de MySQL asociado con el identificador de resultado especificado para apuntar al número de fila especificada. La siguiente llamada a una función de obtención de MySQL, tal como `mysql_fetch_assoc`, devolverá esa fila.

`row_number` empieza en 0. `row_number` debería ser un valor en el rango de 0 a `mysql_num_rows` -1. Sin embargo, si el conjunto de resultados esta vacío (`mysql_num_rows` == 0), una búsqueda a 0 fallará con un `E_WARNING` y `mysql_data_seek` devolverá `false`.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`row_number`  
Número de la fila deseada del puntero de resultados nuevo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_data_seek`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
$bd_seleccionada = mysql_select_db('bd_muestra');
if (!$bd_seleccionada) {
    die('La base de datos no pudo seleccionarse: ' . mysql_error());
}
$consulta = 'SELECT apellido, nombre FROM amigos';
$resultado = mysql_query($consulta);
if (!$resultado) {
    die('La consulta falló: ' . mysql_error());
}
/* obtención de filas en orden inverso */
for ($i = mysql_num_rows($resultado) - 1; $i >= 0; $i--) {
    if (!mysql_data_seek($resultado, $i)) {
        echo "No se encuenta la fila $i: " . mysql_error() . "\n";
        continue;
    }

    if (!($fila = mysql_fetch_assoc($resultado))) {
        continue;
    }

    echo $fila['apellido'] . ' ' . $fila['nombre'] . "<br />\n";
}

mysql_free_result($resultado);
?>

   
```php

## Notas

> [!NOTE]
> La función `mysql_data_seek` puede ser usada solamente junto con `mysql_query`, y no con `mysql_unbuffered_query`.

## Véase también

mysql_query

mysql_num_rows

mysql_fetch_row

mysql_fetch_assoc

mysql_fetch_array

mysql_fetch_object
