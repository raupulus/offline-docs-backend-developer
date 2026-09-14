---
title: posix_uname
description: Obtener el nombre del sistema
source_url: https://www.php.net/manual/es/function.posix-uname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-uname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65500
---

posix_uname

Obtener el nombre del sistema

## Descripción

```php
posix_uname(): array
```php

Obtiene información sobre el sistema.

Posix requiere que estas suposiciones no deben hacerse sobre el formato de los valores, p.ej. la suposición que la versión puede contener tres dígitos o cualquier otra cosa devuelta por esta función.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un hash de cadena con información sobre el sistema. Los índices del hash son

- sysname - nombre del sistema operativo (p.ej. Linux)

- nodename - nombre del sistema (p.ej. valiant)

- release - versión de publicación del sistema operativo (p.ej. 2.2.10)

- version - versión del sistema operativo (p.ej. \#4 Tue Jul 20 17:01:36 MEST 1999)

- machine - arquitectura del sistema (p.ej. i586)

- domainname - nombre del dominio DNS (p.ej. example.com)

domainname es una extensión GNU y no es parte de POSIX.1, por lo que este campo solamente está disponible en sistemas GNU o cuando se usa GNU libc.

La función devuelve `false` en caso de fallo.

## Ejemplos

Ejemplo de uso de `posix_uname`

```
<?php
$uname=posix_uname();
print_r($uname);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [sysname] => Linux
        [nodename] => funbox
        [release] => 2.6.20-15-server
        [version] => #2 SMP Sun Apr 15 07:41:34 UTC 2007
        [machine] => i686
    )
