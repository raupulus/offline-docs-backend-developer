---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/intl.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 39530
---

## Constantes predefinidas

`INTL_ICU_DATA_VERSION` (`string`)  
Versión de los datos en ICU4C.

`INTL_ICU_VERSION` (`string`)  
La versión actual de la biblioteca ICU como una cadena decimal separada con puntos.

`INTL_MAX_LOCALE_LEN` (`int`)  
Limita el tamaño de la configuración local, por defecto a 80 en PHP. Los nombres de configuraciones locales más grandes que este tamaño serán prohibidos.

`IDNA_DEFAULT` (`int`)  
Prohíbe el tratamiento de los codepoints no asignados en la entrada para las funciones IDN y no verifica si la entrada es conforme a las reglas de nombres de dominio ASCII.

`IDNA_ALLOW_UNASSIGNED` (`int`)  
Permite el tratamiento de los codepoints no asignados en la entrada para las funciones IDN.

`IDNA_USE_STD3_RULES` (`int`)  
Verifica si la entrada para las funciones IDN es conforme a las reglas de nombres de dominio ASCII.

`IDNA_CHECK_BIDI` (`int`)  
Verifica si la entrada es conforme a las reglas BiDi. Ignorado por la implementación IDNA2003, que siempre realiza esta verificación.

`IDNA_CHECK_CONTEXTJ` (`int`)  
Verifica si la entrada es conforme a las reglas CONTEXTJ. Ignorado por la implementación IDNA2003, ya que esta verificación es nueva en IDNA2008.

`IDNA_NONTRANSITIONAL_TO_ASCII` (`int`)  
Opción para una ejecución no transicional en la función `idn_to_ascii`. La ejecución transicional está activada por defecto. Esta opción es ignorada por la implementación IDNA2003.

`IDNA_NONTRANSITIONAL_TO_UNICODE` (`int`)  
Opción para una ejecución no transicional en la función `idn_to_utf8`. La ejecución transicional está activada por defecto. Esta opción es ignorada por la implementación IDNA2003.

`INTL_IDNA_VARIANT_2003` (`int`)  
Utiliza el algoritmo IDNA 2003 en la función `idn_to_utf8` así como en la función `idn_to_ascii`. Este es el comportamiento por defecto. Esta constante y el uso por defecto han sido depreciados a partir de la versión PHP 7.2.0.

`INTL_IDNA_VARIANT_UTS46` (`int`)  
Utiliza el algoritmo UTS \#46 en la función `idn_to_utf8` así como en la función `idn_to_ascii`. Disponible a partir de ICU 4.6.

`GRAPHEME_EXTR_COUNT` (`int`)  
El número de graphemas por defecto a extraer.

`GRAPHEME_EXTR_MAXBYTES` (`int`)  
El número máximo de bytes devueltos.

`GRAPHEME_EXTR_MAXCHARS` (`int`)  
El número máximo de caracteres UTF-8 devueltos.

<!-- -->

`IDNA_ERROR_EMPTY_LABEL` (`int`)  

`IDNA_ERROR_LABEL_TOO_LONG` (`int`)  

`IDNA_ERROR_DOMAIN_NAME_TOO_LONG` (`int`)  

`IDNA_ERROR_LEADING_HYPHEN` (`int`)  

`IDNA_ERROR_TRAILING_HYPHEN` (`int`)  

`IDNA_ERROR_HYPHEN_3_4` (`int`)  

`IDNA_ERROR_LEADING_COMBINING_MARK` (`int`)  

`IDNA_ERROR_DISALLOWED` (`int`)  

`IDNA_ERROR_PUNYCODE` (`int`)  

`IDNA_ERROR_LABEL_HAS_DOT` (`int`)  

`IDNA_ERROR_INVALID_ACE_LABEL` (`int`)  

`IDNA_ERROR_BIDI` (`int`)  

`IDNA_ERROR_CONTEXTJ` (`int`)  

`ULOC_ACTUAL_LOCALE` (`int`)  
La configuración local de donde provienen realmente los datos.

`ULOC_VALID_LOCALE` (`int`)  
La configuración local más específica soportada por ICU.

`U_AMBIGUOUS_ALIAS_WARNING` (`int`)  
Este alias de convertidor puede ir a diferentes implementaciones de convertidor.

