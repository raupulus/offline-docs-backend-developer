---
title: '"pwd" --- The password database'
source_url: https://docs.python.org/es/3
source_path: library/pwd.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3550
---

# "pwd" --- The password database

======================================================================

Este módulo proporciona acceso a la base de datos de cuentas de
usuario y contraseñas de Unix.  Está disponible en todas las versiones
de Unix.

Availability: Unix, not WASI, not iOS.

Las entradas de la base de datos de contraseñas se reportan como un
objeto de tipo tupla, cuyos atributos corresponden a los miembros de
la estructura "passwd" (campo Atributo abajo, ver "<pwd.h>"):

+---------+-----------------+-------------------------------+
| Índice  | Atributo        | Significado                   |
|=========|=================|===============================|
## | 0       | "pw_name"       | Nombre de usuario             |

| 1       | "pw_passwd"     | Contraseña encriptada         |
## |         |                 | opcional                      |

| 2       | "pw_uid"        | Identificación numérica de    |
## |         |                 | usuario                       |

| 3       | "pw_gid"        | Identificación del grupo      |
## |         |                 | numérico                      |

| 4       | "pw_gecos"      | Nombre de usuario o campo de  |
## |         |                 | comentarios                   |

| 5       | "pw_dir"        | El directorio *home* del      |
## |         |                 | usuario                       |

| 6       | "pw_shell"      | Intérprete de comandos de     |
## |         |                 | usuario                       |

Los elementos uid y gid son enteros, todos los demás son cadenas.
"KeyError" se lanza si la entrada pedida no se encuentra.

Nota:

  In traditional Unix the field "pw_passwd" usually contains a
  password encrypted with a DES derived algorithm.  However most
  modern unices  use a so-called *shadow password* system.  On those
  unices the *pw_passwd* field only contains an asterisk ("'*'") or
  the  letter "'x'" where the encrypted password is stored in a file
  "/etc/shadow" which is not world readable.  Whether the *pw_passwd*
  field contains anything useful is system-dependent.

Define los siguientes elementos:

pwd.getpwuid(uid)

   Retorna la entrada de la base de datos de contraseñas para el ID de
   usuario numérico dado.

pwd.getpwnam(name)

   Retorna la entrada de la base de datos de contraseñas para el
   nombre de usuario dado.

pwd.getpwall()

   Retorna una lista de todas las entradas de la base de datos de
   contraseñas disponibles, en orden arbitrario.

Ver también:

  Módulo "grp"
     Una interfaz para la base de datos de grupos, similar a esta.
