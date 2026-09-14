---
title: Win32Service\RightInfo::getDomain
description: Devuelve el dominio del usuario
source_url: https://www.php.net/manual/es/win32service-rightinfo.get-domain.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/rightinfo/get-domain.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 77485af08
order: 101510
---

Win32Service\RightInfo::getDomain

Devuelve el dominio del usuario

## Descripción

```php
final public Win32Service\RightInfo::getDomain(): string
```php

Devuelve el dominio del usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de dominio o `null` si no se encuentra ningún dominio (cuenta local o fallo en la resolución del GUID del usuario).

## Véase también

Win32Service\RightInfo::\_\_construct

Win32Service\RightInfo::getRights

Win32Service\RightInfo::isGrantAccess

Win32Service\RightInfo::isDenyAccess

Win32Service\RightInfo::getFullUsername

Win32Service\RightInfo::getUsername
