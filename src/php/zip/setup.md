---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/zip.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108130
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere [libzip](https://libzip.org/). La versión 1.1.2 estaba incluida en PHP hasta la versión 7.3.

La versión mínima soportada es 0.11, pero se recomienda encarecidamente una versión superior.

Versión 1.2 requerida para soporte de encriptación, ver ZipArchive::setEncryptionIndex, Versión 1.3 requerida para soporte de progreso, ver ZipArchive::registerProgressCallback, Versión 1.6 requerida para soporte de cancelación, ver ZipArchive::registerCancelCallback

## Tipos de recursos

Existen dos tipos de recursos usados en el módulo Zip. El primero es el directorio Zip para el fichero Zip, el segundo la entrada Zip para la entrada de archivos.
