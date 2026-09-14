---
title: Throwable
source_url: https://www.php.net/manual/es/class.throwable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/throwable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 4040
---

## Introducción

`Throwable` es la interfaz base para cualquier objeto que pueda ser lanzado mediante una sentencia [`throw`](#language.exceptions), incluyendo `Error` y `Exception`.

> [!NOTE]
> Las clases de PHP no pueden implementar la interfaz `Throwable` directamente, por lo que deben extender en su lugar `Exception`.

## Sinopsis de la interfaz

Throwable

extends

Stringable

Métodos

Métodos heredados

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 8.0.0   | `Throwable` implementa Stringable ahora. |
