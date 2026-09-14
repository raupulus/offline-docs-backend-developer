---
title: mysqli::autocommit
description: Activa o desactiva el modo auto-commit
source_url: https://www.php.net/manual/es/mysqli.autocommit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/autocommit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 63b99082e
order: 54900
---

mysqli::autocommit

mysqli_autocommit

Activa o desactiva el modo auto-commit

## Descripción

Estilo orientado a objetos

```php
public mysqli::autocommit(bool $enable): bool
```php

Estilo procedimental

```php
mysqli_autocommit(mysqli $mysql, bool $enable): bool
```

Activa o desactiva el modo auto-commit para las consultas en la conexión.

Para verificar el estado del auto-commit, se puede utilizar el comando SQL `SELECT @@autocommit`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`enable`  
Si se debe activar o no el auto-commit.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::autocommit

Estilo orientado a objetos

```php
<?php

/* Solicita a mysqli que lance una excepción si ocurre un error */
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* El motor de tabla soporta transacciones */
$mysqli->query("CREATE TABLE IF NOT EXISTS language (
    Code text NOT NULL,
    Speakers int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;");

/* Desactiva el autocommit */
$mysqli->autocommit(false);

$result = $mysqli->query("SELECT @@autocommit");
$row = $result->fetch_row();
printf("El Autocommit vale %s\n", $row[0]);

try {
    /* Prepara una consulta de inserción */
    $stmt = $mysqli->prepare('INSERT INTO language(Code, Speakers) VALUES (?,?)');
    $stmt->bind_param('ss', $language_code, $native_speakers);

    /* Inserta varios valores */
    $language_code = 'DE';
    $native_speakers = 50_123_456;
    $stmt->execute();
    $language_code = 'FR';
    $native_speakers = 40_546_321;
    $stmt->execute();

    /* Confirma los datos en la base de datos. Esto no activa el autocommit */
    $mysqli->commit();
    print "Confirmación de 2 líneas en la base de datos\n";

    $result = $mysqli->query("SELECT @@autocommit");
    $row = $result->fetch_row();
    printf("El autocommit vale %s\n", $row[0]);

    /* Intenta insertar varios valores */
    $language_code = 'PL';
    $native_speakers = 30_555_444;
    $stmt->execute();
    $language_code = 'DK';
    $native_speakers = 5_222_444;
    $stmt->execute();

    /* Establecer autocommit=true provocará el commit */
    $mysqli->autocommit(true);

    print "Confirmación de 2 líneas en la base de datos\n";
} catch (mysqli_sql_exception $exception) {
    $mysqli->rollback();

    throw $exception;
}

   
```

Estilo procedimental

```php
<?php

/* Solicita a mysqli que lance una excepción si ocurre un error */
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

/* El motor de tabla soporta transacciones */
mysqli_query($mysqli, "CREATE TABLE IF NOT EXISTS language (
    Code text NOT NULL,
    Speakers int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;");

/* Desactiva el autocommit */
mysqli_autocommit($mysqli, false);

$result = mysqli_query($mysqli, "SELECT @@autocommit");
$row = mysqli_fetch_row($result);
printf("El Autocommit vale %s\n", $row[0]);

try {
    /* Prepara una consulta de inserción */
    $stmt = mysqli_prepare($mysqli, 'INSERT INTO language(Code, Speakers) VALUES (?,?)');
    mysqli_stmt_bind_param($stmt, 'ss', $language_code, $native_speakers);

    /* Inserta varios valores */
    $language_code = 'DE';
    $native_speakers = 50_123_456;
    mysqli_stmt_execute($stmt);
    $language_code = 'FR';
    $native_speakers = 40_546_321;
    mysqli_stmt_execute($stmt);

    /* Confirma los datos en la base de datos. Esto no activa el autocommit */
    mysqli_commit($mysqli);
    print "Confirmación de 2 líneas en la base de datos\n";

    $result = mysqli_query($mysqli, "SELECT @@autocommit");
    $row = mysqli_fetch_row($result);
    printf("El autocommit vale %s\n", $row[0]);

    /* Intenta insertar varios valores */
    $language_code = 'PL';
    $native_speakers = 30_555_444;
    mysqli_stmt_execute($stmt);
    $language_code = 'DK';
    $native_speakers = 5_222_444;
    mysqli_stmt_execute($stmt);

    /* Establecer autocommit=true provocará el commit */
    mysqli_autocommit($mysqli, true);

    print "Confirmación de 2 líneas en la base de datos\n";
} catch (mysqli_sql_exception $exception) {
    mysqli_rollback($mysqli);

    throw $exception;
}

   
```

Los ejemplos anteriores mostrarán:

    El autocommit vale 0
    Confirmación de 2 líneas en la base de datos
    El autocommit vale 0
    Confirmación de 2 líneas en la base de datos
    El autocommit vale 0
    Confirmación de 2 líneas en la base de datos
    El autocommit vale 0
    Confirmación de 2 líneas en la base de datos

## Notas

> [!NOTE]
> Esta función no funciona con los tipos de tablas no transaccionales, como MyISAM o ISAM.

## Véase también

`mysqli_begin_transaction`, `mysqli_commit`, `mysqli_rollback`
