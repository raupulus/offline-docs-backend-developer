---
title: EventBuffer::pullup
description: Serializa los datos del buffer y devuelve el contenido del buffer en
  forma de string
source_url: https://www.php.net/manual/es/eventbuffer.pullup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/pullup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 19270
---

EventBuffer::pullup

Serializa los datos del buffer y devuelve el contenido del buffer en forma de string

## Descripción

```php
public EventBuffer::pullup(int $size): string
```php

Serializa los primeros `size` bytes del buffer, los copia o los mueve según sea necesario para asegurar que sean contiguos y ocupen la misma parte de la memoria. Si el tamaño es negativo, la función lineariza la totalidad del buffer.

> [!WARNING]
> La llamada al método EventBuffer::pullup con un tamaño muy grande ralentiza la ejecución, ya que puede potencialmente necesitar copiar el contenido entero del buffer.

## Parámetros

`size`  
El número de bytes que deben ser contiguos en el buffer.

## Valores devueltos

Si `size` es superior al número de bytes del buffer, la función devolverá `null`. De lo contrario, EventBuffer::pullup devolverá un string.

## Véase también

EventBuffer::copyout

EventBuffer::drain

EventBuffer::read

EventBuffer::readLine

EventBuffer::appendFrom
