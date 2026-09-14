---
title: Phar::isValidPharFilename
description: Determina si el nombre de fichero especificado es un nombre de fichero
  válido para un archivo phar
source_url: https://www.php.net/manual/es/phar.isvalidpharfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/isValidPharFilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64230
---

Phar::isValidPharFilename

Determina si el nombre de fichero especificado es un nombre de fichero válido para un archivo phar

## Descripción

```php
final public static Phar::isValidPharFilename(string $filename, [bool $executable]): bool
```php

Determina si el nombre de fichero especificado es un nombre de fichero válido para un archivo phar, que será reconocido como tal por la extensión phar. Esto puede ser utilizado para probar un nombre sin tener que instanciar un archivo phar y atrapar la inevitable Exception que será lanzada si se especifica un nombre de fichero no válido.

## Parámetros

`filename`  
El nombre o la ruta completa hacia un archivo phar no creado aún

`executable`  
Este argumento determina si el nombre de fichero debe ser tratado como el de un archivo phar ejecutable o como un archivo de datos no ejecutable.

## Valores devueltos

Devuelve `true` si el nombre de fichero es válido, `false` en caso contrario.
