---
title: PDO::errorCode
description: Devuelve el SQLSTATE asociado con la última operación sobre la base de
  datos
source_url: https://www.php.net/manual/es/pdo.errorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/errorcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 661e6858a
order: 61860
---

PDO::errorCode

Devuelve el SQLSTATE asociado con la última operación sobre la base de datos

## Descripción

```php
public PDO::errorCode(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un SQLSTATE, un identificador alfanumérico de cinco caracteres definido en el estándar ANSI SQL. Brevemente, un SQLSTATE consiste en un valor de clase de dos caracteres seguido por un valor de subclase de tres caracteres. Un valor de clase de 01 indica una alerta y es acompañado por un código de retorno SQL_SUCCESS_WITH_INFO. Los valores de clases distintos a '01', a excepción de la clase 'IM', indican un error. La clase 'IM' es específica para alertas y errores que provienen de la implementación misma de PDO (o quizás ODBC, si se utiliza el driver ODBC). El valor de subclase '000' en cualquier clase, indica que no hay subclase para este SQLSTATE.

PDO::errorCode devuelve únicamente los códigos de error para operaciones ejecutadas directamente sobre el manejador de la base de datos. Si se crea un objeto PDOStatement con la función PDO::prepare o la función PDO::query y se invoca un error sobre el manejador de consulta, PDO::errorCode no devolverá este error. Se debe llamar PDOStatement::errorCode para devolver el código de error para una operación ejecutada sobre un manejador de consulta particular.

Devuelve `null` si ninguna operación ha sido ejecutada sobre la base de datos.

## Ejemplos

Obtención de un código SQLSTATE

```
<?php
/* Provoca un error -- la tabla BONES no existe */
$dbh->exec("INSERT INTO bones(skull) VALUES ('lucy')");

echo "\nPDO::errorCode(): ", $dbh->errorCode();
?>

    
```php

El ejemplo anterior mostrará:

    PDO::errorCode(): 42S02

## Véase también

PDO::errorInfo, PDOStatement::errorCode, PDOStatement::errorInfo
