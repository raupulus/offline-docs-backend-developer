---
title: PDO::connect
description: Conecta a una base de datos y devuelve una subclase PDO para los controladores
  que lo soportan
source_url: https://www.php.net/manual/es/pdo.connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 61840
---

PDO::connect

Conecta a una base de datos y devuelve una subclase PDO para los controladores que lo soportan

## Descripción

```php
public static #[\SensitiveParameter] PDO::connect(string $dsn, [string $username], [string $password], [array $options]): static
```php

Crea una instancia de una subclase de `PDO` para la base de datos a la que se conecta, si existe, de lo contrario devuelve una instancia genérica de `PDO`.

## Valores devueltos

Devuelve una instancia de una subclase de `PDO` para el controlador PDO correspondiente si existe, o una instancia genérica de `PDO`.

## Véase también

Pdo\Dblib

Pdo\Firebird

Pdo\Mysql

Pdo\Odbc

Pdo\Pgsql

Pdo\Sqlite

PDO::\_\_construct
