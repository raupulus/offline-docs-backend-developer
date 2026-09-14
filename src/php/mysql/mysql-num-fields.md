---
title: mysql_num_fields
description: Obtiene el número de campos de un resultado
source_url: https://www.php.net/manual/es/function.mysql-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52380
---

mysql_num_fields

Obtiene el número de campos de un resultado

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_num_fields
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::columnCount
>
> </div>

## Descripción

```php
mysql_num_fields(resource $result): int
```php

Obtiene el número de campos de una consulta.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

## Valores devueltos

Devuelve el número de campos del `resource` de conjunto de resultados en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `mysql_num_fields`

```
<?php
$resultado = mysql_query("SELECT id,email FROM people WHERE id = '42'");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}

/* devuelve 2 ya que id,email === dos campos */
echo mysql_num_fields($resultado);
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_numfields`

## Véase también

mysql_select_db

mysql_query

mysql_fetch_field

mysql_num_rows
