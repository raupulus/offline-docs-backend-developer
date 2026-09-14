---
title: yaz_wait
description: Espera que las peticiones Z39.50 se completeten
source_url: https://www.php.net/manual/es/function.yaz-wait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-wait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107980
---

yaz_wait

Espera que las peticiones Z39.50 se completeten

## Descripción

```php
yaz_wait([array $options]): mixed
```php

Esta función lleva a cabo en red (bloqueada) la actividad para la solicitudes pendientes que han sido preparados por las funciones `yaz_connect`, `yaz_search`, `yaz_present`, `yaz_scan` y `yaz_itemorder`.

`yaz_wait` devuelve cuando todos los servidores han completado todas las solicitudes o abortado (en caso de error).

## Parámetros

`options`  
Un array asociativo de opciones:

`timeout`  
Establece el tiempo de espera en segundos. Si un servidor no ha respondido en el tiempo de espera se considera muerto y retorna `yaz_wait`. El valor por omisión de tiempo de espera es de 15 segundos.

`event`  
Un boolean.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. En modo evento, retorna un recurso o `false` si ocurre un error.