`U_BAD_VARIABLE_DEFINITION` (`int`)  
Falta de `'$'` o nombre de variable en doble.

`U_BRK_ASSIGN_ERROR` (`int`)  
Error de sintaxis en la instrucción de asignación de la regla RBBI.

`U_BRK_ERROR_LIMIT` (`int`)  
Esto debe ser siempre el último valor para indicar el límite de los fallos del iterador de cortes.

`U_BRK_ERROR_START` (`int`)  
Inicio de los códigos que indican los fallos del iterador de cortes.

`U_BRK_HEX_DIGITS_EXPECTED` (`int`)  
Se esperan dígitos hexadecimales como parte de un carácter escapado en una regla.

`U_BRK_INIT_ERROR` (`int`)  
Fallo en la inicialización. Probablemente faltan datos ICU.

`U_BRK_INTERNAL_ERROR` (`int`)  
Se ha detectado un error interno (bug).

`U_BRK_MALFORMED_RULE_TAG` (`int`)  
La etiqueta `{nnn}` en una regla está mal formada.

`U_BRK_MISMATCHED_PAREN` (`int`)  
Paréntesis no apareados en una regla RBBI.

`U_BRK_NEW_LINE_IN_QUOTED_STRING` (`int`)  
Falta comilla de cierre en una regla RBBI.

`U_BRK_RULE_EMPTY_SET` (`int`)  
La regla contiene un conjunto Unicode vacío.

`U_BRK_RULE_SYNTAX` (`int`)  
Error de sintaxis en la regla RBBI.

`U_BRK_SEMICOLON_EXPECTED` (`int`)  
Falta punto y coma `';'` al final de una regla RBBI.

`U_BRK_UNCLOSED_SET` (`int`)  
Conjunto Unicode en una regla RBBI faltando un `']'` de cierre.

`U_BRK_UNDEFINED_VARIABLE` (`int`)  
Uso de una `$Variable` no definida en una regla RBBI.

`U_BRK_UNRECOGNIZED_OPTION` (`int`)  
Opción en las reglas RBBI no reconocida.

`U_BRK_VARIABLE_REDFINITION` (`int`)  
Variable de regla RBBI redefinida.

`U_BUFFER_OVERFLOW_ERROR` (`int`)  
Un resultado no cabría en el búfer proporcionado.

`U_CE_NOT_FOUND_ERROR` (`int`)  
Actualmente utilizado únicamente durante el ajuste del tope variable, pero puede ser utilizado generalmente.

`U_COLLATOR_VERSION_MISMATCH` (`int`)  
La versión del colador no es compatible con la versión base.

`U_DIFFERENT_UCA_VERSION` (`int`)  
ucol_open encontró una incompatibilidad entre la versión UCA y la versión de la imagen del colador, por lo que el colador fue construido a partir de reglas. Sin impacto en la función posterior.

`U_ENUM_OUT_OF_SYNC_ERROR` (`int`)  
`UEnumeration` fuera de sincronización con la colección subyacente.

`U_ERROR_LIMIT` (`int`)  
Alias de `U_PLUGIN_ERROR_LIMIT`.

`U_ERROR_WARNING_LIMIT` (`int`)  
Debe ser siempre el último valor de advertencia para indicar el límite de las advertencias UErrorCode (último código de advertencia +1).

`U_ERROR_WARNING_START` (`int`)  
Inicio de los resultados de información (semánticamente exitosos).

`U_FILE_ACCESS_ERROR` (`int`)  
No se ha podido encontrar el fichero solicitado.

`U_FMT_PARSE_ERROR_LIMIT` (`int`)  
Límite de los errores de la biblioteca de formato.

`U_FMT_PARSE_ERROR_START` (`int`)  
Inicio de los errores de la biblioteca de formato.

`U_IDNA_ACE_PREFIX_ERROR` (`int`)  

`U_IDNA_CHECK_BIDI_ERROR` (`int`)  

`U_IDNA_DOMAIN_NAME_TOO_LONG_ERROR` (`int`)  

`U_IDNA_ERROR_LIMIT` (`int`)  

`U_IDNA_ERROR_START` (`int`)  

`U_IDNA_LABEL_TOO_LONG_ERROR` (`int`)  

`U_IDNA_PROHIBITED_ERROR` (`int`)  

`U_IDNA_STD3_ASCII_RULES_ERROR` (`int`)  

