---
title: disk_free_space
description: Devuelve el espacio en disco disponible en el sistema de archivos o partición
source_url: https://www.php.net/manual/es/function.disk-free-space.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/disk-free-space.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 23350
---

disk_free_space

Devuelve el espacio en disco disponible en el sistema de archivos o partición

## Descripción

```php
disk_free_space(string $directory): float
```php

Devuelve el espacio en disco disponible en el directorio o partición.

## Parámetros

`directory`  
Un directorio del sistema de archivos o una partición de disco.

> [!NOTE]
> Si se proporciona un fichero en lugar de un directorio, el comportamiento de esta función puede ser aleatorio, dependiendo del sistema operativo y las versiones de PHP.

## Valores devueltos

Devuelve el número de bytes disponibles, en forma de `float` o `false` si ocurre un error.

## Ejemplos

Ejemplo con `disk_free_space`

```
<?php
// $df contiene el número de bytes libres en "/"
$df = disk_free_space("/");

// En Windows:
$df_c = disk_free_space("C:");
$df_d = disk_free_space("D:");
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

## Véase también

`disk_total_space`
