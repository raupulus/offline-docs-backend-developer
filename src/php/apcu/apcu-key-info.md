---
title: apcu_key_info
description: Devuelve información detallada sobre la clave de caché
source_url: https://www.php.net/manual/es/function.apcu-key-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-key-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 184764a63
order: 5080
---

apcu_key_info

Devuelve información detallada sobre la clave de caché

## Descripción

```php
apcu_key_info(string $key): array
```php

Devuelve información detallada sobre la clave de caché.

## Parámetros

`key`  
Nombre de la clave.

## Valores devueltos

Un array que contiene información detallada sobre la clave de caché, o el valor `null` si la clave no existe.

## Ejemplos

Un ejemplo con `apcu_key_info`

```
<?php
apcu_add('a','b');
var_dump(apcu_key_info('a'));
?>

   
```php

El ejemplo anterior mostrará:

    array(7) {
      ["hits"]=>
      int(0)
      ["access_time"]=>
      int(1606701783)
      ["mtime"]=>
      int(1606701783)
      ["creation_time"]=>
      int(1606701783)
      ["deletion_time"]=>
      int(0)
      ["ttl"]=>
      int(0)
      ["refs"]=>
      int(0)
    }

## Véase también

apcu_store

apcu_fetch

apcu_delete
