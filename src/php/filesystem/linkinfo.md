---
title: linkinfo
description: Devuelve la información de un enlace
source_url: https://www.php.net/manual/es/function.linkinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/linkinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 23850
---

linkinfo

Devuelve la información de un enlace

## Descripción

```php
linkinfo(string $path): int
```php

Devuelve la información de un enlace.

Esta función se utiliza para verificar si un enlace (indicado por la ruta `path`) existe realmente (utilizando el mismo método que la macro S_ISLNK, definida en `stat.h`).

## Parámetros

`path`  
Ruta hacia el enlace.

## Valores devueltos

`linkinfo` devuelve el campo `st_dev` de la estructura stat de C Unix, devuelta por la llamada al sistema `lstat`. Devuelve un entero no negativo en caso de éxito, -1 en el caso de que el enlace no haya sido encontrado, o `false` si ocurre una violación open.base_dir.

## Ejemplos

Ejemplo con `linkinfo`

```
<?php

echo linkinfo('/vmlinuz'); // 835

?>

    
```php

## Véase también

`symlink`, `link`, `readlink`
