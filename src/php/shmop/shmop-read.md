---
title: shmop_read
description: Lee datos a partir de un bloque
source_url: https://www.php.net/manual/es/function.shmop-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/functions/shmop-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: false
translation_revision: 41d34439e
order: 74230
---

shmop_read

Lee datos a partir de un bloque

## Descripción

```php
shmop_read(Shmop $shmop, int $offset, int $size): string
```php

`shmop_read` lee una cadena en un bloque de memoria compartida.

## Parámetros

`shmop`  
El identificador del bloque de memoria compartida, creado por la función `shmop_open`

`offset`  
Posición desde la cual se debe comenzar a leer; debe ser superior o igual a cero e inferior o igual a la longitud real del segmento de memoria compartida.

`size`  
El número de bytes a leer; debe ser superior o igual a cero, y la suma de `offset` y `size` debe ser inferior o igual a la longitud real del segmento de memoria compartida. `0` lee `shmop_size($shmid) - $start` bytes.

## Valores devueltos

Devuelve los datos.

## Errores/Excepciones

Si `offset` o `size` están fuera del rango, se lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shmop` ahora requiere una instancia de `Shmop` en lugar de un `resource`. |
| 8.0.0 | Si `offset` o `size` están fuera de límite, se lanza una `ValueError`; anteriormente se emitía una `E_WARNING` y se devolvía `false`. |

## Ejemplos

Lee un bloque de memoria compartida

```
<?php
$shm_data = shmop_read($shm_id, 0, 50);
?>

   
```php

Este ejemplo lee 50 bytes del bloque de memoria compartida y los coloca en `$shm_data`.

## Véase también

shmop_write
