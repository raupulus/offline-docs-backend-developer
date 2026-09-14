---
title: La clase Locale
source_url: https://www.php.net/manual/es/class.locale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1f68eecaa
order: 42020
---

## Introducción

Una "Locale" es un identificador utilizado para representar los comportamientos regionales de una API. Las locales de PHP están organizadas e identificadas de la misma manera que los CLDR de ICU (y que muchos otros editores de sistemas Unix, tales como Mac, Java, etc.). Las locales se identifican por los etiquetados de lenguaje de la RFC 4646 (que utiliza guiones y no subrayados) además de la notación tradicional con subrayados. Salvo indicación contraria, las funciones de esta clase son capaces de utilizar las dos notaciones.

Ejemplos de identificadores: en-US (Inglés, EE.UU.), zh-Hant-TW (Chino, tradicional, Taiwán), fr-CA, fr-FR (Francés para Canadá y Francia, respectivamente)

La clase `Locale` y los métodos asociados, son utilizados para interactuar con los identificadores locales: para verificar que un identificador está bien formado, válido, etc. Las extensiones utilizadas por CDR en UAX \#35 y heredadas por ICU son válidas, y utilizadas siempre que sea posible en ICU.

Las locales no pueden ser instanciadas. Todas son funciones estáticas.

La cadena `null` o vacía permite obtener la locale raíz. La raíz es el equivalente de `"en_US_POSIX"` en CLDR. Los etiquetados de lenguaje (y por lo tanto, los identificadores) no son sensibles a mayúsculas/minúsculas. Existe una función de canonalización que permite obtener la especificación exacta.

## Sinopsis de la clase

Locale

Constantes

public

const

int

Locale::ACTUAL_LOCALE

public

const

int

Locale::VALID_LOCALE

public

const

null

Locale::DEFAULT_LOCALE

null

public

const

string

Locale::LANG_TAG

public

const

string

Locale::EXTLANG_TAG

public

const

string

Locale::SCRIPT_TAG

public

const

string

Locale::REGION_TAG

public

const

string

Locale::VARIANT_TAG

public

const

string

Locale::GRANDFATHERED_LANG_TAG

public

const

string

Locale::PRIVATE_TAG

Métodos

## Véase también

[RFC 4646 : etiquetados para identificar los idiomas](https://datatracker.ietf.org/doc/html/rfc4646), [RFC 4647 : Coincidencia de etiquetados de idiomas](https://datatracker.ietf.org/doc/html/rfc4647), [Proyecto Unicode CLDR: Repositorio Común de Datos de Localización](http://www.unicode.org/cldr/), [Registro de subtags de idiomas de IANA](http://www.iana.org/assignments/language-subtag-registry), [Guía del usuario de ICU: Locale](https://unicode-org.github.io/icu/userguide/locale/), [API de Locale de ICU](https://unicode-org.github.io/icu-docs/apidoc/dev/icu4c/uloc_8h.html)

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
