---
title: opcache_get_configuration
description: Recupera la información de configuración del caché
source_url: https://www.php.net/manual/es/function.opcache-get-configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-get-configuration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 87d6bb1bb
order: 58580
---

opcache_get_configuration

Recupera la información de configuración del caché

## Descripción

```php
opcache_get_configuration(): array
```php

Esta función devuelve la información de configuración de la instancia del caché.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de información, incluyendo ini, lista negra y versión.

## Errores/Excepciones

Si `opcache.restrict_api` es utilizado y la ruta de acceso actual viola las reglas, se emitirá una advertencia de nivel E_WARNING; no se devolverá ninguna información de estado.

## Véase también

opcache_get_status
