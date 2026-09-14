---
title: EventConfig::requireFeatures
description: Ingresa una funcionalidad de método de evento solicitada por la aplicación
source_url: https://www.php.net/manual/es/eventconfig.requirefeatures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventconfig/requirefeatures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: ac397fd0d
order: 19700
---

EventConfig::requireFeatures

Ingresa una funcionalidad de método de evento solicitada por la aplicación

## Descripción

```php
public EventConfig::requireFeatures(int $feature): bool
```php

Ingresa una funcionalidad de método de evento solicitada por la aplicación.

## Parámetros

`feature`  
Máscara de funcionalidades solicitadas. Ver las constantes [`EventConfig::FEATURE_*`](#eventconfig.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventConfig::requireFeatures`

```
<?php
$cfg = new EventConfig();

// Crea un event_base asociado con la configuración
$base = new EventBase($cfg);

// Solicitud de la funcionalidad FDS
if ($cfg->requireFeatures(EventConfig::FEATURE_FDS)) {
    echo "funcionalidad FDS solicitada\n";

    $base = new EventBase($cfg);
    ($base->getFeatures() & EventConfig::FEATURE_FDS)
        and print "FDS - tipos arbitrarios de descriptor de fichero y no solo sockets\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    funcionalidad FDS solicitada
    FDS - tipos arbitrarios de descriptor de fichero y no solo sockets

## Véase también

EventBase::getFeatures
