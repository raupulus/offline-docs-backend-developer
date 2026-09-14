---
title: La clase SensitiveParameterValue
source_url: https://www.php.net/manual/es/class.sensitiveparametervalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/sensitiveparametervalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 3890
---

## Introducción

La clase `SensitiveParameterValue` permite envolver valores para protegerlos contra una exposición accidental.

Los valores de los parámetros con el atributo `SensitiveParameter` serán automáticamente envueltos en un objeto `SensitiveParameterValue` en las trazas de pila.

## Sinopsis de la clase

final

SensitiveParameterValue

Propiedades

private

readonly

mixed

value

Métodos

## Propiedades

`value`  
Valor sensible a proteger contra una exposición accidental.
