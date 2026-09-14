---
title: link
description: Crea un enlace
source_url: https://www.php.net/manual/es/function.link.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/link.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 46a0d3708
order: 23840
---

link

Crea un enlace

## Descripción

```php
link(string $target, string $link): bool
```php

`link` crea un enlace.

## Parámetros

`target`  
El destino del enlace.

`link`  
El nombre del enlace.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

La función falla y emite una `E_WARNING` si `link` ya existe, o si `target` no existe.

## Ejemplos

Creación de un enlace

```
<?php

$target = 'source.ext'; // Este es el fichero que existe actualmente
$link = 'newfile.ext';  // Este será el nombre del fichero que se desea enlazar

link($target, $link);
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

> [!NOTE]
> Windows únicamente: esta función requiere un nivel de funcionamiento con derechos elevados, o bien la desactivación de UAC.

## Véase también

`symlink`, `readlink`, `linkinfo`, `unlink`
