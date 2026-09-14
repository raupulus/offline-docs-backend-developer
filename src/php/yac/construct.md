---
title: Yac::__construct
description: Constructor
source_url: https://www.php.net/manual/es/yac.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/yac/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: 74155fb94
order: 104300
---

Yac::\_\_construct

Constructor

## Descripción

```php
public Yac::__construct([string $prefix])
```php

se utiliza un prefijo para preparar las claves, esto podría utilizarse para evitar conflictos entre aplicaciones.

## Parámetros

`prefix`  
Prefijo `string`

## Errores/Excepciones

Lanza una `Exception` si Yac no está habilitado. Lanza `Exception` si `prefix` excede la longitud máxima de clave de 48 (`YAC_MAX_KEY_LEN`) bytes.
