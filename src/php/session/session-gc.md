---
title: session_gc
description: Ejecuta la recolección de basura de los datos de sesión
source_url: https://www.php.net/manual/es/function.session-gc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-gc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 372350f3b
order: 73790
---

session_gc

Ejecuta la recolección de basura de los datos de sesión

## Descripción

```php
session_gc(): int
```php

Por omisión, PHP utiliza [session.gc_probability](#ini.session.gc-probability) para ejecutar el recolector de basura de sesión de forma probabilística en cada solicitud. Este enfoque presenta algunas limitaciones:

Es posible que sitios con poco tráfico no eliminen sus datos de sesión dentro del plazo preferido.

Sitios con mucho tráfico pueden hacer que el recolector de basura funcione con demasiada frecuencia, realizando trabajo extra innecesario.

La recolección de basura se realiza a petición del usuario, y este puede experimentar una demora.

Para sistemas de producción, se recomienda deshabilitar la recolección de basura basada en probabilidad configurando [session.gc_probability](#ini.session.gc-probability) en `0` y activar explícitamente el recolector de basura periódicamente, por ejemplo, utilizando "cron" en sistemas tipo UNIX para ejecutar un script que llame a `session_gc`.

> [!NOTE]
> Al llamar a `session_gc` desde un script PHP de línea de comandos, [session.save_path](#ini.session.save-path) debe tener el mismo valor que las solicitudes web, y el script debe tener permisos de acceso y eliminación para los archivos de sesión. Esto puede verse afectado por el usuario con el que se ejecuta el script y por características de contenedor o aislamiento, como la opción `PrivateTmp=` de systemd.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`session_gc` devuelve el número de datos de sesión eliminados en caso de éxito, o `false` si ocurre un error.

> [!NOTE]
> Los antiguos gestores de almacenamiento de sesiones no devuelven el número de entradas de sesión eliminadas, sino solo un indicador de éxito/fracaso. En este caso, se devuelve `1` independientemente de cuántas entradas de sesión se hayan eliminado realmente.

## Ejemplos

Ejemplo de `session_gc` para planificadores de tareas como cron

```
<?php
// Nota: Este script debe ser ejecutado por el mismo usuario que el proceso del servidor web.

// Requiere la activación de las sesiones para inicializar el acceso al gestor de almacenamiento de sesiones
session_start();

// Ejecutar la recolección de basura inmediatamente
session_gc();

// Eliminar el ID de sesión creado por session_start()
session_destroy();
?>

   
```php

Ejemplo de `session_gc` para scripts accesibles por el usuario

```
<?php
// Nota: Se recomienda que session_gc() sea utilizado por un planificador de tareas,
// pero puede ser utilizado de la siguiente manera.

// Utilizado para verificar la hora del último uso de la recolección de basura
$gc_time = '/tmp/php_session_last_gc';
$gc_period = 1800;

session_start();
// Ejecutar la recolección de basura solo cuando haya transcurrido el período.
// Es decir, llamar a session_gc() en cada solicitud es un desperdicio de recursos.
if (file_exists($gc_time)) {
    if (filemtime($gc_time) < time() - $gc_period) {
        session_gc();
        touch($gc_time);
    }
} else {
    touch($gc_time);
}
?>

   
```php

## Véase también

session_start

session_destroy

session.gc_probability
