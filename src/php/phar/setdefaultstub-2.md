---
title: PharData::setDefaultStub
description: Función inútil (Phar::setDefaultStub no es válido para PharData)
source_url: https://www.php.net/manual/es/phardata.setdefaultstub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/setDefaultStub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64650
---

PharData::setDefaultStub

Función inútil (Phar::setDefaultStub no es válido para PharData)

## Descripción

```php
public PharData::setDefaultStub([string $index], [string $webIndex]): bool
```php

Los archivos tar/zip no ejecutables no pueden tener un contenedor de carga, por lo que este método solo genera una excepción.

## Parámetros

`index`  
Ruta relativa dentro del archivo phar a ejecutar en caso de acceso desde la línea de comandos

`webIndex`  
Ruta relativa dentro del archivo phar a ejecutar en caso de acceso desde un navegador

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Genera una excepción `PharException` al llamar al método

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `webIndex` ahora es nullable. |

## Véase también

`Phar::setDefaultStub`
