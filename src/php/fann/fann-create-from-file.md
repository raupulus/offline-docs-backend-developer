---
title: fann_create_from_file
description: Construye una red neuronal de retropropagación desde un fichero de configuración
source_url: https://www.php.net/manual/es/function.fann-create-from-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-from-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 20940
---

fann_create_from_file

Construye una red neuronal de retropropagación desde un fichero de configuración

## Descripción

```php
fann_create_from_file(string $configuration_file): resource
```php

Construye una red neuronal de retropropagación desde un fichero de configuración, el cual ha sido guardado mediante `fann_save`.

## Parámetros

`configuration_file`  
La ruta al fichero de configuración.

## Valores devueltos

Devuelve un `resource` de red neuronal en caso de éxito, o `false` en caso de error.

## Véase también

`fann_save`
