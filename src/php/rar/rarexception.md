---
title: La clase RarException
source_url: https://www.php.net/manual/es/class.rarexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68670
---

## Introducción

Esta clase sirve para dos propósitos: estas son el tipo de las excepciones lanzadas por la extensión RAR funciones y métodos y esto permite, a través de métodos estáticos consultar y definir el error y el comportamiento de la extensión, por ejemplo, si las excepciones son lanzadas o solamente se emiten advertencias.

Los códigos de error que se utilizan los siguientes:

- -1 - error fuera de biblioteca UnRAR

- 11 - memoria insuficiente

- 12 - datos dañados

- 13 - archivo dañado

- 14 - formato desconocido

- 15 - error de apertura de archivo

- 16 - error al crear archivo

- 17 - error al cerrar archivo

- 18 - error de lectura

- 19 - error de escritura

- 20 - búfer demasiado pequeño

- 21 - error RAR desconocido

- 22 - contraseña requerida pero no especificada

## Sinopsis de la clase

RarException

final

RarException

extends

Exception

Métodos

Métodos heredados
