---
title: '"grp" --- The group database'
source_url: https://docs.python.org/es/3
source_path: library/grp.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2770
---

# "grp" --- The group database

======================================================================

Este módulo proporciona acceso a la base de datos del grupo Unix. Está
disponible en todas las versiones de Unix.

Availability: Unix, not WASI, not Android, not iOS.

Las entradas de base de datos de grupo se notifican como un objeto
similar a una tupla, cuyos atributos corresponden a los miembros de la
estructura "group" (campo atributo a continuación, véase "<grp.h>"):

+---------+-------------+-----------------------------------+
| Índice  | Atributo    | Significado                       |
|=========|=============|===================================|
## | 0       | gr_name     | el nombre del grupo               |

| 1       | gr_passwd   | la contraseña (encriptada) del    |
## |         |             | grupo; usualmente vacío           |

## | 2       | gr_gid      | el grupo ID numérico              |

| 3       | gr_mem      | todos los nombres de usuario de   |
## |         |             | los miembros del grupo            |

El *gid* es un número entero, el nombre y la contraseña son cadenas y
la lista de miembros es una lista de cadenas. (Tenga en cuenta que la
mayoría de los usuarios no se enumeran explícitamente como miembros
del grupo en el que se encuentran de acuerdo con la base de datos de
contraseñas. Consulte ambas bases de datos para obtener información
completa sobre la membresía. También tenga en cuenta que un
‘’gr_name’’ que comienza con un "+" o "-" es probable que sea una
referencia de YP/NIS y puede que no sea accesible vía "getgrnam()" o
"getgrgid()".)

Define los siguientes elementos:

grp.getgrgid(id)

   Retorna la entrada de la base de datos del grupo para el ID de
   grupo numérico dado. Se genera "KeyError" si no se puede encontrar
   la entrada solicitada.

   Distinto en la versión 3.10: "TypeError" se genera para argumentos
   no enteros como flotantes o cadenas de caracteres.

grp.getgrnam(name)

   Retorna la entrada de la base de datos del grupo para el nombre de
   grupo dado. Se genera "KeyError" si no se puede encontrar la
   entrada solicitada.

grp.getgrall()

   Retorna una lista de todas las entradas de grupo disponibles, en
   orden arbitrario.

Ver también:

  Módulo "pwd"
     Una interfaz para la base de datos de usuarios, similar a esta.
