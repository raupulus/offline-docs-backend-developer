---
title: mysql_free_result
description: Libera la memoria del resultado
source_url: https://www.php.net/manual/es/function.mysql-free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52270
---

mysql_free_result

Libera la memoria del resultado

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_free_result
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> Asignar el valor de
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
> al objeto PDO, o
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::closeCursor
>
> </div>

## Descripción

```php
mysql_free_result(resource $result): bool
```php

`mysql_free_result` liberará toda la memoria asociada con el identificador del resultado `result`.

`mysql_free_result` solo necesita ser llamado si se está preocupado por la cantidad de memoria que está siendo usada por las consultas que devuelven conjuntos de resultados grandes. Toda la memoria de resultados asociada se liberará automaticamente al finalizar la ejecución del script.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Si se utiliza un recurso no válido para `result`, se emitirá un error de nivel E_WARNING. Vale la pena señalar que `mysql_query` solo devuelve un `recurso` para las consultas SELECT, SHOW, EXPLAIN, y DESCRIBE.

## Ejemplos

Un ejemplo de `mysql_free_result`

```
<?php
$resultado = mysql_query("SELECT id, email FROM people WHERE id = '42'");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}
/* Usamos el resultado, asumiendo que, acto seguido, hemos terminado con él */
$fila = mysql_fetch_assoc($resultado);

/* Ahora liberamos el resultado y continuamos con nuestro script */
mysql_free_result($resultado);

echo $fila['id'];
echo $fila['email'];
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_freeresult`

## Véase también

mysql_query

is_resource
