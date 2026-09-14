---
title: lchown
description: Cambia el propietario de un enlace simbólico
source_url: https://www.php.net/manual/es/function.lchown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/lchown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23830
---

lchown

Cambia el propietario de un enlace simbólico

## Descripción

```php
lchown(string $filename, string $user): bool
```php

Intenta reemplazar el propietario del enlace simbólico `filename` por el usuario `user`

Solo el superusuario puede cambiar el propietario de un enlace simbólico.

## Parámetros

`filename`  
Ruta hacia el fichero.

`user`  
El usuario, por su nombre o su número.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Modificación del propietario de un enlace simbólico

```
<?php
$target = 'output.php';
$link = 'output.html';
symlink($target, $link);

lchown($link, 8);
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.

## Véase también

`chown`, `lchgrp`, `chgrp`, `chmod`
