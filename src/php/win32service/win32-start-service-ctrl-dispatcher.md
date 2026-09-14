---
title: win32_start_service_ctrl_dispatcher
description: Registra un script con SCM, por lo que puede ser interpretado como un
  servicio con el nombre dado
source_url: https://www.php.net/manual/es/function.win32-start-service-ctrl-dispatcher.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-start-service-ctrl-dispatcher.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 4d72f13ea
order: 101470
---

win32_start_service_ctrl_dispatcher

Registra un script con SCM, por lo que puede ser interpretado como un servicio con el nombre dado

## Descripción

```php
win32_start_service_ctrl_dispatcher(string $name, [bool $gracefulMode]): void
```php

Cuando se ejecuta a través del Gestionador de Control de Servicio, un proceso de servicio debe "registrarse" con él para establecer un servicio de supervisión y comunicación eficiente. Esta función realiza el registro iniciando un hilo para manejar las comunicaciones de bajo nivel con el Gestionador de Control de Servicio.

Una vez iniciado, el proceso del servicio debe hacer dos cosas. La primera es informar al Gestionador de Control de Servicio que el servicio está en ejecución. La segunda es llamar a la función `win32_set_service_status` con la constante `WIN32_SERVICE_RUNNING`. Si necesita lanzar procesos largos antes de que el servicio se inicie, puede usar la constante `WIN32_SERVICE_START_PENDING`. La segunda es continuar verificando con el Gestionador de Control de Servicio para determinar si el servicio se detiene o no. Esto implica llamar periódicamente a la función `win32_get_last_control_message` y tratar el código devuelto.

> [!CAUTION]
> Desde la versión 0.2.0, esta función solo funciona en línea de comandos. Está deshabilitada en otros casos.

## Parámetros

`name`  
El nombre corto del servicio, como se registra con `win32_create_service`.

`gracefulMode`  
`true` para la salida correcta. `false` para la salida con error. Consulte `win32_set_service_exit_mode` para más detalles.

## Valores devueltos

No se retorna ningún valor.

Antes de la versión 1.0.0, retornaba `WIN32_NO_ERROR` en caso de éxito, `false` si hay un problema con los parámetros o un [Código de Error Win32](#win32service.constants.errors) en caso de fallo.

## Errores/Excepciones

Antes de la versión 1.0.0, si esta función se utiliza fuera del SAPI `"cli"`, se emitirá un error `E_ERROR`.

A partir de la versión 1.0.0, lanzará una `Win32ServiceException` si el SAPI no es `"cli"`

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` si un argumento es inválido, anteriormente `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, anteriormente un [Código de error Win32](#win32service.constants.errors) era retornado. |
| PECL win32service 1.0.0 | El tipo de retorno es ahora `void`, anteriormente era `mixed`. |
| PECL win32service 0.4.0 | Se añadió el argumento `gracefulMode`. |
| PECL win32service 0.2.0 | Esta función solo funciona en el SAPI `"cli"`. |

## Ejemplos

Ejemplo con `win32_start_service_ctrl_dispatcher`

Verifica si el servicio funciona bajo SCM.

```
<?php
if (!win32_start_service_ctrl_dispatcher('dummyphp')) {
  die("Probablemente no estoy funcionando bajo el Gestionador de Control de Servicio");
}

win32_set_service_status(WIN32_SERVICE_START_PENDING);

// Algunos procesos largos a recuperar mientras el servicio funciona.

win32_set_service_status(WIN32_SERVICE_RUNNING);

while (WIN32_SERVICE_CONTROL_STOP != win32_get_last_control_message()) {
  # Realice su trabajo aquí.
  # Intente no tomar más de 30 segundos antes de devolver.
}
?>

    
```php

## Véase también

`win32_set_service_status`, `win32_get_last_control_message`, `win32_set_service_exit_mode`, `win32_set_service_exit_code`, Los [códigos de error Win32](#win32service.constants.errors)
