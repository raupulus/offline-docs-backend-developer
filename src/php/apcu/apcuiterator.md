---
title: La clase APCUIterator
source_url: https://www.php.net/manual/es/class.apcuiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/apcuiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_reviewed: false
translation_revision: 804d8a054
order: 4950
---

## Introducción

La clase `APCUIterator` hace más fácil iterar sobre grandes cachés de APCu. Esto es útil ya que permite iterar sobre grandes cachés en pasos, al mismo tiempo que captura un número definido de entradas por instancia de bloqueo, por lo que libera los bloqueos de caché para otras actividades en lugar de mantener todo el caché para obtener 100 entradas (el valor por defecto). Además, utilizar comparación por expresiones regulares es más eficiente ya que se ha movido al nivel de C.

## Sinopsis de la clase

APCUIterator

APCUIterator

Iterator

Métodos
