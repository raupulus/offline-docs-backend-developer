---
title: pcntl_signal_dispatch
description: Llama a los gestores de señales para cada señal en espera
source_url: https://www.php.net/manual/es/function.pcntl-signal-dispatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-signal-dispatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: 782d62b55
order: 61340
---

pcntl_signal_dispatch

Llama a los gestores de señales para cada señal en espera

## Descripción

```php
pcntl_signal_dispatch(): bool
```php

La función `pcntl_signal_dispatch` llama a los gestores de señales instalados por `pcntl_signal` para cada señal en espera.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `pcntl_signal_dispatch`

```
<?php
echo "Instalación de un gestor de señal...\n";
pcntl_signal(SIGHUP,  function($signo) {
     echo "Gestor de señal llamado!\n";
});

echo "Generación de una señal SIGHUP a mí mismo...\n";
posix_kill(posix_getpid(), SIGHUP);

echo "Envío...\n";
pcntl_signal_dispatch();

echo "Hecho\n";

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Instalación de un gestor de señal...
    Generación de una señal SIGHUP a mí mismo...
    Envío...
    Gestor de señal llamado!
    Hecho

## Véase también

`pcntl_signal`, `pcntl_sigprocmask`, `pcntl_sigwaitinfo`, `pcntl_sigtimedwait`
