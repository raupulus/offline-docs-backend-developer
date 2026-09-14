---
title: Swoole\Buffer::substr
description: Lee los datos del búfer de memoria en función del desplazamiento y la
  longitud. O elimina los datos del búfer de memoria.
source_url: https://www.php.net/manual/es/swoole-buffer.substr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/buffer/substr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 90880
---

Swoole\Buffer::substr

Lee los datos del búfer de memoria en función del desplazamiento y la longitud. O elimina los datos del búfer de memoria.

## Descripción

```php
public Swoole\Buffer::substr(int $offset, [int $length], [bool $remove]): string
```php

Si \$remove está definido como true y \$offset está definido como 0, los datos serán eliminados del búfer. La memoria para almacenar los datos será liberada cuando el objeto búfer sea destruido.

## Parámetros

`offset`  
El desplazamiento.

`length`  
La longitud.

`remove`  
Si los datos deben ser eliminados del búfer.

## Valores devueltos

Los datos leídos del búfer de memoria.
