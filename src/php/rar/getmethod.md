---
title: RarEntry::getMethod
description: Obtener método pack de la entrada
source_url: https://www.php.net/manual/es/rarentry.getmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/getmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68550
---

RarEntry::getMethod

Obtener método pack de la entrada

## Descripción

```php
public RarEntry::getMethod(): int
```php

RarEntry::getMethod devuelve el número del método utilizado cuando añadimos archivo actual de entrada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de método o `false` en caso de error.

## Ejemplos

Ejemplo de RarEntry::getMethod

```
<?php

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

echo "Method number: " . $entry->getMethod();

?>

   
```php
