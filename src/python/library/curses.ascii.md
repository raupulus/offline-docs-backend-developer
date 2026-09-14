---
title: '"curses.ascii" --- Utilities for ASCII characters'
source_url: https://docs.python.org/es/3
source_path: library/curses.ascii.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2200
---

# "curses.ascii" --- Utilities for ASCII characters

**Source code:** Lib/curses/ascii.py

======================================================================

The "curses.ascii" module supplies name constants for ASCII characters
and functions to test membership in various ASCII character classes.
The constants supplied are names for control characters as follows:

+-----------------+------------------------------------------------+
| Nombre          | Significado                                    |
|=================|================================================|
| curses.ascii.N  |                                                |
## | UL              |                                                |

| curses.ascii.S  | Inicio del encabezado, interrupción de la      |
## | OH              | consola                                        |

| curses.ascii.S  | Inicio del texto                               |
## | TX              |                                                |

| curses.ascii.E  | Final del texto                                |
## | TX              |                                                |

| curses.ascii.E  | Fin de la transmisión                          |
## | OT              |                                                |

| curses.ascii.E  | Consulta, va con el control de flujo "ACK"     |
## | NQ              |                                                |

| curses.ascii.A  | Reconocimiento                                 |
## | CK              |                                                |

| curses.ascii.B  | Campana                                        |
## | EL              |                                                |

## | curses.ascii.BS | Retroceso                                      |

| curses.ascii.T  | Tabulación                                     |
## | AB              |                                                |

## | curses.ascii.HT | Alias para "TAB": "Tabulación horizontal"      |

## | curses.ascii.LF | Línea de alimentación                          |

## | curses.ascii.NL | Alias para "LF": "Nueva línea"                 |

## | curses.ascii.VT | Tabulación vertical                            |

## | curses.ascii.FF | Alimentación de formulario                     |

## | curses.ascii.CR | Retorno de carro (*Carriage return* en inglés) |

| curses.ascii.SO | *Shift-out*, comenzar un conjunto de           |
## |                 | caracteres alternativo                         |

| curses.ascii.SI | *Shift-in*, reanudar el conjunto de caracteres |
## |                 | predeterminado                                 |

| curses.ascii.D  | Escape de enlace de datos                      |
## | LE              |                                                |

| curses.ascii.D  | XON, para control de flujo                     |
## | C1              |                                                |

| curses.ascii.D  | Control de dispositivo 2, control de flujo en  |
## | C2              | modo bloque                                    |

| curses.ascii.D  | XOFF, para control de flujo                    |
## | C3              |                                                |

| curses.ascii.D  | Control de dispositivo 4                       |
## | C4              |                                                |

| curses.ascii.N  | Reconocimiento negativo                        |
## | AK              |                                                |

| curses.ascii.S  | Inactivo sincrónico                            |
## | YN              |                                                |

| curses.ascii.E  | Bloque de transmisión final                    |
## | TB              |                                                |

| curses.ascii.C  | Cancelar                                       |
## | AN              |                                                |

## | curses.ascii.EM | Fin del medio                                  |

| curses.ascii.S  | Sustituir                                      |
## | UB              |                                                |

| curses.ascii.E  | Escapar                                        |
## | SC              |                                                |

## | curses.ascii.FS | Separador de archivos                          |

## | curses.ascii.GS | Separador de grupos                            |

| curses.ascii.RS | Separador de registros, finalizador en modo    |
## |                 | bloque                                         |

## | curses.ascii.US | Separador de unidades                          |

## | curses.ascii.SP | Espacio                                        |

| curses.ascii.D  | Eliminar                                       |
## | EL              |                                                |

Tenga en cuenta que muchos de estos tienen poca importancia práctica
en el uso moderno. Los mnemónicos se derivan de las convenciones de la
teleimpresora que son anteriores a las computadoras digitales.

El módulo proporciona las siguientes funciones, siguiendo el patrón de
las de la biblioteca C estándar:

