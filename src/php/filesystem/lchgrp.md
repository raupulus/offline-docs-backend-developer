---
title: lchgrp
description: Cambiar la pertenencia al grupo de un enlace simbólico
source_url: https://www.php.net/manual/es/function.lchgrp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/lchgrp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 23820
---

lchgrp

Cambiar la pertenencia al grupo de un enlace simbólico

## Descripción

```php
lchgrp(string $filename, string $group): bool
```php

Intenta reemplazar el grupo del enlace simbólico `filename` por el grupo `group`.

Solo el superusuario puede cambiar el grupo de un enlace simbólico arbitrariamente; los demás usuarios pueden cambiar el grupo de un enlace simbólico a un grupo del cual este usuario es miembro.

## Parámetros

`filename`  
Ruta hacia el enlace simbólico.

`group`  
El grupo, especificado por su nombre o su número.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Modificación del grupo de un enlace simbólico

```
<?php
$target = 'output.php';
$link = 'output.html';
symlink($target, $link);

lchgrp($link, 8);
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.

## Véase también

`chgrp`, `lchown`, `chown`, `chmod`
