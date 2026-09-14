---
title: mysqli_stmt::result_metadata
description: Devuelve las metadatos de preparación de consulta MySQL
source_url: https://www.php.net/manual/es/mysqli-stmt.result-metadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/result-metadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_revision: 8abf6408d
order: 55960
---

mysqli_stmt::result_metadata

mysqli_stmt_result_metadata

Devuelve las metadatos de preparación de consulta MySQL

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::result_metadata(): mysqli_result
```php

Estilo procedimental

```php
mysqli_stmt_result_metadata(mysqli_stmt $statement): mysqli_result
```

Si una orden ha sido preparada por `mysqli_prepare`, y producirá un resultado, `mysqli_stmt_result_metadata` devuelve el objeto de resultado que será utilizado para leer las metadatos, como el número de campos y las informaciones de columnas.

Esta función devuelve un objeto `mysqli_result` vacío que permite acceder a la información de metadatos de la sentencia preparada sin necesidad de recuperar las filas de datos. No es necesario usar esta función si se utiliza `mysqli_stmt_get_result` para recuperar el conjunto de resultados completo de una sentencia preparada como un objeto de resultado.

> [!NOTE]
> Este conjunto de resultados solo se puede pasar como argumento a las funciones basadas en campos para procesar metadatos del conjunto de resultados, tales como:
>
> - `mysqli_num_fields`
>
> - `mysqli_fetch_field`
>
> - `mysqli_fetch_field_direct`
>
> - `mysqli_fetch_fields`
>
> - `mysqli_field_count`
>
> - `mysqli_field_seek`
>
> - `mysqli_field_tell`
>
> - `mysqli_free_result`

> [!NOTE]
> El conjunto de resultados devuelto por `mysqli_stmt_result_metadata` contiene únicamente metadatos. No contiene ninguna fila de resultado. Las filas se obtienen llamando a `mysqli_stmt_get_result` en el manejador de la sentencia o con `mysqli_stmt_fetch`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Devuelve un objeto de resultados, o `false` si ocurre un error. Si la sentencia no produce un conjunto de resultados, también se devuelve `false`.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "test");

$mysqli->query("DROP TABLE IF EXISTS friends");
$mysqli->query("CREATE TABLE friends (id int, name varchar(20))");

$mysqli->query("INSERT INTO friends VALUES (1,'Hartmut'), (2, 'Ulf')");

$stmt = $mysqli->prepare("SELECT id, name FROM friends");
$stmt->execute();

/* Lee las metadatos de resultado */
$result = $stmt->result_metadata();

/* Lee las informaciones de un campo, desde las metadatos */
$field = $result->fetch_field();

printf("Nombre del campo : %s\n", $field->name);
?>

   
```

Estilo procedimental

```php
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "test");

mysqli_query($link, "DROP TABLE IF EXISTS friends");
mysqli_query($link, "CREATE TABLE friends (id int, name varchar(20))");

mysqli_query($link, "INSERT INTO friends VALUES (1,'Hartmut'), (2, 'Ulf')");

$stmt = mysqli_prepare($link, "SELECT id, name FROM friends");
mysqli_stmt_execute($stmt);

/* Lee las metadatos de resultado */
$result = mysqli_stmt_result_metadata($stmt);

/* Lee las informaciones de un campo, desde las metadatos */
$field = mysqli_fetch_field($result);

printf("Nombre del campo : %s\n", $field->name);
?>

   
```

## Véase también

`mysqli_prepare`, `mysqli_free_result`, `mysqli_stmt_get_result`
