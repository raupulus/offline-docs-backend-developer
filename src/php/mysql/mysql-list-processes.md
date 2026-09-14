---
title: mysql_list_processes
description: Lista los procesos de MySQL
source_url: https://www.php.net/manual/es/function.mysql-list-processes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-list-processes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52360
---

mysql_list_processes

Lista los procesos de MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_thread_id
>
> </div>

## Descripción

```php
mysql_list_processes([resource $link_identifier]): resource
```php

Recupera los hilos del servidor MySQL actuales.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Un puntero de resultados de tipo `resource` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_list_processes`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');

$resultado = mysql_list_processes($enlace);

while ($fila = mysql_fetch_assoc($resultado)){
    printf("%s %s %s %s %s\n", $fila["Id"], $fila["Host"], $fila["db"],
        $fila["Command"], $fila["Time"]);
}
mysql_free_result($resultado);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    1 localhost test Processlist 0
    4 localhost mysql sleep 5

## Véase también

mysql_thread_id

mysql_stat
