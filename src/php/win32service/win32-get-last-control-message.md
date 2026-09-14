---
title: win32_get_last_control_message
description: Devuelve el último mensaje de control que ha sido enviado a este servicio
source_url: https://www.php.net/manual/es/function.win32-get-last-control-message.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-get-last-control-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 4d72f13ea
order: 101340
---

win32_get_last_control_message

Devuelve el último mensaje de control que ha sido enviado a este servicio

## Descripción

```php
win32_get_last_control_message(): int
```php

Devuelve el código de control que ha sido enviado por última vez a este proceso de servicio. Cuando funciona como servicio, debe verificar periódicamente para determinar si el servicio debe ser detenido.

> [!CAUTION]
> Desde la versión 0.2.0, esta función solo funciona en línea de comandos ("cli" SAPI). Está deshabilitada en otros casos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una constante de control que será una de [las constantes de control de mensajes de servicio Win32Service](#win32service.constants.servicecontrol) : `WIN32_SERVICE_CONTROL_CONTINUE`, `WIN32_SERVICE_CONTROL_DEVICEEVENT`, `WIN32_SERVICE_CONTROL_HARDWAREPROFILECHANGE`, `WIN32_SERVICE_CONTROL_INTERROGATE`, `WIN32_SERVICE_CONTROL_NETBINDADD`, `WIN32_SERVICE_CONTROL_NETBINDDISABLE`, `WIN32_SERVICE_CONTROL_NETBINDENABLE`, `WIN32_SERVICE_CONTROL_NETBINDREMOVE`, `WIN32_SERVICE_CONTROL_PARAMCHANGE`, `WIN32_SERVICE_CONTROL_PAUSE`, `WIN32_SERVICE_CONTROL_POWEREVENT`, `WIN32_SERVICE_CONTROL_PRESHUTDOWN`, `WIN32_SERVICE_CONTROL_SESSIONCHANGE`, `WIN32_SERVICE_CONTROL_SHUTDOWN`, `WIN32_SERVICE_CONTROL_STOP`.

Si el valor está entre 128 y 255, el código de control es personalizado.

## Errores/Excepciones

Antes de la versión 1.0.0, si esta función se utiliza fuera del SAPI `"cli"`, se emitirá un error `E_ERROR`.

A partir de la versión 1.0.0, lanzará una `Win32ServiceException` si el SAPI no es `"cli"`

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` si un argumento es inválido, antes `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, antes un [Código de error Win32](#win32service.constants.errors) era retornado. |
| PECL win32service 0.2.0 | Esta función solo funciona en el SAPI `"cli"`. |

## Véase también

`win32_start_service_ctrl_dispatcher`, `win32_set_service_status`, `win32_set_service_exit_mode`, `win32_set_service_exit_code`, [las constantes de control de mensajes de servicio Win32Service](#win32service.constants.servicecontrol)
