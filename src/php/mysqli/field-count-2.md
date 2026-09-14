---
title: mysqli_result::$field_count
description: Obtiene el número de campos en el conjunto de resultados
source_url: https://www.php.net/manual/es/mysqli-result.field-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/field-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: a3051835f
order: 55630
---

mysqli_result::\$field_count

mysqli_num_fields

Obtiene el número de campos en el conjunto de resultados

## Descripción

Estilo orientado a objetos

int

mysqli_result-\>field_count

Estilo procedimental

```php
mysqli_num_fields(mysqli_result $result): int
```php

Devuelve el número de campos en el conjunto de resultados.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Un `int` que representa el número de campos.

## Ejemplos

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$result = $mysqli->query("SELECT Name, CountryCode, District, Population FROM City ORDER BY ID LIMIT 1");

/* Determina el número de campos en el conjunto de resultados */
$field_cnt = $result->field_count;

printf("El resultado tiene %d campos.\n", $field_cnt);
?>

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$result = mysqli_query($link, "SELECT Name, CountryCode, District, Population FROM City ORDER BY ID LIMIT 1");

/* Determina el número de campos en el conjunto de resultados */
$field_cnt = mysqli_num_fields($result);

printf("El resultado tiene %d campos.\n", $field_cnt);
?>

   
```php

Los ejemplos anteriores mostrarán:

    El resultado tiene 4 campos.

## Véase también

`mysqli_fetch_field`
