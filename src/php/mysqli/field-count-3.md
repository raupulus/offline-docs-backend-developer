---
title: mysqli_stmt::$field_count
description: Devuelve el número de columnas en la consulta dada
source_url: https://www.php.net/manual/es/mysqli-stmt.field-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/field-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 7e5d0d1bb
order: 55850
---

mysqli_stmt::\$field_count

mysqli_stmt_field_count

Devuelve el número de columnas en la consulta dada

## Descripción

Estilo orientado a objetos

int

mysqli_stmt-\>field_count

Estilo procedimental

```php
mysqli_stmt_field_count(mysqli_stmt $statement): int
```php

Devuelve el número de columnas en la declaración preparada.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Devuelve un integer que representa el número de columnas.

## Ejemplos

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$code = 'FR';

$stmt = $mysqli->prepare("SELECT Name FROM Country WHERE Code=?");
$stmt->bind_param('s', $code);
$stmt->execute();
$row = $stmt->get_result()->fetch_row();
for ($i = 0; $i < $stmt->field_count; $i++) {
    printf("Value of column number %d is %s", $i, $row[$i]);
}

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$code = 'FR';

$stmt = mysqli_prepare($mysqli, "SELECT Name FROM Country WHERE Code=?");
mysqli_stmt_bind_param($stmt, 's', $code);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);
$row = mysqli_fetch_row($result);
for ($i = 0; $i < mysqli_stmt_field_count($stmt); $i++) {
    printf("Value of column number %d is %s", $i, $row[$i]);
}

   
```php

Los ejemplos anteriores mostrarán algo similar a:

    Value of column number 0 is France

## Véase también

`mysqli_stmt_num_rows`
