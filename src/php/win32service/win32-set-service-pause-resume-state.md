---
title: win32_set_service_pause_resume_state
description: Define o devuelve la capacidad de pausa/reanudación para el servicio
  en ejecución
source_url: https://www.php.net/manual/es/function.win32-set-service-pause-resume-state.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-set-service-pause-resume-state.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101450
---

win32_set_service_pause_resume_state

Define o devuelve la capacidad de pausa/reanudación para el servicio en ejecución

## Descripción

```php
win32_set_service_pause_resume_state([bool $state]): bool
```php

Si se proporciona el argumento `state`, se modifica la capacidad de pausa/reanudación.

> [!CAUTION]
> Esta función solo funciona en el SAPI "cli" y en el contexto de ejecución del servicio de Windows. En otros SAPI, esta función está deshabilitada.

## Parámetros

`state`  
`true` para habilitar la capacidad de pausa/reanudación del servicio. `false` para deshabilitar la capacidad de pausa/reanudación del servicio.

## Valores devueltos

Devuelve el estado actual o anterior de la capacidad de pausa/reanudación.

## Errores/Excepciones

A partir de la versión 1.0.0, si el SAPI no es `"cli"`, esta función emite un error de nivel `E_ERROR`.

Desde la versión 1.0.0, lanzará una `Win32ServiceException` si el SAPI no es `"cli"`

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL win32service 1.0.0 | Lanzará una `ValueError` sobre datos inválidos en los argumentos, anteriormente `false` era retornado. |
| PECL win32service 1.0.0 | Lanzará una `Win32ServiceException` en caso de error, anteriormente un [código de error Win32](#win32service.constants.errors) era retornado. |

## Véase también

win32_start_service_ctrl_dispatcher

win32_set_service_status

win32_set_service_exit_code
