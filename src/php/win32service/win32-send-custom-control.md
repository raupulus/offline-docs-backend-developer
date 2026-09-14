---
title: win32_send_custom_control
description: Envía un control personalizado al servicio
source_url: https://www.php.net/manual/es/function.win32-send-custom-control.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-send-custom-control.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101420
---

win32_send_custom_control

Envía un control personalizado al servicio

## Descripción

```php
win32_send_custom_control(string $servicename, int $control, [string $machine]): void
```php

Consulte [Microsoft ControlService function](https://docs.microsoft.com/en-us/windows/desktop/api/winsvc/nf-winsvc-controlservice) para más detalles.

## Parámetros

`servicename`  
El nombre corto del servicio.

`control`  
El valor de control personalizado entre 128 y 255.

`machine`  
Nombre de la máquina opcional. Si se omite, se utilizará la máquina local.

## Valores devueltos

No se retorna ningún valor.

Antes de la versión 1.0.0, retornaba `WIN32_NO_ERROR` en caso de éxito, `false` si hay un problema con los parámetros o un [Código de Error Win32](#win32service.constants.errors) en caso de fallo.

## Errores/Excepciones

Antes de la versión 1.0.0, si el valor de control no está entre 128 y 255, esta función emite un error de nivel `E_ERROR`.

Se lanzará una `ValueError` si el valor del argumento `servicename` está vacío.

Se lanzará una `ValueError` si el valor del argumento `control` no está entre 128 y 255.

Se lanzará una `Win32ServiceException` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` si un argumento es inválido, antes `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, antes un [Código de error Win32](#win32service.constants.errors) era retornado. |
| PECL win32service 1.0.0 | El tipo de retorno es ahora `void`, antes era `mixed`. |

## Véase también

win32_start_service

win32_stop_service

win32_pause_service

win32_continue_service

Códigos de error Win32
