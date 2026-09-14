---
title: La clase IteratorIterator
source_url: https://www.php.net/manual/es/class.iteratoriterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/iteratoriterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 82490
---

## Introducción

Esta envoltura de iteradores permite la conversión de todo aquello que es [Traversable](#class.traversable) a un iterador. Es importante comprender que la mayoría de las clases que no implementan iteradores, lo más probable es que no permitan todas las características del iterador. Si es así, deberían proporcionarse técnicas para evitar un uso indebido, de lo contrario se pueden esperar excepciones o errores fatales.

## Sinopsis de la clase

IteratorIterator

implements

OuterIterator

Métodos

## Notas

> [!NOTE]
> Esta clase permite el acceso a métodos del iterador interno mediante el método mágico \_\_call.
