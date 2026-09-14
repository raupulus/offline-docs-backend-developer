---
title: '"__future__" --- Future statement definitions'
source_url: https://docs.python.org/es/3
source_path: library/__future__.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1460
---

# "__future__" --- Future statement definitions

**Código fuente:** Lib/__future__.py

======================================================================

Imports of the form "from __future__ import feature" are called future
statements. These are special-cased by the Python compiler to allow
the use of new Python features in modules containing the future
statement before the release in which the feature becomes standard.

While these future statements are given additional special meaning by
the Python compiler, they are still executed like any other import
statement and the "__future__" exists and is handled by the import
system the same way any other Python module would be. This design
serves three purposes:

* Para evitar confundir las herramientas existentes que analizan las
  declaraciones de importación y esperan encontrar los módulos que
  están importando.

* To document when incompatible changes were introduced, and when they
  will be --- or were --- made mandatory.  This is a form of
  executable documentation, and can be inspected programmatically via
  importing "__future__" and examining its contents.

* To ensure that future statements run under releases prior to Python
  2.1 at least yield runtime exceptions (the import of "__future__"
  will fail, because there was no module of that name prior to 2.1).

## Module Contents

No feature description will ever be deleted from "__future__". Since
its introduction in Python 2.1 the following features have found their
way into the language using this mechanism:

+---------------------------+---------------------------+---------------------------+---------------------------+
| característica            | opcional en               | obligatorio en            | efecto                    |
|===========================|===========================|===========================|===========================|
| __future__.nested_scopes  | 2.1.0b1                   | 2.2                       | **PEP 227**: *Ámbitos     |
## |                           |                           |                           | anidados estáticamente*   |

| __future__.generators     | 2.2.0a1                   | 2.3                       | **PEP 255**: *Generadores |
## |                           |                           |                           | simples*                  |

| __future__.division       | 2.2.0a2                   | 3.0                       | **PEP 238**: *Cambio de   |
## |                           |                           |                           | operador de división*     |

| __future__.absolute_impo  | 2.5.0a1                   | 3.0                       | **PEP 328**:              |
| rt                        |                           |                           | *Importaciones:           |
|                           |                           |                           | Multilínea y              |
## |                           |                           |                           | Absoluto/Relativo*        |

| __future__.with_statement | 2.5.0a1                   | 2.6                       | **PEP 343**: *The “with”  |
## |                           |                           |                           | Statement*                |

| __future__.print_function | 2.6.0a2                   | 3.0                       | **PEP 3105**: *Hacer de   |
## |                           |                           |                           | print una función*        |

| __future__.unicode_liter  | 2.6.0a2                   | 3.0                       | **PEP 3112**: *Bytes      |
## | als                       |                           |                           | literales en Python 3000* |

| __future__.generator_stop | 3.5.0b1                   | 3.7                       | **PEP 479**: *Manejo de   |
|                           |                           |                           | StopIteration dentro de   |
## |                           |                           |                           | generadores*              |

| __future__.annotations    | 3.7.0b1                   | Never [1]                 | **PEP 563**: *Postponed   |
|                           |                           |                           | evaluation of             |
|                           |                           |                           | annotations*, **PEP       |
|                           |                           |                           | 649**: *Deferred          |
|                           |                           |                           | evaluation of annotations |
## |                           |                           |                           | using descriptors*        |

class __future__._Feature

   Cada declaración en "__future__.py" tiene la forma:

      FeatureName = _Feature(OptionalRelease, MandatoryRelease,
                             CompilerFlag)

   donde, normalmente, *OptionalRelease* es menor que
   *MandatoryRelease* y ambos son 5-tuplas de la misma forma que
   "sys.version_info":

      (PY_MAJOR_VERSION, # the 2 in 2.1.0a3; an int
       PY_MINOR_VERSION, # the 1; an int
       PY_MICRO_VERSION, # the 0; an int
       PY_RELEASE_LEVEL, # "alpha", "beta", "candidate" or "final"; string
       PY_RELEASE_SERIAL # the 3; an int
      )

_Feature.getOptionalRelease()

   *OptionalRelease* registra la primera versión en la que se aceptó
   la característica.

_Feature.getMandatoryRelease()

   En el caso de un *MandatoryRelease* que aún no se ha producido,
   *MandatoryRelease* predice el lanzamiento en el que la
   característica pasará a formar parte del lenguaje.

   De otro modo, *MandatoryRelease* registra cuándo la característica
   se convirtió en parte del lenguaje; en versiones en o después de
   este, los módulos ya no necesitan una declaración futura para usar
   la característica en cuestión, pero pueden continuar usando dichas
   importaciones.

   *MandatoryRelease* may also be "None", meaning that a planned
   feature got dropped or that it is not yet decided.

_Feature.compiler_flag

   *CompilerFlag* is the (bitfield) flag that should be passed in the
   fourth argument to the built-in function "compile()" to enable the
   feature in dynamically compiled code.  This flag is stored in the
   "_Feature.compiler_flag" attribute on "_Feature" instances.

[1] "from __future__ import annotations" was previously scheduled to
    become mandatory in Python 3.10, but the change was delayed and
    ultimately canceled. This feature will eventually be deprecated
    and removed. See **PEP 649** and **PEP 749**.

Ver también:

  Declaraciones Futuras
     Cómo trata el compilador las importaciones futuras.

  **PEP 236** - Back to the __future__
     The original proposal for the __future__ mechanism.
