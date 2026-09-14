---
title: La clase Directory
source_url: https://www.php.net/manual/es/class.directory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/directory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_revision: 29f441a4c
order: 11990
---

## Introducción

Las instancias de `Directory` se crean llamando a la función `dir`, no mediante el operador [new](#language.oop5.basic.new).

## Sinopsis de la clase

final

Directory

Propiedades

public

readonly

string

path

public

readonly

resource

handle

Métodos

## Propiedades

`path`  
El directorio que se abrió.

`handle`  
Puede usarse con otras funciones de directorios como `readdir`, `rewinddir` y `closedir`.

## Historial de cambios

| Versión | Descripción                                                  |
|---------|--------------------------------------------------------------|
| 8.5.0   | La clase ahora es final.                                     |
| 8.1.0   | Las propiedades `path` y `handle` ahora son de solo lectura. |