`U_IDNA_UNASSIGNED_ERROR` (`int`)  

`U_IDNA_VERIFICATION_ERROR` (`int`)  

`U_IDNA_ZERO_LENGTH_LABEL_ERROR` (`int`)  

`U_ILLEGAL_ARGUMENT_ERROR` (`int`)  
Indica un valor de argumento incorrecto.

`U_ILLEGAL_CHAR_FOUND` (`int`)  
Conversión de caracteres: secuencia de entrada ilegal.

`U_ILLEGAL_CHAR_IN_SEGMENT` (`int`)  
No utilizado a partir de ICU 2.4.

`U_ILLEGAL_CHARACTER` (`int`)  
Un carácter especial está fuera de su contexto permitido.

`U_ILLEGAL_ESCAPE_SEQUENCE` (`int`)  
Secuencia de escape ilegal ISO-2022.

`U_ILLEGAL_PAD_POSITION` (`int`)  
Símbolo de relleno mal ubicado en el patrón numérico.

`U_INDEX_OUTOFBOUNDS_ERROR` (`int`)  
Intento de acceder a un índice fuera de rango.

`U_INTERNAL_PROGRAM_ERROR` (`int`)  
Indica un bug en el código de la biblioteca.

`U_INTERNAL_TRANSLITERATOR_ERROR` (`int`)  
Error interno del sistema de transliterator.

`U_INVALID_CHAR_FOUND` (`int`)  
Conversión de caracteres: secuencia de entrada no mapeable. En otras APIs: carácter inválido.

`U_INVALID_FORMAT_ERROR` (`int`)  
El formato de los datos no es el esperado.

`U_INVALID_FUNCTION` (`int`)  
Una regla `'&fn()'` especifica un transliterator desconocido.

`U_INVALID_ID` (`int`)  
Una regla `'::id'` especifica un transliterator desconocido.

`U_INVALID_PROPERTY_PATTERN` (`int`)  
No utilizado a partir de ICU 2.4.

`U_INVALID_RBT_SYNTAX` (`int`)  
Se pasó una regla `'::id'` al parser de RuleBasedTransliterator.

`U_INVALID_STATE_ERROR` (`int`)  
La operación solicitada no puede completarse con ICU en su estado actual.

`U_INVALID_TABLE_FILE` (`int`)  
Archivo de tabla de conversión no encontrado.

`U_INVALID_TABLE_FORMAT` (`int`)  
Archivo de tabla de conversión encontrado, pero corrupto.

`U_INVARIANT_CONVERSION_ERROR` (`int`)  
No se puede convertir una cadena `UChar*` a `char*` con el convertidor invariante.

`U_MALFORMED_EXPONENTIAL_PATTERN` (`int`)  
Símbolo de agrupación en el patrón de exponente.

`U_MALFORMED_PRAGMA` (`int`)  
Un pragma `'use'` es inválido.

`U_MALFORMED_RULE` (`int`)  
Los elementos de una regla están mal ubicados.

`U_MALFORMED_SET` (`int`)  
Un patrón `UnicodeSet` es inválido.

`U_MALFORMED_SYMBOL_REFERENCE` (`int`)  
No utilizado a partir de ICU 2.4.

`U_MALFORMED_UNICODE_ESCAPE` (`int`)  
Un patrón de escape Unicode es inválido.

`U_MALFORMED_VARIABLE_DEFINITION` (`int`)  
Una definición de variable es inválida.

`U_MALFORMED_VARIABLE_REFERENCE` (`int`)  
Una referencia de variable es inválida.

`U_MEMORY_ALLOCATION_ERROR` (`int`)  
Error de asignación de memoria.

`U_MESSAGE_PARSE_ERROR` (`int`)  
No se puede analizar un mensaje (formato de mensaje).

`U_MISMATCHED_SEGMENT_DELIMITERS` (`int`)  
No utilizado a partir de ICU 2.4.

`U_MISPLACED_ANCHOR_START` (`int`)  
Un ancla de inicio aparece en una posición ilegal.

`U_MISPLACED_COMPOUND_FILTER` (`int`)  
Un filtro compuesto está en una posición inválida.

`U_MISPLACED_CURSOR_OFFSET` (`int`)  
Un desplazamiento del cursor ocurre en una posición ilegal.

