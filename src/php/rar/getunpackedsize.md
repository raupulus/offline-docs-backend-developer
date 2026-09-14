---
title: RarEntry::getUnpackedSize
description: Obtener el tamaño descomprimido de la entrada
source_url: https://www.php.net/manual/es/rarentry.getunpackedsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/getunpackedsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 68590
---

RarEntry::getUnpackedSize

Obtener el tamaño descomprimido de la entrada

## Descripción

```php
public RarEntry::getUnpackedSize(): int
```php

Obtiene el tamaño descomprimido del archivo entrada.

> [!NOTE]
> Tenga en cuenta que en las plataformas de 32 bits de longitud (que incluye Windows x64), el tamaño máximo devueltos está limitado a 2 GB. Compruebe la constante `PHP_INT_MAX`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tamaño descomprimido, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 2.0.0 | Este método devuelve ahora valores correctos de tamaño descomprimido superiores a 2 GB en plataformas con 64-bit `int`s y nunca devuelve valores negativos en otras plataformas. |

## Valores devueltos

Ejemplo de RarEntry::getUnpackedSize

```
<?php

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

echo "Unpacked size of " . $entry->getName() . " = " . $entry->getUnpackedSize() . " bytes";

?>

   
```php
