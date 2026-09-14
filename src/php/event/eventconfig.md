---
title: La clase EventConfig
source_url: https://www.php.net/manual/es/class.eventconfig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventconfig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19730
---

## Introducción

Representa la estructura de configuración que puede ser utilizada en la construcción de la clase `EventBase`.

## Sinopsis de la clase

EventConfig

final

EventConfig

Constantes

const

int

EventConfig::FEATURE_ET

1

const

int

EventConfig::FEATURE_O1

2

const

int

EventConfig::FEATURE_FDS

4

Métodos

## Constantes predefinidas

`EventConfig::FEATURE_ET`  
Requiere un método del backend que soporte las I/O edge-triggered.

`EventConfig::FEATURE_O1`  
Requiere un método del backend donde añadir o eliminar un solo evento, o tener un solo evento que se vuelve activo.

`EventConfig::FEATURE_FDS`  
Requiere un método del backend que puede soportar tipos de descriptor de fichero arbitrario, y no solo sockets.
