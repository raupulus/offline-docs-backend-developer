---
title: Ejemplos
source_url: https://www.php.net/manual/es/pcre.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_revision: 96c9d88ba
order: 61560
---

## Ejemplos

Ejemplos de patrones válidos

- `/<\/\w+>/`

- `|(\d{3})-\d+|Sm`

- `/^(?i)php[34]/`

- `{^\s+(\s+)?$}`

Ejemplos de patrones no válidos

- `/href='(.*)'` - falta el delimitador final

- `/\w+\s*\w+/J` - modificador 'J' desconocido

- `1-\d3-\d3-\d4|` - falta el delimitador inicial
