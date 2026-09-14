---
title: Win32Service\RightInfo::getFullUsername
description: Devuelve el dominio y el nombre de usuario
source_url: https://www.php.net/manual/es/win32service-rightinfo.get-full-username.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/rightinfo/get-full-username.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 911fe79de
order: 101520
---

Win32Service\RightInfo::getFullUsername

Devuelve el dominio y el nombre de usuario

## Descripción

```php
final public Win32Service\RightInfo::getFullUsername(): string
```php

Devuelve el dominio y el nombre de usuario separados por una barra invertida `\`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el dominio y el nombre de usuario. Si el dominio es `null`, devuelve solo el nombre de usuario; devuelve `null` si no se encuentra ningún nombre de usuario.

## Véase también

Win32Service\RightInfo::\_\_construct

Win32Service\RightInfo::getRights

Win32Service\RightInfo::isGrantAccess

Win32Service\RightInfo::isDenyAccess

Win32Service\RightInfo::getUsername
