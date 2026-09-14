---
title: mysqli::savepoint
description: Establece un punto de guardado nombrado de la transacción
source_url: https://www.php.net/manual/es/mysqli.savepoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/savepoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 55340
---

mysqli::savepoint

mysqli_savepoint

Establece un punto de guardado nombrado de la transacción

## Descripción

Estilo orientado a objetos

```php
public mysqli::savepoint(string $name): bool
```php

Estilo procedimental:

```php
mysqli_savepoint(mysqli $mysql, string $name): bool
```

Esta función equivale a ejecutar `` $mysqli->query("SAVEPOINT `$name`"); ``

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`name`  
El identificador del punto de guardado

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`mysqli_release_savepoint`
