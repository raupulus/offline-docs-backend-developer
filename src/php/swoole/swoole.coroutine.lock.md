---
title: La clase Swoole\Coroutine\Lock
source_url: https://www.php.net/manual/es/class.swoole-coroutine-lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole.coroutine.lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 93e05c681
order: 93250
---

## Introducción

Swoole 6.0.1 introdujo un bloqueo de corrutina que admite el uso compartido entre procesos e hilos. Este bloqueo está diseñado con un comportamiento no bloqueante y permite una sincronización eficiente de corrutinas en entornos multiproceso y multihilo.

Cuando se compila con la opción `--enable-iouring` y el kernel de Linux admite la característica `io_uring futex`, el bloqueo de corrutina de Swoole implementa la sincronización usando `io_uring futex`. En este caso, las corrutinas esperan las activaciones del bloqueo usando un mecanismo de cola eficiente, mejorando significativamente el rendimiento.

Sin `io_uring futex`, el bloqueo de corrutina recurre a un mecanismo de retroceso exponencial, donde el tiempo de espera aumenta en 2^n milisegundos (siendo n el número de fallos) después de cada intento fallido de adquirir el bloqueo. Aunque este enfoque evita la espera activa, introduce una carga adicional de programación de CPU y latencia.

El bloqueo de corrutina es reentrante, lo que permite a la corrutina que actualmente lo posee realizar múltiples operaciones de bloqueo de manera segura.

> [!WARNING]
> No cree bloqueos en funciones de retrollamada como `onReceive`, ya que esto causará un crecimiento continuo de la memoria y llevará a fugas de memoria.

> [!WARNING]
> El bloqueo y desbloqueo deben realizarse en la misma corrutina, de lo contrario se romperán las condiciones estáticas.

## Sinopsis de la clase

Swoole\Coroutine\Lock

Swoole\Coroutine\Lock

Métodos

## Ejemplos

Uso básico

```php
<?php
use Swoole\Coroutine\Lock;
use Swoole\Coroutine\WaitGroup;
use function Swoole\Coroutine\go;
use function Swoole\Coroutine\run;

$lock = new Lock();
$waitGroup = new WaitGroup();

run(function() use ($lock, $waitGroup) {
    go(function() use ($lock, $waitGroup) {
        $waitGroup->add();
        $lock->lock();
        sleep(1);
        $lock->unlock();
        $waitGroup->done();
    });

    go(function() use ($lock, $waitGroup) {
        $waitGroup->add();
        $lock->lock(); // Espera a que la corrutina que lo posee lo desbloquee
        sleep(1);
        $lock->unlock();
        $waitGroup->done();
    });

    echo 'El bloqueo no bloquea el proceso';
    $waitGroup->wait();
});

    
```
