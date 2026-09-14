---
title: win32_delete_service
description: Elimina una entrada de servicio de la base de datos SCM
source_url: https://www.php.net/manual/es/function.win32-delete-service.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-delete-service.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 95fe2d7de
order: 101330
---

win32_delete_service

Elimina una entrada de servicio de la base de datos SCM

## Descripción

```php
win32_delete_service(string $servicename, [string $machine]): void
```php

Intenta eliminar un servicio de la base de datos SCM. Los privilegios de administrador son necesarios para que esta función tenga éxito.

Esta función solo marca el servicio para eliminación. Si otros procesos (como el Applet Services) están abiertos, entonces la eliminación será pospuesta hasta que estas aplicaciones se cierren. Si un servicio está marcado para eliminación, otros intentos de eliminación fallarán y los intentos de crear un nuevo servicio con ese nombre también fallarán.

## Parámetros

`servicename`  
El nombre corto del servicio.

`machine`  
El nombre opcional de la máquina. Si se omite, se utilizará la máquina local.

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

## Ejemplos

Ejemplo con `win32_delete_service`

Elimina el servicio dummyphp.

```
<?php
win32_delete_service('dummyphp');
?>

    
```php

## Véase también

`win32_create_service`, [Los códigos de error Win32](#win32service.constants.errors)
