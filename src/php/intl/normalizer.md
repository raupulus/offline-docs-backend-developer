---
title: La clase Normalizer
source_url: https://www.php.net/manual/es/class.normalizer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/normalizer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1f68eecaa
order: 42180
---

## Introducción

La normalización es un proceso que implica la transformación de caracteres y de secuencias de caracteres en una representación formal. Este proceso es importante cuando los textos deben ser comparados con fines de ordenación y búsqueda, pero también es importante para el almacenamiento de datos, a fin de que los documentos sean coherentes.

El consorcio Unicode Consortium ha definido un número de formas de normalización para reflejar las diferentes necesidades de las aplicaciones: Forma de normalización D (NFD): descomposición canónica, Forma de normalización C (NFC): descomposición canónica, seguida de una composición canónica, Forma de normalización KD (NFKD): descomposición compatible, Forma de normalización KC (NFKC): descomposición compatible seguida de una composición canónica Las diferentes formas se definen en términos de transformaciones de texto, transformaciones que se expresan con algoritmos y archivos de datos.

## Sinopsis de la clase

Normalizer

Constantes

public

const

int

Normalizer::FORM_D

public

const

int

Normalizer::NFD

public

const

int

Normalizer::FORM_KD

public

const

int

Normalizer::NFKD

public

const

int

Normalizer::FORM_C

public

const

int

Normalizer::NFC

public

const

int

Normalizer::FORM_KC

public

const

int

Normalizer::NFKC

public

const

int

Normalizer::FORM_KC_CF

public

const

int

Normalizer::NFKC_CF

Métodos

## Véase también

[ Normalización Unicode ](http://unicode.org/reports/tr15/), [ Preguntas frecuentes sobre la normalización Unicode ](http://unicode.org/faq/normalization.html), [ Guía del usuario de ICU: Normalización ](https://unicode-org.github.io/icu/userguide/transforms/normalization/), [ Referencia de la API de ICU: Normalización ](https://unicode-org.github.io/icu-docs/apidoc/dev/icu4c/unorm_8h.html)

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
| 8.0.0   | `Normalizer::NONE` ha sido eliminado.        |
