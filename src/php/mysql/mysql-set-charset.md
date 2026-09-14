---
title: mysql_set_charset
description: Establece el conjunto de caracteres del cliente
source_url: https://www.php.net/manual/es/function.mysql-set-charset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-set-charset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52460
---

mysql_set_charset

Establece el conjunto de caracteres del cliente

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_set_charset
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO: Añadir
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> charset
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> al string de conexión, tal como
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> charset=utf8
>
> </div>

## Descripción

```php
mysql_set_charset(string $charset, [resource $link_identifier]): bool
```php

Establece el conjunto de caracteres predeterminado para la conexión actual.

## Parámetros

`charset`  
Un nombre válido de un conjunto de caracteres.

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> Esta función requiere MySQL 5.0.7 o posterior.

> [!NOTE]
> Esta es la mejor forma de cambiar el conjunto de caracteres. El uso de `mysql_query` para establecerlo (como `SET NAMES utf8`) no es recomendable. Véase la sección [conceptos de conjuntos de caracteres de MySQL](#mysqlinfo.concepts.charset) para más información.

## Véase también

Establecer conjuntos de caracteres en MySQL

Listado de los conjuntos de caracteres admitidos por MySQL

mysql_client_encoding
