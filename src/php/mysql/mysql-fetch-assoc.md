---
title: mysql_fetch_assoc
description: Recupera una fila de resultados como un array asociativo
source_url: https://www.php.net/manual/es/function.mysql-fetch-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-fetch-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52160
---

mysql_fetch_assoc

Recupera una fila de resultados como un array asociativo

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_assoc
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::fetch
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> con
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> mode
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> como
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::FETCH_ASSOC
>
> </div>

## Descripción

```php
mysql_fetch_assoc(resource $result): array
```php

Devuelve un array asociativo que corresponde a la fila recuperada y mueve el puntero de datos interno hacia adelante. `mysql_fetch_assoc` es equivalente a llamar a `mysql_fetch_array` con MYSQL_ASSOC como segundo parámetro opcional. Únicamente devuelve un array asociativo.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

## Valores devueltos

Devuelve un array asociativo de strings que corresponde a la fila recuperada, o `false` si no hay más filas disponibles.

Si dos o más columnas del resultado tienen los mismos nombres de campo, la última columna tomará precedencia. Para acceder a la/s otra/s columna/s con el mismo nombre, se tendrá que acceder al resultado con índices numéricos mediante el uso de `mysql_fetch_row` o agregando sobrenombres. Véase el ejemplo en la descripción de `mysql_fetch_array` respecto a los sobrenombres.

## Ejemplos

Un ejemplo desarrolado de `mysql_fetch_assoc`

```
<?php

$conexión = mysql_connect("localhost", "usuario_mysql", "contraseña_mysql");

if (!$conexión) {
    echo "No pudo conectarse a la BD: " . mysql_error();
    exit;
}

if (!mysql_select_db("nombre_de_la_bd")) {
    echo "No ha sido posible seleccionar la BD: " . mysql_error();
    exit;
}

$sql = "SELECT id as id_usuario, nombre_completo, estatus_usuario
        FROM   alguna_tabla
        WHERE  estatus_usuario = 1";

$resultado = mysql_query($sql);

if (!$resultado) {
    echo "No se pudo ejecutar con exito la consulta ($sql) en la BD: " . mysql_error();
    exit;
}

if (mysql_num_rows($resultado) == 0) {
    echo "No se han encontrado filas, nada a imprimir, asi que voy a detenerme.";
    exit;
}

// Mientras exista una fila de datos, colocar esa fila en $fila como un array asociativo
// Nota: Si solo espera una fila, no hay necesidad de usar un bucle
// Nota: Si coloca extract($fila); dentro del siguiente bucle,
//       estará creando $id_usuario, $nombre_completo, y $estatus_usuario
while ($fila = mysql_fetch_assoc($resultado)) {
    echo $fila["id_usuario"];
    echo $fila["nombre_completo"];
    echo $fila["estatus_usuario"];
}

mysql_free_result($resultado);

?>

   
```php

## Notas

> [!NOTE]
> Algo importante a observar es que el uso de `mysql_fetch_assoc` *no es significativamente* más lento que el uso de `mysql_fetch_row`, aunque provee un valor añadido considerable.

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Véase también

mysql_fetch_row

mysql_fetch_array

mysql_data_seek

mysql_query

mysql_error
