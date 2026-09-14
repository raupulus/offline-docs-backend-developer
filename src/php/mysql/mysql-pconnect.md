---
title: mysql_pconnect
description: Abre una conexión persistente a un servidor MySQL
source_url: https://www.php.net/manual/es/function.mysql-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52400
---

mysql_pconnect

Abre una conexión persistente a un servidor MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_connect
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> con el prefijo de host
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> p:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::\_\_construct
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
> PDO::ATTR_PERSISTENT
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> como una opción de controlador
>
> </div>

## Descripción

```php
mysql_pconnect([string $server], [string $username], [string $password], [int $client_flags]): resource
```php

Establece una conexión persistente a un servidor MySQL.

`mysql_pconnect` se parece mucho a `mysql_connect` con dos grandes diferencias.

En primer lugar, cuando se conecta, la función primero intenta encontrar un enlace (persistente) que ya esté abierto con el mismo anfitrión, nombre de usuario y contraseña. Si se encuentra uno, se devolverá un identificador para él, en lugar de abrir una nueva conexión.

Segundo, la conexión al servidor SQL no será cerrada cuando la ejecución del script finalice. En su lugar, el enlace permanecerá abierto para su uso futuro (`mysql_close` no cerrará los enlaces establecidos mediante `mysql_pconnect`).

Por eso a este tipo de enlace se le llama 'persistente'.

## Parámetros

`server`  
El servidor de MySQL. También puede incluir un número de puerto. P.ej. "nombre_anfitrión:puerto" o una ruta a un socket local, p.ej. ":/ruta/al/socket" para el localhost.

Si la directiva de PHP [ mysql.default_host](#ini.mysql.default-host) no se ha definido (predeterminado), entonces el valor por defecto es 'localhost:3306'

`username`  
El nombre de usuario. El valor por defecto es el nombre del usuario al que pertenece el proceso del servidor.

`password`  
La contraseña. El valor por defecto es una contraseña vacia.

`client_flags`  
El parámetro `client_flags` puede ser una combinación de las siguientes constantes: 128 (habilita el manejo de `LOAD DATA LOCAL`), `MYSQL_CLIENT_SSL`, `MYSQL_CLIENT_COMPRESS`, `MYSQL_CLIENT_IGNORE_SPACE` o `MYSQL_CLIENT_INTERACTIVE`.

## Valores devueltos

Devuelve un identificador de enlace persistente a MySQL en caso de éxito o `false` en caso de error.

## Notas

> [!NOTE]
> Tenga en cuenta que este tipo de enlaces solo funcionan si se está usando una versión de módulo de PHP. Véase la sección [Conexiones persistentes a bases de datos](#features.persistent-connections) para más información.

> [!WARNING]
> El uso de conexiones persistentes puede requerir ajustar un poco las configuraciones de Apache y de MySQL para asegurarse de que no se excede el número de conexiones permitidas por MySQL.

## Véase también

mysql_connect

Conexiones persistentes a bases de datos
