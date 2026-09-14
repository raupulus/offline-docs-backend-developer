---
title: mysql_db_query
description: Selecciona una base de datos y ejecuta una consulta sobre la misma
source_url: https://www.php.net/manual/es/function.mysql-db-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-db-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52100
---

mysql_db_query

Selecciona una base de datos y ejecuta una consulta sobre la misma

> [!WARNING]
> Esta función estaba obsoleta en PHP 5.3.0, y toda la [extensión original MySQL](#book.mysql) fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_select_db
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> y luego la consulta
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::\_\_construct
>
> </div>

## Descripción

```php
mysql_db_query(string $database, string $query, [resource $link_identifier]): resource
```php

`mysql_db_query` selecciona una base de datos y ejecuta una consulta en ella.

## Parámetros

`database`  
El nombre de la base de datos que va a ser seleccionada.

`query`  
La consulta MySQL.

Los datos dentro de la consulta deben ser [escapados apropiadamente](#function.mysql-real-escape-string).

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve un recurso de resultados de MySQL positivo al resultado de la consulta, o `false` en caso de error. La función también retorna `true`/`false` para las consultas `INSERT`/`UPDATE`/`DELETE` indicando éxito/fallo.

## Ejemplos

Ejemplo alternativo de `mysql_db_query`

```
<?php

if (!$enlace = mysql_connect('anfitrión_mysql', 'usuario_mysql', 'contraseña_mysql')) {
    echo 'No pudo conectarse a mysql';
    exit;
}

if (!mysql_select_db('nombre_bd_mysql', $enlace)) {
    echo 'No pudo seleccionar la base de datos';
    exit;
}

$sql       = 'SELECT foo FROM bar WHERE id = 42';
$resultado = mysql_query($sql, $enlace);

if (!$resultado) {
    echo "Error de BD, no se pudo consultar la base de datos\n";
    echo "Error MySQL: ' . mysql_error();
    exit;
}

while ($fila = mysql_fetch_assoc($resultado)) {
    echo $fila['foo'];
}

mysql_free_result($resultado);

?>

   
```php

## Notas

> [!NOTE]
> Se ha de tener en cuenta que ésta función **NO** vuelve a la base de datos a la que se estaba conectado anteriormente. En otras palabras, no se puede utilizar ésta función para ejecutar *temporalmente* una consulta SQL en otra base de datos; se tendría que hacer el cambio manualmente. Se recomienda encarecidamente usar la sintaxis `basedatos.tabla` en las consultas SQL o `mysql_select_db` en lugar de esta función.

## Véase también

mysql_query

mysql_select_db
