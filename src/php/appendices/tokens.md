---
title: Lista de tokens del analizador
source_url: https://www.php.net/manual/es/tokens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/tokens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 5f720ab2b
order: 1330
---

## Lista de tokens del analizador

Diversas partes del lenguaje PHP son representadas internamente por tokens. Un fragmento de código que contiene una secuencia inválida de tokens puede llevar a errores tales como `Parse error: syntax error, unexpected token "==", expecting "(" in script.php on line 10."` donde el token `==` es representado internamente por `T_IS_EQUAL`.

La siguiente tabla lista todos los tokens. También están disponibles como constantes PHP.

> [!NOTE]
> Los valores de las constantes T\_\* son generados automáticamente en función de la infraestructura subyacente del analizador PHP. Esto significa que el valor concreto de un token puede cambiar entre dos versiones de PHP. Esto significa que su código nunca debe utilizar el valor literal de las constantes T\_\* de una versión PHP X.Y.Z, para proporcionar cierta compatibilidad entre varias versiones de PHP.
>
> Para utilizar las constantes T\_\* a través de varias versiones de PHP, las constantes indefinidas pueden ser definidas por el usuario (utilizando números grandes como `10000`) con una estrategia apropiada que funcione con las dos versiones de PHP y los valores de T\_\*.
>
> ```
> <?php
> // Anterior a PHP 7.4.0, T_FN no está definida.
> defined('T_FN') || define('T_FN', 10001);
> ?>
>
>    
> ```

