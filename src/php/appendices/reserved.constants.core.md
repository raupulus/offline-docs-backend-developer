---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/reserved.constants.core.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/reserved.constants.core.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 5208882ce
order: 1280
---

## Constantes predefinidas

Estas constantes están definidas por el núcleo de PHP. Esto incluye PHP, el motor Zend y los módulos SAPI.

`PHP_VERSION` (`string`)  
La versión actual de PHP como una cadena en la notación "mayor.menor.lanzamiento\[extra\]".

`PHP_MAJOR_VERSION` (`int`)  
La versión mayor actual de PHP como una cadena (por ejemplo, int(5) desde la versión "5.2.7-extra").

`PHP_MINOR_VERSION` (`int`)  
La versión menor actual de PHP como una cadena (por ejemplo, int(2) desde la versión "5.2.7-extra").

`PHP_RELEASE_VERSION` (`int`)  
La versión de lanzamiento actual de PHP como una cadena (por ejemplo, int(7) desde la versión "5.2.7-extra").

`PHP_VERSION_ID` (`int`)  
La versión actual de PHP como un entero, útil para la comparación de versiones (por ejemplo, int(50207) desde la versión "5.2.7-extra").

`PHP_EXTRA_VERSION` (`string`)  
La versión "extra" actual de PHP como una cadena (por ejemplo, '-extra' desde la versión "5.2.7-extra"). Ocasionalmente utilizada por los empaquetadores de distribuciones para indicar una versión de paquete.

`PHP_BUILD_DATE` (`string`)  
La fecha y hora en que se compiló PHP, en formato `"M d Y H:i:s"`. Disponible desde PHP 8.5.0.

`PHP_BUILD_PROVIDER` (`string`)  
El proveedor que compiló PHP. Disponible desde PHP 8.5.0.

> [!NOTE]
> Es posible que esta constante no esté disponible en todas las compilaciones de PHP. (p. ej., no se define al compilar desde el código fuente sin especificar un valor durante la configuración).

`ZEND_THREAD_SAFE` (`bool`)  
Indica si la versión actual de PHP se compiló con soporte para subprocesos.

`ZEND_DEBUG_BUILD` (`bool`)  
Indica si la versión actual de PHP es una compilación de depuración.

`PHP_ZTS` (`bool`) Alias de `ZEND_THREAD_SAFE`  
Indica si la versión actual de PHP se compiló con soporte para subprocesos.

`PHP_DEBUG` (`bool`) Alias de `ZEND_DEBUG_BUILD`  
Indica si la versión actual de PHP es una compilación de depuración.

`DEBUG_BACKTRACE_PROVIDE_OBJECT` (`int`)  
Reemplaza el índice "object".

`DEBUG_BACKTRACE_IGNORE_ARGS` (`int`)  
No incluye información de argumentos para las funciones en la traza de la pila.

`PHP_MAXPATHLEN` (`int`)  
La longitud máxima de los nombres de archivo (incluyendo el camino) soportada por este binario de PHP.

`PHP_OS` (`string`)  
El sistema operativo para el que se compiló PHP.

`PHP_OS_FAMILY` (`string`)  
La familia del sistema operativo para el que se compiló PHP. Uno de `'Windows'`, `'BSD'`, `'Darwin'`, `'Solaris'`, `'Linux'` o `'Unknown'`. Disponible desde PHP 7.2.0.

`PHP_SAPI` (`string`)  
La API del servidor para este binario de PHP. Véase también `php_sapi_name`.

`PHP_EOL` (`string`)  
El carácter de nueva línea correcto para esta plataforma.

`PHP_INT_MAX` (`int`)  
El entero más grande soportado por este binario de PHP. Habitualmente, int(2147483647) en sistemas de 32 bits y int(9223372036854775807) en sistemas de 64 bits.

`PHP_INT_MIN` (`int`)  
El entero más pequeño soportado en esta versión de PHP. Habitualmente, int(-2147483648) en sistemas de 32 bits y int(-9223372036854775808) en sistemas de 64 bits. Habitualmente, PHP_INT_MIN === ~PHP_INT_MAX.

`PHP_INT_SIZE` (`int`)  
El tamaño de un entero, en bytes, en esta versión de PHP.

`PHP_FLOAT_DIG` (`int`)  
Número de dígitos decimales de precisión en un número de punto flotante y devueltos sin pérdida de precisión. Disponible desde PHP 7.2.0.

`PHP_FLOAT_EPSILON` (`float`)  
El número de punto flotante positivo más pequeño x, de modo que `x + 1.0 != 1.0`. Disponible desde PHP 7.2.0.

