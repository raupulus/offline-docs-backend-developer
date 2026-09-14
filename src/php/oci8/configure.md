---
title: Instalación
source_url: https://www.php.net/manual/es/oci8.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 5e41012cf
order: 57110
---

## Instalación

## Configuración de PHP con OCI8

Revísese la sección anterior sobre los [Requisitos previos](#oci8.requirements) antes de configurar OCI8.

Antes de iniciar el servidor web, OCI8, típicamente, requiere varias variables de entorno (ver a continuación) para localizar las bibliotecas, para apuntar a archivos de configuración, y para definir algunas propiedades básicas como el juego de caracteres utilizado por las bibliotecas OCI8. Las variables deben ser definidas *antes* del inicio de cualquier proceso PHP.

El binario PHP debe ser enlazado con las mismas (o versiones más recientes) de las bibliotecas Oracle para las cuales ha sido configurado. Por ejemplo, si se compila OCI8 con las bibliotecas Oracle 19, entonces PHP también debe ser desplegado y ejecutado con las bibliotecas Oracle 19. Las aplicaciones PHP pueden conectarse a otras versiones de bases de datos Oracle, sabiendo que Oracle contiene compatibilidades de versiones de los diferentes clientes - servidores.

## Instalación de OCI8 desde PECL utilizando el comando pecl

La extensión OCI8 puede ser añadida a una instalación PHP existente utilizando el repositorio [PECL](https://pecl.php.net/package/oci8).

- Si se encuentra detrás de un firewall, defínase el proxy de PEAR, por ejemplo:

      pear config-set http_proxy http://my-proxy.example.com:80/

- Ejecútese:

      pecl install oci8

  Para PHP 7, utilícese `pecl install oci8-2.2.0`.

- Cuando se le solicite, introdúzcase el valor de `$ORACLE_HOME` o `instantclient,/ruta/al/directorio/instant/client/lib`.

  Nota: No se introduzcan nombres de variables como `$ORACLE_HOME` o `$HOME` ya que `pecl` no los expandirá. En su lugar, introdúzcase una ruta expandida, por ejemplo `/opt/oracle/product/19c/dbhome_1` o `instantclient,/Users/monnom/Descargas/instantclient_19_8`.

- Si se obtiene un error `oci8_dtrace_gen.h: No existe el archivo o directorio`, esto significa que PHP ha sido compilado con [DTrace Dynamic Tracing](#features.dtrace) activado. Instálese utilizando el comando:

      $ export PHP_DTRACE=yes
      $ pecl install oci8

- Modifíquese el archivo `php.ini` y añádase la línea:

      extension=oci8.so

  Asegúrese de que la directiva `php.ini` [extension_dir](#ini.extension-dir) está definida en el directorio en el cual `oci8.so` ha sido instalado.

## Instalación de OCI8 desde PECL utilizando phpize

Para instalar OCI8 en una instalación PHP existente cuando el comando `pecl` no está disponible, descárguese manualmente el paquete OCI8 [PECL](https://pecl.php.net/package/oci8), por ejemplo `oci8-3.0.0.tgz`.

- Extraer el paquete:

      tar -zxf oci8-3.0.0.tgz
      cd oci8-3.0.0

- Preparar el paquete:

      phpize

- Configurar el paquete utilizando `$ORACLE_HOME` o Instant Client.

      ./configure -with-oci8=shared,$ORACLE_HOME

  o

      ./configure -with-oci8=shared,instantclient,/ruta/a/instant/client/lib

- Instalar el paquete:

      make install

- Si se obtiene un error `oci8_dtrace_gen.h: No existe el archivo o directorio`, esto significa que PHP ha sido compilado con [DTrace Dynamic Tracing](#features.dtrace) activado. Ejecútese nuevamente los comandos `configure` y `make` después de haber definido esta variable de entorno:

      $ export PHP_DTRACE=yes

- Modifíquese el archivo `php.ini` y añádase la línea:

      extension=oci8.so

  Asegúrese de que la directiva `php.ini` [extension_dir](#ini.extension-dir) está configurada en el directorio en el cual `oci8.so` ha sido instalado.

## Instalación de OCI8 como extensión compartida durante la compilación de PHP

Si se compila PHP a partir del código fuente, la opción de configuración `shared` puede ser utilizada para construir OCI8 como una biblioteca compartida que puede ser cargada dinámicamente en PHP. La construcción de una extensión compartida permite a OCI8 ser fácilmente actualizado sin afectar al resto de PHP.

Configúrese OCI8 utilizando una de las siguientes opciones de configuración.

- Si se utilizan las bibliotecas gratuitas [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html), hágase lo siguiente:

      ./configure --with-oci8=shared,instantclient,/ruta/a/instant/client/lib

  Si Instant Client 12.2 (o una versión anterior) está instalado a partir de archivos ZIP, asegúrese de crear primero el enlace simbólico a la biblioteca, por ejemplo `ln -s libclntsh.so.12.1 libclntsh.so`.

  Si se utiliza una instalación basada en RPM de Oracle Instant Client, la línea de configuración se verá así:

      ./configure --with-oci8=shared,instantclient,/usr/lib/oracle/<version>/client/lib

  Por ejemplo, `--with-oci8=shared,instantclient,/usr/lib/oracle/19.9/client/lib`

- Si se utiliza una base de datos Oracle o una instalación completa de Oracle Client, procedase de la siguiente manera:

      ./configure --with-oci8=shared,$ORACLE_HOME

  Asegúrese de que el usuario del servidor web (`nobody`, `www`) tiene acceso a las bibliotecas, a los archivos de inicialización y al archivo `tnsnames.ora` (si se utiliza) bajo el directorio `$ORACLE_HOME`. Con Oracle 10*g*R2, puede que sea necesario ejecutar la utilidad `$ORACLE_HOME/install/changePerm.sh` para dar acceso al directorio.

Después de la configuración, sigase el procedimiento habitual de compilación de PHP, por ejemplo *make install*. La extensión compartida OCI8 `oci8.so` será creada. Puede ser necesario moverla manualmente al directorio de extensiones PHP, especificado por la opción [extension_dir](#ini.extension-dir) en su archivo `php.ini`.

Para completar la instalación de OCI8, modifíquese el archivo `php.ini` y añádase la línea:

    extension=oci8.so

## Instalación de OCI8 como extensión compilada estáticamente durante la compilación de PHP

Si se compila PHP a partir del código fuente, puede configurarse PHP para incluir OCI8 como una extensión estática utilizando una de las siguientes opciones de configuración.

- Si se utiliza Oracle Instant Client, hágase lo siguiente:

      ./configure --with-oci8=instantclient,/ruta/a/instant/client/lib

- Si se utiliza una base de datos Oracle o una instalación completa del cliente Oracle, hágase lo siguiente:

      ./configure --with-oci8=$ORACLE_HOME

Después de la configuración, sigase el procedimiento habitual de construcción de PHP, por ejemplo *make install*. Después de una compilación exitosa, no es necesario añadir `oci8.so` a su `php.ini`. No se requiere ningún paso adicional de construcción.

## Instalación de OCI8 bajo Windows

La biblioteca OCI8 puede ser añadida a una instalación existente de PHP utilizando las DLL del repositorio [PECL](https://pecl.php.net/package/oci8) o las bibliotecas situadas en el directorio `ext` de su instalación PHP.

Con las bibliotecas Oracle 12*c* (o posteriores), descoméntese una de las siguientes líneas en su archivo `php.ini` `extension=php_oci8_12c.dll` o `extension=php_oci8_11g.dll`, o bien `extension=php_oci8.dll`. Solo una de estas DLLs debe estar activa al mismo tiempo. Las DLLs con versiones superiores pueden contener más funcionalidades. Todas las DLLs pueden no estar disponibles para todas las versiones de PHP. Asegúrese de que la opción [extension_dir](#ini.extension-dir) está definida en la carpeta que contiene las extensiones DLL de PHP.

Si se utiliza el cliente Oracle Instant, defínase la variable de entorno `PATH` del sistema a la carpeta que contiene las bibliotecas Oracle.

## Definición del entorno Oracle

Antes de utilizar esta extensión, asegúrese de que las variables de entorno Oracle están correctamente definidas para el usuario que ejecuta el servidor Web. Si su servidor Web se inicia automáticamente al arrancar el servidor, entonces asegúrese también de la correcta configuración de la variable de entorno utilizada en ese momento.

> [!NOTE]
> No se definan las variables de entorno Oracle utilizando la función `putenv` en sus scripts PHP, ya que las bibliotecas Oracle son cargadas e inicializadas antes de la ejecución de su script. Las variables definidas con `putenv` podrían entrar en conflicto y provocar tanto fallos como comportamientos totalmente inesperados. Algunas funciones pueden reaccionar normalmente, otras pueden provocar errores. Las variables deben ser definidas *antes* del inicio del servidor.

En los sistemas Red Hat Linux y sus variantes, debe exportarse las variables al final del archivo `/etc/sysconfig/httpd`. En otros sistemas que utilicen Apache 2, debe utilizarse el script `envvars` que se encontrará en el directorio `bin` de Apache. Otra opción consiste en utilizar la directiva `SetEnv` del archivo `httpd.conf`, pero esto puede no ser suficiente en algunos sistemas.

Para verificar si las variables de entorno han sido definidas correctamente, utilícese la función `phpinfo` y prestese atención a la sección *Environment* (y no a la sección *Apache Environment*); debe contener todas las variables definidas.

Las variables que se necesitan están incluidas en la tabla siguiente. Consúltese la documentación Oracle para más información sobre todas las variables.

| Nombre | Propósito |
|----|----|
| ORACLE_HOME | Ruta al directorio que contiene el software de base de datos Oracle. No se defina esta variable si se utiliza el cliente Oracle Instant. De hecho, no es necesaria pero puede causar problemas durante la instalación. |
| ORACLE_SID | El nombre de la base de datos en la máquina local. No es necesario definirla si se utiliza el cliente Oracle Instant, o entonces, pasarla siempre como argumento de conexión a la función `oci_connect`. |
| LD_LIBRARY_PATH | Defínase esta variable (o su equivalente en la plataforma actual, como `LIBPATH`, o `SHLIB_PATH`) como la ruta a las bibliotecas Oracle, por ejemplo `$ORACLE_HOME/lib` o `/usr/lib/oracle/19/client/lib`. Esta variable no es necesaria si las bibliotecas son localizadas por un mecanismo de búsqueda diferente, como con `ldconfig` o con `LD_PRELOAD` en lugar de `LD_LIBRARY_PATH`. |
| NLS_LANG | Es la variable principal para definir el juego de caracteres y las informaciones de globalización utilizadas por las bibliotecas Oracle. |
| ORA_SDTZ | Define el desplazamiento horario a utilizar por las sesiones Oracle. |
| TNS_ADMIN | Ruta al directorio que contiene los archivos de configuración Oracle Net Services (`tnsnames.ora` y `sqlnet.ora`). Innecesario si la cadena de conexión utilizada por la función `oci_connect` está en formato de conexión fácil como `localhost/XE`. También innecesario si los archivos de configuración de red están en ubicaciones por defecto como `/usr/lib/oracle/VERSION/client/lib/network/admin`, `$ORACLE_HOME/network/admin` o `/etc`. |

Variables de entorno Oracle comunes

Existen otras variables de entorno Oracle menos frecuentemente utilizadas, como `TWO_TASK`, `ORA_TZFILE`, así como las diversas variables de globalización como `NLS*` y `ORA_NLS_*`.

## En caso de problemas

El problema más común durante la instalación de OCI8 es haber configurado incorrectamente el juego de variables de entorno. Es un problema típico cuando se recibe un mensaje de error al utilizar las funciones `oci_connect` o `oci_pconnect`. El error puede ser un error puramente PHP como *Llamada a la función no definida oci_connect()*, un error Oracle como ORA-12705 o incluso un fallo brusco de Apache. Verifíquese el contenido de los archivos de registro de Apache durante su inicio y refiérase a las secciones anteriores para resolver el problema.

Mientras que los errores de red como ORA-12154 o ORA-12514 indican un problema de nombramiento de red o un problema de configuración, muy a menudo, la causa principal es que el entorno PHP no está correctamente definido y que las bibliotecas Oracle son incapaces de encontrar el archivo de configuración `tnsnames.ora`.

En Windows, tener varias versiones de Oracle en la misma máquina puede hacer que la instalación falle fácilmente a menos que se asegure de que PHP no está utilizando únicamente la versión correcta de Oracle.

Una utilidad que permite examinar las bibliotecas buscadas y cargadas puede ayudar a resolver este tipo de problema, especialmente en Windows.

> [!NOTE]
> Verifíquese que Apache está enlazado con la biblioteca pthread:
>
> <div class="informalexample">
>
>     # ldd /www/apache/bin/httpd
>       libpthread.so.0 => /lib/libpthread.so.0 (0x4001c000)
>       libm.so.6 => /lib/libm.so.6 (0x4002f000)
>       libcrypt.so.1 => /lib/libcrypt.so.1 (0x4004c000)
>       libdl.so.2 => /lib/libdl.so.2 (0x4007a000)
>       libc.so.6 => /lib/libc.so.6 (0x4007e000)
>       /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0x40000000)
>
>          
>
> </div>
>
> Si la biblioteca libpthread no está listada, reinstálese Apache:
>
> <div class="informalexample">
>
>     # cd /usr/src/apache_1.3.xx
>     # make clean
>     # LIBS=-lpthread ./config.status
>     # make
>     # make install
>
>          
>
> </div>
>
> Tenga en cuenta que en sistemas como UnixWare, la biblioteca se llama libthread en lugar de libpthread. PHP y Apache deben ser configurados con EXTRA_LIBS=-lthread.
