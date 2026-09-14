---
title: Consiguiendo PHP
source_url: https://www.php.net/manual/es/faq.obtaining.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/obtaining.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 1500
---

## Consiguiendo PHP

Esta sección contiene detalles sobre las ubicaciones de descarga de PHP, y asuntos específicos a diferentes sistemas operativos.

**Q:** ¿Donde puedo conseguir PHP?

**A:** Se puede descargar PHP desde cualquier miembro de la red de Sitios de PHP. Estos se pueden encontrar en <https://www.php.net/>. También puede utilizar Git anónimo para conseguir la última versión del código fuente. Para mayor información, visite <https://www.php.net/git.php>.

**Q:** ¿Hay versiones binarias pre-compiladas disponibles?

**A:** Nosotros solo distribuímos binarios pre-compilados para sistemas Windows, debido a que no tenemos la capacidad de compilar PHP para cada plataforma popular Linux/Unix con todas las combinaciones de extensiones. También tenga en cuenta que muchas distribuciones Linux actualmente vienen con PHP integrado. Los binarios para Windows pueden ser descargados desde nuestra página de [Descargas](https://www.php.net/downloads.php). Para binarios de Linux, por favor visite el sitio de su distribución.

**Q:** ¿Donde consigo las bibliotecas requeridas para compilar algunas de las extensiones opcionales de PHP?

> [!NOTE]
> Aquellas marcadas con \* no son seguras a nivel de hilos; no se recomienda su uso en entornos multihilo.

- [LDAP (Unix)](https://www.openldap.org/software/download/).

- [LDAP (Unix/Win)](https://wiki.mozilla.org/LDAP_C_SDK) : Directorio de Mozilla (LDAP) SDK

- [servidor LDAP libre](http://www.bind9.net/download-openldap/).

- [Berkeley DB2 (Unix/Win)](http://www.sleepycat.com/) : http://www.sleepycat.com/.

- [SNMP\* (Unix): ](http://www.net-snmp.org/).

- [GD (Unix/Win)](http://www.libgd.org/).

- [mSQL\* (Unix)](https://hughestech.com.au/products/msql/).

- [PostgreSQL (Unix)](http://www.postgresql.org/).

- [IMAP\* (Win/Unix)](https://github.com/uw-imap/imap).

- [Sybase-CT\* (Linux, libc5)](http://www.sybase.com/) : Disponible localmente.

- [FreeType (libttf):](http://www.freetype.org/).

- [ZLib (Unix/Win32)](http://www.zlib.net/).

- [expat XML parser (Unix/Win32)](https://libexpat.github.io/).

- [PDFLib](http://www.pdflib.com/products/pdflib-family/).

- [mcrypt](http://mcrypt.sourceforge.net/).

- [mhash](http://mhash.sourceforge.net/).

- [t1lib](http://www.ibiblio.org/pub/Linux/libs/graphics/).

- [dmalloc](http://dmalloc.com/).

- [aspell](http://aspell.net/).

- [libedit](http://www.thrysoee.dk/editline/).

**Q:** ¿Cómo hago para que esas bibliotecas funcionen?

**A:** Necesitará seguir las instrucciones provistas en la biblioteca. Algunas de estas bibliotecas son detectadas automáticamente cuando ejecuta el script 'configure' de PHP (tal como la biblioteca GD), y otras tendran que ser habilitadas usando opciones '`--with-EXTENSION`' con '`configure`'. Ejecute '`configure --help`' para una lista de estas opciones.

**Q:** He conseguido la última versión del código fuente de PHP desde el repositorio Git en mi máquina Windows, ¿Qué necesito para su compilación?

**A:** Consulte el Wiki de PHP para las últimas instrucciones: [Instrucciones de construcción paso a paso](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)

**Q:** ¿Dónde consigo el Archivo de Capacidades del Explorador?

**A:** Se puede encontrar el archivo `browscap.ini` en <http://browscap.org/>.

**Q:** ¿Que significa thread safety cuando se descarga PHP?

**A:** Thread Safety significa que el binario puede funcionar en un servidor multi-hilo como por ejemplo bajo Apache 2 para windows.Thread Safety funciona creando una copia local de almacenamiento para cada hilo, de manera que los datos no colisionarán con otros hilos.

Entonces ¿que necesito? Si se elige ejecutar PHP como binario CGI, entonces no se necesita thread safety, por que el binario es invocado en cada petición. Para servidores multi-hilo, como IIS5 y IIS6 se debe utilizar la versión threaded de PHP.
