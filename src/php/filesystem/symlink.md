---
title: symlink
description: Crea un enlace simbólico
source_url: https://www.php.net/manual/es/function.symlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/symlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: d5f735c7b
order: 24040
---

symlink

Crea un enlace simbólico

## Descripción

```php
symlink(string $target, string $link): bool
```php

`symlink` crea un enlace simbólico para el objeto `target` con el nombre de `link`.

## Parámetros

`target`  
El objetivo del enlace.

`link`  
El nombre del enlace.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

La función falla, y emite una `E_WARNING`, si `link` ya existe. En Windows, esta función falla igualmente, y emite una `E_WARNING`, si `target` no existe.

## Ejemplos

Creación de un enlace simbólico

```
<?php
$target = 'uploads.php';
$link = 'uploads';
symlink($target, $link);

echo readlink($link);
?>

    
```php

## Véase también

`is_link`, `link`, `readlink`, `linkinfo`, `unlink`
