---
title: La clase parallel\Events\Input
source_url: https://www.php.net/manual/es/class.parallel-events-input.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel.events.input.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60300
---

## Eventos de entrada

Un objeto de entrada es un contenedor para los datos que el objeto `parallel\Events` escribirá en los objetos `parallel\Channel` a medida que se vayan haciendo disponibles. Varios bucles de eventos pueden compartir un contenedor de entrada - parallel no verifica el contenido del contenedor cuando se establece como entrada para un objeto `parallel\Events`.

> [!NOTE]
> Cuando un objeto `parallel\Events` realiza una escritura, el objetivo se retira del objeto de entrada como si parallel\Events\Input::remove fuera llamado.

## Sinopsis de la clase

parallel\Events\Input

final

parallel\Events\Input
