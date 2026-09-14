---
title: register_shutdown_function
description: Registra una función de retrollamada para ejecución al cierre
source_url: https://www.php.net/manual/es/function.register-shutdown-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/register-shutdown-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: true
translation_revision: 2312f826e
order: 24820
---

register_shutdown_function

Registra una función de retrollamada para ejecución al cierre

## Descripción

```php
register_shutdown_function(callable $callback, mixed ...$args): void
```php

Registra una función de retrollamada `callback` para ejecución al cierre o cuando `exit` es llamado.

Varios llamados a `register_shutdown_function` son posibles en el mismo script, y las funciones serán llamadas en el mismo orden en que son registradas. Si se llama `exit` durante una de las funciones de cierre, el proceso será definitivamente detenido, sin que las otras funciones sean llamadas.

> [!CAUTION]
> Desde PHP 8.4.0, una llamada a `exit` sin parámetros dentro de una función de cierre registrada restablece el código de salida a `0`. Llamar a `exit` con un estado explícito sobrescribe el código de salida anterior en todas las versiones.

Las funciones de cierre pueden también llamar a la función `register_shutdown_function` ellas mismas para añadir una función de cierre al final de la cola.

## Parámetros

`callback`  
La función de retrollamada a registrar.

La función de retrollamada es ejecutada como parte de la petición, por lo tanto, es posible enviar algo a la salida desde esta última, así como acceder a los buffers de salida.

`args`  
Es posible pasar argumentos a las funciones de cierre configurando estos argumentos adicionales.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `register_shutdown_function`

```
<?php
function shutdown()
{
    // Aquí está nuestra función shutdown
    // en la cual podemos realizar
    // todas las últimas operaciones
    // antes del fin del script.

    echo 'Script ejecutado con éxito', PHP_EOL;
}

register_shutdown_function('shutdown');
?>

    
```php

## Notas

> [!NOTE]
> El directorio de trabajo del script puede cambiar en la función de cierre bajo algunos servidores web, por ejemplo Apache.

> [!NOTE]
> Las funciones de cierre no serán ejecutadas si el proceso es terminado con un señal SIGTERM o SIGKILL. Aunque no se puede interceptar un SIGKILL, se puede usar la función `pcntl_signal` para instalar un manejador para un SIGTERM que utilice la función `exit` para terminar correctamente.

> [!NOTE]
> Las funciones de cierre se ejecutan por separado del tiempo seguido por [max_execution_time](#ini.max-execution-time). Esto significa que incluso si un proceso es terminado por haber funcionado demasiado tiempo, las funciones de cierre serán siempre llamadas. Además, si el `max_execution_time` alcanza su límite mientras una función de cierre está en ejecución, no será interrumpida.

## Véase también

[auto_append_file](#ini.auto-append-file), `exit`, `fastcgi_finish_request`, La sección sobre la [gestión de conexiones](#features.connection-handling)
