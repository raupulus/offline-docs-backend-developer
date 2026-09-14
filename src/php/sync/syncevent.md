---
title: La clase SyncEvent
source_url: https://www.php.net/manual/es/class.syncevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93560
---

## Introducción

Una implementación multiplataforma nativa de objetos de eventos nombrados o sin nombre. Se soportan tanto los objetos de eventos automáticos como manuales.

Un objeto de evento espera, sin cola, que los objetos sean lanzados/definidos. Una instancia espera en el objeto de evento mientras otra lanza/define el evento. Los objetos de eventos son útiles a lo largo de un proceso largo (i.e. verificar si una descarga de datos debe ser analizada).

## Sinopsis de la clase

SyncEvent

SyncEvent

Métodos
