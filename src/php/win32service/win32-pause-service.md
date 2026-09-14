---
title: win32_pause_service
description: Pone en pausa un servicio
source_url: https://www.php.net/manual/es/function.win32-pause-service.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-pause-service.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101360
---

win32_pause_service

Pone en pausa un servicio

## Descripción

```php
win32_pause_service(string $servicename, [string $machine]): void
```php

Pone en pausa un servicio. Se requieren privilegios de administrador o una cuenta con los derechos adecuados definidos en la ACL del servicio.

## Parámetros

`servicename`  
El nombre corto del servicio.

`machine`  
Nombre de la máquina (opcional). Si se omite, se utilizará la máquina local.

## Valores devueltos

No se retorna ningún valor.

Antes de la versión 1.0.0, retornaba `WIN32_NO_ERROR` en caso de éxito, `false` si hay un problema con los parámetros o un [Código de Error Win32](#win32service.constants.errors) en caso de fallo.

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del argumento `servicename` está vacío.

Se lanzará una `Win32ServiceException` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` si un argumento es inválido, antes `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, antes un [Código de error Win32](#win32service.constants.errors) era retornado. |
| PECL win32service 1.0.0 | El tipo de retorno es ahora `void`, antes era `mixed`. |
| PECL win32service 0.3.0 | Esta función ya no requiere una cuenta de administrador si la ACL está definida para otra cuenta. |

## Véase también

`win32_start_service`, `win32_stop_service`, `win32_continue_service`, `win32_send_custom_control`, Los [códigos de error Win32](#win32service.constants.errors)
