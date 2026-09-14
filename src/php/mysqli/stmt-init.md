---
title: mysqli::stmt_init
description: Inicializa una sentencia MySQL
source_url: https://www.php.net/manual/es/mysqli.stmt-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/stmt-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55400
---

mysqli::stmt_init

mysqli_stmt_init

Inicializa una sentencia MySQL

## Descripción

Estilo orientado a objetos

```php
public mysqli::stmt_init(): mysqli_stmt
```php

Estilo procedimental

```php
mysqli_stmt_init(mysqli $mysql): mysqli_stmt
```

Asigna e inicializa un objeto de sentencia, para ser utilizado con `mysqli_stmt_prepare`.

> [!NOTE]
> Todas las llamadas posteriores a las funciones mysqli_stmt\_\* fallarán, si `mysqli_stmt_prepare` es llamada.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve un objeto.

## Véase también

`mysqli_stmt_prepare`
