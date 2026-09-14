---
title: mysql_list_dbs
description: Lista las bases de datos disponibles en un servidor MySQL
source_url: https://www.php.net/manual/es/function.mysql-list-dbs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-list-dbs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52340
---

mysql_list_dbs

Lista las bases de datos disponibles en un servidor MySQL

> [!WARNING]
> Esta función estaba obsoleta en PHP 5.4.0, y toda la [extensión original MySQL](#book.mysql) fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> Consulta SQL:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> SHOW DATABASES
>
> </div>

## Descripción

```php
mysql_list_dbs([resource $link_identifier]): resource
```php

Devuelve un puntero de resultados que contiene las bases de datos disponibles en el demonio de mysql actual.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve un `resource` de puntero de resultados en caso de éxito, o `false` en caso de error. Use la función `mysql_tablename` para atravesar este puntero de resultado, o cualquier función para obtener tablas, tal como `mysql_fetch_array`.

## Ejemplos

Ejemplo de `mysql_list_dbs`

```
<?php
// Uso sin mysql_list_dbs()
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
$resultado = mysql_query("SHOW DATABASES");

while ($fila = mysql_fetch_assoc($res)) {
    echo $fila['Database'] . "\n";
}

// Obsoleto a partir de PHP 5.4.0
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
$lista_bd = mysql_list_dbs($enlace);

while ($fila = mysql_fetch_object($lista_bd)) {
     echo $fila->Database . "\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    basedatos1
    basedatos2
    basedatos3

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_listdbs`

## Véase también

mysql_db_name

mysql_select_db
