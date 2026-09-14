---
title: Phar::apiVersion
description: Devuelve la versión de la API
source_url: https://www.php.net/manual/es/phar.apiversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/apiVersion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63900
---

Phar::apiVersion

Devuelve la versión de la API

## Descripción

```php
final public static Phar::apiVersion(): string
```php

Devuelve la versión de la API del formato de archivo phar que será utilizada para la creación de phars. La extensión Phar soporta la lectura de las versiones de API 1.0.0 y superiores. La versión de API 1.1.0 es requerida para los hashes SHA-256 y SHA-512, y la versión de API 1.1.1 es requerida para almacenar directorios vacíos.

## Parámetros

## Valores devueltos

La versión de la API, por ejemplo `"1.0.0"`.

## Ejemplos

Un ejemplo con`Phar::apiVersion`

```
<?php
echo Phar::apiVersion();
?>

    
```php

El ejemplo anterior mostrará:

    1.1.1
