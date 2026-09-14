---
title: Otras opciones
source_url: https://www.php.net/manual/es/configure.options.misc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/configure/misc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 4c676dacf
order: 50
---

### Otras opciones

`--enable-debug`  
Compilar con símbolos de depuración.

`--with-layout=TYPE`  
Establecer la forma de presentar los ficheros instalados. El tipo es PHP (predeterminado) o GNU. Se debe tener en cuenta que si se instalan las páginas de manual bajo PREFIX (predeterminado), se debe elegir el estilo GNU para que puedan ser encontradas en la ruta de búsqueda de la utilidad `manpath`.

`--with-pear=DIR`  
Instalar PEAR en DIR (valor predeterminado PREFIX/lib/php).

`--without-pear`  
No instalar PEAR.

`--enable-sigchild`  
Habilitar el propio manejador SIGCHLD de PHP.

`--disable-rpath`  
Deshabilitar el paso de rutas adicionales de búsqueda de bibliotecas en tiempo de ejecución.

`--enable-libgcc`  
Habilitar explícitamente el enlazado con libgcc.

`--enable-php-streams`  
Incluir flujos de PHP experimentales. No usar a menos que se esté probando el código.

`--with-zlib-dir[=DIR]`  
Definir la localización del directorio de instalación de zlib.

`--with-tsrm-pthreads`  
Usar hilos de POSIX (predeterminado).

`--enable-shared[=PKGS]`  
Construir bibliotecas compartidas \[predeterminado=yes\].

`--enable-static[=PKGS]`  
Construir bibliotecas estáticas \[predeterminado=yes\].

`--enable-fast-install[=PKGS]`  
Optimizar para una instalación rápida \[predeterminado=yes\].

`--with-gnu-ld`  
Asumir que el compilador de C usa ld de GNU \[predeterminado=no\].

`--disable-libtool-lock`  
Evitar bloqueos (podría romper construcciones en paralelo).

`--with-pic`  
Intentar usar solo objetos PIC/no PIC \[predeterminado=use both\].

`--enable-versioning`  
Exportar solo los símbolos requeridos. Véase INSTALL para más información.
