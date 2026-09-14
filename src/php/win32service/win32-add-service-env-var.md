---
title: win32_add_service_env_var
description: Añade una variable de entorno personalizada al servicio
source_url: https://www.php.net/manual/es/function.win32-add-service-env-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-add-service-env-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101300
---

win32_add_service_env_var

Añade una variable de entorno personalizada al servicio

## Descripción

```php
win32_add_service_env_var(string $servicename, string $varname, string $value): void
```php

Añade una variable de entorno personalizada `varname` al servicio `servicename`. Esta función solo funciona para la máquina local. Se requieren privilegios administrativos para que esto tenga éxito.

## Parámetros

`servicename`  
El nombre del servicio al que se añadirá la variable de entorno.

`varname`  
El nombre de la variable de entorno.

`value`  
El valor de la variable de entorno.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del parámetro `service` está vacío.

Se lanzará una `ValueError` si el valor del parámetro `varname` está vacío.

Se lanzará una `Win32ServiceException` en caso de error.

## Véase también

`win32_get_service_env_vars`, `win32_remove_service_env_var`