`U_MISPLACED_QUANTIFIER` (`int`)  
Un cuantificador aparece después de un delimitador de fin de segmento.

`U_MISSING_OPERATOR` (`int`)  
Una regla no contiene ningún operador.

`U_MISSING_RESOURCE_ERROR` (`int`)  
El recurso solicitado no se encuentra.

`U_MISSING_SEGMENT_CLOSE` (`int`)  
No utilizado desde ICU 2.4.

`U_MULTIPLE_ANTE_CONTEXTS` (`int`)  
Más de un contexto anterior.

`U_MULTIPLE_COMPOUND_FILTERS` (`int`)  
Más de un filtro compuesto.

`U_MULTIPLE_CURSORS` (`int`)  
Más de un cursor.

`U_MULTIPLE_DECIMAL_SEPARATORS` (`int`)  
Más de un separador decimal en el modelo numérico.

`U_MULTIPLE_DECIMAL_SEPERATORS` (`int`)  
Alias de `U_MULTIPLE_DECIMAL_SEPARATORS`.

`U_MULTIPLE_EXPONENTIAL_SYMBOLS` (`int`)  
Más de un símbolo exponencial en el modelo numérico.

`U_MULTIPLE_PAD_SPECIFIERS` (`int`)  
Más de un símbolo de relleno en el modelo numérico.

`U_MULTIPLE_PERCENT_SYMBOLS` (`int`)  
Más de un símbolo de porcentaje en el modelo numérico.

`U_MULTIPLE_PERMILL_SYMBOLS` (`int`)  
Más de un símbolo de por mil en el modelo numérico.

`U_MULTIPLE_POST_CONTEXTS` (`int`)  
Más de un contexto posterior.

`U_NO_SPACE_AVAILABLE` (`int`)  
No hay espacio disponible para la expansión en búfer para el formato árabe.

`U_NO_WRITE_PERMISSION` (`int`)  
Intento de modificar datos de solo lectura o datos constantes.

`U_PARSE_ERROR` (`int`)  
Equivalente a Java `ParseException`.

`U_PARSE_ERROR_LIMIT` (`int`)  
El límite para los errores del Transliterator.

`U_PARSE_ERROR_START` (`int`)  
Inicio de los errores del Transliterator.

`U_PATTERN_SYNTAX_ERROR` (`int`)  
Error de sintaxis en el modelo de formato.

`U_PRIMARY_TOO_LONG_ERROR` (`int`)  
El usuario intentó definir una variable superior a un valor primario de más de dos bytes.

`U_REGEX_BAD_ESCAPE_SEQUENCE` (`int`)  
Secuencia de escape no reconocida en el modelo.

`U_REGEX_BAD_INTERVAL` (`int`)  
Error en el intervalo `{min,max}`.

`U_REGEX_ERROR_LIMIT` (`int`)  
Este debe ser siempre el último valor para indicar el límite de los errores de regexp.

`U_REGEX_ERROR_START` (`int`)  
Inicio de los códigos que indican fallos de regexp.

`U_REGEX_INTERNAL_ERROR` (`int`)  
Se detectó un error interno (bug).

`U_REGEX_INVALID_BACK_REF` (`int`)  
Retro-referencia a un grupo de captura inexistente.

`U_REGEX_INVALID_FLAG` (`int`)  
Valor inválido para los flags del modo de coincidencia.

`U_REGEX_INVALID_STATE` (`int`)  
`RegexMatcher` en estado inválido para la operación solicitada.

`U_REGEX_LOOK_BEHIND_LIMIT` (`int`)  
Las coincidencias del patrón Look-Behind deben tener una longitud máxima acotada.

`U_REGEX_MAX_LT_MIN` (`int`)  
En `{min,max}`, max es menor que min.

`U_REGEX_MISMATCHED_PAREN` (`int`)  
Paréntesis anidados incorrectamente en el patrón regexp.

`U_REGEX_NUMBER_TOO_BIG` (`int`)  
El número decimal es demasiado grande.

`U_REGEX_PROPERTY_SYNTAX` (`int`)  
Propiedad Unicode incorrecta.

`U_REGEX_RULE_SYNTAX` (`int`)  
Error de sintaxis en el patrón regexp.

`U_REGEX_SET_CONTAINS_STRING` (`int`)  
Los regexps no pueden tener `UnicodeSet`s que contengan cadenas.

