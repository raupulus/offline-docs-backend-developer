---
title: posix_getpwuid
description: Devolver información sobre un usuario mediante su id de usuario
source_url: https://www.php.net/manual/es/function.posix-getpwuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getpwuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_revision: 265acc36e
order: 65290
---

posix_getpwuid

Devolver información sobre un usuario mediante su id de usuario

## Descripción

```php
posix_getpwuid(int $user_id): array
```php

Devuelve un `array` de información sobre el usuario denotado por el ID de usuario dado.

## Parámetros

`user_id`  
El identificador de usuario.

## Valores devueltos

Devuelve un array asociativo con los siguientes elementos:

| Elemento | Descripción |
|----|----|
| name | El elemento 'name' contiene el nombre de usuario. Es una abreviatura, normalmente un "apodo" de menos de 16 caracteres del nombre del usuario, no el nombre real completo. |
| passwd | El elemento 'passwd' contiene la contraseña del usuario en un formato encriptado. A menudo, por ejemplo, bajo un sistema que emplea contraseñas "shadow", se devuelve un asterisco en su lugar. |
| uid | El ID del usuario, debería ser el mismo que el del parámetro `user_id` empleado al llamar a la función, y por lo tanto redundante. |
| gid | El ID de grupo del usuario. Emplee la función `posix_getgrgid` para resolver el nombre de grupo y una lista de sus miembros. |
| gecos | GECOS es un término obsoleto que se refiere al campo de información "finger" de un sistema de procesamiento por lotes Honeywell. El campo, sin embargo, todavía existe, y su contenido ha sido formalizado por POSIX. El campo contiene una lista separada por comas con el nombre completo del usuario, teléfono de oficina, número de oficina, y el número de teléfono de casa. En la mayoría de los sistemas solo está disponible el nombre de usuario completo. |
| dir | Este elemento contiene la ruta absoluta al directorio "home" del usuario. |
| shell | El elemento 'shell' contiene la ruta absoluta al ejecutable del shell predeterminado del usuario. |

El array de información de usuario

La función devuelve `false` en caso de fallo.

## Ejemplos

Ejemplo de uso de `posix_getpwuid`

```
<?php

$userinfo = posix_getpwuid(10000);

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

`posix_getpwnam`, Página GETPWNAM(3) del man de POSIX
