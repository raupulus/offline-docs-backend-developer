---
title: fann_save
description: Guarda la red completa a un fichero de configuración
source_url: https://www.php.net/manual/es/function.fann-save.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-save.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21710
---

fann_save

Guarda la red completa a un fichero de configuración

## Descripción

```php
fann_save(resource $ann, string $configuration_file): bool
```php

Guarda la red completa a un fichero de configuración.

El fichero de configuración contiene toda la información sobre la red neuronal y habilita a `fann_create_from_file` para crear una copia exacta de la red neuronal y de todos los parámetros asociados a dicha red.

Estos tres parámetros (`fann_set_callback`, `fann_set_error_log`, `fann_set_user_data`) NO se guardan en el fichero porque no se pueden llevar a una ubicación diferente de forma segura. Tampoco se guardan los parámetros temporales generados durante el entrenamiento, como `fann_get_MSE`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`configuration_file`  
La ruta al fichero de configuración.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_create_from_file`
