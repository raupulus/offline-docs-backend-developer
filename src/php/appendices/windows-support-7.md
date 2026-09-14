---
title: Soporte para Windows
source_url: https://www.php.net/manual/es/migration85.windows-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration85/windows-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 1260
---

## Soporte para Windows

## Núcleo

Las variables de configuración `PHP_VERSION`, `PHP_MINOR_VERSION` y `PHP_RELEASE_VERSION` ahora siempre son números. Anteriormente, eran strings para las compilaciones de buildconf.

Las compilaciones de `phpize` ahora reflejan el árbol de origen en el directorio de compilación (como ya funcionaba para las compilaciones dentro del árbol); algunas compilaciones de extensión (especialmente cuando se usa Makefile.frag.w32) pueden necesitar ajustes.

Ahora se admite `--enable-sanitizer` para compilaciones de MSVC. Esto habilita ASan y las aserciones de depuración, y es compatible a partir de MSVC 16.10 y Windows 10.

La `--with-uncritical-warn-choke` para las compilaciones de clang ya no es compatible. En su lugar, seleccione las advertencias que desea suprimir mediante CFLAGS.

## COM

Ahora la extensión se compila de forma compartida por defecto; anteriormente se compilaba como una extensión estática por defecto, aunque los binarios oficiales de Windows compilaban una extensión compartida.

## FFI

Ya no es necesario especificar la biblioteca al usar FFI::cdef y FFI::load. Sin embargo, esta funcionalidad no debe utilizarse en producción.

## Streams

Si el array `read` solo contiene pipe streams y los arrays `write` y `except` están vacíos, `stream_select` ahora se comporta de forma similar a los sistemas POSIX; es decir, la función solo retorna si al menos un pipe está listo para leerse o después de que expire el tiempo de espera. Anteriormente, `stream_select` retornaba inmediatamente, indicando que todos los flujos estaban listos para leerse.
