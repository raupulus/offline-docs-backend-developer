---
title: mysql_close
description: Cerrar una conexión de MySQL
source_url: https://www.php.net/manual/es/function.mysql-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52050
---

mysql_close

Cerrar una conexión de MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_close
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO: Asignar el valor de
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> null
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> al objeto PDO
>
> </div>

## Descripción

```php
mysql_close([resource $link_identifier]): bool
```php

`mysql_close` cierra la conexión no persistente al servidor de MySQL que está asociada con el identificador de enlace especificado. Si `link_identifier` no se especifica, se usará el último enlace abierto.

Las conexiones y los juegos de resultados abiertos de forma no persistente son automáticamente destruidos cuando un script PHP termina su ejecución. También, el hecho de cerrar una conexión y liberar los resultados siendo opcional, el hecho de hacerlo explícitamente es altamente recomendado. Esto devolverá los recursos inmediatamente a PHP y a MySQL, lo que mejorará las performance. Para más información, refiérase a la [liberación de recursos](#language.types.resource.self-destruct)

## Parámetros

`link_identifier`  
La conexión MySQL. Si el identificador del enlace no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_close`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No se pudo conectar: ' . mysql_error());
}
echo 'Conectado con éxito';
mysql_close($enlace);
?>

   
```php

El ejemplo anterior mostrará:

    Conectado con éxito

## Notas

> [!NOTE]
> `mysql_close` no cerrará los enlaces persistentes creados por `mysql_pconnect`. Para más detalles, véase la página del manual sobre [conexiones persistentes](#features.persistent-connections).

## Véase también

mysql_connect

mysql_free_result
