---
title: PDOStatement::fetchObject
description: Recupera la siguiente línea y la devuelve como objeto
source_url: https://www.php.net/manual/es/pdostatement.fetchobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/fetchobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 082ddc19f
order: 62130
---

PDOStatement::fetchObject

Recupera la siguiente línea y la devuelve como objeto

## Descripción

```php
public PDOStatement::fetchObject([string $class], [array $constructorArgs]): object
```php

Recupera la siguiente línea y la devuelve como objeto. Esta función es una alternativa a PDOStatement::fetch con `PDO::FETCH_CLASS` o el estilo `PDO::FETCH_OBJ`.

Cuando se recupera un objeto, sus propiedades son asignadas a partir de los valores de columna respectivos, y luego se llama a su constructor.

## Parámetros

`class`  
Nombre de la clase creada.

`constructorArgs`  
Los elementos de este array son pasados al constructor.

## Valores devueltos

Devuelve una instancia de la clase solicitada con propiedades de nombres que corresponden a los nombres de las columnas o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Véase también

PDOStatement::fetch
