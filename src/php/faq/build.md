---
title: Problemas de Compilación
source_url: https://www.php.net/manual/es/faq.build.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/build.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 1420
---

## Problemas de Compilación

Esta sección reune la mayoría de errores que ocurren al momento de compilar.

**Q:** Tengo la última versión de PHP usando el servicio anónimo Git, pero no hay un script de configuración.

**A:** Se tiene que tener el paquete autoconf de GNU instalado y así se podrá generar el script de configuración desde `configure.in`. Solo se ejecuta `./buildconf` en el directorio de nivel superior después de obtener los fuentes desde el servidor Git. (También, a menos que se ejecute `configure` con la opción `--enable-maintainer-mode`, el script de configuración no se recompilará automaticamente cuando el archivo `configure.in` es actualizado, así que debe de asegurarse que se hace manualmente cuando se note que `configure.in` haya cambiado. Un sintoma de esto es encontrar cosas como @VARIABLE@ en el archivo Makefile después de configurar o ejecutar `config.status`).

**Q:** Tengo problemas configurando PHP para que trabaje con Apache. Dice que no puede encontrar el `httpd.h`, pero esta justo donde digo que esta!

**A:** Se necesita decirle al script configure/setup de apache la ubicación del nivel superior del árbol origen. Esto significa que se debe especificar `--with-apache=/path/to/apache` y *no* `--with-apache=/path/to/apache/src`.

**Q:** Mientras se configura PHP (`./configure`), se devuelve un error similar al siguiente:

           checking lex output file root... ./configure: lex: command not found
           configure: error: cannot find output from lex; giving up
          

