---
title: mysql_fetch_object
description: Recupera una fila de resultados como un objeto
source_url: https://www.php.net/manual/es/function.mysql-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52190
---

mysql_fetch_object

Recupera una fila de resultados como un objeto

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_object
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
> PDO::FETCH_OBJ
>
> </div>

## Descripción

```php
mysql_fetch_object(resource $result, [string $class_name], [array $params]): object
```php

Devuelve un objeto con propiedades que corresponden a la fila recuperada y mueve el puntero interno hacia delante.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`class_name`  
El nombre de la clase donde instanciar, configurar las propiedades y devolver. Si no se especifica, se devuelve un objeto `stdClass`.

`params`  
Un `array` opcional de parámetros para pasar al constructor de los objetos `class_name`.

## Valores devueltos

Devuelve un `object` con propiedades de tipo string que se corresponden con la fila recuperada, o `false` si no quedan más filas.

## Ejemplos

Ejemplo de `mysql_fetch_object`

```
<?php
mysql_connect("nombre_anfitrión", "usuario", "contraseña");
mysql_select_db("mibd");
$resultado = mysql_query("select * from mitabla");
while ($fila = mysql_fetch_object($resultado)) {
    echo $fila->id_usuario;
    echo $fila->nombre_completo;
}
mysql_free_result($resultado);
?>

   
```php

Ejemplo de `mysql_fetch_object`

```
<?php
class foo {
    public $nombre;
}

mysql_connect("nombre_anfitrión", "usuario", "contraseña");
mysql_select_db("mibd");

$resultado = mysql_query("select nombre from mitabla limit 1");
$objeto = mysql_fetch_object($resultado, 'foo');
var_dump($objeto);
?>

   
```php

## Notas

> [!NOTE]
> En cuestión de velocidad, la función es idéntica a `mysql_fetch_array`, y casi tan rápida como `mysql_fetch_row` (la diferencia es insignificante).

> [!NOTE]
> `mysql_fetch_object` es similar a `mysql_fetch_array`, con una diferencia: se devuelve un objeto, en lugar de un array. Indirectamente, esto significa que se puede acceder a los datos únicamente mediante los nombres de los campos, y no mediante sus índices (los números son ilegales como nombres de propiedades).

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Véase también

mysql_fetch_array

mysql_fetch_assoc

mysql_fetch_row

mysql_data_seek

mysql_query
