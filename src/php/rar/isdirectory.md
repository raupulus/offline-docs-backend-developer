---
title: RarEntry::isDirectory
description: Comprobar si una entrada representa un directorio
source_url: https://www.php.net/manual/es/rarentry.isdirectory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/isdirectory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68610
---

RarEntry::isDirectory

Comprobar si una entrada representa un directorio

## Descripción

```php
public RarEntry::isDirectory(): bool
```php

Comprueba si una entrada representa un directorio.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la entrada es un directorio y `false` en caso contrario.

## Notas

Esta función sólo está disponible desde la versión 2.0.0, pero también puede comprobarse si una entrada es un directorio mediante la comprobación de los atributos de entrada, así (sólo funciona para los archivos comprimidos en RAR por Windows o Unix):

```
<?php
//...
//Abrir archivo, obtener la entrada y almacenarla en la variable $e...
//...

$isDirectory = (bool) ((($e->getHostOs() == RAR_HOST_WIN32) && ($e->getAttr() & 0x10)) ||
    (($e->getHostOs() == RAR_HOST_UNIX) && (($e->getAttr() & 0xf000) == 0x4000)));
?>

  
```php
