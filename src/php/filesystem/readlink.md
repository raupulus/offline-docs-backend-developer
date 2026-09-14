---
title: readlink
description: Devuelve el contenido de un enlace simbólico
source_url: https://www.php.net/manual/es/function.readlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/readlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 23950
---

readlink

Devuelve el contenido de un enlace simbólico

## Descripción

```php
readlink(string $path): string
```php

`readlink` realiza la misma operación que la función C `readlink`.

## Parámetros

`path`  
La ruta hacia el enlace simbólico.

## Valores devueltos

Devuelve el contenido del enlace simbólico o `false` si ocurre un error.

> [!NOTE]
> La función falla si el argumento `path` no es un enlace simbólico, excepto en Windows, donde se devolverá la ruta personalizada.

## Ejemplos

Ejemplo con `readlink`

```
<?php

// Muestra por ejemplo /boot/vmlinux-2.4.20-xfs
echo readlink('/vmlinuz');

?>

    
```php

## Véase también

`is_link`, `symlink`, `linkinfo`