**A:** Se debe asegurar de leer cuidadosamente las instrucciones de [instalación](#install.unix) y notar que se necesita flex y bison instalados para compilar PHP. Dependiendo de la configuración, se necesitará instalar bison y flex desde el paquete de origen, como un RPM

**Q:** Cuando intento iniciar Apache, obtengo el siguiente mensaje:

           fatal: relocation error: file /path/to/libphp4.so:
           symbol ap_block_alarms: referenced symbol not found
          

**A:** Este error usualmente se da cuando un programa del núcleo de Apache se compila como una librería DS0 para uso compartido. Se debe reconfigurar apache, asegurándose de usar al menos una de los siguientes flags:

          --enable-shared=max --enable-rule=SHARED_CORE
          

Para mas información, leer el archivo de nivel superior de Apache `INSTALL` o las páginas del [manual sobre DSO](http://httpd.apache.org/docs/current/dso.html).

**Q:** Cuando ejecuto la configuración, dice que no puede encontrar los archivos o librerías para GD, gdbm, o algún otro paquete!

**A:** Se puede configurar el script para que busque los archivos de encabezados y librerías en ubicaciones no estándar para especificar flags adicionales para ser pasados al preprocesador y compilador C, como:

        CPPFLAGS=-I/path/to/include LDFLAGS=-L/path/to/library ./configure

          

Si se esta usando una variante de csh como login shell (por qué?), debería de ser:

        env CPPFLAGS=-I/path/to/include LDFLAGS=-L/path/to/library ./configure

          

**Q:** Cuando se esta compilando el archivo `language-parser.tab.c`, da errores así `yytname undeclared`.

**A:** Se debe actualizar la versión de Bison. Se puede encontrar la ultima versión en <http://www.gnu.org/software/bison/bison.html>.

**Q:** Cuando ejecuto `make`, parece que se ejecuta bien, pero luego falla cuando intenta enlazar la aplicación final quejandose de que faltan algunos archivos.

**A:** Algunas versiones antiguas de make no colocan correctamente las versiones compiladas de archivos y funciones de directorio en el mismo directorio. Se debe intentar ejecutar las `funciones cp *.o` y entonces re-ejecutar `make` para ver si eso ayuda. Si no lo hace, realmente se debería actualizar a la versión más reciente de GNU Make.

**Q:** Cuando se enlaza PHP, se queja del número de referencias indefenidas.

**A:** Hay que mirar la linea del enlace y asegurarse de que todas las librerías apropiadas han sido incluidas al final. Las mas comunes que podrían estar perdidas son las '-ldl' y librerías requeridas como soporte por cualquier base de datos que se haya incluido.

Algunas personas han reportado que han tenido que adicionar '-ldl' inmediatamente seguido por `libphp4.a` cuando enlazan con Apache.

**Q:** He seguido todos los pasos para instalar la versión del módulo de Apache en Unix, y cuando mis scripts de PHP aparecen se me pregunta por guardar el archivo.

**A:** Esto significa que el módulo de PHP no esta siendo invocado por alguna razón. Hay tres cosas que chequear antes de pedir ayuda:

- Asegurarse que el binario del httpd que se esta ejecutando es el nuevo binario httpd que se acaba de hacer. Para ver esto, se debe intentar ejecutar: `/path/to/binary/httpd -l`

  Si no se ve `mod_php4.c` listado, entonces no se esta ejecutando el binario correcto. Hay que encontrarlo e instalar el binario correcto.

- Asegurarse de que es agregado el Mime Type correcto en uno de los archivos de `Apache .conf`. Debería de ser: `AddType application/x-httpd-php .php`

  También asegurarse que esta línea AddType no esta oculta dentro de un bloque de \<Virtualhost\> o uno de \<Directory\> el cual podría evitar que se aplique en el lugar donde se prueba el script.

- Por último, el lugar por defecto de los archivos de configuración de Apache cambio entre Apache 1.2 y Apache 1.3. Se debería chequear que el archivo de configuración al cual se le agrega la línea AddType esta siendo leído actualmente. Se puede poner un error de sintaxis obvio dentro del archivo `httpd.conf` o algún otro cambio que pueda decir si el archivo esta siendo leído de forma correcta.

**Q:** Dice que use: `--activate-module=src/modules/php4/libphp4.a`, pero ese archivo no existe, asi que lo cambie a `--activate-module=src/modules/php4/libmodphp4.a` y no funciona!? que esta pasando?

**A:** Hay que tener en cuenta que el archivo `libphp4.a` no se supone que exista. El proceso de apache sera creado!.

**Q:** Cuando intento compilar Apache con PHP como un módulo estatico usando `--activate-module=src/modules/php4/libphp4.a` me dice que mi compilador no es compatible con ANSI.

**A:** Este es un mensaje de error equivocado de Apache que ha sido corregido en las versiones mas recientes.

**Q:** Cuando intento compilar PHP usando `--with-apxs` obtengo mensajes de error extraños.

**A:** Hay 3 cosas que chequear aqui. Primero, por alguna razón cuando Apache compila el script de Perl apxs, algunas veces termina compilandose sin el compilador apropiado y sin los flags correspondientes. Hay que encontrar el script apxs (intentar con el comando `which apxs`), algunas veces se encuentra en `/usr/local/apache/bin/apxs` o `/usr/sbin/apxs`. Abrirlo y revisar las líneas similares a estas:

    my $CFG_CFLAGS_SHLIB  = ' ';          # substituted via Makefile.tmpl
    my $CFG_LD_SHLIB      = ' ';          # substituted via Makefile.tmpl
    my $CFG_LDFLAGS_SHLIB = ' ';          # substituted via Makefile.tmpl

          

Si esto es lo que se ve, se ha encontrado el problema. Podrían contener espacios u otros valores incorrectos, como 'q()'. Hay que cambiar esas linas para que digan:

    my $CFG_CFLAGS_SHLIB  = '-fpic -DSHARED_MODULE'; # substituted via Makefile.tmpl
    my $CFG_LD_SHLIB      = 'gcc';                   # substituted via Makefile.tmpl
    my $CFG_LDFLAGS_SHLIB = q(-shared);              # substituted via Makefile.tmpl

          

El segundo problema posible podría ser un caso único en Red Hat 6.1 y 6.2. El script apxs de Red Hat esta malo. Hay que ver esta línea:

    my $CFG_LIBEXECDIR    = 'modules';         # substituted via APACI install

          

Si se ve como la línea anterior, hay que cambiarla por:

    my $CFG_LIBEXECDIR    = '/usr/lib/apache'; # substituted via APACI install

          

Por último, si se reconfigura/reinstala Apache, hay que agregar un `make clean` al proceso después de `./configure` y antes de `make`.

**Q:** Durante el `make`, obtengo errores sobre microtime, y muchas cosas de `RUSAGE_`.

**A:** Durante la parte de la instalación de `make`, si se encuentran problemas que se vean similares a esto:

    microtime.c: In function `php_if_getrusage':
    microtime.c:94: storage size of `usg' isn't known
    microtime.c:97: `RUSAGE_SELF' undeclared (first use in this function)
    microtime.c:97: (Each undeclared identifier is reported only once
    microtime.c:97: for each function it appears in.)
    microtime.c:103: `RUSAGE_CHILDREN' undeclared (first use in this function)
    make[3]: *** [microtime.lo] Error 1
    make[3]: Leaving directory `/home/master/php-4.0.1/ext/standard'
    make[2]: *** [all-recursive] Error 1
    make[2]: Leaving directory `/home/master/php-4.0.1/ext/standard'
    make[1]: *** [all-recursive] Error 1
    make[1]: Leaving directory `/home/master/php-4.0.1/ext'
    make: *** [all-recursive] Error 1

          

Significa que el sistema esta mal. Se necesita corregir los archivos `/usr/include` instalando el paquete glibc-devel que coincida con tu glibc. Esto no tiene nada que ver con PHP. Para comprobar esto, hay que hacer esta simple prueba:

    $ cat >test.c <<X
    #include <sys/resource.h>
    X
    $ gcc -E test.c >/dev/null

          

Si esto produce errores, se sabrá que los archivos incluidos están mal.

**Q:** Cuando compilo PHP con MySQL, la configuración se ejecuta bien, pero durante el `make` obtengo un error similar al siguiente: *ext/mysql/libmysqlclient/my_tempnam.o(.text+0x46): In function my_tempnam': /php4/ext/mysql/libmysqlclient/my_tempnam.c:103: the use of tempnam' is dangerous, better use mkstemp'*, ¿Qué esta mal?

**A:** Primero, es importante darse cuenta que esto es un `Warning` y no un error fatal. Debido a que esto es la última salida vista durante el `make`, podría verse como un error fatal pero no lo es. Por supuesto, si se ha puesto el compilador a que pare en los Warnings, lo hará. También hay que tener en mente que el soporte por MySQL es habilitado por defecto.

> [!NOTE]
> Como en PHP 4.3.2, se verá el siguiente texto después de que se complete la compilación (make):
>
>             Compilación completada.
>             (Es seguro hacer caso omiso de las advertencias sobre tempnam y tmpnam).
>            

**Q:** Si deseo actualizar mi PHP. ¿Donde puedo encontrar la línea `./configure` que fue usada para compilar mi instalación actual de PHP?

**A:** Si se mira el archivo config.nice, en el árbol origen de la instalación actual de PHP o, si esto no esta disponible, simplemente se debe ejecutar un script con

```php
       <?php phpinfo(); ?>

      
```

Al inicio de la salida se mostrará la línea `./configure` que fue usada para compilar la instalación de PHP.

**Q:** Cuando compilo PHP con la librería GD, también da errores raros de compilación o segfaults en la ejecución.

**A:** Hay que asegurar que la librería GD y PHP estan enlazados contra las mismas librerías dependientes (ej: libpng).

**Q:** Cuando compilo PHP parece que recibo errores al azar, como si se colgara. Estoy usando Solaris si eso importa.

**A:** Usando utilidades no-GNU mientras se compila PHP podría causar problemas. Hay que asegurarse de usar herramientas GNU para estar seguros que la compilación de PHP funcionará. Por ejemplo, en Solaris, usando el SunOS BSD-compatible o versiones de Solaris de `sed` no funcionará, pero usando las versiones GNU o Sun POSIX (xpg4) de `sed` hará que funcione. Enlaces: [GNU sed](http://www.gnu.org/software/sed/sed.html), [GNU flex](http://www.gnu.org/software/flex/flex.html), y [GNU bison](http://www.gnu.org/software/bison/bison.html).
