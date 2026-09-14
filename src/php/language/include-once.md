---
title: include_once
source_url: https://www.php.net/manual/es/function.include-once.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/include-once.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 89d80c92a
order: 2190
---

## include_once

La expresión `include_once` incluye y evalúa el fichero especificado durante la ejecución del script. El comportamiento es similar a `include`, pero la diferencia es que si el código ya ha sido incluido, no lo será una segunda vez, y include_once devuelve `true`. Como su nombre indica, el fichero será incluido solo una vez.

La estructura `include_once` se utiliza preferentemente cuando el fichero va a ser incluido o evaluado varias veces en un script, o bien cuando se desea asegurar que solo se incluirá una vez, para evitar redefiniciones de funciones o clases.

Véase la estructura `include` para más detalles sobre su funcionamiento.
