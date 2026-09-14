---
title: win32_read_right_access_service
description: Lee los derechos de acceso al servicio para un usuario
source_url: https://www.php.net/manual/es/function.win32-read-right-access-service.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/functions/win32-read-right-access-service.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 3738e1b83
order: 101390
---

win32_read_right_access_service

Lee los derechos de acceso al servicio para un usuario

## Descripción

```php
win32_read_right_access_service(string $servicename, string $username, [string $machine]): Win32Service\RightInfo
```php

Lee los derechos de acceso para `username` en el servicio `servicename`. Se requieren privilegios administrativos para que esto tenga éxito.

## Parámetros

`servicename`  
El nombre del servicio para leer los derechos de acceso.

`username`  
Lee los derechos de acceso para `username`

`machine`  
El nombre opcional de la máquina en la que se desea crear un servicio. Si se omite, se utilizará la máquina local.

## Valores devueltos

Devuelve un objeto `Win32Service\RightInfo`.

## Errores/Excepciones

Se lanzará una `ValueError` si el valor del argumento `service` está vacío.

Se lanzará una `ValueError` si el valor del argumento `username` está vacío.

Se lanzará una `Win32ServiceException` en caso de error.

## Véase también

`win32_read_all_rights_access_service`, `win32_add_right_access_service`, `win32_remove_right_access_service`, [Constantes de permisos Win32](#win32service.constants.rights)
