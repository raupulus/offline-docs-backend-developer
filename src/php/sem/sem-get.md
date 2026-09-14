---
title: sem_get
description: Retorna un identificador de semáforo
source_url: https://www.php.net/manual/es/function.sem-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/sem-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: false
translation_revision: fd2f14b2e
order: 73530
---

sem_get

Retorna un identificador de semáforo

## Descripción

```php
sem_get(int $key, [int $max_acquire], [int $permissions], [bool $auto_release]): SysvSemaphore
```php

`sem_get` retorna un identificador que podrá ser utilizado para acceder a un semáforo System V.

Una segunda llamada a `sem_get` con la misma clave retornará un identificador diferente, pero ambos identificadores permitirán acceder al mismo semáforo.

Si `key` es `0`, un nuevo semáforo privado se crea para cada llamada a `sem_get`.

## Parámetros

`key`  

`max_acquire`  
El número de procesos que pueden reservar simultáneamente el semáforo se especifica en el argumento `max_acquire`.

`permissions`  
Los permisos del semáforo. Actualmente, este valor solo se aplica si el proceso es el único proceso actualmente adjunto al semáforo.

`auto_release`  
El argumento opcional `auto_release` especifica si el semáforo debe ser liberado automáticamente al cerrar.

## Valores devueltos

Retorna un recurso de semáforo en caso de éxito, y `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función retorna una instancia de `SysvSemaphore` ahora; anteriormente; un `resource` era retornado. |
| 8.0.0 | El tipo de `auto_release` ha sido modificado de `int` a `bool`. |

## Notas

> [!WARNING]
> Al utilizar la función `sem_get` para acceder a un semáforo creado fuera de PHP, tenga en cuenta que el semáforo debe haber sido creado como un conjunto de 3 semáforos (por ejemplo, especificando 3 como argumento `nsems` durante la llamada a la función C `semget()`), de lo contrario, PHP no será capaz de acceder a este semáforo.

## Véase también

sem_acquire

sem_release

ftok
