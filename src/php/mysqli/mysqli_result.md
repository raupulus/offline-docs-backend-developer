---
title: La clase mysqli_result
source_url: https://www.php.net/manual/es/class.mysqli-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 55690
---

## Introducción

Representa el conjunto de resultados obtenido desde una consulta.

## Sinopsis de la clase

mysqli_result

implements

IteratorAggregate

Propiedades

public

readonly

int

current_field

public

readonly

int

field_count

public

readonly

array

null

lengths

public

readonly

int

string

num_rows

public

int

type

Métodos

## Propiedades

`type`  
Registra si el resultado se almacena en el búfer o no en forma de `int` (`MYSQLI_STORE_RESULT` o `MYSQLI_USE_RESULT`, respectivamente).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La clase `mysqli_result` implementa ahora IteratorAggregate. Anteriormente, solo se implementaba Traversable. |
