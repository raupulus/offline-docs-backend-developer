---
title: posix_getsid
description: Obtener el sid actual del proceso
source_url: https://www.php.net/manual/es/function.posix-getsid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getsid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65310
---

posix_getsid

Obtener el sid actual del proceso

## Descripción

```php
posix_getsid(int $process_id): int
```php

Devuelve el identificador de sesión del proceso `process_id`. El identificador de sesión de un proceso es el id de grupo del proceso del líder de la sesión.

## Parámetros

`process_id`  
El identificador de proceso. Si se establece a 0, se asume el proceso actual. Si se especifica un `process_id` no válido, se devuelve `false` y se establece un error que puede ser verificado con `posix_get_last_error`.

## Valores devueltos

Devuelve el identificador, como valor de tipo `int`, o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso de `posix_getsid`

```
<?php
$pid = posix_getpid();
echo posix_getsid($pid); //8805
?>

    
```php

## Véase también

`posix_getpgid`, `posix_setsid`, Página GETSID(2) del man de POSIX
