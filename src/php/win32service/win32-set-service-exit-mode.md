---
title: win32_set_service_exit_mode
description: Define o devuelve el modo de salida para el servicio en ejecución
source_url: https://www.php.net/manual/es/function.win32-set-service-exit-mode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-set-service-exit-mode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 330a38c4d
order: 101440
---

win32_set_service_exit_mode

Define o devuelve el modo de salida para el servicio en ejecución

## Descripción

```php
win32_set_service_exit_mode([bool $gracefulMode]): bool
```php

Si se proporciona el argumento `gracefulMode`, se modifica el modo de salida. Cuando el modo de salida no es correcto, el código de salida utilizado puede ser definido con la función `win32_set_service_exit_code`.

> [!CAUTION]
> Esta función solo funciona en el SAPI "cli". En otros SAPI, esta función está deshabilitada.

## Parámetros

`gracefulMode`  
`true` para la salida correcta. `false` para la salida con error.

## Valores devueltos

Devuelve el modo de salida actual o anterior.

## Errores/Excepciones

Antes de la versión 1.0.0, si esta función se utiliza fuera del SAPI `"cli"`, se emitirá un error `E_ERROR`.

A partir de la versión 1.0.0, lanzará una `Win32ServiceException` si el SAPI no es `"cli"`

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` si un argumento es inválido, antes `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, antes un [Código de error Win32](#win32service.constants.errors) era retornado. |

## Véase también

win32_start_service_ctrl_dispatcher

win32_set_service_status

win32_set_service_exit_code
