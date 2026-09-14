---
title: Creación de archivos Phar
source_url: https://www.php.net/manual/es/phar.creating.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/creating.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 64880
---

## Creación de archivos Phar

## Creación de archivos Phar: Introducción

Para ser escrita completamente en un futuro próximo. Antes de leer esto, asegúrese de leer [Como utilizar archivos PHAR](#phar.using).

Un buen lugar para empezar es leer acerca de `Phar::buildFromIterator`, y los detalles de la elección del [formato de fichero](#phar.fileformat) disponible para los archivos. Una adecuada comprensión de lo que es y hace una rutina de interoperabilidad (stub), es crucial para la creación de un archivo PHAR, así `Phar::setStub` y `Phar::createDefaultStub` son buenos lugares para comenzar. Si va a distribuir una aplicación basada en web es fundamental saber qué es y cómo funciona `Phar::webPhar` y el método relacionado `Phar::mungServer`. Cualquier aplicación que tenga acceso a sus propios ficheros también debe considerar el uso de `Phar::interceptFileFuncs`.
