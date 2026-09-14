---
title: posix_getpwnam
description: Devolver información sobre un usuario mediante su nombre de usuario
source_url: https://www.php.net/manual/es/function.posix-getpwnam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getpwnam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65280
---

posix_getpwnam

Devolver información sobre un usuario mediante su nombre de usuario

## Descripción

```php
posix_getpwnam(string $username): array
```php

Devuelve un `array` de información sobre el usuario dado.

## Parámetros

`username`  
Un nombre de usuario alfanumérico.

## Valores devueltos

En caso de éxito se devuelve un array con los siguientes elementos, si no se devuelve `false`:

| Elemento | Descripción |
|----|----|
| name | El elemento name contiene el nombre del grupo. Es una abreviatura, normalmente menos de 16 caracteres "soportan" el groupo, no el nombre real completo. Debería se el mismo que el parámetro `username` usado al llamar a la función, y por lo tanto redundante. |
| passwd | El elemento passwd contiene la contraseña del grupo en un formato encriptado. A menudo, por ejemplo bajo un sistema que emplea contraseñas "shadow", se devuelve un asterisco en su lugar. |
| uid | El ID del usuario en forma numérica. |
| gid | El ID de grupo del usuario. Use la función `posix_getgrgid` para resolver el nombre de grupo y una lista de sus miembros. |
| gecos | GECOS es un término obosleto que se refiere al campo de información "finger" de un sistema de procesamiento por lotes Honeywell. El campo, sin embargo, todavía existe, y su contenido ha sido formalizado por POSIX. El campo contiene una lista separada por comas que contiene el nombre completo del usuario, teléfono de oficina, número de oficina, y el número de teléfono de casa. En la mayoría de los sistemas solo está disponible el nombre de usuario completo. |
| dir | Este elemento contiene la ruta absoluta al directorio "home" del usuario. |
| shell | El elemento shell contiene la ruta absoluta al ejecutable del shell predeterminado de usuario. |

El array de información de usuario

## Ejemplos

Ejemplo de uso de `posix_getpwnam`

```
<?php

$userinfo = posix_getpwnam("tom");

print_r($userinfo);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [name]    => tom
        [passwd]  => x
        [uid]     => 10000
        [gid]     => 42
        [gecos]   => "tom,,,"
        [dir]     => "/home/tom"
        [shell]   => "/bin/bash"
    )

## Véase también

`posix_getpwuid`, Página GETPWNAM(3) del man de POSIX
