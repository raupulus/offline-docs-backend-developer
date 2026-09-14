---
title: Ejemplos
source_url: https://www.php.net/manual/es/pcntl.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: e91b2dd25
order: 61170
---

## Ejemplos

## Uso simple

Este ejemplo forkea un proceso demonio, con un gestor de señales.

Ejemplo de control de procesos

```php
<?php
pcntl_async_signals(true);

$pid = pcntl_fork();
if ($pid == -1) {
     die("imposible de forkear");
} else if ($pid) {
     exit(); // somos el proceso padre
} else {
     // somos el proceso hijo
}

// desvinculemos el proceso del terminal
if (posix_setsid() == -1) {
    die("imposible de desvincularse del terminal");
}

// configuración de los gestores de señales
pcntl_signal(SIGTERM, "sig_handler");
pcntl_signal(SIGHUP, "sig_handler");

// bucle infinito
while (1) {

    // ejecución de algo

}

function sig_handler($signo)
{

     switch ($signo) {
         case SIGTERM:
             // gestión de las tareas de terminación
             exit;
             break;
         case SIGHUP:
             // gestión de las tareas de reinicio
             break;
         default:
             // gestión de otras tareas
     }

}

?>

   
```
