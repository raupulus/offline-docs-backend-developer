---
title: mysql_db_name
description: Recupera el nombre de la base de datos desde una llamada a mysql_list_dbs
source_url: https://www.php.net/manual/es/function.mysql-db-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-db-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52090
---

mysql_db_name

Recupera el nombre de la base de datos desde una llamada a

mysql_list_dbs

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> Consulta:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> SELECT DATABASE()
>
> </div>

## Descripción

```php
mysql_db_name(resource $result, int $row, [mixed $field]): string
```php

Recupera el nombre de la base de datos de una llamada a `mysql_list_dbs`.

## Parámetros

`result`  
El puntero de resultados desde una llamada a `mysql_list_dbs`.

`row`  
El índice dentro del conjunto de resultados.

`field`  
El nombre del campo.

## Valores devueltos

Devuelve el nombre de la base de datos en caso de éxito, y `false` en caso de error. Si se devuelve `false`, se usa `mysql_error` para determinar la naturaleza del error.

## Ejemplos

Ejemplo de `mysql_db_name`

```
<?php
error_reporting(E_ALL);

$enlace = mysql_connect('anfitrión_bd', 'nombre_usuario', 'contraseña');
$lista_bd = mysql_list_dbs($enlace);

$i = 0;
$cuenta = mysql_num_rows($lista_bd);
while ($i < $cuenta) {
    echo mysql_db_name($lista_bd, $i) . "\n";
    $i++;
}
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_dbname`

## Véase también

mysql_list_dbs

mysql_tablename
