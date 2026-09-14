---
title: Pdo\Pgsql::lobUnlink
description: Elimina un objeto grande
source_url: https://www.php.net/manual/es/pdo-pgsql.lobunlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/lobunlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62580
---

Pdo\Pgsql::lobUnlink

Elimina un objeto grande

## Descripción

```php
public Pdo\Pgsql::lobUnlink(string $oid): bool
```php

Elimina un objeto grande de la base de datos identificado por OID.

## Parámetros

`oid`  
Un identificador de objeto grande.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de Pdo\Pgsql::lobUnlink

Este ejemplo desvincula un objeto grande de la base de datos antes de eliminar la fila que lo referencia. Utiliza la tabla blobs de los ejemplos de Pdo\Pgsql::lobCreate y Pdo\Pgsql::lobOpen.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->beginTransaction();
$db->lobUnlink($oid);
$stmt = $db->prepare("DELETE FROM BLOBS where ident = ?");
$stmt->execute([$some_id]);
$db->commit();
?>

   
```php

## Véase también

Pdo\Pgsql::lobCreate

Pdo\Pgsql::lobOpen

pg_lo_create

pg_lo_open
