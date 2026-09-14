---
title: '"token" --- Constants used with Python parse trees'
source_url: https://docs.python.org/es/3
source_path: library/token.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4250
---

# "token" --- Constants used with Python parse trees

**Código fuente:** Lib/token.py

======================================================================

Este módulo proporciona constantes que representan los valores
numéricos de los nodos hoja del árbol de análisis (tokens terminales).
Consulte el archivo "Grammar/Tokens" en la distribución de Python para
conocer las definiciones de los nombres en el contexto de la gramática
del lenguaje. Los valores numéricos específicos a los que se asignan
los nombres pueden cambiar entre las versiones de Python.

El módulo también proporciona un mapeo de códigos numéricos a nombres
y algunas funciones.  Las funciones asemejan definiciones en los
archivos Python C encabezados.

Note that a token's value may depend on tokenizer options. For
example, a ""+"" token may be reported as either "PLUS" or "OP", or a
""match"" token may be either "NAME" or "SOFT_KEYWORD".

token.tok_name

   Diccionario que mapea los valores numéricos de las constantes
   definidas en este módulo a cadenas de nombres, permitiendo una
   representación de árboles de sintaxis a ser generados más legible
   para humanos.

token.ISTERMINAL(x)

   Retorna "True" para valores token terminales.

token.ISNONTERMINAL(x)

   Retorna "True" para valores token no terminales.

token.ISEOF(x)

   Retorna "True" si *x* es el marcador indicando el final del input.

Las constantes de token son:

token.NAME

   Token value that indicates an identifier or keyword.

token.NUMBER

   Token value that indicates a numeric literal

token.STRING

   Token value that indicates a string or byte literal, excluding
   formatted string literals. The token string is not interpreted: it
   includes the surrounding quotation marks and the prefix (if given);
   backslashes are included literally, without processing escape
   sequences.

token.OP

   A generic token value that indicates an operator or delimiter.

   **Detalles de implementación de CPython:** This value is only
   reported by the "tokenize" module. Internally, the tokenizer uses
   exact token types instead.

token.COMMENT

   Token value used to indicate a comment. The parser ignores
   "COMMENT" tokens.

token.NEWLINE

   Token value that indicates the end of a logical line.

token.NL

   Token value used to indicate a non-terminating newline. "NL" tokens
   are generated when a logical line of code is continued over
   multiple physical lines. The parser ignores "NL" tokens.

token.INDENT

   Token value used at the beginning of a logical line to indicate the
   start of an indented block.

token.DEDENT

   Token value used at the beginning of a logical line to indicate the
   end of an indented block.

token.FSTRING_START

   Token value used to indicate the beginning of an f-string literal.

   **Detalles de implementación de CPython:** The token string
   includes the prefix and the opening quote(s), but none of the
   contents of the literal.

token.FSTRING_MIDDLE

   Token value used for literal text inside an f-string literal,
   including format specifications.

   **Detalles de implementación de CPython:** Replacement fields (that
   is, the non-literal parts of f-strings) use the same tokens as
   other expressions, and are delimited by "LBRACE", "RBRACE",
   "EXCLAMATION" and "COLON" tokens.

token.FSTRING_END

   Token value used to indicate the end of a f-string.

   **Detalles de implementación de CPython:** The token string
   contains the closing quote(s).

token.TSTRING_START

   Token value used to indicate the beginning of a template string
   literal.

   **Detalles de implementación de CPython:** The token string
   includes the prefix and the opening quote(s), but none of the
   contents of the literal.

   Added in version 3.14.

token.TSTRING_MIDDLE

   Token value used for literal text inside a template string literal
   including format specifications.

   **Detalles de implementación de CPython:** Replacement fields (that
   is, the non-literal parts of t-strings) use the same tokens as
   other expressions, and are delimited by "LBRACE", "RBRACE",
   "EXCLAMATION" and "COLON" tokens.

   Added in version 3.14.

token.TSTRING_END

   Token value used to indicate the end of a template string literal.

   **Detalles de implementación de CPython:** The token string
   contains the closing quote(s).

   Added in version 3.14.

token.ENDMARKER

   Token value that indicates the end of input. Used in top-level
   grammar rules.

token.ENCODING

   Valor de token que indica la codificación usada para decodificar
   los bytes de origen en texto. El primer token retornado por
   "tokenize.tokenize()" siempre será un token "ENCODING".

   **Detalles de implementación de CPython:** This token type isn't
   used by the C tokenizer but is needed for the "tokenize" module.

The following token types are not produced by the "tokenize" module,
and are defined for special uses in the tokenizer or parser:

token.TYPE_IGNORE

   Token value indicating that a "type: ignore" comment was
   recognized. Such tokens are produced instead of regular "COMMENT"
   tokens only with the "PyCF_TYPE_COMMENTS" flag.

