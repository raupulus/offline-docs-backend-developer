---
title: shmop_size
description: Leer el tamaño del bloque de memoria compartida
source_url: https://www.php.net/manual/es/function.shmop-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/functions/shmop-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: true
translation_revision: 41d34439e
order: 74240
---

shmop_size

Leer el tamaño del bloque de memoria compartida

## Descripción

```php
shmop_size(Shmop $shmop): int
```php

`shmop_size` sirve para conocer el tamaño en bytes de un bloque de memoria compartida.

## Parámetros

`shmop`  
El identificador del bloque de memoria compartido creado por la función `shmop_open`

## Valores devueltos

Devuelve un `int`, que representa el número de bytes que ocupa la memoria compartida.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shmop` espera ahora una instancia de `Shmop` anteriormente se esperaba un `resource`. |

## Ejemplos

Lee el tamaño de un bloque de memoria compartida

```
<?php
$shm_size = shmop_size($shm_id);
?>

   
```php

Este ejemplo lee el tamaño del bloque identificado por `$shm_id`, y lo coloca en `$shm_size`.
