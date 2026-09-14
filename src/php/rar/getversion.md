---
title: RarEntry::getVersion
description: Obtener la versión mínima del programa RAR requerida para desempaquetar
  la entrada
source_url: https://www.php.net/manual/es/rarentry.getversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/getversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68600
---

RarEntry::getVersion

Obtener la versión mínima del programa RAR requerida para desempaquetar la entrada

## Descripción

```php
public RarEntry::getVersion(): int
```php

Devuelve la versión mínima del programa RAR (por ejemplo WinRAR) requerida para desempaquetar la entrada. Esta es codificada como 10 \* version mayor + versión menor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la versión o `false` en caso de error.

## Ejemplos

Ejemplo de RarEntry::getVersion

```
<?php

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

echo "Rar version required for unpacking: " . $entry->getVersion();

?>

   
```php
