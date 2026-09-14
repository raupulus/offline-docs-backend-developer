---
title: Filtros de Flujos
source_url: https://www.php.net/manual/es/stream.filters.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/filters.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: a3bb15df3
order: 87770
---

## Filtros de Flujos

Un `filtro` es una pieza final de código que puede realizar operaciones sobre información que está siendo leída o escrita en un flujo. Se puede apilar cualquier número de filtros en un flujo. Los filtros personalizados se pueden definir en un script de PHP usando `stream_filter_register` o en una extensión. Para acceder a la lista de los filtros actualmente registrados, use `stream_get_filters`.
