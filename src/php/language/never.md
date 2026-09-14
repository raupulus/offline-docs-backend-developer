---
title: Never
source_url: https://www.php.net/manual/es/language.types.never.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/never.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 161dde4fe
order: 4470
---

## Never

`never` es únicamente un tipo de retorno que indica que la función no se termina. Esto significa que llama a `exit`, lanza una excepción, o es un bucle infinito. Por lo tanto, no puede formar parte de una declaración de [type union](#language.types.type-system.composite.union) Disponible a partir de PHP 8.1.0.

`never` es, en el lenguaje de la teoría de tipos, el tipo vacío. Esto significa que es el subtipo de todos los otros tipos y que puede reemplazar cualquier otro tipo de retorno durante la herencia.
