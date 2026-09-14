---
title: PDO::pgsqlCopyFromArray
description: Alias de Pdo\Pgsql::copyFromArray
source_url: https://www.php.net/manual/es/pdo.pgsqlcopyfromarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo_overloaded/pgsqlCopyFromArray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 858400b07
order: 62610
---

PDO::pgsqlCopyFromArray

Alias de

Pdo\Pgsql::copyFromArray

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public PDO::pgsqlCopyFromArray(string $tableName, array $rows, [string $separator], [string $nullAs], [string $fields]): bool
```php

Este método es un alias de: Pdo\Pgsql::copyFromArray.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El parámetro `rows` ahora también acepta un `Traversable`; anteriormente sólo se aceptaba un `array`. |
