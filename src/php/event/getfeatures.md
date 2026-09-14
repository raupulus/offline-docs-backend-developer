---
title: EventBase::getFeatures
description: Devuelve una máscara de las funcionalidades soportadas
source_url: https://www.php.net/manual/es/eventbase.getfeatures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/getfeatures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19050
---

EventBase::getFeatures

Devuelve una máscara de las funcionalidades soportadas

## Descripción

```php
public EventBase::getFeatures(): int
```php

Devuelve una máscara de las funcionalidades soportadas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un entero que representa una máscara de las funcionalidades soportadas. Consulte las constantes [EventConfig::FEATURE\_\*](#eventconfig.constants).

## Ejemplos

Ejemplo con `EventBase::getFeatures`

```
<?php
// Desactivación del método "select"
$cfg = new EventConfig();
if ($cfg->avoidMethod("select")) {
    echo "Desactivación del método 'select'\n";
}

$base = new EventBase($cfg);

echo "funcionalidades:\n";
$features = $base->getFeatures();
($features & EventConfig::FEATURE_ET) and print "ET - edge-triggered IO\n";
($features & EventConfig::FEATURE_O1) and print "O1 - O(1) operation for adding/deleting events\n";
($features & EventConfig::FEATURE_FDS) and print "FDS - arbitrary file descriptor types, and not just sockets\n";
?>

   
```php

## Véase también

EventBase::getMethod

EventConfig
