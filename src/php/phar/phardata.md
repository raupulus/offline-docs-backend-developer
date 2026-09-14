---
title: La clase PharData
source_url: https://www.php.net/manual/es/class.phardata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 64690
---

## Introducción

La clase PharData proporciona una interfaz de alto nivel para acceder y crear archivos tar y zip no ejecutables. Dado que estos archivos no contienen un contenedor y no pueden ser ejecutados por la extensión phar, es posible crear y manipular archivos zip y tar normales utilizando la clase PharData incluso si el parámetro `phar.readonly` del php.ini está a `1`.

## Sinopsis de la clase

PharData

extends

RecursiveDirectoryIterator

implements

Countable

ArrayAccess

Constantes heredadas

Métodos

Métodos heredados
