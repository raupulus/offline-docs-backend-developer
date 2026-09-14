---
title: mysql_thread_id
description: Devuelve el ID del hilo actual
source_url: https://www.php.net/manual/es/function.mysql-thread-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-thread-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52490
---

mysql_thread_id

Devuelve el ID del hilo actual

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
mysql_thread_id([resource $link_identifier]): int
```php

Recupera el ID del hilo actual. Si la conexión se ha perdido, y se ejecuta una reconexión con `mysql_ping`, el ID del hilo cambiará. Esto quiere decir que sólo se ha de recuperar el ID del hilo cuando sea necesario.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

El ID del hilo en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_thread_id`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
$id_hilo = mysql_thread_id($enlace);
if ($id_hilo){
    printf("El ID del hilo actual es %d\n", $id_hilo);
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    El ID del hilo actual es 73

## Véase también

mysql_ping

mysql_list_processes
