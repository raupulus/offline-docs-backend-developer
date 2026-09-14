---
title: Portar módulos de extensión a Python 3
source_url: https://docs.python.org/es/3
source_path: howto/cporting.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: howto
order: 1190
---

# Portar módulos de extensión a Python 3

Recomendamos los siguientes recursos para portar módulos de
extensiones a Python 3:

* El capítulo Migrating C extensions de *Support Python 3: An in-depth
  guide*, un libro sobre migrar de Python 2 a Python 3 en general,
  guía al lector a través cómo portar un módulo de extensión.

* La Porting guide de el proyecto *py3c* provee sugerencias dogmáticas
  con código de ejemplo.

* Recommended third party tools offer abstractions over the Python's C
  API. Extensions generally need to be re-written to use one of them,
  but the library then handles differences between various Python
  versions and implementations.
