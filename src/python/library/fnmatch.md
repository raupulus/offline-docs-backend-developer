---
title: '"fnmatch" --- Unix filename pattern matching'
source_url: https://docs.python.org/es/3
source_path: library/fnmatch.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2640
---

# "fnmatch" --- Unix filename pattern matching

**Código fuente:** Lib/fnmatch.py

======================================================================

Este módulo proporciona soporte para comodines de estilo shell de
Unix, que *no* son lo mismo que las expresiones regulares (que se
documentan en el módulo "re"). Los caracteres especiales utilizados en
los comodines de estilo shell son:

+--------------+--------------------------------------+
| Patrón       | Significado                          |
|==============|======================================|
## | "*"          | coincide con todo                    |

## | "?"          | coincide con un solo carácter        |

| "[seq]"      | coincide con cualquier carácter      |
## |              | presente en *seq*                    |

| "[!seq]"     | coincide con cualquier carácter      |
## |              | ausente en *seq*                     |

Para una coincidencia literal, envuelva los meta-caracteres entre
paréntesis. Por ejemplo, "'[?]'" coincide con el carácter "'?'".

Ten en cuenta que el separador de nombre de archivo ("'/'" en Unix)
*no* es tratado de forma especial en este módulo. Consulta el módulo
"glob" para realizar expansiones de nombre de ruta ("glob" usa
"filter()" para hacer coincidir con los componentes del nombre de
ruta). Del mismo modo, los nombres de archivo que comienzan con un
punto tampoco son tratados de forma especial por este módulo y se
corresponden con los patrones "*" y "?".

Unless stated otherwise, "filename string" and "pattern string" either
refer to "str" or "ISO-8859-1" encoded "bytes" objects. Note that the
functions documented below do not allow to mix a "bytes" pattern with
a "str" filename, and vice-versa.

Finally, note that "@functools.lru_cache" with a *maxsize* of 32768 is
used to cache the (typed) compiled regex patterns in the following
functions: "fnmatch()", "fnmatchcase()", "filter()", "filterfalse()".

fnmatch.fnmatch(name, pat)

   Test whether the filename string *name* matches the pattern string
   *pat*, returning "True" or "False".  Both parameters are case-
   normalized using "os.path.normcase()". "fnmatchcase()" can be used
   to perform a case-sensitive comparison, regardless of whether
   that's standard for the operating system.

   Este ejemplo imprimirá todos los nombres de archivo en el
   directorio actual con la extensión ".txt":

      import fnmatch
      import os

      for file in os.listdir('.'):
          if fnmatch.fnmatch(file, '*.txt'):
              print(file)

fnmatch.fnmatchcase(name, pat)

   Test whether the filename string *name* matches the pattern string
   *pat*, returning "True" or "False"; the comparison is case-
   sensitive and does not apply "os.path.normcase()".

fnmatch.filter(names, pat)

   Construct a list from those elements of the *iterable* of filename
   strings *names* that match the pattern string *pat*. It is the same
   as "[n for n in names if fnmatch(n, pat)]", but implemented more
   efficiently.

fnmatch.filterfalse(names, pat)

   Construct a list from those elements of the *iterable* of filename
   strings *names* that do not match the pattern string *pat*. It is
   the same as "[n for n in names if not fnmatch(n, pat)]", but
   implemented more efficiently.

   Added in version 3.14.

fnmatch.translate(pat)

   Return the shell-style pattern *pat* converted to a regular
   expression for using with "re.match()". The pattern is expected to
   be a "str".

   Ejemplo:

   >>> import fnmatch, re
   >>>
   >>> regex = fnmatch.translate('*.txt')
   >>> regex
   '(?s:.*\\.txt)\\z'
   >>> reobj = re.compile(regex)
   >>> reobj.match('foobar.txt')
   <re.Match object; span=(0, 10), match='foobar.txt'>

Ver también:

  Módulo "glob"
     Expansión de ruta estilo shell en Unix.
