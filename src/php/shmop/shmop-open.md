---
title: shmop_open
description: Crea o abre un bloque de memoria compartida
source_url: https://www.php.net/manual/es/function.shmop-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/functions/shmop-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: true
translation_revision: 41d34439e
order: 74220
---

shmop_open

Crea o abre un bloque de memoria compartida

## Descripción

```php
shmop_open(int $key, string $mode, int $permissions, int $size): Shmop
```php

`shmop_open` puede crear o abrir un bloque de memoria compartida.

## Parámetros

`key`  
Identificador del sistema para el bloque de memoria compartida. Este argumento puede ser pasado como un decimal o un hexadecimal.

`mode`  
Se pueden utilizar:

- `"a"` para acceso (utiliza `SHM_RDONLY` para shmat) utilice esta opción para abrir un bloque ya existente en modo solo lectura.

- `"c"` para creación (utiliza `IPC_CREATE`) utilice esta opción para crear un nuevo bloque, o, si un segmento con el mismo identificador existe, intentar acceder a él en modo lectura y escritura.

- `"w"` para acceso en lectura y escritura. Utilice esta opción cuando se deba acceder en lectura y escritura a un segmento de memoria compartida. Este es el caso más común.

- `"n"` crea un nuevo segmento de memoria compartida (utiliza `IPC_CREATE|IPC_EXCL`). Utilice esta opción cuando se quiera crear un nuevo segmento de memoria compartida a menos que ya exista uno corrupto con la misma opción. Esto es muy útil por razones de seguridad, para evitar agujeros de seguridad que exploten la carrera por los recursos.

`permissions`  
Los permisos que se otorgan a este bloque. Son los mismos que para los archivos. Estos permisos deben ser pasados en formato octal (i.e. 0644).

`size`  
El tamaño del bloque de memoria compartida que se quiere crear, en bytes

> [!NOTE]
> Nota: Los tercer y cuarto argumentos deben ser pasados a 0 si se quiere abrir un bloque de memoria compartida ya existente.

## Valores devueltos

En caso de éxito, `shmop_open` devuelve una instancia de `Shmop` que puede ser utilizada para acceder a la memoria que se acaba de crear. `false` será devuelto en caso de fallo.

## Errores/Excepciones

Si `mode` es inválido, o si `size` es inferior o igual a cero, se lanza una `ValueError`. En otros casos de fallo, se emite un `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shmop` ahora espera una instancia de `Shmop` anteriormente se esperaba un `resource`. |
| 8.0.0 | Si `mode` es inválido, o si `size` es inferior o igual a cero, se lanza una `ValueError`; anteriormente, se emitía un `E_WARNING` en su lugar, y la función devolvía `false`. |

## Ejemplos

Crear un nuevo bloque de memoria compartida Shmop

```
<?php
$shm_key = ftok(__FILE__, 't');
$shm_id = shmop_open($shm_key, "c", 0644, 100);
?>

   
```php

Este ejemplo abre un nuevo bloque de memoria compartida, cuyo identificador es devuelto por `ftok`.

## Véase también

shmop_close

shmop_delete
