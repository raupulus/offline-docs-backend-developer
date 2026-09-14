---
title: '"webbrowser" --- Convenient web-browser controller'
source_url: https://docs.python.org/es/3
source_path: library/webbrowser.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4510
---

# "webbrowser" --- Convenient web-browser controller

**Código fuente:** Lib/webbrowser.py

======================================================================

The "webbrowser" module provides a high-level interface to allow
displaying web-based documents to users. Under most circumstances,
simply calling the "open()" function from this module will do the
right thing.

En Unix, son privilegiados los navegadores gráficos bajo X11, pero
serán usados navegadores en modo texto si los navegadores gráficos no
están disponibles o un *display* X11 no está disponible. Si se usan
navegadores en modo texto, el proceso invocador será bloqueado hasta
que el usuario salga del navegador.

If the environment variable "BROWSER" exists, it is interpreted as the
"os.pathsep"-separated list of browsers to try ahead of the platform
defaults.  When the value of a list part contains the string "%s",
then it is interpreted as a literal browser command line to be used
with the argument URL substituted for "%s"; if the value is a single
word that refers to one of the already registered browsers this
browser is added to the front of the search list; if the part does not
contain "%s", it is simply interpreted as the name of the browser to
launch. [1]

Distinto en la versión 3.14: The "BROWSER" variable can now also be
used to reorder the list of platform defaults. This is particularly
useful on macOS where the platform defaults do not refer to command-
line tools on "PATH".

En plataformas no Unix o cuando está disponible un navegador remoto en
Unix, el proceso de control no esperará a que el usuario finalice el
navegador, sino que permitirá al navegador remoto mantener su propia
ventana en la pantalla. Si no están disponibles navegadores remotos en
Unix, el proceso de control lanzará un nuevo navegador y esperará.

On iOS, the "BROWSER" environment variable, as well as any arguments
controlling autoraise, browser preference, and new tab/window creation
will be ignored. Web pages will *always* be opened in the user's
preferred browser, in a new tab, with the browser being brought to the
foreground. The use of the "webbrowser" module on iOS requires the
"ctypes" module. If "ctypes" isn't available, calls to "open()" will
fail.

## Command-line interface

The script **webbrowser** can be used as a command-line interface for
the module. It accepts a URL as the argument. It accepts the following
optional parameters:

-n, --new-window

   Opens the URL in a new browser window, if possible.

-t, --new-tab

   Opens the URL in a new browser tab.

The options are, naturally, mutually exclusive.  Usage example:

   python -m webbrowser -t "https://www.python.org"

Availability: not WASI, not Android.

La siguiente excepción es definida:

exception webbrowser.Error

   Excepción generada cuando ocurre un error de control de navegador.

Las siguientes funciones son definidas:

webbrowser.open(url, new=0, autoraise=True)

   Muestra *url* usando el navegador por defecto. Si *new* es 0, se
   abre la *url* en la misma ventana del navegador si es posible. Si
   *new* es 1, se abre una nueva ventana del navegador si es posible.
   Si *new* es 2, se abre una nueva página del navegador ("pestaña")
   si es posible. Si *autoraise* es "True", la ventana es lanzada si
   es posible (ten en cuenta que bajo muchos gestores de ventana esto
   ocurrirá independientemente de la configuración de esta variable).

   Returns "True" if a browser was successfully launched, "False"
   otherwise.

   Ten en cuenta que en algunas plataformas, tratar de abrir un nombre
   de archivo usando esta función puede funcionar e iniciar el
   programa asociado del sistema operativo. Sin embargo, esto no es
   soportado ni portable.

   Lanza un evento de auditoría "webbrowser.open" con el argumento
   "url".

webbrowser.open_new(url)

   Abre *url* en una nueva ventana del navegador por defecto, si es
   posible, si no, abre *url* en la única ventana del navegador.

   Returns "True" if a browser was successfully launched, "False"
   otherwise.

webbrowser.open_new_tab(url)

   Abre *url* en una nueva página ("pestaña") del navegador por
   defecto, si es posible, si no equivale a "open_new()".

   Returns "True" if a browser was successfully launched, "False"
   otherwise.

webbrowser.get(using=None)

   Retorna un objeto de controlador para el tipo de navegador *using*.
   Si *using* es "None", retorna un controlador de un navegador por
   defecto apropiado para el entorno del invocador.