curses.ascii.isalnum(c)

   Comprueba un carácter alfanumérico ASCII; esto es equivalente a
   "isalpha(c) or isdigit(c)".

curses.ascii.isalpha(c)

   Comprueba si hay un carácter alfabético ASCII; es equivalente a
   "isupper(c) or islower(c)".

curses.ascii.isascii(c)

   Comprueba un valor de carácter que se ajuste al conjunto ASCII de 7
   bits.

curses.ascii.isblank(c)

   Checks for an ASCII blank character; space or horizontal tab.

curses.ascii.iscntrl(c)

   Comprueba un carácter de control ASCII (en el rango de 0x00 a 0x1f
   o 0x7f).

curses.ascii.isdigit(c)

   Comprueba si hay un dígito decimal ASCII, desde "'0'" hasta "'9'".
   Esto es equivalente a "c in string.digits".

curses.ascii.isgraph(c)

   Checks for any ASCII printable character except space.

curses.ascii.islower(c)

   Comprueba un carácter ASCII en minúscula.

curses.ascii.isprint(c)

   Comprueba cualquier carácter imprimible ASCII, incluido el espacio.

curses.ascii.ispunct(c)

   Checks for any ASCII printable character which is not a space or an
   alphanumeric character.

curses.ascii.isspace(c)

   Comprueba los caracteres de espacio en blanco ASCII; espacio, línea
   de alimentación, retorno de carro, formulario de alimentación,
   tabulación horizontal, tabulación vertical.

curses.ascii.isupper(c)

   Comprueba una letra mayúscula ASCII.

curses.ascii.isxdigit(c)

   Comprueba si hay un dígito hexadecimal ASCII. Esto es equivalente a
   "c in string.hexdigits".

curses.ascii.isctrl(c)

   Checks for an ASCII control character (ordinal values 0 to 31).
   Unlike "iscntrl()", this does not include the delete character
   (0x7f).

curses.ascii.ismeta(c)

   Comprueba si hay un carácter no ASCII (valores ordinales 0x80 y
   superiores).

Estas funciones aceptan enteros o cadenas de un solo carácter; cuando
el argumento es una cadena de caracteres, primero se convierte
utilizando la función *built-in* "ord()".

Tenga en cuenta que todas estas funciones verifican los valores de
bits ordinales derivados del carácter de la cadena que ingresa; en
realidad, no saben nada sobre la codificación de caracteres de la
máquina host.

Las siguientes dos funciones toman una cadena de un solo carácter o un
valor de byte entero; devuelven un valor del mismo tipo.

curses.ascii.ascii(c)

   Retorna el valor ASCII correspondiente a los 7 bits bajos de *c*.

curses.ascii.ctrl(c)

   Retorna el carácter de control correspondiente al carácter dado (el
   valor del bit del carácter es bit a bit (*bitwise-anded*) con
   0x1f).

curses.ascii.alt(c)

   Retorna el carácter de 8 bits correspondiente al carácter ASCII
   dado (el valor del bit de carácter se escribe bit a bit (*bitwise-
   ored*) con 0x80).

La siguiente función toma una cadena de un solo carácter o un valor
entero; devuelve una cadena.

curses.ascii.unctrl(c)

   Retorna una representación de cadena del carácter ASCII *c*. Si *c*
   es imprimible, esta cadena es el propio carácter. Si el carácter es
   un carácter de control (0x00--0x1f) la cadena consta de un signo de
   intercalación ("'^'") seguido de la letra mayúscula
   correspondiente. Si el carácter es una eliminación ASCII (0x7f), la
   cadena es "'^?'". Si el carácter tiene su meta bit establecido
   (0x80), el meta bit se elimina, se aplican las reglas anteriores y
   se antepone "'!'" al resultado.

curses.ascii.controlnames

   Una matriz de cadena de caracteres de 33 elementos que contiene los
   mnemónicos ASCII para los treinta y dos caracteres de control ASCII
   desde 0 (NUL) a 0x1f (US), en orden, más el mnemónico "SP" para el
   carácter de espacio.
