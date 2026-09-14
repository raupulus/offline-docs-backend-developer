---
title: PDOStatement::closeCursor
description: Cierra el cursor, permitiendo que la consulta pueda ser ejecutada de
  nuevo
source_url: https://www.php.net/manual/es/pdostatement.closecursor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/closecursor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 082ddc19f
order: 62040
---

PDOStatement::closeCursor

Cierra el cursor, permitiendo que la consulta pueda ser ejecutada de nuevo

## Descripción

```php
public PDOStatement::closeCursor(): bool
```php

PDOStatement::closeCursor libera la conexión al servidor, permitiendo así que otras consultas SQL puedan ser ejecutadas, pero deja la consulta en un estado que permite su ejecución posterior.

Este método es útil para los drivers de bases de datos que no soportan la ejecución de objetos PDOStatement cuando un objeto PDOStatement ejecutado previamente aún tiene filas no recuperadas. Si su driver de base de datos sufre de esta limitación, el problema se manifestará por sí mismo en un error fuera de secuencia.

PDOStatement::closeCursor se implementa bien como un método específico del driver con máxima eficiencia, o como una solución genérica si no se ha instalado ninguna función específica del driver. Semánticamente, la función genérica PDO equivale a escribir el siguiente código en su script PHP:

```
<?php
do {
    while ($stmt->fetch())
        ;
    if (!$stmt->nextRowset())
        break;
} while (true);
?>

   
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Ejemplo con PDOStatement::closeCursor

En el siguiente ejemplo, el objeto PDOStatement `$stmt` devuelve múltiples filas, pero la aplicación recupera únicamente la primera fila, dejando el objeto PDOStatement en un estado donde aún quedan filas no recuperadas. Para asegurar que la aplicación funcione con todos los drivers de bases de datos, el autor inserta una llamada a la función PDOStatement::closeCursor en `$stmt` antes de la ejecución del objeto PDOStatement `$otherStmt`.

```
<?php
/* Creación de un objeto PDOStatement */
$stmt = $dbh->prepare('SELECT foo FROM bar');

/* Creación de un segundo objeto PDOStatement */
$otherStmt = $dbh->prepare('SELECT foobaz FROM foobar');

/* Ejecución de la primera consulta */
$stmt->execute();

/* Recuperación de la primera fila únicamente desde el resultado */
$stmt->fetch();

/* La siguiente llamada a closeCursor() puede ser requerida por algunos drivers */
$stmt->closeCursor();

/* Ahora, podemos ejecutar la segunda consulta */
$otherStmt->execute();
?>

    
```php

## Véase también

PDOStatement::execute