webbrowser.register(name, constructor, instance=None, *, preferred=False)

   Registra el tipo de navegador *name*. Una vez que el tipo de
   navegador es registrado, la función "get()" puede retornar un
   controlador para ese tipo de navegador. Si no se provee *instance*
   o es "None", *constructor* será invocado sin parámetros al crear
   una instancia cuando sea necesario. Si se provee *instance*,
   *constructor* no será nunca invocado y puede ser "None".

   Definir *preferred* a "True" hace de este navegador un resultado
   preferido para una invocación "get()" sin argumento. De otra
   manera, este punto de entrada sólo es útil si planeas definir la
   variable "BROWSER" o invocar "get()" con un argumento no vacío
   correspondiendo con el nombre de un manejador que declaras.

   Distinto en la versión 3.7: fue añadido el parámetro sólo de
   palabra clave *preferred*.

Un número de tipos de navegador son predefinidos. Esta tabla muestra
los nombres de los tipos que se pueden pasar a la función "get()" y
las instanciaciones correspondientes para las clases de los
controladores, todas definidas en este módulo.

+--------------------------+-------------------------------------------+---------+
| Nombre de tipo           | Nombre de clase                           | Notas   |
|==========================|===========================================|=========|
## | "'mozilla'"              | "Mozilla('mozilla')"                      |         |

## | "'firefox'"              | "Mozilla('mozilla')"                      |         |

## | "'epiphany'"             | "Epiphany('epiphany')"                    |         |

## | "'kfmclient'"            | "Konqueror()"                             | (1)     |

## | "'konqueror'"            | "Konqueror()"                             | (1)     |

## | "'kfm'"                  | "Konqueror()"                             | (1)     |

## | "'opera'"                | "Opera()"                                 |         |

## | "'links'"                | "GenericBrowser('links')"                 |         |

## | "'elinks'"               | "Elinks('elinks')"                        |         |

## | "'lynx'"                 | "GenericBrowser('lynx')"                  |         |

## | "'w3m'"                  | "GenericBrowser('w3m')"                   |         |

## | "'windows-default'"      | "WindowsDefault"                          | (2)     |

## | "'macosx'"               | "MacOSXOSAScript('default')"              | (3)     |

## | "'safari'"               | "MacOSXOSAScript('safari')"               | (3)     |

## | "'google-chrome'"        | "Chrome('google-chrome')"                 |         |

## | "'chrome'"               | "Chrome('chrome')"                        |         |

## | "'chromium'"             | "Chromium('chromium')"                    |         |

## | "'chromium-browser'"     | "Chromium('chromium-browser')"            |         |

## | "'iosbrowser'"           | "IOSBrowser"                              | (4)     |

Notas:

1. "Konqueror" is the file manager for the KDE desktop environment for
   Unix, and only makes sense to use if KDE is running.  Some way of
   reliably detecting KDE would be nice; the "KDEDIR" variable is not
   sufficient.  Note also that the name "kfm" is used even when using
   the **konqueror** command with KDE 2 --- the implementation selects
   the best strategy for running Konqueror.

2. Sólo en plataformas Windows.

3. Only on macOS.

4. Only on iOS.

Added in version 3.2: A new "MacOSXOSAScript" class has been added and
is used on Mac instead of the previous "MacOSX" class. This adds
support for opening browsers not currently set as the OS default.

Added in version 3.3: Ha sido añadido soporte para Chrome/Chromium.

Distinto en la versión 3.12: Se ha eliminado el soporte para varios
navegadores obsoletos. Los navegadores eliminados son Grail, Mosaic,
Netscape, Galeon, Skipstone, Iceape y Firefox versión 35 e inferiores.

Distinto en la versión 3.13: Support for iOS has been added.

Aquí están algunos ejemplos simples:

   url = 'https://docs.python.org/'

   # Open URL in a new tab, if a browser window is already open.
   webbrowser.open_new_tab(url)

   # Open URL in new window, raising the window if possible.
   webbrowser.open_new(url)

## Browser controller objects

Browser controllers provide the "name" attribute, and the following
three methods which parallel module-level convenience functions:

controller.name

   Nombre dependiente del sistema para el navegador.

controller.open(url, new=0, autoraise=True)

   Despliega *url* usando el navegador manejado por este controlador.
   Si *new* es 1, se abre una nueva ventana del navegador si es
   posible. Si *new* es 2, se abre una nueva página del navegador
   ("pestaña") si es posible.

controller.open_new(url)

   Abre *url* en una nueva ventana del navegador manejado por este
   controlador, si es posible, si no, abre *url* en la única ventana
   del navegador. Alias "open_new()".

controller.open_new_tab(url)

   Abre *url* en una nueva página ("pestaña") del navegador manejado
   por este controlador, si es posible, si no equivale a "open_new()".

-[ Notas al pie ]-

[1] Los ejecutables nombrados aquí sin una ruta completa serán
    buscados en los directorios dados en la variable de entorno
    "PATH".
