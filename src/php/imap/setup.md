---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/imap.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38700
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere la biblioteca C cliente. Descargue la última versión en <https://github.com/uw-imap/imap> y compílela.

Es importante no copiar los ficheros fuente IMAP directamente en el directorio de inclusión del sistema para evitar conflictos. En lugar de esto, cree un nuevo directorio en el directorio de inclusión del sistema, como `/usr/local/imap-2000b/` (la ruta y el nombre dependen de su configuración y de su versión de IMAP) y en este nuevo directorio, cree los directorios nombrados `lib/` y `include/`. Desde el directorio `c-client` de las fuentes IMAP, copie todos los ficheros `*.h` en el directorio `include/` y todos los ficheros `*.c` en el directorio `lib/`. Adicionalmente, cuando se compila IMAP, se crea un fichero nombrado `c-client.a`. Póngalo también en el directorio `lib/` pero renómbrelo a `libc-client.a`.

> [!NOTE]
> Para compilar la biblioteca C cliente con SSL y/o con soporte Kerberos, lea la documentación proporcionada en la distribución.

> [!NOTE]
> En Mandrake Linux, la biblioteca IMAP (`libc-client.a`) se compila sin soporte Kerberos. Una versión separada con SSL (`client-PHP4.a`) se instala. La biblioteca debe ser recompilada para añadir soporte Kerberos.

## Tipos de recursos

Anterior a PHP 8.1.0, esta extensión utilizaba un tipo de recurso `imap` devuelto por `imap_open` que hace referencia a un flujo IMAP abierto.
