---
title: rmdir
description: Elimina un directorio
source_url: https://www.php.net/manual/es/function.rmdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/rmdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: ea62fb831
order: 24010
---

rmdir

Elimina un directorio

## Descripción

```php
rmdir(string $directory, [resource $context]): bool
```php

Intenta eliminar el directorio cuyo camino es `directory`. El directorio debe estar vacío, y el script debe tener los permisos adecuados. Una advertencia de nivel `E_WARNING` será generada en caso de fallo.

## Parámetros

`directory`  
El camino hacia el directorio.

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `rmdir`

```
<?php
if (!is_dir('examples')) {
    mkdir('examples');
}

rmdir('examples');
?>

     
```php

## Véase también

`is_dir`, `mkdir`, `unlink`
