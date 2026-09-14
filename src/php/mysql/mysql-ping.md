---
title: mysql_ping
description: Efectuar un chequeo de respuesta (ping) sobre una conexión al servidor
  o reconectarse si no hay conexión
source_url: https://www.php.net/manual/es/function.mysql-ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52410
---

mysql_ping

Efectuar un chequeo de respuesta (ping) sobre una conexión al servidor o reconectarse si no hay conexión

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_ping
>
> </div>

## Descripción

```php
mysql_ping([resource $link_identifier]): bool
```php

Chequea si está activa o no la conexión con el servidor. Si ésta se ha caído, se intenta una reconexión automática. Esta función puede ser usada por scripts que permanecen pasivos durante largos espacios de tiempo, para chequear si el servidor ha cerrado la conexión y reconectarse de ser necesario.

> [!NOTE]
> La reconexión automática está deshabilitada de forma predeterminada en versiones de MySQL \>= 5.0.3.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve `true` si la conexión con el servidor MySQL está funcionando, o `false` si no.

## Ejemplos

Un ejemplo de `mysql_ping`

```
<?php
set_time_limit(0);

$conexión = mysql_connect('localhost', 'usuario_mysql', 'contraseña');
$bd  = mysql_select_db('mi_bd');

/* Se asume que esta consulta toma mucho tiempo */
$resultado = mysql_query($sql);
if (!$resultado) {
    echo 'La consulta #1 falló; Saliendo.';
    exit;
}

/* Asegurarse de que la conexión sigue viva, si no, intentar una reconexión */
if (!mysql_ping($conexión)) {
    echo 'Se ha perdido la conexión, saliendo después de la consulta #1';
    exit;
}
mysql_free_result($resultado);

/* Ya que la conexión sigue viva, ejecutemos otra consulta */
$resultado2 = mysql_query($sql2);
?>

   
```php

## Véase también

mysql_thread_id

mysql_list_processes
