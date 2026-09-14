---
title: Win32Service\RightInfo::getRights
description: Devuelve la lista de derechos
source_url: https://www.php.net/manual/es/win32service-rightinfo.get-rights.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/rightinfo/get-rights.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 48783163f
order: 101530
---

Win32Service\RightInfo::getRights

Devuelve la lista de derechos

## Descripción

```php
final public Win32Service\RightInfo::getRights(): array
```php

Devuelve la lista de derechos del usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la lista de derechos del usuario.

El array indexado es la máscara de bits del derecho representado por las [constantes de permisos](#win32service.constants.rights).

El valor es una cadena con el nombre de la constante de Windows (sin el prefijo `WIN32_`).

## Véase también

Win32Service\RightInfo::\_\_construct

Win32Service\RightInfo::isGrantAccess

Win32Service\RightInfo::isDenyAccess

Win32Service\RightInfo::getFullUsername

Win32Service\RightInfo::getUsername

Win32Service\RightInfo::getDomain

Constantes de permisos Win32
