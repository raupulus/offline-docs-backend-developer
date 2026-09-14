---
title: SQLite3::escapeString
description: Devuelve una cadena limpiada
source_url: https://www.php.net/manual/es/sqlite3.escapestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/escapestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85710
---

SQLite3::escapeString

Devuelve una cadena limpiada

## Descripción

```php
public static SQLite3::escapeString(string $string): string
```php

Devuelve una cadena que ha sido limpiada para poder ser incluida de forma segura en las consultas SQL.

> [!WARNING]
> Esta función no es capaz de manejar strings binarios (aún)!

Para manejar correctamente los campos BLOB que contienen caracteres NUL, es preferible utilizar la función `SQLite3Stmt::bindParam`.

## Parámetros

`string`  
La cadena a limpiar.

## Valores devueltos

Devuelve una cadena limpiada, que podrá ser utilizada de forma segura en una consulta SQL.

## Notas

> [!WARNING]
> La función `addslashes` no debe *PAS* ser utilizada para proteger la cadena en las consultas SQL; podrían observarse resultados extraños al recuperar los datos.
