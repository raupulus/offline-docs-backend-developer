---
title: RarEntry::isEncrypted
description: Comprobar si una entrada está cifrada
source_url: https://www.php.net/manual/es/rarentry.isencrypted.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/isencrypted.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68620
---

RarEntry::isEncrypted

Comprobar si una entrada está cifrada

## Descripción

```php
public RarEntry::isEncrypted(): bool
```php

Comprueba si el contenido de la entrada actual está cifrado.

> [!NOTE]
> La contraseña utilizada puede variar entre los archivos dentro del mismo archivo RAR.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la entrada actual se encuentra cifrada y `false` en caso contrario.
