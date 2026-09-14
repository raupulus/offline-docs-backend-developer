---
title: Pdo\Pgsql::lobCreate
description: Crear un nuevo objeto grande
source_url: https://www.php.net/manual/es/pdo-pgsql.lobcreate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/lobcreate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 02b075821
order: 62560
---

Pdo\Pgsql::lobCreate

Crear un nuevo objeto grande

## Descripción

```php
public Pdo\Pgsql::lobCreate(): string
```php

Pdo\Pgsql::lobCreate crea un objeto grande y devuelve el OID que lo referencia. Puede abrirse para leer o escribir datos con Pdo\Pgsql::lobOpen.

El OID puede almacenarse en columnas de tipo OID y utilizarse para referenciar el objeto grande, sin que la fila crezca de manera arbitraria. El objeto grande continuará existiendo en la base de datos hasta que sea eliminado mediante la llamada a Pdo\Pgsql::lobUnlink.

Los objetos grandes son objetos voluminosos para utilizar. De hecho, es necesario llamar a Pdo\Pgsql::lobUnlink antes de eliminar la última fila que referencia el OID en toda la base de datos; de lo contrario, los objetos grandes no referenciados permanecerán en el servidor indefinidamente. Además, los objetos grandes no tienen controles de acceso. Una alternativa es el tipo de columna bytea, que puede ser de hasta 1 GB de tamaño, y este tipo de columna gestiona de manera transparente el almacenamiento para un tamaño de fila óptimo.

> [!NOTE]
> Esta función, y todas las manipulaciones del objeto grande, deben ser llamadas y realizadas dentro de una transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el OID del nuevo objeto grande creado en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de Pdo\Pgsql::lobCreate

Este ejemplo crea un nuevo objeto grande y copia el contenido de un fichero dentro. El OID es almacenado posteriormente en una tabla.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->beginTransaction();
$oid = $db->lobCreate();
$stream = $db->lobOpen($oid, 'w');
$local = fopen($filename, 'rb');
stream_copy_to_stream($local, $stream);
$local = null;
$stream = null;
$stmt = $db->prepare("INSERT INTO BLOBS (ident, oid) VALUES (?, ?)");
$stmt->execute([$some_id, $oid]);
$db->commit();
?>

   
```php

## Véase también

Pdo\Pgsql::lobOpen

Pdo\Pgsql::lobUnlink

pg_lo_create

pg_lo_open
