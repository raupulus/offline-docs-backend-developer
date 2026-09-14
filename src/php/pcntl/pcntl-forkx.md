---
title: pcntl_forkx
description: Crea un proceso hijo usando forkx(2)
source_url: https://www.php.net/manual/es/function.pcntl-forkx.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-forkx.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: acb474ea9
order: 61230
---

pcntl_forkx

Crea un proceso hijo usando forkx(2)

## Descripción

```php
pcntl_forkx(int $flags): int
```php

La función `pcntl_forkx` crea un proceso hijo usando la llamada al sistema `forkx(2)`, que está disponible en los sistemas illumos y Solaris.

## Parámetros

`flags`  
El parámetro `flags` controla el comportamiento del fork. Pase `0` para el comportamiento por defecto o `FORK_NOSIGCHLD` para impedir que la señal `SIGCHLD` se envíe al padre cuando el hijo termina.

## Valores devueltos

En caso de éxito, el PID del proceso hijo es devuelto en el hilo de ejecución del padre, y se devuelve un `0` en el hilo de ejecución del hijo. En caso de fallo, se devolverá un `-1` en el contexto del padre, no se creará ningún proceso hijo, y se generará un error de PHP.

## Véase también

pcntl_fork

pcntl_rfork

pcntl_waitpid
