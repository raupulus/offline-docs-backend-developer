---
title: posix_getgrgid
description: Devolver información sobre un grupo mediante un id de grupo
source_url: https://www.php.net/manual/es/function.posix-getgrgid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getgrgid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65200
---

posix_getgrgid

Devolver información sobre un grupo mediante un id de grupo

## Descripción

```php
posix_getgrgid(int $gid): array
```php

Obtiene información sobre un grupo porporcionando su id.

## Parámetros

`gid`  
El id del grupo.

## Valores devueltos

Los elementos del array devueltos son:

| Elemento | Descripción |
|----|----|
| name | El elemento name contiene el nombre del grupo. Es una abreviatura, normalmente menos de 16 caracteres "soportan" el groupo, no el nombre real completo. |
| passwd | El elemento passwd contiene la contraseña del grupo en un formato encriptado. A menudo, por ejemplo bajo un sistema que emplea contraseñas "shadow", se devuelve un asterisco en su lugar. |
| gid | El ID del grupo, debería ser el mismo que el del parámetro `gid` usado al llamar a la función, y por lo tanto redundante. |
| members | Consiste en un `array` de `string`s de todos los miembros del grupo. |

El array de información de grupo

## Ejemplos

Ejemplo de uso de`posix_getgrgid`

```
<?php

$groupid   = posix_getegid();
$groupinfo = posix_getgrgid($groupid);

print_r($groupinfo);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [name]    => toons
        [passwd]  => x
        [members] => Array
            (
                [0] => tom
                [1] => jerry
            )
        [gid]     => 42
    )

## Véase también

`posix_getegid`, `posix_getgrnam`, `filegroup`, `stat`, Página GETGRNAM(3) del man de POSIX
