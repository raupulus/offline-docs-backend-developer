---
title: PharData::setAlias
description: Función inútil (Phar::setAlias no es válido para PharData)
source_url: https://www.php.net/manual/es/phardata.setalias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/setAlias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64640
---

PharData::setAlias

Función inútil (Phar::setAlias no es válido para PharData)

## Descripción

```php
public PharData::setAlias(string $alias): bool
```php

Los archivos tar/zip no ejecutables no pueden tener alias, por lo que este método solo genera una excepción.

## Parámetros

`alias`  
Una corta cadena de caracteres a la cual referirse para invocar al archivo mediante el gestor de flujos phar. Este argumento es ignorado.

## Valores devueltos

## Errores/Excepciones

Genera una excepción `PharException` al llamar al método

## Véase también

`Phar::setAlias`
