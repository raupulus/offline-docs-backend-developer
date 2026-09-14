---
title: La enumeración RoundingMode
source_url: https://www.php.net/manual/es/enum.roundingmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/roundingmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: true
translation_revision: aeba24a37
order: 44910
---

## Introducción

La enumeración RoundingMode se utiliza para especificar cómo debe realizarse el redondeo para `round`, `bcround` y BCMath\Number::round.

## Sinopsis del enum

RoundingMode

HalfAwayFromZero

Redondear al integer más cercano. Si la parte decimal es

5

, redondea al integer con el valor absoluto más grande.

HalfTowardsZero

Redondear al integer más cercano. Si la parte decimal es

5

, redondea al integer con el valor absoluto más pequeño.

HalfEven

Redondear al integer más cercano. Si la parte decimal es

5

, redondea al integer par.

HalfOdd

Redondear al integer más cercano. Si la parte decimal es

5

, redondea al integer impar.

TowardsZero

Redondear al integer más cercano con un valor absoluto más pequeño o igual.

AwayFromZero

Redondear al integer más cercano con un valor absoluto más grande o igual.

NegativeInfinity

Redondear al integer más grande más pequeño o igual.

PositiveInfinity

Redondear al integer más pequeño más grande o igual.
