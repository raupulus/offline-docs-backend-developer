---
title: mysqli::$info
description: Devuelve información acerca de la última consulta ejecutada
source_url: https://www.php.net/manual/es/mysqli.info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 015aa90a1
order: 55150
---

mysqli::\$info

mysqli_info

Devuelve información acerca de la última consulta ejecutada

## Descripción

Estilo orientado a objetos

string

null

mysqli-\>info

Estilo procedimental

```php
mysqli_info(mysqli $mysql): string
```php

La función `mysqli_info` devuelve un string que proporciona información acerca de la última consulta ejecutada. La naturaleza de este string se detalla a continuación:

| Tipo de consulta | Ejemplo de retorno |
|----|----|
| INSERT INTO...SELECT... | Records: 100 Duplicates: 0 Warnings: 0 |
| INSERT INTO...VALUES (...),(...),(...) | Records: 3 Duplicates: 0 Warnings: 0 |
| LOAD DATA INFILE ... | Records: 1 Deleted: 0 Skipped: 0 Warnings: 0 |
| ALTER TABLE ... | Records: 3 Duplicates: 0 Warnings: 0 |
| UPDATE ... | Rows matched: 40 Changed: 40 Warnings: 0 |

Valores de retorno posibles para `mysqli_info` {#mysqli.info.description}

> [!NOTE]
> Las consultas que no forman parte de la lista anterior no están soportadas. En esta situación, `mysqli_info` devolverá un string vacío.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un string que proporciona información adicional acerca de la última consulta ejecutada.

## Ejemplos

Ejemplo con `$mysqli->info`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$mysqli->query("CREATE TEMPORARY TABLE t1 LIKE City");

/* INSERT INTO ... SELECT */
$mysqli->query("INSERT INTO t1 SELECT * FROM City ORDER BY ID LIMIT 150");
printf("%s\n", $mysqli->info);

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

mysqli_query($link, "CREATE TEMPORARY TABLE t1 LIKE City");

/* INSERT INTO ... SELECT */
mysqli_query($link, "INSERT INTO t1 SELECT * FROM City ORDER BY ID LIMIT 150");
printf("%s\n", mysqli_info($link));

   
```php

Los ejemplos anteriores mostrarán:

    Records: 150  Duplicates: 0  Warnings: 0

## Véase también

`mysqli_affected_rows`, `mysqli_warning_count`, `mysqli_num_rows`
