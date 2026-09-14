---
title: Instalación de extensiones PECL
source_url: https://www.php.net/manual/es/install.pecl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/pecl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: false
translation_revision: d1fa30969
order: 1760
---

## Instalación de extensiones PECL

## Introducción a las instalaciones PECL

> [!NOTE]
> El instalador de Extensiones para PHP (PHP Installer for Extensions - PIE) es una nueva herramienta que reemplazará PECL. Recomendamos usar PIE para instalar extensiones. Más información en <https://github.com/php/pie>

[PECL](https://pecl.php.net/) es un repositorio de extensiones PHP que están disponibles a través del sistema de empaquetado [PEAR](https://pear.php.net/). Esta sección del manual está destinada a demostrar cómo obtener e instalar extensiones PECL.

Estas instrucciones asumen que `/path/to/php/src/dir/` es la ruta a la distribución del código fuente de PHP y que `extname` es el nombre de la extensión PECL. Ajuste según corresponda. Estas instrucciones también asumen familiaridad con el [comando pear](https://pear.php.net/manual/en/guide.users.commandline.cli.php). La información en el manual de PEAR para el comando `pear` también se aplica al comando `pecl`.

Una extensión compartida debe ser compilada, instalada y cargada para ser útil. Los métodos descritos a continuación proporcionan varias instrucciones sobre cómo compilar e instalar las extensiones, pero no las cargan automáticamente. Las extensiones pueden cargarse añadiendo una directiva [extension](#ini.extension) al fichero `php.ini` o mediante el uso de la función `dl`.

Al compilar módulos PHP, es importante tener versiones conocidas y buenas de las herramientas requeridas (autoconf, automake, libtool, etc.). Consulte las [Instrucciones de Git Anónimo](https://www.php.net/git.php) para obtener detalles sobre las herramientas requeridas y las versiones necesarias.

## Descarga de extensiones PECL

> [!NOTE]
> El instalador de Extensiones para PHP (PHP Installer for Extensions - PIE) es una nueva herramienta que reemplazará PECL. Recomendamos usar PIE para instalar extensiones. Más información en <https://github.com/php/pie>

Hay varias opciones para descargar extensiones PECL, como:

- El comando `pecl install extname` descarga el código de la extensión automáticamente, por lo que en este caso no es necesaria una descarga separada.

- <https://pecl.php.net/>

  El sitio web de PECL contiene información sobre las diferentes extensiones que ofrece el Equipo de Desarrollo de PHP. La información disponible aquí incluye: registro de cambios, notas de la versión, requisitos y otros detalles similares.

- `pecl download extname`

  Las extensiones PECL que tienen versiones publicadas en el sitio web de PECL están disponibles para descarga e instalación usando el [comando pecl](https://pear.php.net/manual/en/guide.users.commandline.cli.php). También pueden especificarse revisiones específicas.

- git

  Muchas extensiones PECL residen en GitHub.

- SVN

  Algunas extensiones PECL también residen en SVN. Una vista basada en web puede verse en <https://svn.php.net/pecl/>. Para descargar directamente desde SVN, puede usarse la siguiente secuencia de comandos:

      $ svn checkout https://svn.php.net/repository/pecl/extname/trunk extname

          

- Descargas para Windows

  El proyecto PHP compila y ofrece DLLs de Windows para la mayoría de las extensiones PECL en la página del paquete.

## Instalación de una extensión PHP en Windows

Hay dos formas de cargar una extensión PHP en Windows: compilarla en PHP o cargar la DLL. Cargar una extensión precompilada es la forma más fácil y preferida.

Para cargar una extensión, debe estar disponible como un fichero `.dll` en el sistema. Todas las extensiones son compiladas automáticamente y periódicamente por el Grupo PHP (consulte la siguiente sección para la descarga).

Para compilar una extensión en PHP, consulte la documentación de [compilación desde el código fuente](#install.windows.building).

Para compilar una extensión independiente (también conocida como un fichero DLL), consulte la documentación de [compilación desde el código fuente](#install.windows.building). Si el fichero DLL no está disponible ni con la distribución de PHP ni en PECL, puede ser necesario compilarlo antes de que la extensión pueda usarse.

### ¿Dónde encontrar una extensión?

Las extensiones PHP suelen llamarse `php_*.dll` (donde el asterisco representa el nombre de la extensión), y se encuentran en la carpeta `PHP\ext`.

PHP incluye las extensiones más útiles para la mayoría de los desarrolladores. Se llaman extensiones *incluidas*.

Sin embargo, si las extensiones incluidas no proporcionan la funcionalidad necesaria, aún puede encontrarse una extensión que lo haga en [PECL](https://pecl.php.net/). La Biblioteca de Extensiones de la Comunidad PHP (PECL) es un repositorio para Extensiones PHP, que proporciona un directorio de todas las extensiones conocidas y ofrece instalaciones para descargar y desarrollar extensiones PHP.

Si una extensión ha sido desarrollada para usos particulares, puede estar alojada en PECL para que otros con las mismas necesidades puedan beneficiarse de ella. Un buen efecto secundario es que es una buena oportunidad para recibir comentarios, (con suerte) agradecimientos, informes de errores e incluso correcciones/parches. Antes de enviar una extensión para alojarla en PECL, lea [PECL submit](https://pecl.php.net/package-new.php).

### ¿Qué extensión descargar?

*Muchas veces, habrá varias versiones de cada DLL disponibles:*

- Diferentes números de versión (al menos los dos primeros números deben coincidir)

- Diferentes configuraciones de seguridad de hilos

- Diferentes arquitecturas de procesador (x86, x64, ...)

- Diferentes configuraciones de depuración

- `etc.`

Tenga en cuenta que la configuración de la extensión debe coincidir con todas las configuraciones de el ejecutable de PHP que se está utilizando. El siguiente script PHP informará *todo* sobre la configuración de PHP:

Llamada a `phpinfo`

```php
<?php
phpinfo();
?>

     
```

O desde la línea de comandos, ejecute:

    drive:\path\to\php\executable\php.exe -i

        

### Carga de una extensión

La forma más común de cargar una extensión PHP es incluirla en el fichero de configuración `php.ini`. Tenga en cuenta que muchas extensiones ya están presentes en el `php.ini` y que solo es necesario eliminar el punto y coma para activarlas.

Tenga en cuenta que, a partir de PHP 7.2.0, puede usarse el nombre de la extensión en lugar del nombre del fichero de la extensión. Al ser independiente del sistema operativo y más fácil, especialmente para los recién llegados, se convierte en la forma recomendada de especificar las extensiones a cargar. Los nombres de fichero siguen siendo compatibles con versiones anteriores.

    ;extension=php_extname.dll

       

    extension=php_extname.dll

       

    ; A partir de PHP 7.2.0, se prefiere:
    extension=extname
    zend_extension=another_extension

       

Sin embargo, algunos servidores web son confusos porque no usan el `php.ini` ubicado junto al ejecutable de PHP. Para averiguar dónde reside el `php.ini` real, busque su ruta en `phpinfo`:

    Configuration File (php.ini) Path  C:\WINDOWS

       

    Loaded Configuration File   C:\Program Files\PHP\8.2\php.ini

       

Después de activar una extensión, guarde `php.ini`, reinicie el servidor web y verifique `phpinfo` nuevamente. La nueva extensión debería tener ahora su propia sección.

### Resolución de problemas

Si la extensión no aparece en `phpinfo`, deben revisarse los registros para saber de dónde proviene el problema.

Si PHP se está utilizando desde la línea de comandos (CLI), el error de carga de la extensión puede leerse directamente en la pantalla.

Si PHP se está utilizando con un servidor web, la ubicación y el formato de los registros varían según el software. Lea la documentación del servidor web para localizar los registros, ya que no tiene nada que ver con PHP en sí.

Los problemas comunes son la ubicación de la DLL y las DLLs de las que depende, el valor de la configuración "[extension_dir](#ini.extension-dir)" dentro de `php.ini` y las incompatibilidades en la configuración de compilación.

Si el problema radica en una incompatibilidad en la configuración de compilación, probablemente la DLL descargada no es la correcta. Intente descargar la extensión nuevamente con la configuración adecuada. Nuevamente, `phpinfo` puede ser de gran ayuda.

## Compilación de extensiones PECL compartidas con el comando pecl

PECL facilita la creación de extensiones PHP compartidas. Usando el [comando pecl](https://pear.php.net/manual/en/guide.users.commandline.cli.php), haga lo siguiente:

    $ pecl install extname

      

Esto descargará el código fuente de *extname*, lo compilará e instalará `extname.so` en el [extension_dir](#ini.extension-dir). `extname.so` luego puede cargarse a través de `php.ini`.

Por omisión, el comando `pecl` no instalará paquetes que estén marcados con el estado `alpha` o `beta`. Si no hay paquetes `stable` disponibles, puede instalarse un paquete `beta` usando el siguiente comando:

    $ pecl install extname-beta

      

También puede instalarse una versión específica usando esta variante:

    $ pecl install extname-0.1

      

> [!NOTE]
> Después de habilitar la extensión en `php.ini`, es necesario reiniciar el servicio web para que los cambios surtan efecto.

## Compilación de extensiones PECL compartidas con phpize

A veces, usar el instalador `pecl` no es una opción. Esto podría deberse a que hay un firewall o porque la extensión que se está instalando no está disponible como un paquete compatible con PECL, como extensiones no publicadas de git. Si es necesario compilar dicha extensión, se pueden usar las herramientas de compilación de bajo nivel para realizar la compilación manualmente.

El comando `phpize` se utiliza para preparar el entorno de compilación para una extensión PHP. En el siguiente ejemplo, los fuentes de una extensión están en un directorio llamado `extname`:

    $ cd extname
    $ phpize
    $ ./configure
    $ make
    # make install

       

Una instalación exitosa habrá creado `extname.so` y lo habrá colocado en el directorio de extensiones de PHP [extensions directory](#ini.extension-dir). El `php.ini` deberá ajustarse y se deberá añadir una línea `extension=extname.so` antes de que la extensión pueda usarse.

Si el sistema no tiene el comando `phpize`, y se usan paquetes precompilados (como RPMs), asegúrese de instalar también la versión de desarrollo adecuada del paquete PHP, ya que a menudo incluyen el comando `phpize` junto con los ficheros de cabecera adecuados para compilar PHP y sus extensiones.

Ejecute `phpize --help` para mostrar información adicional de uso.

## `php-config`

`php-config` es un script de shell simple para obtener información sobre la configuración instalada de PHP.

Cuando las extensiones se están compilando, si hay varias versiones de PHP instaladas, la instalación para la cual se va a compilar puede especificarse usando la opción `--with-php-config` durante la configuración, estableciendo la ruta del script respectivo `php-config`.

La lista de opciones de línea de comandos proporcionadas por el script `php-config` puede consultarse en cualquier momento ejecutando `php-config` con el modificador `-h`:

    Usage: /usr/local/bin/php-config [OPTION]
    Options:
      --prefix            [...]
      --includes          [...]
      --ldflags           [...]
      --libs              [...]
      --extension-dir     [...]
      --include-dir       [...]
      --php-binary        [...]
      --php-sapis         [...]
      --configure-options [...]
      --version           [...]
      --vernum            [...]

       

| Opción | Descripción |
|----|----|
| --prefix | Prefijo del directorio donde está instalado PHP, p. ej. /usr/local |
| --includes | Lista de opciones `-I` con todos los ficheros de inclusión |
| --ldflags | `LD` flags con los que se compiló PHP |
| --libs | Bibliotecas adicionales con las que se compiló PHP |
| --extension-dir | Directorio donde se buscan las extensiones por omisión |
| --include-dir | Prefijo del directorio donde se instalan los ficheros de cabecera por omisión |
| --php-binary | Ruta completa al binario CLI o CGI de php |
| --php-sapis | Mostrar todos los módulos SAPI disponibles |
| --configure-options | Opciones de configuración para recrear la configuración de la instalación actual de PHP |
| --version | Versión de PHP |
| --vernum | Versión de PHP como entero |

Opciones de línea de comandos

## Compilación de extensiones PECL estáticamente en PHP

Puede ser necesario compilar una extensión PECL estáticamente en el binario de PHP. Para hacerlo, el código fuente de la extensión deberá colocarse bajo el directorio `/path/to/php/src/dir/ext/`, y el sistema de compilación de PHP deberá regenerar su script de configuración.

    $ cd /path/to/php/src/dir/ext
    $ pecl download extname
    $ gzip -d < extname.tgz | tar -xvf -
    $ mv extname-x.x.x extname

       

Esto dará como resultado el siguiente directorio:

    /path/to/php/src/dir/ext/extname

      

Desde aquí, PHP necesita ser forzado a reconstruir el script de configuración, y luego puede ser compilado normalmente:

    $ cd /path/to/php/src/dir
    $ rm configure
    $ ./buildconf --force
    $ ./configure --help
    $ ./configure --with-extname --enable-someotherext --with-foobar
    $ make
    $ make install

      

> [!NOTE]
> Para ejecutar el script `buildconf`, se necesitarán `autoconf` `2.68` y `automake` `1.4+`. Versiones más recientes de `autoconf` pueden funcionar pero no están soportadas.

Si se usa `--enable-extname` o `--with-extname` depende de la extensión. Normalmente, una extensión que no requiere bibliotecas externas usa `--enable`. Para estar seguro, ejecute lo siguiente después de `buildconf`:

    $ ./configure --help | grep extname
