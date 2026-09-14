---
title: mysql_client_encoding
description: Devuelve el nombre del conjunto de caracteres
source_url: https://www.php.net/manual/es/function.mysql-client-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-client-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52040
---

mysql_client_encoding

Devuelve el nombre del conjunto de caracteres

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_character_set_name
>
> </div>

## Descripción

```php
mysql_client_encoding([resource $link_identifier]): string
```php

Recupera la variable `character_set` de MySQL.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve el nombre del conjunto de caracteres predeterminado de la conexión actual.

## Ejemplos

Ejemplo de `mysql_client_encoding`

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
$conjunto_caracteres = mysql_client_encoding($enlace);

echo "El conjunto de caracteres actual es: $conjunto_caracteres\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    El conjunto de caracteres actual es: latin1

## Véase también

mysql_set_charset

mysql_real_escape_string
