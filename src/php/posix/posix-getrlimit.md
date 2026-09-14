---
title: posix_getrlimit
description: Devuelve información sobre los límites de recursos del sistema
source_url: https://www.php.net/manual/es/function.posix-getrlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getrlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 55d731ec5
order: 65300
---

posix_getrlimit

Devuelve información sobre los límites de recursos del sistema

## Descripción

```php
posix_getrlimit([int $resource]): array
```php

`posix_getrlimit` devuelve un `array` con información sobre los límites actuales blandos y duros del recurso.

Cada recurso tiene un límite soft y hard asociados. El límite soft corresponde al valor que el núcleo fuerza para el recurso correspondiente. El límite hard actúa como un techo del límite soft. Un proceso no privilegiado solo puede definir su límite soft en un valor comprendido entre 0 y el límite hard, lo que solo hará bajar su límite hard.

## Parámetros

`resource`  
Si es `null`, se devolverán todos los límites de recursos actuales. De lo contrario, especifique la [constante de límite de recurso](#posix.constants.setrlimit) para recuperar un límite específico.

## Valores devueltos

Devuelve un `array` asociativo de elementos para cada límite que esté definido. Cada límite tiene un límite blando y uno duro.

| Nombre del límite | Descripción del límite |
|----|----|
| core | El tamaño máximo del fichero de memoria. Cuando es 0, no se crean ficheros de memoria. Cuando los ficheros de memoria son más grandes que este tamaño, se truncarán a este tamaño. |
| totalmem | El tamaño máximo de la memoria del proceso, en bytes. |
| virtualmem | El tamaño máximo de la memoria virtual para el proceso, en bytes. |
| data | El tamaño máximo del segmento de datos para el proceso, en bytes. |
| stack | El tamaño máximo de la pila del proceso, en bytes. |
| rss | El número máximo de páginas virtuales residentes en RAM |
| maxproc | El número máximo de procesos que pueden ser creados para el ID de usuario real del proceso llamante. |
| memlock | El número máximo de bytes de memoria que pueden ser bloqueados en RAM. |
| cpu | La cantidad de tiempo que se permite al proceso usar la CPU. |
| filesize | El tamaño máximo del segmento de datos para el proceso, en bytes. |
| openfiles | Uno más que el número máximo de descriptores de fichero abiertos. |

Lista de límites posibles devueltos

La función devuelve `false` en caso de error.

## Historial de cambios

| Versión | Descripción                                     |
|---------|-------------------------------------------------|
| 8.3.0   | Se ha añadido el parámetro opcional `resource`. |

## Ejemplos

Ejemplo de uso de `posix_getrlimit`

```
<?php

$limits = posix_getrlimit();

print_r($limits);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [soft core] => 0
        [hard core] => unlimited
        [soft data] => unlimited
        [hard data] => unlimited
        [soft stack] => 8388608
        [hard stack] => unlimited
        [soft totalmem] => unlimited
        [hard totalmem] => unlimited
        [soft rss] => unlimited
        [hard rss] => unlimited
        [soft maxproc] => unlimited
        [hard maxproc] => unlimited
        [soft memlock] => unlimited
        [hard memlock] => unlimited
        [soft cpu] => unlimited
        [hard cpu] => unlimited
        [soft filesize] => unlimited
        [hard filesize] => unlimited
        [soft openfiles] => 1024
        [hard openfiles] => 1024
    )

## Véase también

página del manual GETRLIMIT(2), `posix_setrlimit`
