---
title: EventConfig::__construct
description: Construye un objeto EventConfig
source_url: https://www.php.net/manual/es/eventconfig.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventconfig/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: b621ab27a
order: 19690
---

EventConfig::\_\_construct

Construye un objeto EventConfig

## Descripción

```php
public EventConfig::__construct()
```php

Construye un objeto EventConfig que podrá ser pasado al constructor EventBase::\_\_construct.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo con `EventConfig::__construct`

```
<?php
// Se ignora el método "select"
$cfg = new EventConfig();
if ($cfg->avoidMethod("select")) {
    echo "Método 'select' ignorado\n";
}

// Crea un event_base asociado con la configuración
$base = new EventBase($cfg);

/* Ahora, $base está configurado para ignorar el método select */
?>

   
```php

## Véase también

EventBase::\_\_construct
