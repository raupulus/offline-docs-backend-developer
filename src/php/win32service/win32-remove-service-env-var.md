---
title: win32_remove_service_env_var
description: Elimina una variable de entorno personalizada del servicio
source_url: https://www.php.net/manual/es/function.win32-remove-service-env-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-remove-service-env-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101410
---

win32_remove_service_env_var

Elimina una variable de entorno personalizada del servicio

## Descripción

```php
win32_remove_service_env_var(string $servicename, string $varname): void
```php

Elimina una variable de entorno personalizada `varname` del servicio `servicename`. Esta función solo funciona para la máquina local. Se requieren privilegios administrativos para que esto tenga éxito.

## Parámetros

`servicename`  
El nombre del servicio del que se eliminará la variable de entorno.

`varname`  
El nombre de la variable de entorno.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del argumento `service` está vacío.

Se lanzará una `ValueError` si el valor del argumento `varname` está vacío.

Se lanzará una `Win32ServiceException` en caso de error.

## Véase también

`win32_get_service_env_vars`, `win32_add_service_env_var`
