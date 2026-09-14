---
title: win32_query_service_status
description: Consulta el estado de un servicio
source_url: https://www.php.net/manual/es/function.win32-query-service-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-query-service-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 330a38c4d
order: 101370
---

win32_query_service_status

Consulta el estado de un servicio

## Descripción

```php
win32_query_service_status(string $servicename, [string $machine]): array
```php

Consulta el estado actual de un servicio, devolviendo un array de información.

## Parámetros

`servicename`  
El nombre corto del servicio.

`machine`  
El nombre opcional de la máquina. Si se omite, se utilizará la máquina local.

## Valores devueltos

Devuelve un array que contiene la siguiente información en caso de éxito.

Antes de la versión 1.0.0, `false` si hay un problema con los parámetros o un [Código de Error Win32](#win32service.constants.errors) en caso de fallo.

`ServiceType`  
El dwServiceType. Consulte las [máscaras de tipo de servicio Win32Service](#win32service.constants.servicetype).

`CurrentState`  
El dwCurrentState. Consulte las [constantes de estado de los servicios Win32Service](#win32service.constants.servicestatus).

`ControlsAccepted`  
Qué controles de servicio son aceptados por el servicio. Consulte las [máscaras aceptadas para los mensajes de control de servicio Win32Service](#win32service.constants.controlsaccepted).

`Win32ExitCode`  
Si el servicio termina, el código de retorno del proceso. Este valor es igual a `WIN32_ERROR_SERVICE_SPECIFIC_ERROR` si el modo de salida no es correcto. Consulte [códigos de error Win32Service](#win32service.constants.errors) y `win32_set_service_exit_mode`.

`ServiceSpecificExitCode`  
Si el servicio termina con una condición de error, el código específico del servicio que se registrará en el registro de eventos es visible aquí. Este valor es igual al valor definido por `win32_set_service_exit_code`.

`CheckPoint`  
Si el servicio se detiene, mantiene el número actual de punto de control. Esto es utilizado por SCM como una especie de latido para detectar un proceso de servicio detenido. El valor del punto de control se interpreta mejor en conjunción con el valor WaitHint.

`WaitHint`  
Si el servicio se detiene, establecerá un WaitHint a un valor de punto de control que indique la ejecución al 100%. Esto puede ser utilizado para implementar una barra de progreso.

`ProcessId`  
El identificador de proceso de ventana. Si es 0, el proceso no está en ejecución.

`ServiceFlags`  
El dwServiceFlags. Consulte las [constantes utilizadas para las banderas de los servicios Win32Service](#win32service.constants.serviceflag).

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del argumento `servicename` está vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` si un argumento es inválido, antes `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, antes un [Código de error Win32](#win32service.constants.errors) era retornado. |
| PECL win32service 1.0.0 | El tipo de retorno es ahora `array`, antes era `mixed`. |

## Véase también

Las [constantes Win32Service predefinidas](#win32service.constants)
