---
title: Pdo\Pgsql::copyFromFile
description: Copia datos de un fichero a una tabla
source_url: https://www.php.net/manual/es/pdo-pgsql.copyfromfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/copyfromfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62500
---

Pdo\Pgsql::copyFromFile

Copia datos de un fichero a una tabla

## Descripción

```php
public Pdo\Pgsql::copyFromFile(string $tableName, string $filename, [string $separator], [string $nullAs], [string $fields]): bool
```php

Copia datos de un fichero especificado por `filename` a la tabla `tableName` utilizando `separator` como delimitador de campos y la lista `fields`

## Parámetros

`filename`  
El nombre del fichero desde el cual importar los datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si `filename` no puede abrirse para lectura, el fallo se notifica a través del manejo de errores de la conexión (véase `PDO::ATTR_ERRMODE`); con `PDO::ERRMODE_EXCEPTION` se lanza una PDOException.

## Ejemplos

Ejemplo de Pdo\Pgsql::copyFromFile

El fichero contiene un registro por línea, con los campos unidos por `separator` (un tabulador por defecto).

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');

file_put_contents('/tmp/fruits.tsv', "1\tapple\t10\n2\tbanana\t20\n");
$db->copyFromFile('fruits', '/tmp/fruits.tsv');

echo $db->query('SELECT count(*) FROM fruits')->fetchColumn(), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2

## Véase también

Pdo\Pgsql::copyToFile

Pdo\Pgsql::copyFromArray

Pdo\Pgsql::copyToArray
