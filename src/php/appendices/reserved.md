---
title: Palabras reservadas en PHP
source_url: https://www.php.net/manual/es/reserved.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/reserved.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: ff9181ea0
order: 1310
---

## Palabras reservadas en PHP

Este anexo es una lista de identificadores predefinidos en PHP. Ninguno de los identificadores utilizados aquí debe ser reutilizado como nombre de variable o de función en los scripts, salvo que se indique explícitamente lo contrario. Estos identificadores incluyen palabras clave, constantes, clases y variables predefinidas. Estas listas no son completas ni exhaustivas.

## Lista de palabras clave

Estas palabras tienen un significado especial para PHP. Algunas representan objetos similares a funciones, otras a constantes, y así sucesivamente, pero no lo son realmente: son estructuras de lenguaje. Las palabras clave siguientes no pueden ser utilizadas como nombre de constante, de clase o de función. Sin embargo, están permitidas como nombre de propiedad, constante y de método en las clases, interfaces, traits excepto la palabra clave `class` que no debe ser utilizada como nombre de constante.

|  |  |  |  |  |
|----|----|----|----|----|
| `__halt_compiler` | [abstract](#language.oop5.abstract) | [and](#language.operators.logical) | `array` | [as](#control-structures.foreach) |
| [break](#control-structures.break) | [callable](#language.types.callable) | [case](#control-structures.switch) | [catch](#language.exceptions) | [class](#language.oop5.basic.class) |
| [clone](#language.oop5.cloning) | [const](#language.oop5.constants) | [continue](#control-structures.continue) | [declare](#control-structures.declare) | [default](#control-structures.switch) |
| `die` | [do](#control-structures.do.while) | `echo` | [else](#control-structures.else) | [elseif](#control-structures.elseif) |
| `empty` | [enddeclare](#control-structures.declare) | [endfor](#control-structures.alternative-syntax) | [endforeach](#control-structures.alternative-syntax) | [endif](#control-structures.alternative-syntax) |
| [endswitch](#control-structures.alternative-syntax) | [endwhile](#control-structures.alternative-syntax) | `eval` | `exit` | [extends](#language.oop5.basic.extends) |
| [final](#language.oop5.final) | [finally](#language.exceptions) | [fn](#functions.arrow) (disponible a partir de PHP 7.4) | [for](#control-structures.for) | [foreach](#control-structures.foreach) |
| [function](#functions.user-defined) | [global](#language.variables.scope) | [goto](#control-structures.goto) | [if](#control-structures.if) | [implements](#language.oop5.interfaces) |
| `include` | `include_once` | [instanceof](#language.operators.type) | [insteadof](#language.oop5.traits.conflict) | [interface](#language.oop5.interfaces) |
| `isset` | `list` | [match](#control-structures.match) (disponible a partir de PHP 8.0) | [namespace](#language.namespaces) | [new](#language.oop5.basic.new) |
| [or](#language.operators.logical) | `print` | [private](#language.oop5.visibility) | [protected](#language.oop5.visibility) | [public](#language.oop5.visibility) |
| [readonly](#language.oop5.properties.readonly-properties) (disponible a partir de PHP 8.1.0) \* | `require` | `require_once` | `return` | [static](#language.variables.scope) |
| [switch](#control-structures.switch) | [throw](#language.exceptions) | [trait](#language.oop5.traits) | [try](#language.exceptions) | `unset` |
| [use](#language.namespaces.importing) | [var](#language.oop5.properties) | [while](#control-structures.while) | [xor](#language.operators.logical) | [yield](#language.generators) |
| [yield from](#control-structures.yield.from) |  |  |  |  |

Palabras reservadas en PHP

\* `readonly` puede ser utilizado como nombre de función.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| [\_\_CLASS\_\_](#language.constants.magic) | [\_\_DIR\_\_](#language.constants.magic) | [\_\_FILE\_\_](#language.constants.magic) | [\_\_FUNCTION\_\_](#language.constants.magic) | [\_\_LINE\_\_](#language.constants.magic) |  |  |  |
| [\_\_METHOD\_\_](#language.constants.magic) | [\_\_PROPERTY\_\_](#language.constants.magic) | [\_\_NAMESPACE\_\_](#language.namespaces.nsconstants) | [\_\_TRAIT\_\_](#language.constants.magic) |  |  |  |  |

Constantes utilizadas durante la compilación

## Clases predefinidas

Esta sección lista las clases estándar predefinidas. Las otras extensiones que definen otras clases se describen en su referencia.

## Clases estándar

Estas clases están definidas en el conjunto de clases estándar de PHP, incluidas en todas las versiones de PHP.

`Directory`  
Creado por la función `dir`.

`stdClass`  
Una clase vacía genérica creada por [la conversión en objeto](#language.types.object.casting) o el resultado de diversas funciones estándar.

`__PHP_Incomplete_Class`  
Puede ser creado por la función `unserialize`.

`Exception`  

`ErrorException`  

`php_user_filter`  

`Closure`  
La clase predefinida final `Closure` se utiliza para representar las [funciones anónimas](#functions.anonymous).

`Generator`  
La clase final predefinida `Generator` se utiliza para representar los [generadores](#language.generators).

`ArithmeticError`  

`AssertionError`  

`DivisionByZeroError`  

`Error`  

`Throwable`  

`ParseError`  

`TypeError`  

## Clases especiales

Los identificadores siguientes no deberían ser utilizados como nombre de clase debido a su papel particular.

`self`  
[Clase actual](#language.oop5.paamayim-nekudotayim).

`static`  
[Clase actual en el momento de la ejecución](#language.oop5.late-static-bindings).

`parent`  
[Clase padre](#language.oop5.paamayim-nekudotayim).

## Otra lista de palabras reservadas

Las palabras siguientes no pueden ser utilizadas como nombre de clase, de interfaz o de trait. Anteriormente a PHP 8.0, también estaba prohibido utilizarlas en los espacios de nombres.

|  |  |  |  |
|----|----|----|----|
| parent | self | int | float |
| bool | string | true | false |
| null | void (disponible a partir de PHP 7.1) | iterable (disponible a partir de PHP 7.1) | object (disponible a partir de PHP 7.2) |
| mixed (disponible a partir de PHP 8.0) | never (disponible a partir de PHP 8.1) | array (disponible a partir de PHP 8.5) | callable (disponible a partir de PHP 8.5) |

Palabras reservadas

La lista de palabras siguientes presenta una particularidad. Aunque pueden ser utilizadas en los nombres de clase, de interfaz, y de trait, conviene evitar utilizarlas sabiendo que pueden ser utilizadas en las futuras versiones de PHP.

|      |          |         |     |
|------|----------|---------|-----|
| enum | resource | numeric |     |

Palabras reservadas suaves