`PHP_FLOAT_MIN` (`float`)  
El número de punto flotante *positivo* más pequeño. Si necesita la representación *negativa* más pequeña de un número de punto flotante, use `- PHP_FLOAT_MAX`. Disponible desde PHP 7.2.0.

`PHP_FLOAT_MAX` (`float`)  
El número de punto flotante positivo más grande. Disponible desde PHP 7.2.0.

`DEFAULT_INCLUDE_PATH` (`string`)  

`PEAR_INSTALL_DIR` (`string`)  

`PEAR_EXTENSION_DIR` (`string`)  

`PHP_EXTENSION_DIR` (`string`)  
El directorio predeterminado donde buscar extensiones cargables dinámicamente (a menos que se sobrescriba con [extension_dir](#ini.extension-dir)). Por defecto `PHP_PREFIX` (o `PHP_PREFIX . "\\ext"` en Windows).

`PHP_PREFIX` (`string`)  
El valor de `--prefix` que se definió durante la configuración. En Windows, es el valor de `--with-prefix` que se definió durante la configuración.

`PHP_BINDIR` (`string`)  
El valor de `--bindir` que se definió durante la configuración. En Windows, es el valor de `--with-prefix` que se definió durante la configuración.

`PHP_SBINDIR` (`string`)  
El valor definido por `--sbindir` durante la configuración. En Windows, es el valor definido por `--with-prefix` durante la configuración. Disponible desde PHP 8.4.0.

`PHP_BINARY` (`string`)  
Especifica el camino hacia el binario de PHP durante la ejecución del script.

`PHP_MANDIR` (`string`)  
Especifica el camino de instalación de las páginas man.

> [!NOTE]
> Esta constante no está presente en las compilaciones de PHP para Windows.

`PHP_LIBDIR` (`string`)  

`PHP_DATADIR` (`string`)  

`PHP_SYSCONFDIR` (`string`)  

`PHP_LOCALSTATEDIR` (`string`)  

`PHP_CONFIG_FILE_PATH` (`string`)  

`PHP_CONFIG_FILE_SCAN_DIR` (`string`)  

`PHP_SHLIB_SUFFIX` (`string`)  
El sufijo de la plataforma de compilación para bibliotecas compartidas, como "so" (en sistemas Unix) o "dll" (en Windows).

`PHP_FD_SETSIZE` (`int`)  
Número máximo de descriptores de archivo para seleccionar funciones de sistema. Disponible desde PHP 7.1.0.

`E_ERROR` (`int`); `E_WARNING` (`int`); `E_PARSE` (`int`); `E_NOTICE` (`int`); `E_CORE_ERROR` (`int`); `E_CORE_WARNING` (`int`); `E_COMPILE_ERROR` (`int`); `E_COMPILE_WARNING` (`int`); `E_USER_ERROR` (`int`); `E_USER_WARNING` (`int`); `E_USER_NOTICE` (`int`); `E_RECOVERABLE_ERROR` (`int`); `E_DEPRECATED` (`int`); `E_USER_DEPRECATED` (`int`); `E_ALL` (`int`); `E_STRICT` (`int`)  
[Constantes de informe de errores](#errorfunc.constants).

`__COMPILER_HALT_OFFSET__` (`int`)  

`true` (`bool`)  
Ver [Booleanos](#language.types.boolean).

`false` (`bool`)  
Ver [Booleanos](#language.types.boolean).

`null` (`null`)  
Ver [Null](#language.types.null).

`PHP_WINDOWS_EVENT_CTRL_C` (`int`)  
Evento de Windows <span class="keycombo"> +CTRL+ +C+ </span>. Disponible desde PHP 7.4.0 (solo Windows).

`PHP_WINDOWS_EVENT_CTRL_BREAK` (`int`)  
Evento de Windows <span class="keycombo"> +CTRL+ +BREAK+ </span>. Disponible desde PHP 7.4.0 (solo Windows).

`PHP_CLI_PROCESS_TITLE` (`bool`)  
Indica si el establecimiento y la recuperación del título del proceso están disponibles. Disponible solo en la API CLI.

`STDERR` (`resource`)  
Un flujo ya abierto hacia `stderr`. Disponible solo en la API CLI.

`STDIN` (`resource`)  
Un flujo ya abierto hacia `stdin`. Disponible solo en la API CLI.

`STDOUT` (`resource`)  
Un flujo ya abierto hacia `stdout`. Disponible solo en la API CLI.

Véase también las [constantes mágicas](#language.constants.magic).
