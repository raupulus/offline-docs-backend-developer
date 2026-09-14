---
title: La clase RarArchive
source_url: https://www.php.net/manual/es/class.rararchive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_revision: ee741f54f
order: 68490
---

## Introducción

Esta clase representa un archivo RAR que puede estar formado por varios volúmenes (partes) y que contiene una serie de entradas RAR (por ejemplo: archivos, directorios y otros objetos especiales, como enlaces simbólicos).

Los objetos de esta clase puede ser atravesado, dando las entradas almacenadas en el archivo RAR respectivamente. Estas entradas también pueden ser obtenidas mediante RarArchive::getEntry y RarArchive::getEntries.

## Sinopsis de la clase

RarArchive

final

RarArchive

Traversable

Métodos
