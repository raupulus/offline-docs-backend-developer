---
title: mysql_fetch_row
description: Obtiene una fila de resultados como un array numérico
source_url: https://www.php.net/manual/es/function.mysql-fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52200
---

mysql_fetch_row

Obtiene una fila de resultados como un array numérico

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_row
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::fetch
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
> mode
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
> PDO::FETCH_NUM
>
> </div>

## Descripción

```php
mysql_fetch_row(resource $result): array
```php

Devuelve un array numérico que corresponde a la fila recuperada y mueve el puntero de datos interno hacia delante.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

## Valores devueltos

Devuelve un array numérico que corresponde a la fila recuperada, o `false` si no quedan más filas.

`mysql_fetch_row` recupera una fila de datos del resultado asociado al identificador de resultados especificado. La fila es devuelta como un array. Cada columna del resultado es almacenada en un índice del array, empezando desde 0.

## Ejemplos

Recuperar una fila con `mysql_fetch_row`

```
<?php
$resultado = mysql_query("SELECT id, email FROM people WHERE id = '42'");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}
$fila = mysql_fetch_row($resultado);

echo $fila[0]; // 42
echo $fila[1]; // el valor de email
?>

   
```php

## Notas

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Véase también

mysql_fetch_array

mysql_fetch_assoc

mysql_fetch_object

mysql_data_seek

mysql_fetch_lengths

mysql_result
