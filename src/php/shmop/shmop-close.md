---
title: shmop_close
description: Cierra un bloque de memoria compartida
source_url: https://www.php.net/manual/es/function.shmop-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/functions/shmop-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: true
translation_revision: 41d34439e
order: 74200
---

shmop_close

Cierra un bloque de memoria compartida

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] shmop_close(Shmop $shmop): void
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

`shmop_close` sirve para cerrar un bloque de memoria compartida.

## Parámetros

`shmop`  
El recurso de memoria compartida creado por `shmop_open`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido declarada obsoleta, ya que no tiene ningún efecto. |
| 8.0.0 | `shmop` espera una instancia de `Shmop` ahora; anteriormente se esperaba un `resource`. |

## Ejemplos

Cierre de un bloque de memoria compartida

```
<?php
shmop_close($shm_id);
?>

   
```php

Este ejemplo cierra el bloque de memoria compartida identificado por `$shm_id`.

## Véase también

shmop_open
