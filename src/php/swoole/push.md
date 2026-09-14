---
title: Swoole\Channel::push
description: Escribe y empuja datos en el canal Swoole.
source_url: https://www.php.net/manual/es/swoole-channel.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/channel/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 90940
---

Swoole\Channel::push

Escribe y empuja datos en el canal Swoole.

## Descripción

```php
public Swoole\Channel::push(string $data): bool
```php

Los datos pueden ser cualquier variable PHP no vacía, la variable será serializada si no es de tipo string.

Si el tamaño de los datos es superior a 8 Ko, el canal swoole utilizará un almacenamiento de ficheros temporales.

La función devolverá true si la operación de escritura es exitosa, o devolverá false si no hay suficiente espacio.

## Parámetros

`data`  
Los datos a empujar en el canal Swoole.

## Valores devueltos

Si los datos son empujados en el canal Swoole.
