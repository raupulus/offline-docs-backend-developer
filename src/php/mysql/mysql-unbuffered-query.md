---
title: mysql_unbuffered_query
description: Envía una consulta SQL a MySQL, sin recuperar ni almacenar en búfer las
  filas de resultados
source_url: https://www.php.net/manual/es/function.mysql-unbuffered-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-unbuffered-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52500
---

mysql_unbuffered_query

Envía una consulta SQL a MySQL, sin recuperar ni almacenar en búfer las filas de resultados

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> Véase:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> Consultas almacenadas y no almacenadas en buffer
>
> </div>

## Descripción

```php
mysql_unbuffered_query(string $query, [resource $link_identifier]): resource
```php

`mysql_unbuffered_query` envía la consulta SQL `query` a MySQL, sin recuperar ni almacenar automáticamente en búfer las filas de resultados, como `mysql_query` lo hace. Esto ahorra una considerable cantidad de memoria con las consultas SQL que producen conjuntos de resultados grandes, y se puede empezar a trabajar con el conjunto de resultados inmediatamente después de que la primera fila haya sido recuperada, ya que no es necesario esperar hasta que la consulta SQL completa haya sido ejecutada. Para usar `mysql_unbuffered_query` mientras están abiertas múltiples conexiones a la base de datos, se debe especificar el parámetro opcional `link_identifier` para identificar qué conexión se desea utilizar.

## Parámetros

`query`  
La consulta SQL a ejecutar.

Los datos dentro de la consulta deben estar [propiamente escapados](#function.mysql-real-escape-string).

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Para sentencias SELECT, SHOW, DESCRIBE o EXPLAIN, `mysql_unbuffered_query` devuelve un `resource` en caso de éxito, o `false` en caso de error.

Para otro tipo de sentencias SQL, UPDATE, DELETE, DROP, etc, `mysql_unbuffered_query` devuelve `true` en caso de éxito o `false` en caso de error.

## Notas

> [!NOTE]
> Los beneficios de `mysql_unbuffered_query` tienen un precio: no se puede usar `mysql_num_rows` ni `mysql_data_seek` en un conjunto de resultados devuelto por `mysql_unbuffered_query`, hasta que todas las filas sean recuperadas. También se tendrán que recuperar todas las filas de resultados de una consulta SQL no almacenada en búfer antes de poder enviar una nueva consulta SQL a MySQL, usando el mismo `link_identifier`.

## Véase también

mysql_query
