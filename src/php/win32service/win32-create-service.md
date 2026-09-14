---
title: win32_create_service
description: Crea una nueva entrada para servicio en la base de datos SCM
source_url: https://www.php.net/manual/es/function.win32-create-service.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-create-service.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101320
---

win32_create_service

Crea una nueva entrada para servicio en la base de datos SCM

## Descripción

```php
win32_create_service(array $details, [string $machine]): void
```php

Intenta añadir un servicio en la base de datos SCM. Se necesitan privilegios de administrador para que esto tenga éxito.

## Parámetros

`details`  
Un array de detalles del servicio:

`service`  
El nombre corto del servicio. Este es el nombre que se utilizará para controlar el servicio utilizando el comando `net`. El servicio debe ser único (dos servicios no pueden compartir el mismo nombre), e idealmente, debería evitar tener espacios en su nombre.

`display`  
El nombre de visualización del servicio. Este es el nombre que se verá en la Applet Servicios.

`description`  
La descripción larga del servicio. Esta es la descripción que se verá en la Applet de Servicios.

`user`  
El nombre de usuario bajo el cual se desea que el servicio se ejecute. Si se omite, el servicio funcionará como LocalSystem. Si se especifica el nombre de usuario, también se debe proporcionar una contraseña.

`password`  
La contraseña que corresponde a `user`.

`path`  
La ruta completa al módulo ejecutable que se iniciará cuando el servicio se inicie. Si se omite, se utilizará la ruta del proceso actual de PHP.

`params`  
Argumentos de comando a pasar al servicio cuando se inicie. Si se desea ejecutar un script PHP como servicio, entonces el primer argumento debería ser la ruta completa al script PHP que se planea ejecutar. Si el nombre del script o la ruta contienen espacios, entonces, rodee la ruta completa del script PHP con `"`

`load_order`  
Controla el load_order. Esto aún no está completamente soportado.

`svc_type`  
Establece el tipo de servicio. Si se omite, el valor por omisión es `WIN32_SERVICE_WIN32_OWN_PROCESS`. No se debe cambiar esto a menos que se sepa realmente lo que se está haciendo.

`start_type`  
Especifica cómo debe iniciarse el servicio. El valor por omisión es `WIN32_SERVIDE_AUTO_START` lo que significa que el servicio se iniciará cuando la máquina se inicie.

`error_control`  
Informa al SCM sobre qué hacer cuando detecte un problema con el servicio. El valor por omisión es `WIN32_SERVER_ERROR_IGNORE`. Cambiar este valor aún no está completamente soportado.

`delayed_start`  
Si `delayed_start` está establecido a `true`, entonces informará al SCM que este servicio debe iniciarse después de los servicios iniciados automáticamente y un cierto retraso.

Cualquier servicio puede ser marcado como un servicio retrasado después del inicio automático; sin embargo, esta configuración no tiene ningún efecto mientras el parámetro `start_type` del servicio valga `WIN32_SERVICE_AUTO_START`.

Esta configuración solo se aplica en Windows Vista y servidores Windows 2008 y posteriores.

`base_priority`  
Para reducir el impacto en el uso del procesador, puede ser necesario establecer una prioridad más baja que la normal.

