---
title: EvEmbed::sweep
description: Barre, una sola vez y de forma no bloqueante, el bucle interno
source_url: https://www.php.net/manual/es/evembed.sweep.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evembed/sweep.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18040
---

EvEmbed::sweep

Barre, una sola vez y de forma no bloqueante, el bucle interno

## Descripción

```php
public EvEmbed::sweep(): void
```php

Barre, una sola vez y de forma no bloqueante, el bucle interno. Funciona de la misma manera que lo siguiente, pero de una forma más apropiada para los bucles internos:

```
<?php
$other->start(Ev::RUN_NOWAIT);
?>

   
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EvWatcher::start
