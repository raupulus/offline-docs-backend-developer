---
title: Uso de PHP integrado anterior a macOS Monterey
source_url: https://www.php.net/manual/es/install.macosx.bundled.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/macos/bundled.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: ee1ce6a0e
order: 1720
---

## Uso de PHP integrado anterior a macOS Monterey

PHP está integrado con macOS desde macOS X (10.0.0) y anterior a macOS Monterey (12.0.0). Activar PHP con el servidor Web por defecto requiere descomentar algunas líneas en el fichero de configuración de Apache `httpd.conf` mientras que el modo CGI y/o CLI están activados por defecto (acceso simple a través del terminal).

La activación de PHP siguiendo estas instrucciones permite configurar rápidamente un entorno local de desarrollo. Se recomienda encarecidamente siempre actualizar PHP a su versión más reciente. Como la mayoría de los programas, las nuevas versiones se crean para corregir errores y añadir funcionalidades y es el caso de PHP. Consulte la documentación de la instalación de macOS para más detalles. Las siguientes instrucciones están destinadas al principiante, proporcionando solo los detalles suficientes para configurar una configuración por defecto para trabajar. Se recomienda encarecidamente a todos los usuarios compilar e instalar una versión reciente del paquete.

El tipo de instalación estándar utiliza mod_php, y activa el mod_php integrado en macOS para el servidor Web Apache (el servidor Web por defecto que es accesible a través de las preferencias del sistema), en algunos pasos:

1.  Encuentre y abra el fichero de configuración de Apache. Por defecto, será: `/private/etc/apache2/httpd.conf`

    Utilizar el programa `Finder` o `Spotlight` para encontrar este fichero puede resultar difícil, sabiendo que, por defecto, pertenece al usuario `root`.

    > [!NOTE]
    > Una forma de abrirlo es utilizar un editor de texto Unix en un terminal, por ejemplo, `nano`, y sabiendo que el fichero es propiedad del usuario `root`, deberá utilizar el comando `sudo` para abrirlo (como `root`); además, deberá introducir el siguiente comando en su `Terminal` (se le pedirá su contraseña): `sudo nano /private/etc/apache2/httpd.conf`
    >
    > Algunos comandos de nano: `^w` (búsqueda), `^o` (guardar), y `^x` (salida) donde `^` representa la tecla Ctrl.

    > [!NOTE]
    > Las versiones de Mac OS X anteriores a 10.5 proporcionan versiones antiguas de PHP y Apache. Además, el fichero de configuración de Apache en las máquinas originales puede ser `/etc/httpd/httpd.conf`.

2.  Con un editor de texto, descomente las líneas (borrando el carácter \#) que se parecen a las siguientes líneas (estas 2 líneas no se encuentran en el mismo lugar):

        # LoadModule php5_module libexec/httpd/libphp5.so

        # AddModule mod_php5.c

             

    Tenga en cuenta la ruta. En el futuro, cuando compile PHP, los ficheros anteriores deben ser reemplazados o comentados.

3.  Asegúrese de que las extensiones deseadas sean analizadas por PHP (ejemplos: `.php`, `.html` y `.inc`)

    Sabiendo que este comportamiento ya ha sido activado en su fichero `httpd.conf` (desde Mac Panther), una vez activado PHP, los ficheros `.php` serán automáticamente analizados por PHP.

        <IfModule mod_php5.c>
            # Si php está activado, respetamos los ficheros .php y .phps.
            AddType application/x-httpd-php .php
            AddType application/x-httpd-php-source .phps

            # Como la mayoría de los usuarios querrá que index.php funcione,
            # también activamos automáticamente index.php
            <IfModule mod_dir.c>
                DirectoryIndex index.html index.php
            </IfModule>
        </IfModule>

             

    > [!NOTE]
    > Antes de OS X 10.5 (Leopard), PHP 4 se entregaba por defecto en lugar de PHP 5. Por lo tanto, las instrucciones anteriores diferirán solo cambiando 5 por 4.

4.  Asegúrese de que DirectoryIndex cargue el fichero index por defecto.

    Esto también se define en el fichero `httpd.conf`. Normalmente, los ficheros `index.php` y `index.html` se utilizan. Por defecto, `index.php` está activado porque también está en la verificación de PHP anterior. Ajuste según sea necesario.

5.  Defina la ruta hacia el fichero `php.ini` o utilice la ruta por defecto.

    La ruta por defecto en macOS es `/usr/local/php/php.ini` y una llamada a la función `phpinfo` revelará esta información. Si no se utiliza ningún fichero `php.ini`, PHP utilizará todos los valores por defecto. Consulte la FAQ sobre "[encontrar el fichero php.ini](#faq.installation.phpini)".

6.  Encuentre y defina el `DocumentRoot`

    Este es el directorio principal para todos los ficheros Web. Los ficheros en este directorio serán servidos por el servidor Web, y por lo tanto, los ficheros PHP serán analizados por PHP antes de enviarlos al navegador. La ruta por defecto es `/Library/WebServer/Documents` pero puede definirse a cualquier valor en el fichero `httpd.conf`. Además, el directorio `DocumentRoot` para los diferentes usuarios es `/Users/yourusername/Sites`

7.  Cree un fichero `phpinfo`.

    La función `phpinfo` muestra la información sobre PHP. Cree un fichero en el DocumentRoot con el siguiente código PHP:

```php
    <?php phpinfo(); ?>

         
    ```

8.  Reinicie Apache y cargue el fichero PHP que acabamos de crear.

    Para reiniciar, ejecute el comando `sudo apachectl graceful` en un terminal o detenga/inicie la opción "Personal Web Server" en las preferencias del sistema de macOS. Por defecto, la carga de ficheros locales en el navegador se realiza a través de URL como esta: `http://localhost/info.php` o, si está utilizando el DocumentRoot de un directorio de usuario, la URL será: `http://localhost/~yourusername/info.php`

CLI (o CGI en versiones anteriores) se llama `php` y normalmente reside en `/usr/bin/php`. Abra un terminal, lea la sección sobre [la línea de comandos](#features.commandline) del manual de PHP, y ejecute el comando `php -v` para verificar la versión de PHP de este binario. Una llamada a la función `phpinfo` también puede revelar esta información.
