---
title: Stomp::__destruct
description: Cierra una conexión stomp
source_url: https://www.php.net/manual/es/stomp.destruct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/destruct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: 9c7e8795c
order: 87580
---

Stomp::\_\_destruct

stomp_close

Cierra una conexión stomp

## Descripción

Estilo orientado a objetos (destructor):

```php
public Stomp::__destruct()
```php

Estilo procedimental:

```php
stomp_close(resource $link): bool
```

Cierra una conexión previamente abierta.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Vea `stomp_connect`.
