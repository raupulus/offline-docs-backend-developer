---
title: require
source_url: https://www.php.net/manual/es/function.require.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/require.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 30c0106d5
order: 2230
---

## require

`require` es idéntico a `include` excepto por el hecho de que cuando ocurre un error, produce también una excepción `Error` (error de nivel `E_COMPILE_ERROR` antes de PHP 8.0.0), mientras que `include` solo producirá una advertencia (error de nivel `E_WARNING`).

Consulte la documentación de la instrucción `include` para conocer su funcionamiento.
