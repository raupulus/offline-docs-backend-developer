---
title: SQLite3Result::finalize
description: Cierra un conjunto de resultados
source_url: https://www.php.net/manual/es/sqlite3result.finalize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3result/finalize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 2ab6e3ff1
order: 85900
---

SQLite3Result::finalize

Cierra un conjunto de resultados

## Descripción

```php
public SQLite3Result::finalize(): true
```php

Cierra un conjunto de resultados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se produce una excepción Error si el método se invoca sobre un objeto no inicializado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Este método genera ahora una excepción Error si el objeto no está correctamente inicializado. Anteriormente, devolvía `false`. |