`U_REGEX_UNIMPLEMENTED` (`int`)  
Uso de una característica regexp que aún no está implementada.

`U_RESOURCE_TYPE_MISMATCH` (`int`)  
Se solicita una operación sobre un recurso que no la soporta.

`U_RULE_MASK_ERROR` (`int`)  
Una regla está oculta por una regla más general anterior.

`U_SAFECLONE_ALLOCATED_WARNING` (`int`)  
Una operación `SafeClone` requirió la asignación de memoria (solo informativo).

`U_SORT_KEY_TOO_SHORT_WARNING` (`int`)  
El número de niveles solicitados en `getBound` es mayor que el número de niveles en la clave de ordenación.

`U_STANDARD_ERROR_LIMIT` (`int`)  
Este debe ser siempre el último valor para indicar el límite de los errores estándar.

`U_STATE_OLD_WARNING` (`int`)  
ICU debe usar la capa de compatibilidad para construir el servicio. Se debe esperar una degradación del rendimiento/uso de memoria.

`U_STATE_TOO_OLD_ERROR` (`int`)  
ICU no puede construir un servicio a partir de este estado, ya que ya no es soportado.

`U_STRING_NOT_TERMINATED_WARNING` (`int`)  
Una cadena de salida no pudo ser terminada en NUL porque la salida `length==destCapacity`.

`U_STRINGPREP_CHECK_BIDI_ERROR` (`int`)  
Alias de `U_IDNA_CHECK_BIDI_ERROR`.

`U_STRINGPREP_PROHIBITED_ERROR` (`int`)  
Alias de `U_IDNA_PROHIBITED_ERROR`.

`U_STRINGPREP_UNASSIGNED_ERROR` (`int`)  
Alias de `U_IDNA_UNASSIGNED_ERROR`.

`U_TOO_MANY_ALIASES_ERROR` (`int`)  
Hay demasiados alias en la ruta al recurso solicitado. Es muy posible que haya ocurrido una definición de alias circular.

`U_TRAILING_BACKSLASH` (`int`)  
Una barra invertida colgante.

`U_TRUNCATED_CHAR_FOUND` (`int`)  
Conversión de caracteres: secuencia de entrada incompleta.

`U_UNCLOSED_SEGMENT` (`int`)  
Falta un `')'` de cierre.

`U_UNDEFINED_SEGMENT_REFERENCE` (`int`)  
Una referencia a un segmento no corresponde a un segmento definido.

`U_UNDEFINED_VARIABLE` (`int`)  
Una referencia a una variable no corresponde a una variable definida.

`U_UNEXPECTED_TOKEN` (`int`)  
Error de sintaxis en el patrón de formato.

`U_UNMATCHED_BRACES` (`int`)  
Las llaves no coinciden en el patrón del mensaje.

`U_UNQUOTED_SPECIAL` (`int`)  
Un carácter especial no fue entrecomillado ni escapado.

`U_UNSUPPORTED_ATTRIBUTE` (`int`)  
No utilizado a partir de ICU 2.4.

`U_UNSUPPORTED_ERROR` (`int`)  
La operación solicitada no está soportada en el contexto actual.

`U_UNSUPPORTED_ESCAPE_SEQUENCE` (`int`)  
Secuencia de escape ISO-2022 no soportada.

`U_UNSUPPORTED_PROPERTY` (`int`)  
No utilizado a partir de ICU 2.4.

`U_UNTERMINATED_QUOTE` (`int`)  
Falta una comilla simple de cierre.

`U_USELESS_COLLATOR_ERROR` (`int`)  
El collator solo tiene opciones y no se ha especificado una base.

`U_USING_DEFAULT_WARNING` (`int`)  
Una búsqueda en un resource bundle devolvió un resultado de la configuración local raíz (no es un error).

`U_USING_FALLBACK_WARNING` (`int`)  
Una búsqueda en un resource bundle devolvió un resultado de respaldo (no es un error).

`U_VARIABLE_RANGE_EXHAUSTED` (`int`)  
Se generaron demasiados sustitutos para el rango de variables dado.

`U_VARIABLE_RANGE_OVERLAP` (`int`)  
El rango de variables se superpone con caracteres utilizados en las reglas.

`U_ZERO_ERROR` (`int`)  
Sin error, sin advertencia.
