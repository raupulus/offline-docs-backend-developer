---
title: Phar::isFileFormat
description: Retorna true si el archivo phar está basado en el formato de archivo
  tar/phar/zip según el argumento
source_url: https://www.php.net/manual/es/phar.isfileformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/isFileFormat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64220
---

Phar::isFileFormat

Retorna

true

si el archivo phar está basado en el formato de archivo tar/phar/zip según el argumento

## Descripción

```php
public Phar::isFileFormat(int $format): bool
```php

## Parámetros

`format`  
Puede ser `Phar::PHAR`, `Phar::TAR` o `Phar::ZIP` para probar el formato de archivo del archivo.

## Valores devueltos

Retorna `true` si el archivo phar utiliza el formato de archivo especificado en el argumento

## Errores/Excepciones

Se lanza una excepción `PharException` si el argumento es un formato de archivo desconocido.

## Véase también

`Phar::convertToExecutable`, `Phar::convertToData`
