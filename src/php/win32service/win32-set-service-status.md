---
title: win32_set_service_status
description: Actualiza el estado de un servicio
source_url: https://www.php.net/manual/es/function.win32-set-service-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-set-service-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 055685822
order: 101460
---

win32_set_service_status

Actualiza el estado de un servicio

## Descripción

```php
win32_set_service_status(int $status, [int $checkpoint]): void
```php

Informa al SCM del estado actual de un servicio en ejecución. Esta llamada solo es válida para un proceso de servicio en ejecución.

> [!CAUTION]
> Desde la versión 0.2.0, esta función solo funciona en línea de comandos ("cli" SAPI). Está deshabilitada en otros casos.

## Parámetros

`status`  
El código de estado del servicio, uno de `WIN32_SERVICE_RUNNING`, `WIN32_SERVICE_STOPPED`, `WIN32_SERVICE_STOP_PENDING`, `WIN32_SERVICE_START_PENDING`, `WIN32_SERVICE_CONTINUE_PENDING`, `WIN32_SERVICE_PAUSE_PENDING`, `WIN32_SERVICE_PAUSED`.

`checkpoint`  
Este valor será incrementado periódicamente por el servicio para reportar su progreso durante las operaciones de inicio, detención, pausa o reanudación. Por ejemplo, el servicio incrementará este valor cuando haya completado cada paso de su inicialización durante el inicio.

`checkpoint` solo es válido cuando `status` es una de las siguientes constantes: `WIN32_SERVICE_STOP_PENDING`, `WIN32_SERVICE_START_PENDING`, `WIN32_SERVICE_CONTINUE_PENDING` o `WIN32_SERVICE_PAUSE_PENDING`.

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
| PECL win32service 0.2.0 | Esta función solo funciona en el SAPI `"cli"`. |

## Véase también

`win32_start_service_ctrl_dispatcher`, `win32_get_last_control_message`, `win32_set_service_exit_mode`, `win32_set_service_exit_code`, Las [constantes de estado de los servicios Win32Service](#win32service.constants.servicestatus)
