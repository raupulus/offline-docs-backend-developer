---
title: La clase BcMath\Number
source_url: https://www.php.net/manual/es/class.bcmath-number.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath.number.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: 3f82c5450
order: 6200
---

## Introducción

Una clase para un número de precisión arbitraria. Estos objetos soportan los operadores [aritméticos](#language.operators.arithmetic) y [de comparación](#language.operators.comparison).

> [!NOTE]
> Esta clase no se ve afectada por la directiva INI [bcmath.scale](#ini.bcmath.scale) definida en el `php.ini`.

> [!NOTE]
> El comportamiento de un operador sobrecargado es el mismo que especificar `null` para el argumento `scale` en el método correspondiente.

## Sinopsis de la clase

BcMath

final

readonly

Number

implements

Stringable

Propiedades

public

string

value

public

int

scale

Métodos

## Propiedades

`value`  
Una representación en string de un número de precisión arbitraria.

`scale`  
El valor de la escala actualmente definida en el objeto. Para los objetos resultantes de cálculos, este valor se calcula y define automáticamente, a menos que el argumento `scale` haya sido definido en el método de cálculo.
