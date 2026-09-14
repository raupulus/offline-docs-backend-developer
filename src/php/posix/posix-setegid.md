---
title: posix_setegid
description: Establecer el GID efectivo del proceso actual
source_url: https://www.php.net/manual/es/function.posix-setegid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-setegid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65390
---

posix_setegid

Establecer el GID efectivo del proceso actual

## Descripción

```php
posix_setegid(int $group_id): bool
```php

Establece el ID de grupo efectivo del proceso actual. Esta es una función privilegiada y se necesitan los permisos apropiados (usualmente root) en el sistema para contar con la capacidad de ejecutar esta función.

## Parámetros

`group_id`  
El id de grupo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `posix_setegid`

Este ejemplo imprimirá el id de grupo efectivo, una vez cambiado.

```
<?php
echo 'Mi id de grupo real es '.posix_getgid(); //20
posix_setegid(40);
echo 'Mi id de grupo real es '.posix_getgid(); //20
echo 'Mi id de grupo efectivo es '.posix_getegid(); //40
?>

    
```php

## Véase también

`posix_getgrgid`, `posix_getgid`, `posix_setgid`
