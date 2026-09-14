---
title: mysql_get_client_info
description: Obtiene información del cliente MySQL
source_url: https://www.php.net/manual/es/function.mysql-get-client-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-get-client-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52280
---

mysql_get_client_info

Obtiene información del cliente MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_get_client_info
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::getAttribute
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
> attribute
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
> PDO::ATTR_CLIENT_VERSION
>
> </div>

## Descripción

```php
mysql_get_client_info(): string
```php

`mysql_get_client_info` devuelve un string que representa la versión de la biblioteca cliente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La versión del cliente MySQL.

## Ejemplos

Ejemplo de `mysql_get_client_info`

```
<?php
printf("Información del cliente MySQL: %s\n", mysql_get_client_info());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Información del cliente MySQL: 3.23.39

## Véase también

mysql_get_host_info

mysql_get_proto_info

mysql_get_server_info
