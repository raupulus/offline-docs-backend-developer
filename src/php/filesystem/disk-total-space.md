---
title: disk_total_space
description: Devuelve el tamaño de un directorio o partición
source_url: https://www.php.net/manual/es/function.disk-total-space.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/disk-total-space.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 23360
---

disk_total_space

Devuelve el tamaño de un directorio o partición

## Descripción

```php
disk_total_space(string $directory): float
```php

Lee recursivamente todos los tamaños del directorio `directory` y devuelve la suma en bytes.

## Parámetros

`directory`  
Un directorio del sistema de archivos o la partición de un disco.

## Valores devueltos

Devuelve el tamaño en bytes, en forma de `float` o `false` si ocurre un error.

## Ejemplos

Ejemplo con `disk_total_space`

```
<?php
// $ds contiene el número de bytes del directorio "/"
$ds = disk_total_space("/");

// En Windows:
$ds = disk_total_space("C:");
$ds = disk_total_space("D:");
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

## Véase también

`disk_free_space`