token.TYPE_COMMENT

   Token value indicating that a type comment was recognized. Such
   tokens are produced instead of regular "COMMENT" tokens only with
   the "PyCF_TYPE_COMMENTS" flag.

token.SOFT_KEYWORD

   Token value indicating a soft keyword.

   The tokenizer never produces this value. To check for a soft
   keyword, pass a "NAME" token's string to "keyword.issoftkeyword()".

token.ERRORTOKEN

   Token value used to indicate wrong input.

   The "tokenize" module generally indicates errors by raising
   exceptions instead of emitting this token. It can also emit tokens
   such as "OP" or "NAME" with strings that are later rejected by the
   parser.

The remaining tokens represent specific operators and delimiters. (The
"tokenize" module reports these as "OP"; see "exact_type" in the
"tokenize" documentation for details.)

+----------------------------------------------------+----------------------------------------------------+
| Token                                              | Value                                              |
|====================================================|====================================================|
## | token.LPAR                                         | ""(""                                              |

## | token.RPAR                                         | "")""                                              |

## | token.LSQB                                         | ""[""                                              |

## | token.RSQB                                         | ""]""                                              |

## | token.COLON                                        | "":""                                              |

## | token.COMMA                                        | "",""                                              |

## | token.SEMI                                         | "";""                                              |

## | token.PLUS                                         | ""+""                                              |

## | token.MINUS                                        | ""-""                                              |

## | token.STAR                                         | ""*""                                              |

## | token.SLASH                                        | ""/""                                              |

## | token.VBAR                                         | ""|""                                              |

## | token.AMPER                                        | ""&""                                              |

## | token.LESS                                         | ""<""                                              |

## | token.GREATER                                      | "">""                                              |

## | token.EQUAL                                        | ""=""                                              |

## | token.DOT                                          | "".""                                              |

## | token.PERCENT                                      | ""%""                                              |

## | token.LBRACE                                       | ""{""                                              |

## | token.RBRACE                                       | ""}""                                              |

## | token.EQEQUAL                                      | ""==""                                             |

## | token.NOTEQUAL                                     | ""!=""                                             |

## | token.LESSEQUAL                                    | ""<=""                                             |

## | token.GREATEREQUAL                                 | "">=""                                             |

## | token.TILDE                                        | ""~""                                              |

## | token.CIRCUMFLEX                                   | ""^""                                              |

## | token.LEFTSHIFT                                    | ""<<""                                             |

## | token.RIGHTSHIFT                                   | "">>""                                             |

## | token.DOUBLESTAR                                   | ""**""                                             |

## | token.PLUSEQUAL                                    | ""+=""                                             |

## | token.MINEQUAL                                     | ""-=""                                             |

## | token.STAREQUAL                                    | ""*=""                                             |

## | token.SLASHEQUAL                                   | ""/=""                                             |

## | token.PERCENTEQUAL                                 | ""%=""                                             |

## | token.AMPEREQUAL                                   | ""&=""                                             |

## | token.VBAREQUAL                                    | ""|=""                                             |

## | token.CIRCUMFLEXEQUAL                              | ""^=""                                             |

## | token.LEFTSHIFTEQUAL                               | ""<<=""                                            |

## | token.RIGHTSHIFTEQUAL                              | "">>=""                                            |

## | token.DOUBLESTAREQUAL                              | ""**=""                                            |

## | token.DOUBLESLASH                                  | ""//""                                             |

## | token.DOUBLESLASHEQUAL                             | ""//=""                                            |

## | token.AT                                           | ""@""                                              |

## | token.ATEQUAL                                      | ""@=""                                             |

## | token.RARROW                                       | ""->""                                             |

## | token.ELLIPSIS                                     | ""...""                                            |

## | token.COLONEQUAL                                   | "":=""                                             |

## | token.EXCLAMATION                                  | ""!""                                              |

The following non-token constants are provided:

token.N_TOKENS

   The number of token types defined in this module.

token.EXACT_TOKEN_TYPES

   A dictionary mapping the string representation of a token to its
   numeric code.

   Added in version 3.8.

Distinto en la versión 3.5: Added "AWAIT" and "ASYNC" tokens.

Distinto en la versión 3.7: Agregados los tokens "COMMENT", "NL" y
"ENCODING".

Distinto en la versión 3.7: Removed "AWAIT" and "ASYNC" tokens.
"async" and "await" are now tokenized as "NAME" tokens.

Distinto en la versión 3.8: Added "TYPE_COMMENT", "TYPE_IGNORE",
"COLONEQUAL". Added "AWAIT" and "ASYNC" tokens back (they're needed to
support parsing older Python versions for "ast.parse()" with
"feature_version" set to 6 or lower).

Distinto en la versión 3.12: Added "EXCLAMATION".

Distinto en la versión 3.13: Removed "AWAIT" and "ASYNC" tokens again.
