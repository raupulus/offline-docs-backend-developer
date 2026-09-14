---
title: ZipArchive::setEncryptionIndex
description: Establece el método de cifrado de una entrada definida por su índice
source_url: https://www.php.net/manual/es/ziparchive.setencryptionindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setencryptionindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108530
---

ZipArchive::setEncryptionIndex

Establece el método de cifrado de una entrada definida por su índice

## Descripción

```php
public #[\SensitiveParameter] ZipArchive::setEncryptionIndex(int $index, int $method, [string $password]): bool
```php

Establece el método de cifrado de una entrada definida por su índice.

## Parámetros

`index`  
Índice de la entrada.

`method`  
El método de cifrado definido por una de las constantes ZipArchive::EM\_.

`password`  
Contraseña opcional, se utiliza por defecto cuando falta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `password` ahora es anulable. |

## Notas

> [!NOTE]
> Esta función sólo está disponible si se construye con libzip ≥ 1.2.0.

## Véase también

ZipArchive::setPassword, ZipArchive::setEncryptionName
