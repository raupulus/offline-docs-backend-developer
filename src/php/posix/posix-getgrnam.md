---
title: posix_getgrnam
description: Devolver información sobre un grupo mediante su nombre
source_url: https://www.php.net/manual/es/function.posix-getgrnam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getgrnam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 65210
---

posix_getgrnam

Devolver información sobre un grupo mediante su nombre

## Descripción

```php
posix_getgrnam(string $name): array
```php

Obtiene información sobre un grupo, proporcionado su nombre.

## Parámetros

`name`  
EL nombre del grupo

## Valores devueltos

Los elementos del array devuelto son:

| Elemento | Descripción |
|----|----|
| name | El elemento name contiene el nombre del grupo. Es una abreviatura, normalmente menos de 16 caracteres "soportan" el groupo, no el nombre real completo. Debería ser el mismo que el del parámetro `name` usado al llamar a la función, y por lo tanto redundante. |
| passwd | El elemento passwd contiene la contraseña del grupo en un formato encriptado. A menudo, por ejemplo bajo un sistema que emplea contraseñas "shadow", se devuelve un asterisco en su lugar. |
| gid | El ID del grupo en forma numérica. |
| members | Consiste en un `array` de `string`s de todos los miembros del grupo. |

El array de información del grupo

## Ejemplos

Ejemplo de uso de `posix_getgrnam`

```
<?php

$groupinfo = posix_getgrnam("toons");

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

`posix_getegid`, `posix_getgrgid`, `filegroup`, `stat`, Página GETGRNAM(3) del man de POSIX
