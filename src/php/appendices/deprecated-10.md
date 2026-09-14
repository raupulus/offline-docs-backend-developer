---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration83.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration83/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 4de6272a1
order: 1010
---

## Funcionalidades obsoletas

## Núcleo de PHP

### Operadores de incremento/decremento más seguros

El uso del operador de [incremento](#language.operators.increment) (`++`) en cadenas vacías, no numéricas o no alfanuméricas está ahora depreciado. Además, la incrementación de cadenas no numéricas está fuertemente depreciada. Esto significa que ningún diagnóstico `E_DEPRECATED` se emite, pero esta funcionalidad no debe usarse para producir nuevo código. La nueva función `str_increment` debe usarse en su lugar.

El uso del operador de [decremento](#language.operators.increment) (`--`) en cadenas vacías, no numéricas o no alfanuméricas está ahora depreciado.

### get_class()/get_parent_class() llamadas sin argumentos

Llamar a `get_class` y `get_parent_class` sin argumentos está ahora depreciado.

## DBA

Llamar a `dba_fetch` con `dba` como tercer argumento está ahora depreciado.

## FFI

Llamar a FFI::cast, FFI::new, y FFI::type de manera estática está ahora depreciado.

## Intl

Las constantes `U_MULTIPLE_SEPARATOR_SEPARATORS` han sido depreciadas, se recomienda usar la constante `U_MULTIPLE_SEPARATOR_SEPARATORS` en su lugar.

La constante `NumberFormatter::TYPE_CURRENCY` ha sido depreciada.

## LDAP

Llamar a `ldap_connect` con `hostname` y `port` separados está depreciado.

## MBString

Pasar un `width` negativo a `mb_strimwidth` está ahora depreciado.

## Phar

Llamar a Phar::setStub con un `resource` y un `length` está ahora depreciado. Estas llamadas deben ser reemplazadas por: `$phar->setStub(stream_get_contents($resource));`

## Random

La variante MT19937 `MT_RAND_PHP` está depreciada.

## Reflection

Llamar a ReflectionProperty::setValue con solo un parámetro está depreciado. Para definir propiedades estáticas, pasar `null` como primer parámetro.

## Estándar

La función `assert_options` está ahora depreciada.

Las constantes `ASSERT_ACTIVE`, `ASSERT_BAIL`, `ASSERT_CALLBACK`, `ASSERT_EXCEPTION`, y `ASSERT_WARNING` están ahora depreciadas.

Las directivas INI `assert.*` han sido depreciadas. Ver la página [Cambios en la gestión del fichero INI](#migration83.other-changes.ini) para más detalles.

## SQLite3

El uso de excepciones está ahora desaconsejado, y las advertencias serán eliminadas en el futuro. Llamar a `SQLite3::enableExceptions(false)` suprimirá una advertencia de depreciación en esta versión.

## Zip

La constante `ZipArchive::FL_RECOMPRESS` está depreciada y será eliminada en una versión futura de libzip.
