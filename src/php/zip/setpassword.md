---
title: ZipArchive::setPassword
description: Establece la contraseña para el archivo activo
source_url: https://www.php.net/manual/es/ziparchive.setpassword.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setpassword.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108590
---

ZipArchive::setPassword

Establece la contraseña para el archivo activo

## Descripción

```php
public #[\SensitiveParameter] ZipArchive::setPassword(string $password): bool
```php

Establece la contraseña para el archivo activo.

## Parámetros

`password`  
La contraseña a emplear para el archivo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> A partir de PHP 7.2.0 y libzip 1.2.0 la contraseña se utiliza para descomprimir el archivo, y también es la contraseña por omisión para ZipArchive::setEncryptionName y ZipArchive::setEncryptionIndex. Anteriormente, esta función sólo establecía la contraseña que se usaría para descomprimir el archivo; No se convirtió en un no protegido con contraseña `ZipArchive` en un protegido con contraseña `ZipArchive`.

## Véase también

ZipArchive::setEncryptionIndex, ZipArchive::setEncryptionName
