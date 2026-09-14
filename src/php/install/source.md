---
title: Instalación desde las fuentes en sistemas Unix y macOS
source_url: https://www.php.net/manual/es/install.unix.source.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/source.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: 1c9fb1265
order: 1890
---

## Instalación desde las fuentes en sistemas Unix y macOS

Software requerido para la compilación: [GNU `make`](https://www.gnu.org/software/make/make.html), Un compilador C (a partir de PHP 8.0.0, se requiere compatibilidad con C99; a partir de PHP 8.4.0, se requiere compatibilidad con C11), Un servidor web, Cualquier componente específico de un módulo (como las bibliotecas GD, PDF, etc.)

Cuando la compilación se realiza directamente desde las fuentes de Git o después de modificaciones personalizadas, pueden ser necesarias estas herramientas adicionales:

- [autoconf](https://www.gnu.org/software/autoconf/autoconf.html):

  PHP 7.3 y más reciente: 2.68+
  PHP 7.2: 2.64+
  PHP 7.1 y más antiguo: 2.59+

- [re2c](https://re2c.org/):

  PHP 8.3 y más reciente: 1.0.3+
  PHP 8.2 y más antiguo: 0.13.4+

- [bison](http://www.gnu.org/software/bison/bison.html):

  PHP 7.4 y más reciente: 3.0.0+
  PHP 7.3 y más antiguo: 2.4+ (incluido Bison 3.x)

Para obtener pasos más detallados para compilar PHP desde el código fuente, véase el fichero [README.md](https://github.com/php/php-src/blob/master/README.md) en el archivo tarball de origen.

La configuración y el proceso inicial de compilación de PHP están controlados por el uso de las opciones de línea de comandos del script `configure`. Una lista de las opciones disponibles con breves explicaciones puede mostrarse ejecutando `./configure --help`. Este manual documenta las diferentes opciones por separado. Las [opciones básicas están disponibles en el apéndice](#configure.about), mientras que las diferentes opciones específicas de las extensiones están descritas en las páginas de referencia.

Después de que el script de configuración se haya ejecutado, PHP puede ser compilado usando el comando `make`. El [ capítulo de preguntas frecuentes sobre la instalación ](#faq.installation) contiene más información sobre cómo manejar los problemas de compilación.

> [!NOTE]
> Algunos sistemas Unix (como OpenBSD y SELinux) pueden prohibir el mapeo de páginas tanto en escritura como en ejecución por razones de seguridad, lo cual se llama [PaX MPROTECT](https://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options#Restrict_mprotect()) o [protección contra las violaciones W^X](https://en.wikipedia.org/wiki/W^X). Este tipo de mapeo de memoria es necesario para el soporte JIT de PCRE, por lo tanto PHP debe ser compilado [sin el soporte JIT de PCRE](#pcre.installation), o el binario debe ser incluido en la lista blanca por cualquier medio proporcionado por el sistema.

> [!NOTE]
> La compilación cruzada para ARM con la cadena de herramientas de Android no es actualmente soportada.
