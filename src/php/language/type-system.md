---
title: Sistema de tipos
source_url: https://www.php.net/manual/es/language.types.type-system.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/type-system.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: dfd68fd22
order: 4560
---

## Sistema de tipos

PHP utiliza un sistema de tipos nominal con una fuerte relación de subtipado comportamental. La relación de subtipado se verifica en la compilación, mientras que la verificación de tipos se verifica dinámicamente en el momento de la ejecución.

El sistema de tipos de PHP soporta varios tipos atómicos que pueden ser compuestos juntos para crear tipos más complejos. Algunos de estos tipos pueden ser escritos en forma de [declaración de tipo](#language.types.declarations).

## Tipos atómicos

Algunos tipos atómicos son tipos que están estrechamente integrados en el lenguaje y no pueden ser reproducidos con tipos definidos por el usuario.

La lista de tipos básicos es la siguiente:

- Tipos integrados

  - Tipos escalares:

    - tipo `bool`

    - tipo `int`

    - tipo `float`

    - tipo `string`

  - tipo `array`

  - tipo `object`

  - tipo `resource`

  - tipo `never`

  - tipo `void`

  - [Tipos de clases relativas](#language.types.relative-class-types): `self`, `parent`, y `static`

  - [Tipos singleton](#language.types.singleton)

    - `false`

    - `true`

  - Tipos unitarios

    - `null`

- Tipos definidos por el usuario (generalmente llamados clases-tipos)

  - [Interfaces](#language.oop5.interfaces)

  - [Clases](#language.oop5.basic.class)

  - [Enumeraciones](#language.types.enumerations)

- tipo `callable`

### Tipos escalares

Un valor se considera escalar si es de tipo `int`, `float`, `string` o `bool`.

### Tipos definidos por el usuario

Es posible definir tipos personalizados con [interfaces](#language.oop5.interfaces), [clases](#language.oop5.basic.class) y [enumeraciones](#language.types.enumerations). Estos se consideran tipos definidos por el usuario, o tipos de clase. Por ejemplo, una clase llamada `Elephant` puede ser definida, luego objetos de tipo `Elephant` pueden ser instanciados, y una función puede requerir un argumento de tipo `Elephant`.

## Tipos compuestos

Es posible combinar varios tipos atómicos en tipos compuestos. PHP permite combinar los tipos de la siguiente manera:

- Intersección de clases-tipos (interfaces y nombres de clases).

- Unión de tipos.

### Intersección de tipos

Un tipo de intersección acepta valores que satisfacen varias declaraciones de tipo de clase, en lugar de una sola. Los tipos individuales que forman el tipo de intersección están unidos por el símbolo `&`. Por lo tanto, un tipo de intersección compuesto por los tipos `T`, `U` y `V` se escribe `T&U&V`.

### Tipos de unión

Un tipo de unión acepta valores de varios tipos diferentes, en lugar de uno solo. Los tipos individuales que forman el tipo de unión están unidos por el símbolo `|`. Por lo tanto, un tipo de unión compuesto por los tipos `T`, `U` y `V` se escribe `T|U|V`. Si uno de los tipos es un tipo de intersección, debe ser puesto entre paréntesis para ser escrito en DNF. `T|(X&Y)`.

## Alias de tipo

PHP soporta dos alias de tipo: `mixed` y `iterable` que corresponde al tipo [tipo de unión](#language.types.type-system.composite.union) de `object|resource|array|string|float|int|bool|null` y `Traversable|array` respectivamente.

> [!NOTE]
> PHP no soporta alias de tipo definidos por el usuario.
