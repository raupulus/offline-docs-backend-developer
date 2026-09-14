---
title: Pdo\Pgsql::lobOpen
description: Abre un flujo sobre un objeto grande existente
source_url: https://www.php.net/manual/es/pdo-pgsql.lobopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/lobopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62570
---

Pdo\Pgsql::lobOpen

Abre un flujo sobre un objeto grande existente

## Descripción

```php
public Pdo\Pgsql::lobOpen(string $oid, [string $mode]): resource
```php

Pdo\Pgsql::lobOpen abre un flujo para acceder a los datos referenciados por `oid`. Todas las funciones habituales del sistema de ficheros, tales como `fread`, `fwrite` o `fgets` pueden ser utilizadas para manipular el contenido del flujo.

## Parámetros

`oid`  
Un identificador de objeto grande.

`mode`  
El modo de acceso. Si `mode` contiene `w` o `+`, el flujo se abre para lectura y escritura; en caso contrario, se abre solo para lectura. Un indicador `b` (binario) no tiene efecto. El valor predeterminado `"rb"` abre el flujo para lectura.

## Valores devueltos

Devuelve un recurso de flujo en caso de éxito, o `false` si ocurre un error

## Ejemplos

Ejemplo de Pdo\Pgsql::lobOpen

Según el ejemplo de Pdo\Pgsql::lobCreate, este código extrae el objeto grande de la base de datos y lo devuelve al navegador.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->beginTransaction();
$stmt = $db->prepare("SELECT oid FROM BLOBS WHERE ident = ?");
$stmt->execute([$some_id]);
$stmt->bindColumn('oid', $oid, PDO::PARAM_STR);
$stmt->fetch(PDO::FETCH_BOUND);
$stream = $db->lobOpen($oid, 'r');
header("Content-type: application/octet-stream");
fpassthru($stream);
?>

   
```php

## Véase también

Pdo\Pgsql::lobCreate

Pdo\Pgsql::lobUnlink

pg_lo_create

pg_lo_open
