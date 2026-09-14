---
title: shmop_write
description: Escribir en un bloque de memoria compartida
source_url: https://www.php.net/manual/es/function.shmop-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/functions/shmop-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: true
translation_revision: 41d34439e
order: 74250
---

shmop_write

Escribir en un bloque de memoria compartida

## Descripción

```php
shmop_write(Shmop $shmop, string $data, int $offset): int
```php

`shmop_write` escribe una cadena en un bloque de memoria compartida.

## Parámetros

`shmop`  
El identificador del bloque de memoria compartida, creado por la función `shmop_open`

`data`  
Una cadena para escribir en el bloque de la memoria compartida

`offset`  
Especifica la posición desde la cual los datos deben ser escritos en la memoria compartida. El offset debe ser superior o igual a cero e inferior o igual al tamaño real del segmento de memoria compartida.

## Valores devueltos

El tamaño de los datos escritos.

## Errores/Excepciones

Si `offset` está fuera de límite, o si un segmento de memoria compartida de solo lectura debe ser escrito, se levanta una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Anterior a PHP 8.0.0, `false` era devuelto en caso de fallo. |
| 8.0.0 | `shmop` espera ahora una instancia de `Shmop`; anteriormente se esperaba un `resource`. |

## Ejemplos

Escribe un bloque de memoria compartida

```
<?php
$shm_bytes_written = shmop_write($shm_id, $my_string, 0);
?>

   
```php

Este ejemplo escribe los datos de la cadena `$my_string` en un bloque de memoria compartida. `$shm_bytes_written` representará el número de bytes escritos.

## Véase también

shmop_read
