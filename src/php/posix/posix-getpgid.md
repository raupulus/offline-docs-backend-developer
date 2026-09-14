---
title: posix_getpgid
description: Obtener el id del grupo de procesos para un control de trabajo
source_url: https://www.php.net/manual/es/function.posix-getpgid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getpgid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65240
---

posix_getpgid

Obtener el id del grupo de procesos para un control de trabajo

## Descripción

```php
posix_getpgid(int $process_id): int
```php

Devuelve el identificador del grupo de procesos del proceso `process_id` o `false` si ocurre un error.

## Parámetros

`process_id`  
El id del proceso.

## Valores devueltos

Devuelve el identificador, como valor de tipo `int`.

## Ejemplos

Ejemplo de uso de `posix_getpgid`

```
<?php
$pid = posix_getppid();
echo posix_getpgid($pid); //35
?>

    
```php

## Notas

> [!NOTE]
> Esta no es una función POSIX, pero es usual en sistemas BSD y System V. Si el sistema no soporta esta función, no será incluidaen tiempo de compilación. Se puede comprobar con `function_exists`.

## Véase también

`posix_getppid`, Página del manual SETPGID(2)
