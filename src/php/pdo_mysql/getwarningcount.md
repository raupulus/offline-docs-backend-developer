---
title: Pdo\Mysql::getWarningCount
description: Devuelve el número de advertencias de la última consulta ejecutada
source_url: https://www.php.net/manual/es/pdo-mysql.getwarningcount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_mysql/pdo/mysql/getwarningcount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_mysql
translation_status: ready
translation_reviewed: true
translation_revision: 99abc1432
order: 62390
---

Pdo\Mysql::getWarningCount

Devuelve el número de advertencias de la última consulta ejecutada

## Descripción

```php
public Pdo\Mysql::getWarningCount(): int
```php

Devuelve el número de advertencias de la última consulta ejecutada.

> [!NOTE]
> Para recuperar los mensajes de advertencia, puede utilizarse el siguiente comando SQL: `SHOW WARNINGS [limit row_count]`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `int` que representa el número de advertencias generadas por la última consulta.

## Ejemplos

Ejemplo de Pdo\Mysql::getWarningCount

```
<?php

$conn = PDO::connect("mysql:host=localhost;dbname=test;charset=utf8mb4", 'user', 'password');

$conn->query('SELECT 42/0');
if ($conn->getWarningCount() > 0) {
    $result = $conn->query("SHOW WARNINGS");
    $row = $result->fetch();
    printf("%s (%d): %s\n", $row[0], $row[1], $row[2]);
}

?>

   
```php

El ejemplo anterior mostrará:

    Warning (1365): Division by 0
