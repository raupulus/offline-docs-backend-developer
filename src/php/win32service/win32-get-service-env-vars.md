---
title: win32_get_service_env_vars
description: Lee todas las variables de entorno personalizadas del servicio
source_url: https://www.php.net/manual/es/function.win32-get-service-env-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-get-service-env-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101350
---

win32_get_service_env_vars

Lee todas las variables de entorno personalizadas del servicio

## Descripción

```php
win32_get_service_env_vars(string $servicename): array
```php

Lee todas las variables de entorno personalizadas del servicio `servicename`. Esta función solo funciona para la máquina local. Los privilegios administrativos son necesarios para que esto tenga éxito.

## Parámetros

`servicename`  
El nombre del servicio para leer las variables de entorno.

## Valores devueltos

Devuelve un `array` con el nombre de la variable como clave y el valor de la variable como valor.

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del argumento `service` está vacío.

Se lanzará una `Win32ServiceException` en caso de error.

## Véase también

`win32_add_service_env_var`, `win32_remove_service_env_var`
