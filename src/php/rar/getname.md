---
title: RarEntry::getName
description: Obtener el nombre de la entrada
source_url: https://www.php.net/manual/es/rarentry.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68560
---

RarEntry::getName

Obtener el nombre de la entrada

## Descripción

```php
public RarEntry::getName(): string
```php

Devuelve el nombre (con la ruta) de el archivo entrada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de la entrada como una cadena, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 2.0.0 | Desde la versión 2.0.0, la cadena devuelta está codificada en Unicode/UTF-8. |

## Ejemplos

Ejemplo de RarEntry::getName

```
<?php

//este ejemplo, es seguro, incluso en páginas no codificados en UTF-8
//para esa codificación en UTF-8, la llamada a mb_convert_encoding es innecesaria.

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

echo "Entry name: " . mb_convert_encoding(
    htmlentities(
        $entry->getName(),
        ENT_COMPAT,
        "UTF-8"
    ),
    "HTML-ENTITIES",
    "UTF-8"
);

?>

   
```php
