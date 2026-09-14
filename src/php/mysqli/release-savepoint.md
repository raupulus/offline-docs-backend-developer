---
title: mysqli::release_savepoint
description: Elimina el punto de guardado nombrado del conjunto de puntos de guardado
  de la transacción actual
source_url: https://www.php.net/manual/es/mysqli.release-savepoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/release-savepoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 55320
---

mysqli::release_savepoint

mysqli_release_savepoint

Elimina el punto de guardado nombrado del conjunto de puntos de guardado de la transacción actual

## Descripción

Estilo orientado a objetos

```php
public mysqli::release_savepoint(string $name): bool
```php

Estilo procedimental:

```php
mysqli_release_savepoint(mysqli $mysql, string $name): bool
```

Esta función equivale a ejecutar `` $mysqli->query("RELEASE SAVEPOINT `$name`"); ``. Esta función no provocará un commit ni un rollback.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`name`  
El identificador del punto de guardado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`mysqli_savepoint`
