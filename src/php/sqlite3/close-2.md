---
title: SQLite3Stmt::close
description: Cierra una consulta preparada
source_url: https://www.php.net/manual/es/sqlite3stmt.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 2ab6e3ff1
order: 85970
---

SQLite3Stmt::close

Cierra una consulta preparada

## Descripción

```php
public SQLite3Stmt::close(): true
```php

Cierra una consulta preparada.

> [!NOTE]
> Tenga en cuenta que todos los `SQLite3Result` que han sido recuperados al ejecutar esta instrucción serán invalidados cuando la instrucción sea cerrada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se levanta una Error si el método es llamado sobre un objeto no inicializado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Este método levanta ahora una excepción Error si el objeto no está correctamente inicializado. Anteriormente, retornaba `false`. |
