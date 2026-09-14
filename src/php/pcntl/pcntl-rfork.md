---
title: pcntl_rfork
description: Manipula los recursos del proceso
source_url: https://www.php.net/manual/es/function.pcntl-rfork.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-rfork.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 61374bbe2
order: 61290
---

pcntl_rfork

Manipula los recursos del proceso

## Descripción

```php
pcntl_rfork(int $flags, [int $signal]): int
```php

Manipula los recursos del proceso.

## Parámetros

`flags`  
El parámetro `flags` determina qué recursos del proceso llamante (padre) son compartidos por el nuevo proceso (hijo) o inicializados a sus valores por omisión.

`flags` es el OU lógico de un subconjunto de los siguientes valores: `RFPROC`: Si está definido, se crea un nuevo proceso; de lo contrario, los cambios afectan al proceso actual., `RFNOWAIT`: Si está definido, el proceso hijo será disociado del padre. Al salir, el proceso hijo no dejará un estado a recolectar para el padre., `RFFDG`: Si está definido, la tabla de descriptores de ficheros del llamante es copiada; de lo contrario, ambos procesos comparten una sola tabla., `RFCFDG`: Si está definido, el nuevo proceso comienza con una tabla de descriptores de ficheros propia. Es mutuamente excluyente con `RFFDG`., `RFLINUXTHPN`: Si está definido, el núcleo devolverá SIGUSR1 en lugar de SIGCHILD al salir del hilo para el hijo. Esto está destinado a hacer la notificación de salida del padre de salida del hilo Linux clone., `RFTSIGZMB`: Si está definido, el núcleo enviará la señal especificada por el parámetro `signal` al padre al salir el hijo, en lugar del SIGCHLD por omisión. Especificar el número de señal 0 desactiva la entrega de señal al salir el hijo., `RFTHREAD`: Si está definido, el nuevo proceso comparte el descriptor de fichero a la tabla de líderes de proceso con su padre. Solo se aplica cuando ni `RFFDG` ni `RFCFDG` están definidos.

`signal`  
El número de señal a enviar al padre cuando el hijo sale. Solo se usa cuando el indicador `RFTSIGZMB` está definido. Especificar `0` desactiva la entrega de señal al salir el hijo.

## Valores devueltos

En caso de éxito, el PID del proceso hijo es devuelto en el contexto del padre, y un `0` es devuelto en el contexto del proceso hijo. En caso de fallo, un `-1` será devuelto en el contexto del padre, ningún proceso hijo será creado, y se lanzará un error PHP.

## Ejemplos

Ejemplo de `pcntl_rfork`

```
<?php

$pid = pcntl_rfork(RFNOWAIT|RFTSIGZMB, SIGUSR1);
if ($pid > 0) {
  // Esto es el proceso padre.
  var_dump($pid);
} else {
  // Esto es el proceso hijo.
  var_dump($pid);
  sleep(2); // mientras el hijo no duerma, vemos su "pid"
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(77093)
    int(0)

## Notas

> [!NOTE]
> Esta función solo está disponible en sistemas BSD.

## Véase también

`pcntl_fork`, `pcntl_waitpid`, `pcntl_signal`, `cli_set_process_title`
