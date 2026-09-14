---
title: Instalación
source_url: https://www.php.net/manual/es/faq.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/installation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_revision: 2dbf3d906
order: 1470
---

## Instalación

Esta sección contiene preguntas comunes sobre la forma de instalar PHP. Este está disponible para casi cualquier SO y casi cualquier servidor web.

Para instalar PHP, siga las instrucciones de [???](#install).

**Q:** ¿Por qué no debe utilizarse Apache2 con un MPM con hilos en un entorno de producción?

**A:** PHP es el «pegamento» utilizado para desarrollar buenas aplicaciones web uniendo docenas de bibliotecas de terceros y haciéndolas que parezcan una entidad coherente a través de una interfaz de lenguaje intuitiva y fácil de aprender. La flexibilidad y la potencia de PHP residen en la estabilidad y robustez de la plataforma subyacente. Requiere la combinación de un SO, de un servidor web y de bibliotecas de terceros, todos correctamente funcionando. Cuando cualquiera de ellos deja de funcionar, PHP necesita identificar los problemas y corregirlos rápidamente. Cuando el marco de trabajo subyacente se hace más complejo al no tener hilos de ejecución completamente independientes, segementos de memoria completamente independientes y un fuerte entorno de pruebas por cada petición a cubrir, se introducirán más debilidades en el sistema de PHP.

Si desea utilizar un MPM con hilos, considere una configuración de FastCGI donde PHP se ejecute en su propio espacio de memoria.

**Q:** Unix/Windows: ¿Donde debería ubicarse mi fichero `php.ini`?

**A:** Por defecto, en Unix debería estar en `/usr/local/lib`, lo que es `<install-path>/lib`. Para cambiar esta ruta durante la compilación se ha de usar la bandera [--with-config-file-path](#configure.with-config-file-path). Se debería establecer a algo como por ejemplo:

```php
      --with-config-file-path=/etc
     
```

Luego se debería copiar el fichero `php.ini-development` de la distribución a `/etc/php.ini` y editarlo para realizar cualquier cambio necesario.

```php
     --with-config-file-scan-dir=PATH
    
```

En Windows, la ruta predeterminada para el fichero `php.ini` es el directorio Windows. Si se utiliza el servidor web Apache, `php.ini` se busca primero en el directorio de instalación de Apache, p. ej. en `C:\Archivos de programa\Apache Group\Apache`. De esta forma se pueden tener distintos ficheros `php.ini` para diferentes versiones de Apache en la misma máquina.

Véase también el capítulo sobre el [fichero de configuración](#configuration.file).

**Q:** Unix: He instalado PHP, pero con cada documento que cargo, obtengo el mensaje 'Document Contains No Data'. ¿Qué está pasando?

**A:** Esto probablemente signifique que PHP esté teniendo algún tipo de problema y esté realizando un volcado de memoria. Revise el registro de errores del servidor para ver si este es el caso, y después intente reproducir el problema con una pequeña prueba. Si sabe cómo usar 'gdb', le será de gran ayuda al poder proporcionar la traza de la pila con el informe de errores para que los desarrolladores puedan precisar el origen del problema. Si está utilizando PHP como un módulo de Apache, intente algo así:

- Detener los procesos httpd

- gdb httpd

- Detener los procesos httpd

- \> run -X -f /ruta/al/httpd.conf

- Luego obtenga el URL que causa el problema con su explorador

- \> run -X -f /ruta/al/httpd.conf

- Si resulta en un volcado de memoria, gdb debería informárselo al instante

- escriba: bt

- Debería incluir la traza en su informe de errores, el cual debe ser enviado a <https://github.com/php/php-src/issues>

Si su script utiliza las funciones de expresiones regulares (`preg_match` y similares), debería asegurarse de que PHP y Apache se compilaron con los mismos paquetes de expresiones regulares. Esto debería ocurrir automáticamente con PHP y Apache 1.3.x

**Q:** Unix: He instalado PHP usando paquetes RPM, pero Apache no procesa los las páginas de PHP. ¿Qué está pasando?

**A:** Asumiendo que instaló tanto Apache como PHP desde paquetes RPM, necesita descomentar o agregar algunas o todas de las siguientes líneas en su fichero `httpd.conf`:

```php
## Módulos adicionales
AddModule mod_php.c
AddModule mod_perl.c

## Módulos adicionales
LoadModule php_module         modules/mod_php.so
LoadModule php5_module        modules/libphp5.so
LoadModule perl_module        modules/libperl.so

     
```

Y agregar:

```php
AddType application/x-httpd-php .php

     
```

a las propiedades globales, o a las propiedades del VirtualDomain que desee que tenga añadido el soporte para PHP.

**Q:** Unix: Le he aplicado a Apache el parche de extensiones de FrontPage, y de pronto PHP dejó de funcionar. ¿Acaso PHP es incompatible con las extensiones de FrontPage para Apache?

**A:** No, PHP funciona bien con las extensiones de FrontPage. El problema radica en que dicho parche modifica varias estructuras de Apache de las que depende PHP. La recompilación de PHP (con 'make clean ; make') tras la aplicación del parche debería resolver el problema.

**Q:** Unix/Windows: He inslatado PHP, pero cuando intento acceder a ficheros de script de PHP a través de mi navegador obtengo la pantalla en blanco.

**A:** Ejecute 'ver código fuente' en el navegador web y probablemente encontrará que puede ver el código fuente de su script de PHP. Esto significa que el servidor web no envió el script a PHP para interpretarlo. Algo está mal en la configuración del servidor: vuelva a comprobarla con respecto a las instrucciones de instalación de PHP.

**Q:** Unix/Windows: He instalado PHP, pero cuando intento acceder a un fichero de script de PHP a través de mi navegador, obtengo un error 500 del servidor.

**A:** Algo falló cuando el servidor intentó ejecutar PHP. Para obtener un mensaje de error detallado desde la línea de comandos, vaya al directorio que tiene el ejecutable de PHP (`php.exe` en Windows) y ejecute `php -i`. Si PHP tiene problemas al ejecutarse, el correspondiente error será mostrado en pantalla proporcionando una pista sobre lo que debe hacer a continuación. Si obtiene una pantalla completa de código HTML (la salida de la función `phpinfo`) es porque PHP está funcionando, y su problema puede estar relacionado con la configuración del servidor, la cual debería de volver a revisar.

**Q:** Algunos sistemas operativos: He instalado PHP sin errores, pero cuando intento iniciar Apache, obtengo errores de Símbolos no definidos:

```php
      [mybox:user /src/php5] root# apachectl configtest
      apachectl: /usr/local/apache/bin/httpd Undefined symbols:
      _compress
      _uncompress
     
```

**A:** Esto, en realidad, no tiene nada que ver con PHP, sino con las bibliotecas cliente de MySQL. Algunas necesitan `--with-zlib`, otras no. Esto también se trata en las Preguntas frecuentes de MySQL.

**Q:** Windows: He instalado PHP, pero cuando intento acceder a un fichero de script de PHP a través de mi navegador, obtengo el error:

    cgi error:
     The specified CGI application misbehaved by not
     returning a complete set of HTTP headers.
     The headers it did return are:

         

**A:** Este mensaje de error significa que PHP no pudo imprimir nada. Para obtener un mensaje de error detallado desde la línea de comandos, vaya al directorio que contiene el ejecutable de PHP (`php.exe` en Windows) y ejecute `php -i`. Si PHP tiene problemas al ejecutarse, el correspondiente error será mostrado en pantalla proporcionando una pista sobre lo que debe hacer a continuación. Si obtiene una pantalla completa de código HTML (la salida de la función `phpinfo`) es porque PHP está funcionando.

Una vez que PHP esté funcionando desde la línea de comandos, intente acceder nuevamente al script a través de su navegador. Si continúa fallando, podría ser por una de las siguientes razones:

- Los permisos de fichero en el script de PHP, `php.exe`, `php5ts.dll`, `php.ini` o cualquier extensión de PHP que esté intentando cargar, son tales que el usuario de internet anónimo `ISUR_<machinename>` no puede acceder a ellos.

- El fichero de script no existe (o quizá no se ubique en donde usted cree que está en relación a su directorio raíz web). Observe que para IIS se puede manejar este error señalando la casilla 'comprobar si el fichero existe' al configurar la correspondencia de scripts en el Administrador de Servicios de Internet. Si un fichero de script no existe, el servidor devolverá un error HTTP 404 en su lugar. IIS también brinda el beneficio adicional de encargarse de cualquier autenticación requerida de forma automática basándose en lospermisos NTLanMan de su fichero de script.

**Q:** Windows: He seguido todas las instrucciones, pero todavía no puedo hacer que PHP e IIS funcionen juntos.

**A:** Asegúrese de que todo usuario que necesite ejecutar un script de PHP tenga los permisos para ejecutar `php.exe`. IIS utiliza un usuario anónimo que se añade en el momento de su instalación. Este usuario necesita permisos para `php.exe`. Además, cualquier usuario autenticado necesitará permisos para poder ejecutar `php.exe`. Asimismo, es necesario indicarle a IIS4 que PHP es un motor de script. Le podría interesar leer también estas [preguntas frecuentes](#faq.installation.forceredirect).

**Q:** Cuando ejecuto PHP como CGI con IIS, PWS, OmniHTTPD o Xitami, obtengo el siguiente error: `Security Alert! PHP CGI cannot be accessed directly.`.

**A:** La directiva [ cgi.force_redirect](#ini.cgi.force-redirect) debe establecerse a `0`. Por defecto es `1`, por lo que debe asegurarse de que no esté comentada (con un `;`). Como todas las directivas, se configura en `php.ini`

Debido a que su valor predeterminado es `1`, es crítico asegurarse al 100% de estar leyendo el fichero `php.ini` correcto. Lea estas [preguntas frecuentes](#faq.installation.findphpini) para más detalles.

**Q:** ¿Cómo sé si mi `php.ini` se ha encontrado y se está leyendo? Parece como si no lo fuera, ya que los cambios que realizo no se implementan.

**A:** Para asegurarse de que PHP está leyendo su `php.ini`, realice una llamada a `phpinfo`. Cerca de la parte superior, habrá una lista llamada `Configuration File (php.ini)`. Allí figurará dónde está buscando PHP el `php.ini` y si está siendo leído o no. Si existe solo un directorio en `PATH`, entonces PHP no está leyéndolo, por lo que debería colocar su `php.ini` en tal directorio. Si `php.ini` está incluido dentro de `PATH`, es que se está leyendo.

Si `php.ini` está siendo leído y PHP se está ejecutando como un módulo, deberá reiniciar su servidor web tras aplicar los cambios a `php.ini`

Véase también `php_ini_loaded_file`.

**Q:** ¿Cómo agrego mi directorio de PHP a `PATH` en Windows?

**A:** En Windows:

- Vaya a Panel de Control y abra el icono Sistema (Inicio → Panel de control)

- Vaya a la pestaña Avanzado

- Haga clic en el botón 'Variables de Entorno'

- Revise la parte de 'Variables de Sistema'

- Encuentre la entrada Path (seguramente tendrá que desplazarse para encontrarla)

- Haga doble clic en la entrada Path

- Ingrese su directorio de PHP al final de todo, con un ';' antes (p.ej., `;C:\php`)

- Presione OK

> [!NOTE]
> Asegúrese de reiniciar tras seguir los pasos anteriores para garantizar que se apliquen los cambios a `PATH`.

**Q:** ¿Cómo hago que el fichero `php.ini` esté disponible para PHP en Windows?

**A:** Hay varias formas de hacerlo. Si está usando Apache, lea las instrucciones específicas de instalación, o de lo contrario, debe configurar la variable de entorno `PHPRC`.

**Q:** Windows: ¿Cómo se verifica que PHP puede escribir en el directorio temporal bajo IIS?

1.  Haga clic derecho en el directorio temporal (`%TEMP%`) en el Explorador de archivos para obtener los permisos. El directorio temporal está disponible desde la configuración o `phpinfo`.

2.  Para IIS, verifique que el usuario `IIS_User` tenga permiso `MODIFY`.

**Q:** ¿Es posible usar la negociación de contenidos de Apache (opción MultiViews) con PHP?

**A:** Si los enlaces a ficheros de PHP incluyen la extensión, todo funciona perfectamente. Estas preguntas frecuentes son solo para aquellos casos en los que los enlaces a ficheros de PHP no incluyen la extensión y se desea utilizar la negociación de contenidos para elegir ficheros de PHP sin extensión desde un URL. En este caso, reemplace la línea `AddType application/x-httpd-php .php` con:

```php
AddHandler php5-script php
AddType text/html php

      
```

Esta solución no funciona para Apache 1 ya que el módulo de PHP no capta `php-script`.

**Q:** ¿PHP se limita a procesar únicamente métodos de peticiones GET y POST?

**A:** No. Es posible manejar cualquier método de peticiones, por, ej., CONNECT. El estado de respuesta apropiado puede ser enviado con `header`. Si solo se van a manejar los métodos GET y POST, esto se puede lograr con la siguiente configuración de Apache:

```php
<LimitExcept GET POST>
Deny from all
</LimitExcept>

      
```
