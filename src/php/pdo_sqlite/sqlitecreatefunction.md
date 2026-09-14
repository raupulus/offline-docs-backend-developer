---
title: PDO::sqliteCreateFunction
description: Alias de Pdo\Sqlite::createFunction
source_url: https://www.php.net/manual/es/pdo.sqlitecreatefunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlite/pdo_overloaded/sqliteCreateFunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlite
translation_status: ready
translation_revision: 8d40a1fab
order: 62790
---

PDO::sqliteCreateFunction

Alias de

Pdo\Sqlite::createFunction

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public PDO::sqliteCreateFunction(string $function_name, callable $callback, [int $num_args], [int $flags]): bool
```php

Este método es un alias de: Pdo\Sqlite::createFunction.

## Historial de cambios

| Versión | Descripción                           |
|---------|---------------------------------------|
| 7.1.4   | El argumento `flags` ha sido añadido. |
