---
title: RarEntry::getCrc
description: Obtener el CRC de la entrada
source_url: https://www.php.net/manual/es/rarentry.getcrc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/getcrc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68520
---

RarEntry::getCrc

Obtener el CRC de la entrada

## Descripción

```php
public RarEntry::getCrc(): string
```php

Devuelve una cadena hexadecimal representación de el CRC del archivo de entrada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el CRC del archivo de entrada o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 2.0.0 | Este método devuelve ahora valores correctos para archivos de varios volúmenes. |
