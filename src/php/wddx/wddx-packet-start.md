---
title: wddx_packet_start
description: Inicia un nuevo paquete WDDX con una estructura dentro de él
source_url: https://www.php.net/manual/es/function.wddx-packet-start.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/functions/wddx-packet-start.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: e41806c30
order: 101230
---

wddx_packet_start

Inicia un nuevo paquete WDDX con una estructura dentro de él

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.4.0.

## Descripción

```php
wddx_packet_start([string $comment]): resource
```php

Inicia un nuevo paquete WDDX para la adición incremental de variables. Automáticamente crea una definición de estructura en el paquete, para alojar variables.

## Parámetros

`comment`  
Un `string` opcional que contiene el comentario.

## Valores devueltos

Devuelve un identificador de paquete para su uso posterior con las funciones WDDX, o `false` si ocurre un error.
