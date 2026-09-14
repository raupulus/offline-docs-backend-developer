---
title: Pdo\Pgsql::copyToFile
description: Copia datos de una tabla a un fichero
source_url: https://www.php.net/manual/es/pdo-pgsql.copytofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/copytofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62520
---

Pdo\Pgsql::copyToFile

Copia datos de una tabla a un fichero

## Descripción

```php
public Pdo\Pgsql::copyToFile(string $tableName, string $filename, [string $separator], [string $nullAs], [string $fields]): bool
```php

Copia datos de la tabla al fichero especificado por `filename` utilizando `separator` como delimitador de campos y la lista `fields`.

## Parámetros

`filename`  
El nombre del fichero donde exportar los datos.

`fields`  
La lista de campos a exportar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si `filename` no puede abrirse para escritura, o no puede escribirse en él, el fallo se notifica a través del manejo de errores de la conexión (ver `PDO::ATTR_ERRMODE`); con `PDO::ERRMODE_EXCEPTION` se lanza una PDOException.

## Ejemplos

Ejemplo de Pdo\Pgsql::copyToFile

La tabla se escribe en `filename`, un registro por línea, con los campos unidos por `separator`.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');
$db->exec("INSERT INTO fruits VALUES (1, 'apple', 10), (2, 'banana', 20)");

$db->copyToFile('fruits', '/tmp/fruits.tsv');
echo file_get_contents('/tmp/fruits.tsv');
?>

   
```php

El ejemplo anterior mostrará:

    1   apple   10
    2   banana  20

## Véase también

Pdo\Pgsql::copyFromFile

Pdo\Pgsql::copyFromArray

Pdo\Pgsql::copyToArray
