---
title: La clase IntlIterator
source_url: https://www.php.net/manual/es/class.intliterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intliterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 41460
---

## Introducción

Esta clase representa objetos iteradores a través de la extensión intl cada vez que el iterador no puede ser identificado con otro objeto proporcionado por la extensión. El objeto de iterador distinto utilizado en interno por la [`foreach` ](#control-structures.foreach) solo puede ser obtenido (en la parte pertinente aquí) desde objetos, por lo que los objetos de esta clase sirven para proporcionar el gancho mediante el cual este objeto interno puede ser obtenido. Por conveniencia, esta clase también implementa la interfaz `Iterator`, permitiendo que la colección de valores sea recorridos utilizando los métodos definidos en esta interfaz. Estos métodos y los objetos de iterador internos proporcionados a `foreach` son soportados por el mismo estado (por ejemplo, la posición del iterador y su valor actual).

Las subclases pueden proporcionar una funcionalidad más rica.

## Sinopsis de la clase

IntlIterator

implements

Iterator

Métodos
