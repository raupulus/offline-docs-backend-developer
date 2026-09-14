---
title: rename
description: Renombra un fichero o un directorio
source_url: https://www.php.net/manual/es/function.rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: ea62fb831
order: 23990
---

rename

Renombra un fichero o un directorio

## Descripción

```php
rename(string $from, string $to, [resource $context]): bool
```php

Intenta renombrar `from` a `to`, moviéndolo de directorio si es necesario. Si se renombra un fichero y `to` existe, será sobrescrito. Si se renombra un directorio y `to` existe, esta función emite un aviso.

## Parámetros

`from`  
El nombre antiguo.

> [!NOTE]
> El gestor utilizado en el argumento `from` *DEBE* ser el mismo que el utilizado en `to`.

`to`  
El nuevo nombre.

> [!NOTE]
> En Windows, si `to` ya existe, debe poder ser escrito. De lo contrario `rename` falla y emite un `E_WARNING`.

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `rename`

```
<?php
rename("/tmp/tmp_file.txt", "/home/user/login/docs/my_file.txt");
?>

    
```php

## Véase también

`copy`, `unlink`, `move_uploaded_file`