| Token | Sintaxis | Referencia |
|----|----|----|
| `T_ABSTRACT` (`int`) | abstract | [???](#language.oop5.abstract) |
| `T_AMPERSAND_FOLLOWED_BY_VAR_OR_VARARG` (`int`) | & | [???](#language.types.declarations) (disponible a partir de PHP 8.1.0) |
| `T_AMPERSAND_NOT_FOLLOWED_BY_VAR_OR_VARARG` (`int`) | & | [???](#language.types.declarations) (disponible a partir de PHP 8.1.0) |
| `T_AND_EQUAL` (`int`) | &= | [operadores de asignación](#language.operators.assignment) |
| `T_ARRAY` (`int`) | array() | `array`, [sintaxis de array](#language.types.array.syntax) |
| `T_ARRAY_CAST` (`int`) | (array) | [conversión de tipos](#language.types.typecasting) |
| `T_AS` (`int`) | as | [`foreach`](#control-structures.foreach) |
| `T_ATTRIBUTE` (`int`) | \#\[ | [atributos](#language.attributes) (disponible a partir de PHP 8.0.0) |
| `T_BAD_CHARACTER` (`int`) |  | Todos los caracteres por debajo de ASCII 32 excepto \t (0x09), \n (0x0a) y \r (0x0d) (disponible a partir de PHP 7.4.0) |
| `T_BOOLEAN_AND` (`int`) | && | [operadores lógicos](#language.operators.logical) |
| `T_BOOLEAN_OR` (`int`) | \|\| | [operadores lógicos](#language.operators.logical) |
| `T_BOOL_CAST` (`int`) | (bool) o (boolean) | [conversión de tipos](#language.types.typecasting) |
| `T_BREAK` (`int`) | break; | [break](#control-structures.break) |
| `T_CALLABLE` (`int`) | callable | [callable](#language.types.callable) |
| `T_CASE` (`int`) | case | [switch](#control-structures.switch) |
| `T_CATCH` (`int`) | catch | [???](#language.exceptions) |
| `T_CLASS` (`int`) | class | [clases y objetos](#language.oop5) |
| `T_CLASS_C` (`int`) | \_\_CLASS\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_CLONE` (`int`) | clone | [clases y objetos](#language.oop5) |
| `T_CLOSE_TAG` (`int`) | ?\> or %\> | [escapar desde el HTML](#language.basic-syntax.phpmode) |
| `T_COALESCE` (`int`) | ?? | [operadores de comparación](#language.operators.comparison.coalesce) |
| `T_COALESCE_EQUAL` (`int`) | ??= | [operadores de asignación](#language.operators.assignment) (disponible a partir de PHP 7.4.0) |
| `T_COMMENT` (`int`) | // o \#, y /\* \*/ | [comentarios](#language.basic-syntax.comments) |
| `T_CONCAT_EQUAL` (`int`) | .= | [operadores de asignación](#language.operators.assignment) |
| `T_CONST` (`int`) | const | [constantes de clase](#language.constants) |
| `T_CONSTANT_ENCAPSED_STRING` (`int`) | "foo" o 'bar' | [sintaxis de string](#language.types.string.syntax) |
| `T_CONTINUE` (`int`) | continue | [continue](#control-structures.continue) |
| `T_CURLY_OPEN` (`int`) | {\$ | sintaxis de interpolación de strings de variables [avanzada](#language.types.string.parsing.advanced) |
| `T_DEC` (`int`) | -- | [operadores de incremento/decremento](#language.operators.increment) |
| `T_DECLARE` (`int`) | declare | [declare](#control-structures.declare) |
| `T_DEFAULT` (`int`) | default | [switch](#control-structures.switch) |
| `T_DIR` (`int`) | \_\_DIR\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_DIV_EQUAL` (`int`) | /= | [operadores de asignación](#language.operators.assignment) |
| `T_DNUMBER` (`int`) | 0.12, etc. | [números de coma flotante](#language.types.float) |
| `T_DO` (`int`) | do | [do..while](#control-structures.do.while) |
| `T_DOC_COMMENT` (`int`) | /\*\* \*/ | [estilo de comentario en la PHPDoc](#language.basic-syntax.comments) |
| `T_DOLLAR_OPEN_CURLY_BRACES` (`int`) | \${ | interpolación de string de variables de [base](#language.types.string.parsing.basic) |
| `T_DOUBLE_ARROW` (`int`) | =\> | [sintaxis de array](#language.types.array.syntax) |
| `T_DOUBLE_CAST` (`int`) | (real), (double) o (float) | [conversión de tipos](#language.types.typecasting) |
| `T_DOUBLE_COLON` (`int`) | :: | Véase `T_PAAMAYIM_NEKUDOTAYIM` más abajo |
| `T_ECHO` (`int`) | echo | `echo` |
| `T_ELLIPSIS` (`int`) | ... | [los argumentos de función](#functions.variable-arg-list) |
| `T_ELSE` (`int`) | else | [else](#control-structures.else) |
| `T_ELSEIF` (`int`) | elseif | [elseif](#control-structures.elseif) |
| `T_EMPTY` (`int`) | empty | `empty` |
| `T_ENCAPSED_AND_WHITESPACE` (`int`) | " \$a" | [parte de las constantes de un `string` que contiene variables](#language.types.string.parsing) |
| `T_ENDDECLARE` (`int`) | enddeclare | [declare](#control-structures.declare), [sintaxis alternativa](#control-structures.alternative-syntax) |
| `T_ENDFOR` (`int`) | endfor | [for](#control-structures.for), [sintaxis alternativa](#control-structures.alternative-syntax) |
| `T_ENDFOREACH` (`int`) | endforeach | [`foreach`](#control-structures.foreach), [sintaxis alternativa](#control-structures.alternative-syntax) |
| `T_ENDIF` (`int`) | endif | [if](#control-structures.if), [sintaxis alternativa](#control-structures.alternative-syntax) |
| `T_ENDSWITCH` (`int`) | endswitch | [switch](#control-structures.switch), [sintaxis alternativa](#control-structures.alternative-syntax) |
| `T_ENDWHILE` (`int`) | endwhile | [while](#control-structures.while), [sintaxis alternativa](#control-structures.alternative-syntax) |
| `T_ENUM` (`int`) | enum | [Enumeraciones](#language.types.enumerations) (disponible a partir de PHP 8.1.0) |
| `T_END_HEREDOC` (`int`) |  | [sintaxis heredoc](#language.types.string.syntax.heredoc) |
| `T_EVAL` (`int`) | eval() | `eval` |
| `T_EXIT` (`int`) | exit o die | `exit`, `die` |
| `T_EXTENDS` (`int`) | extends | [extends](#language.oop5.basic.extends), [clases y objetos](#language.oop5) |
| `T_FILE` (`int`) | \_\_FILE\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_FINAL` (`int`) | final | [???](#language.oop5.final) |
| `T_FINALLY` (`int`) | finally | [???](#language.exceptions) |
| `T_FN` (`int`) | fn | [funciones flecha](#functions.arrow) (disponible a partir de PHP 7.4.0) |
| `T_FOR` (`int`) | for | [for](#control-structures.for) |
| `T_FOREACH` (`int`) | foreach | [`foreach`](#control-structures.foreach) |
| `T_FUNCTION` (`int`) | function | [funciones](#language.functions) |
| `T_FUNC_C` (`int`) | \_\_FUNCTION\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_GLOBAL` (`int`) | global | [ámbito de variable](#language.variables.scope) |
| `T_GOTO` (`int`) | goto | [goto](#control-structures.goto) |
| `T_HALT_COMPILER` (`int`) | \_\_halt_compiler() | [???](#function.halt-compiler) |
| `T_IF` (`int`) | if | [if](#control-structures.if) |
| `T_IMPLEMENTS` (`int`) | implements | [???](#language.oop5.interfaces) |
| `T_INC` (`int`) | ++ | [operadores de incremento/decremento](#language.operators.increment) |
| `T_INCLUDE` (`int`) | include | `include` |
| `T_INCLUDE_ONCE` (`int`) | include_once | `include_once` |
| `T_INLINE_HTML` (`int`) |  | [texto fuera de PHP](#language.basic-syntax.phpmode) |
| `T_INSTANCEOF` (`int`) | instanceof | [operadores de tipo](#language.operators.type) |
| `T_INSTEADOF` (`int`) | insteadof | [???](#language.oop5.traits) |
| `T_INTERFACE` (`int`) | interface | [???](#language.oop5.interfaces) |
| `T_INT_CAST` (`int`) | (int) o (integer) | [conversión de tipos](#language.types.typecasting) |
| `T_ISSET` (`int`) | isset() | `isset` |
| `T_IS_EQUAL` (`int`) | == | [operadores de comparación](#language.operators.comparison) |
| `T_IS_GREATER_OR_EQUAL` (`int`) | \>= | [operadores de comparación](#language.operators.comparison) |
| `T_IS_IDENTICAL` (`int`) | === | [operadores de comparación](#language.operators.comparison) |
| `T_IS_NOT_EQUAL` (`int`) | != o \<\> | [operadores de comparación](#language.operators.comparison) |
| `T_IS_NOT_IDENTICAL` (`int`) | !== | [operadores de comparación](#language.operators.comparison) |
| `T_IS_SMALLER_OR_EQUAL` (`int`) | \<= | [operadores de comparación](#language.operators.comparison) |
| `T_LINE` (`int`) | \_\_LINE\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_LIST` (`int`) | list() | `list` |
| `T_LNUMBER` (`int`) | 123, 012, 0x1ac, etc. | [enteros](#language.types.integer) |
| `T_LOGICAL_AND` (`int`) | and | [operadores lógicos](#language.operators.logical) |
| `T_LOGICAL_OR` (`int`) | or | [operadores lógicos](#language.operators.logical) |
| `T_LOGICAL_XOR` (`int`) | xor | [operadores lógicos](#language.operators.logical) |
| `T_MATCH` (`int`) | match | [match](#control-structures.match) (disponible a partir de PHP 8.0.0) |
| `T_METHOD_C` (`int`) | \_\_METHOD\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_MINUS_EQUAL` (`int`) | -= | [operadores de asignación](#language.operators.assignment) |
| `T_MOD_EQUAL` (`int`) | %= | [operadores de asignación](#language.operators.assignment) |
| `T_MUL_EQUAL` (`int`) | \*= | [operadores de asignación](#language.operators.assignment) |
| `T_NAMESPACE` (`int`) | namespace | [espacios de nombres](#language.namespaces) |
| `T_NAME_FULLY_QUALIFIED` (`int`) | \App\Namespace | [espacios de nombres](#language.namespaces) (disponible a partir de PHP 8.0.0) |
| `T_NAME_QUALIFIED` (`int`) | App\Namespace | [namespaces](#language.namespaces) (disponible a partir de PHP 8.0.0) |
| `T_NAME_RELATIVE` (`int`) | namespace\Namespace | [namespaces](#language.namespaces) (disponible a partir de PHP 8.0.0) |
| `T_NEW` (`int`) | new | [clases y objetos](#language.oop5) |
| `T_NS_C` (`int`) | \_\_NAMESPACE\_\_ | [espacios de nombres](#language.namespaces) |
| `T_NS_SEPARATOR` (`int`) | \\ | [espacios de nombres](#language.namespaces) |
| `T_NUM_STRING` (`int`) | "\$a\[0\]" | [índice de un array numérico que se encuentra en un `string`](#language.types.string.parsing) |
| `T_OBJECT_CAST` (`int`) | (object) | [conversión de tipos](#language.types.typecasting) |
| `T_OBJECT_OPERATOR` (`int`) | -\> | [clases y objetos](#language.oop5) |
| `T_NULLSAFE_OBJECT_OPERATOR` (`int`) | ?-\> | [clases y objetos](#language.oop5) |
| `T_OPEN_TAG` (`int`) | \<?php, \<? or \<% | [salida del modo HTML](#language.basic-syntax.phpmode) |
| `T_OPEN_TAG_WITH_ECHO` (`int`) | \<?= or \<%= | [salida del modo HTML](#language.basic-syntax.phpmode) |
| `T_OR_EQUAL` (`int`) | \|= | [operadores de asignación](#language.operators.assignment) |
| `T_PAAMAYIM_NEKUDOTAYIM` (`int`) | :: | [resolución de ámbito](#language.oop5.paamayim-nekudotayim). Definido también como `T_DOUBLE_COLON`. |
| `T_PIPE` | \|\> | [operadores funcionales](#language.operators.functional) (disponible a partir de PHP 8.5.0) |
| `T_PLUS_EQUAL` (`int`) | += | [operadores de asignación](#language.operators.assignment) |
| `T_POW` (`int`) | \*\* | [los operadores aritméticos](#language.operators.arithmetic) |
| `T_POW_EQUAL` (`int`) | \*\*= | [los operadores de asignación](#language.operators.assignment) |
| `T_PRINT` (`int`) | print | `print` |
| `T_PRIVATE` (`int`) | private | [clases y objetos](#language.oop5) |
| `T_PRIVATE_SET` (`int`) | privado(set) | hooks de propiedad (disponible a partir de PHP 8.4.0) |
| `T_PROPERTY_C` (`int`) | \_\_PROPERTY\_\_ | [constantes mágicas](#language.constants.magic) |
| `T_PROTECTED` (`int`) | protected | [clases y objetos](#language.oop5) |
| `T_PROTECTED_SET` (`int`) | protegido(set) | hooks de propiedad (disponible a partir de PHP 8.4.0) |
| `T_PUBLIC` (`int`) | public | [clases y objetos](#language.oop5) |
| `T_PUBLIC_SET` (`int`) | public(set) | hooks de propiedad (disponible a partir de PHP 8.4.0) |
| `T_READONLY` (`int`) | readonly | [clases y objetos](#language.oop5) (disponible a partir de PHP 8.1.0) |
| `T_REQUIRE` (`int`) | require | `require` |
| `T_REQUIRE_ONCE` (`int`) | require_once | `require_once` |
| `T_RETURN` (`int`) | return | [valores devueltos](#functions.returning-values) |
| `T_SL` (`int`) | \<\< | [operadores a nivel de bits](#language.operators.bitwise) |
| `T_SL_EQUAL` (`int`) | \<\<= | [operadores de asignación](#language.operators.assignment) |
| `T_SPACESHIP` (`int`) | \<=\> | [operadores de comparación](#language.operators.comparison) |
| `T_SR` (`int`) | \>\> | [operadores a nivel de bits](#language.operators.bitwise) |
| `T_SR_EQUAL` (`int`) | \>\>= | [operadores de asignación](#language.operators.assignment) |
| `T_START_HEREDOC` (`int`) | \<\<\< | [sintaxis heredoc](#language.types.string.syntax.heredoc) |
| `T_STATIC` (`int`) | static | [ámbito de variable](#language.variables.scope) |
| `T_STRING` (`int`) | parent, self, etc. | identificadores, e.g. palabras clave como `parent` y `self`, nombres de funciones, clases y otros, correspondientes. Véase también `T_CONSTANT_ENCAPSED_STRING`. |
| `T_STRING_CAST` (`int`) | (string) | [conversión de tipos](#language.types.typecasting) |
| `T_STRING_VARNAME` (`int`) | "\${a | [variables flexibles](#language.variables.variable) a interpolar en un string |
| `T_SWITCH` (`int`) | switch | [switch](#control-structures.switch) |
| `T_THROW` (`int`) | throw | [???](#language.exceptions) |
| `T_TRAIT` (`int`) | trait | [???](#language.oop5.traits) |
| `T_TRAIT_C` (`int`) | \_\_TRAIT\_\_ | `__TRAIT__` |
| `T_TRY` (`int`) | try | [???](#language.exceptions) |
| `T_UNSET` (`int`) | unset() | `unset` |
| `T_UNSET_CAST` (`int`) | (unset) | [conversión de tipos](#language.types.typecasting) |
| `T_USE` (`int`) | use | [namespaces](#language.namespaces) |
| `T_VAR` (`int`) | var | [clases y objetos](#language.oop5) |
| `T_VARIABLE` (`int`) | \$foo | [variables](#language.variables) |
| `T_VOID_CAST` | (void) | [conversión void](#language.types.void) (disponible a partir de PHP 8.5.0) |
| `T_WHILE` (`int`) | while | [while](#control-structures.while), [do...while](#control-structures.do.while) |
| `T_WHITESPACE` (`int`) | \t \r\n |  |
| `T_XOR_EQUAL` (`int`) | ^= | [operadores de asignación](#language.operators.assignment) |
| `T_YIELD` (`int`) | yield | [generadores](#control-structures.yield) |
| `T_YIELD_FROM` (`int`) | yield from | [generadores](#control-structures.yield.from) |

Tokens

Véase también `token_name`.
