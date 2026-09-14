---
title: mysqli::begin_transaction
description: Inicia una transacción
source_url: https://www.php.net/manual/es/mysqli.begin-transaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/begin-transaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 54910
---

mysqli::begin_transaction

mysqli_begin_transaction

Inicia una transacción

## Descripción

Estilo orientado a objetos

```php
public mysqli::begin_transaction([int $flags], [string $name]): bool
```php

Estilo procedimental:

```php
mysqli_begin_transaction(mysqli $mysql, [int $flags], [string $name]): bool
```

Inicia una transacción. Requiere el motor InnoDB (está activo por omisión). Para más detalles sobre el funcionamiento de las transacciones MySQL, ver <http://dev.mysql.com/doc/mysql/en/commit.html>.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`flags`  
Los flag válidos son:

- `MYSQLI_TRANS_START_READ_ONLY`: Inicia la transacción como "START TRANSACTION READ ONLY". Requiere MySQL 5.6 o superior.

- `MYSQLI_TRANS_START_READ_WRITE`: Inicia la transacción como "START TRANSACTION READ WRITE". Requiere MySQL 5.6 o superior.

- `MYSQLI_TRANS_START_WITH_CONSISTENT_SNAPSHOT`: Inicia la transacción como "START TRANSACTION WITH CONSISTENT SNAPSHOT".

`name`  
Nombre del punto de guardado para la transacción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `name` ahora es nullable. |

## Ejemplos

Ejemplo con mysqli::begin_transaction

Estilo orientado a objetos

```php
<?php

/* Indica a mysqli que lance una excepción si ocurre un error */
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* El motor de tabla soporta transacciones */
$mysqli->query("CREATE TABLE IF NOT EXISTS language (
    Code text NOT NULL,
    Speakers int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;");

/* Inicia la transacción */
$mysqli->begin_transaction();

try {
    /* Inserta varios valores */
    $mysqli->query("INSERT INTO language(Code, Speakers) VALUES ('DE', 42000123)");

    /* Intenta insertar valores incorrectos */
    $language_code = 'FR';
    $native_speakers = 'Unknown';
    $stmt = $mysqli->prepare('INSERT INTO language(Code, Speakers) VALUES (?,?)');
    $stmt->bind_param('ss', $language_code, $native_speakers);
    $stmt->execute();

    /* Si el código llega a este punto sin errores, entonces se confirman los datos en
       la base de datos */
    $mysqli->commit();
} catch (mysqli_sql_exception $exception) {
    $mysqli->rollback();

    throw $exception;
}

   
```

Estilo procedimental

```php
<?php

/* Indica a mysqli que lance una excepción si ocurre un error */
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

/* El motor de tabla soporta transacciones */
mysqli_query($mysqli, "CREATE TABLE IF NOT EXISTS language (
    Code text NOT NULL,
    Speakers int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;");

/* Inicia la transacción */
mysqli_begin_transaction($mysqli);

try {
    /* Inserta varios valores */
    mysqli_query($mysqli, "INSERT INTO language(Code, Speakers) VALUES ('DE', 42000123)");

    /* Intenta insertar valores incorrectos */
    $language_code = 'FR';
    $native_speakers = 'Unknown';
    $stmt = mysqli_prepare($mysqli, 'INSERT INTO language(Code, Speakers) VALUES (?,?)');
    mysqli_stmt_bind_param($stmt, 'ss', $language_code, $native_speakers);
    mysqli_stmt_execute($stmt);

    /* Si el código llega a este punto sin errores, entonces se confirman los datos en
       la base de datos */
    mysqli_commit($mysqli);
} catch (mysqli_sql_exception $exception) {
    mysqli_rollback($mysqli);

    throw $exception;
}

   
```

## Notas

> [!NOTE]
> Esta función no funciona con tipos de tabla no transaccionales (como MyISAM o ISAM).

## Véase también

`mysqli_autocommit`, `mysqli_commit`, `mysqli_rollback`
