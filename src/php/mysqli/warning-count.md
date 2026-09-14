---
title: mysqli::$warning_count
description: Devuelve el número de advertencias generadas por la última consulta ejecutada
source_url: https://www.php.net/manual/es/mysqli.warning-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/warning-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_revision: de5eb4b43
order: 55450
---

mysqli::\$warning_count

mysqli_warning_count

Devuelve el número de advertencias generadas por la última consulta ejecutada

## Descripción

Estilo orientado a objetos

int

mysqli-\>warning_count

Estilo procedimental

```php
mysqli_warning_count(mysqli $mysql): int
```php

Devuelve el número de advertencias generadas por la última consulta ejecutada.

> [!NOTE]
> Para recuperar los mensajes de advertencia, se puede utilizar el siguiente comando SQL: `SHOW WARNINGS [LIMIT row_count]`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

El número de advertencias o `0` si no hay ninguna.

## Ejemplos

Ejemplo con `$mysqli->warning_count`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$mysqli->query("SELECT 42/0");

if ($mysqli->warning_count > 0) {
    $result = $mysqli->query("SHOW WARNINGS");
    $row = $result->fetch_row();
    printf("%s (%d): %s\n", $row[0], $row[1], $row[2]);
}

?>

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

mysqli_query($link, "SELECT 42/0");

if (mysqli_warning_count($link) > 0) {
    $result = mysqli_query($link, "SHOW WARNINGS");
    $row = mysqli_fetch_row($result);
    printf("%s (%d): %s\n", $row[0], $row[1], $row[2]);
}
?>

   
```php

Los ejemplos anteriores mostrarán:

    Warning (1365): Division by 0

## Véase también

`mysqli_errno`, `mysqli_error`, `mysqli_sqlstate`