El parámetro `base_priority` puede ser establecido a una de las constantes definidas en las [clases de baja prioridad Win32](#win32service.constants.basepriorities).

`dependencies`  
Para definir las dependencias del servicio, es necesario establecer este parámetro con la lista de nombres de servicios en un array.

`recovery_delay`  
Este parámetro define el retraso entre el fallo y la ejecución de la acción de recuperación. El valor es en milisegundos.

El valor por omisión es 60000.

`recovery_action_1`  
La acción que se ejecutará en caso de la primera falla. La acción por omisión es `WIN32_SC_ACTION_NONE`.

El parámetro `recovery_action_1` puede ser establecido con una de las constantes definidas en las [Acciones de recuperación Win32](#win32service.constants.recovery-action).

`recovery_action_2`  
La acción que se ejecutará en caso de la segunda falla. La acción por omisión es `WIN32_SC_ACTION_NONE`.

El parámetro `recovery_action_2` puede ser establecido con una de las constantes definidas en las [Acciones de recuperación Win32](#win32service.constants.recovery-action).

`recovery_action_3`  
La acción que se ejecutará en caso de fallas subsiguientes. La acción por omisión es `WIN32_SC_ACTION_NONE`.

El parámetro `recovery_action_3` puede ser establecido con una de las constantes definidas en las [Acciones de recuperación Win32](#win32service.constants.recovery-action).

`recovery_reset_period`  
El contador de fallas se reiniciará después del retraso definido en este parámetro. El retraso se expresa en segundos.

El valor por omisión es `86400`.

`recovery_enabled`  
Establecer este parámetro a `true` para habilitar las opciones de recuperación, y `false` para deshabilitarlas.

El valor por omisión es `false`

`recovery_reboot_msg`  
Añadir este parámetro para definir el mensaje registrado en el registro de eventos de Windows antes del reinicio. Solo se utiliza si una de las acciones está definida a `WIN32_SC_ACTION_REBOOT`.

`recovery_command`  
Añadir este parámetro para definir el comando a ejecutar cuando una acción está definida a `WIN32_SC_ACTION_RUN_COMMAND`.

`machine`  
El nombre opcional de la máquina en la que se desea crear el servicio. Si se omite, se utilizará la máquina local.

## Valores devueltos

No se retorna ningún valor.

Antes de la versión 1.0.0, retornaba `WIN32_NO_ERROR` en caso de éxito, `false` si hay un problema con los parámetros o un [Código de Error Win32](#win32service.constants.errors) en caso de fallo.

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del parámetro `service` está vacío.

Se lanzará una `ValueError` si el valor del parámetro `path` está omitido o vacío.

Se lanzará una `ValueError` si el valor del parámetro `svc_type` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `start_type` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `error_control` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `base_priority` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `recovery_delay` no está entre 0 y PHP_INT_MAX.

Se lanzará una `ValueError` si el valor del parámetro `recovery_action_1` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `recovery_action_2` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `recovery_action_3` es incorrecto.

Se lanzará una `ValueError` si el valor del parámetro `recovery_reset_period` no está entre 0 y PHP_INT_MAX.

Se lanzará una `Win32ServiceException` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Se lanzará una `ValueError` si un parámetro es inválido, antes `false` era devuelto. |
| PECL win32service 1.0.0 | Se lanzará una `Win32ServiceException` en caso de error, antes un [Código de error Win32](#win32service.constants.errors) era devuelto. |
| PECL win32service 1.0.0 | El tipo de retorno ahora es `void`, antes era `mixed`. |
| PECL win32service 0.4.0 | Los parámetros `dependencies`, `recovery_delay`, `recovery_action_1`, `recovery_action_2`, `recovery_action_3`, `recovery_reset_period`, `recovery_enabled`, `recovery_reboot_msg` y `recovery_command` han sido añadidos. |

## Ejemplos

Ejemplo con `win32_create_service`

Crea un servicio cuyo nombre corto es 'dummyphp'.

```
<?php
\$x = win32_create_service(array(
    'service'     => 'dummyphp',                                          // el nombre del servicio
    'display'     => 'ejemplo de servicio PHP ficticio',                  // la descripción corta
    'description' => 'Este es un servicio Windows creado utilizando PHP', // la descripción larga
    'params'      => '"' . __FILE__ . '"  run',                           // ruta al script así como los argumentos
));
debug_zval_dump(\$x);
?>

    
```php

Un ejemplo `win32_create_service` con dependencias

Crea un servicio cuyo nombre corto es 'dummyphp' con dependencias.

```
<?php
\$x = win32_create_service(array(
    'service'      => 'dummyphp',                                                    // El nombre del servicio
    'display'               => 'ejemplo de servicio PHP ficticio',                   // Una descripción corta
    'description'           => 'Este es un servicio Windows creado utilizando PHP.', // Una descripción larga
    'params'                => '"' . __FILE__ . '"  run',                            // ruta al script así como los argumentos
    'dependencies' => array("Netman"),                                               // La lista de dependencias
));
debug_zval_dump(\$x);
?>

     
```php

Ejemplo de `win32_create_service` con opciones de recuperación

Crea un servicio cuyo nombre corto es 'dummyphp' con opciones de recuperación.

```
<?php
\$x = win32_create_service(array(
    'service'               => 'dummyphp',                                           // El nombre del servicio
    'display'               => 'ejemplo de servicio PHP ficticio',                   // Una descripción corta
    'description'           => 'Este es un servicio Windows creado utilizando PHP.', // Una descripción larga
    'params'                => '"' . __FILE__ . '"  run',                            // ruta al script así como los argumentos
    'recovery_delay'        => 120000,                                               // Las acciones de recuperación se ejecutarán después de 2 minutos
    'recovery_action_1'     => WIN32_SC_ACTION_RESTART,                              // Primera falla, reiniciar el servicio
    'recovery_action_2'     => WIN32_SC_ACTION_RUN_COMMAND,                          // Segunda falla, ejecutar un comando
    'recovery_action_3'     => WIN32_SC_ACTION_NONE,                                 // Fallas subsiguientes, no hacer nada
    'recovery_reset_period' => 86400,                                                // Reiniciar el contador de fallas después de 1 día (86400 minutos)
    'recovery_enabled'      => true,                                                 // Habilitar las opciones de recuperación
    'recovery_reboot_msg'   => null,                                                 // No definir un mensaje de reinicio, no es útil.
    'recovery_command'      => "c:\clean-service.bat",                               // Cuando la acción es WIN32_SC_ACTION_RUN_COMMAND, ejecutar este comando.
));
debug_zval_dump(\$x);
?>

     
```php

## Véase también

`win32_delete_service`, [Las clases de baja prioridad Win32](#win32service.constants.basepriorities), [Las acciones de recuperación Win32](#win32service.constants.recovery-action), [Los códigos de error Win32](#win32service.constants.errors)
