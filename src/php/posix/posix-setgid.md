---
title: posix_setgid
description: Establecer el GID de proceso actual
source_url: https://www.php.net/manual/es/function.posix-setgid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-setgid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65410
---

posix_setgid

Establecer el GID de proceso actual

## Descripción

```php
posix_setgid(int $group_id): bool
```php

Establece el ID real de grupo al proceso actual. Esta es una función privilegiada y necesita los privilegios apropiados (normalmente "root") en el sistema para ser capaz de realizar esta función. El orden apropiado de las llamadas a las funciones es `posix_setgid` primero, `posix_setuid` la última.

> [!NOTE]
> Si el llamador es un superusuario también se establecerá el id efectivo de grupo.

## Parámetros

`group_id`  
El id de grupo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `posix_setgid`

Este ejemplo imprimirá el id efectivo de grupo, una vez cambiado.

```
<?php
echo 'Mi id real de grupo es '.posix_getgid(); //20
posix_setgid(40);
echo 'Mi id real de grupo es '.posix_getgid(); //40
echo 'Mi id efectivo de grupo es '.posix_getegid(); //40
?>

    
```php

## Véase también

`posix_getgrgid`, `posix_getgid`
