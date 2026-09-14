---
title: parallel\Events::setBlocking
description: Comportamiento
source_url: https://www.php.net/manual/es/parallel-events.setblocking.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/events/setblocking.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60070
---

parallel\Events::setBlocking

Comportamiento

## Descripción

Por omisión, cuando un evento es interrogado, se produce un bloqueo (a nivel de PHP) hasta que el primer evento pueda ser devuelto: Definir el modo de bloqueo a `false` hará que la interrogación devuelva el control si la primera cible interrogada no está lista.

Esto difiere de definir un tiempo límite de 0 con parallel\Events::setTimeout, ya que un tiempo límite de 0, aunque permitido, provocará que se lance una excepción, lo cual puede ser extremadamente lento o derrochador si lo que realmente se desea es un comportamiento no bloqueante.

Un bucle no bloqueante afecta el valor de retorno de parallel\Events::poll, de modo que puede ser `null` antes de que todos los eventos hayan sido procesados.

```php
public parallel\Events::setBlocking(bool $blocking): void
```php

Define el modo de bloqueo.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Events\Error` si el bucle tiene un tiempo límite definido.
