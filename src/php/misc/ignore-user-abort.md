---
title: ignore_user_abort
description: Activa la interrupción de script al desconectarse el visitante
source_url: https://www.php.net/manual/es/function.ignore-user-abort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/ignore-user-abort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 47130
---

ignore_user_abort

Activa la interrupción de script al desconectarse el visitante

## Descripción

```php
ignore_user_abort([bool $enable]): int
```php

`ignore_user_abort` activa la opción que permite que, al desconectarse el cliente Web, el script continúe su ejecución.

Cuando PHP se ejecuta como script en línea de comandos, y el tty del script se cierra sin que el script haya terminado, entonces el script se detendrá tan pronto como intente escribir algo, a menos que `enable` sea `true`

## Parámetros

`enable`  
Si está definido y no es `null`, la función asignará a la directiva [ignore_user_abort](#ini.ignore-user-abort) el valor de `enable`. Si se omite, esta función solo devuelve el valor de la configuración actual.

## Valores devueltos

Devuelve la configuración anterior, en forma de `int`.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `enable` ahora es nullable. |

## Ejemplos

Ejemplo con `ignore_user_abort`

```
<?php
// Ignora la desconexión del usuario y permite
// que el script continúe ejecutándose
ignore_user_abort(true);
set_time_limit(0);

echo 'Prueba del gestor de conexión de PHP';

// Ejecución de un bucle infinito que monitorea
// la actividad del usuario. O bien hace clic fuera
// de la página, o bien hace clic en el botón "Stop".
while(1)
{
    // ¿Ha fallado la conexión?
    if(connection_status() != CONNECTION_NORMAL)
    {
        break;
    }

    // Se espera 10 segundos
    sleep(10);
}

// Si se alcanza este punto, entonces la instrucción 'break'
// se ejecutará desde el bucle infinito

// Además, en este nivel se pueden ingresar datos en el historial,
// o ejecutar otras tareas necesarias, sin depender del navegador.
?>

    
```php

## Notas

PHP no detecta la desconexión del cliente Web hasta que se intenta enviar algo. Simplemente usar un `echo` no garantiza que la información se envíe, ver la función `flush`.

## Véase también

`connection_aborted`, `connection_status`, [Gestor de conexión](#features.connection-handling) para una descripción completa del gestor de conexión en PHP.
