---
title: posix_sysconf
description: Devuelve información sobre el sistema en ejecución
source_url: https://www.php.net/manual/es/function.posix-sysconf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-sysconf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: ccebf5c8b
order: 65470
---

posix_sysconf

Devuelve información sobre el sistema en ejecución

## Descripción

```php
posix_sysconf(int $conf_id): int
```php

Devuelve información sobre el sistema en ejecución.

## Parámetros

`conf_id`  
El identificador de la variable con las constantes siguientes: `POSIX_SC_ARG_MAX`, `POSIX_SC_PAGESIZE`, `POSIX_SC_NPROCESSORS_CONF`, `POSIX_SC_NPROCESSORS_ONLN`, `POSIX_SC_CHILD_MAX`, `POSIX_SC_CLK_TCK`

## Valores devueltos

Devuelve el valor numérico asociado a `conf_id`

## Ejemplos

Ejemplo de `posix_sysconf`

Devuelve el número de procesadores activos.

```
<?php
echo posix_sysconf(POSIX_SC_NPROCESSORS_ONLN);
?>

   
```php

El ejemplo anterior mostrará:

    2
