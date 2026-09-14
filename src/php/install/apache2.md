---
title: Apache 2.x en sistemas Unix
source_url: https://www.php.net/manual/es/install.unix.apache2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/apache2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: a38e360ae
order: 1790
---

## Apache 2.x en sistemas Unix

Esta sección contiene las notas y consejos de instalación de PHP con el servidor Apache 2.x en sistemas Unix.

> [!WARNING]
> No se recomienda el uso de PHP en un entorno thread MPM, con Apache 2. Utilice el modo prefork MPM, que es el MPM predeterminado para Apache 2.0 y 2.2. Para saber por qué, lea la entrada de la FAQ correspondiente a la [utilización de Apache 2 en un entorno thread MPM](#faq.installation.apache2).

La [Documentación Apache](http://httpd.apache.org/docs/current/) es la mejor fuente de información sobre el servidor Apache 2.x. La mayoría de la información sobre las opciones de instalación de Apache puede encontrarse allí.

La versión más reciente del servidor HTTP Apache puede obtenerse desde la [página de descarga de Apache](http://httpd.apache.org/), y una versión adaptada de PHP desde los enlaces anteriores. Esta guía cubre únicamente las bases de funcionamiento de Apache 2.x con PHP. Para más información, leer la [documentación Apache](http://httpd.apache.org/docs/current/). Los números de versión se omiten aquí, para asegurarse de que las instrucciones no sean incorrectas. En los ejemplos a continuación, 'NN' deberá ser reemplazado por la versión específica de Apache a utilizar.

Actualmente hay 2 versiones de Apache 2.x - 2.4 y 2.2. Hay varias razones para elegir una sobre la otra; sin embargo, la versión 2.4 es actualmente la última versión disponible y también la que recomendamos. Sin embargo, las instrucciones contenidas en esta guía deberían funcionar para la versión 2.4 así como para la versión 2.2. Nota: Apache httpd 2.2 está oficialmente en Fin de Vida, no habrá más desarrollo ni parches para esta versión.

1.  Descargue el servidor HTTP Apache desde el sitio anterior y descomprímalo :

        tar -xzf httpd-2.x.NN.tar.gz

2.  De la misma manera, descargue y descomprima las fuentes de PHP :

        tar -xzf php-NN.tar.gz

3.  Compile e instale Apache. Consulte la documentación sobre la instalación de Apache para más detalles sobre la compilación de este software.

        cd httpd-2_x_NN
        ./configure --enable-so
        make
        make install

4.  Ahora que se tiene Apache 2.x.NN disponible bajo /usr/local/apache2, configúrelo con soporte para la carga de módulos, así como el MPM prefork estándar. Para probar la instalación, utilice el procedimiento normal para iniciar el servidor Apache, es decir:

        /usr/local/apache2/bin/apachectl start

    y deténgalo para continuar con la configuración de PHP :

        /usr/local/apache2/bin/apachectl stop

5.  Ahora, configure y compile PHP. Será en este momento cuando se podrá personalizar PHP con las diversas opciones disponibles, como la lista de extensiones a activar. Ejecute `./configure --help` para obtener la lista de opciones disponibles. En nuestro ejemplo, realizaremos una configuración simple, con Apache 2 y soporte MySQL.

    Si se ha construido Apache desde las fuentes, tal como se describe anteriormente, el siguiente ejemplo debería ser correcto en cuanto a las rutas hacia `apxs`, pero si se ha instalado Apache de otra manera, se deberán tener en cuenta las especificidades y ajustar las rutas `apxs` en consecuencia. Tenga en cuenta que, según las distribuciones, podría ser necesario renombrar `apxs` a `apxs2`.

        cd ../php-NN
        ./configure --with-apxs2=/usr/local/apache2/bin/apxs --with-pdo-mysql
        make
        make install

    Si se decide modificar las opciones de configuración después de la instalación, se deberán ejecutar nuevamente las etapas `configure`, `make` y `make install`. Entonces solo se necesitará reiniciar Apache para que el nuevo módulo surta efecto. Una recompilación de Apache no es necesaria.

    Tenga en cuenta que, salvo indicaciones contrarias, `make install` también instalará [PEAR](https://pear.php.net/), así como diversas herramientas PHP como [phpize](#install.pecl.phpize), PHP CLI y mucho más.

6.  Configurar el archivo `php.ini`

        cp php.ini-development /usr/local/lib/php.ini

    Se debe editar el archivo `.ini` para definir las opciones PHP. Si se prefiere colocar `php.ini` en otro directorio, utilice la opción `--with-config-file-path=/some/path` en la etapa 5.

    Si se elige el archivo `php.ini-production`, asegúrese de leer la lista de modificaciones correspondiente ya que puede afectar considerablemente la forma en que PHP funcionará.

7.  Edite el archivo `httpd.conf` para cargar el módulo PHP. La ruta especificada a la derecha de la cadena LoadModule, debe corresponder a la ruta del sistema del módulo PHP. `make install` anterior debería haber realizado esta operación por usted, pero una simple verificación permitirá asegurarse.

    Para PHP 8:

```php
    LoadModule php_module modules/libphp.so

        
    ```

    Para PHP 7:

```php
    LoadModule php7_module modules/libphp5.so

        
    ```

8.  Indique a Apache que analice ciertas extensiones como scripts PHP. Por ejemplo, deje que Apache pase a PHP los archivos cuya extensión es `.php`. En lugar de utilizar solo la directiva `AddType` de Apache, se desea evitar cualquier riesgo potencialmente peligroso, cuando se descarga y crea un archivo como `exploit.php.jpg`, de ejecución PHP. Utilizando este ejemplo, se puede tener cualquier extensión analizada por PHP. Se ha añadido `.php` para el ejemplo.

```php
    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

        
    ```

    O, si se desea permitir que los archivos `.php`, `.php2`, `.php3`, `.php4`, `.php5`, `.php6`, y `.phtml` sean analizados por PHP, pero nada más, se utilizará esto :

```php
    <FilesMatch "\.ph(p[2-6]?|tml)$">
        SetHandler application/x-httpd-php
    </FilesMatch>

        
    ```

    Y para permitir que los archivos `.phps` sean manejados por el filtro del código fuente de PHP, y así, ser mostrados como código fuente con coloración sintáctica, utilice esto :

```php
    <FilesMatch "\.phps$">
        SetHandler application/x-httpd-php-source
    </FilesMatch>

        
    ```

    Para permitir el uso de un archivo PHP como manejador por defecto cuando no se encuentra ningún otro manejador, por ejemplo al utilizar un motor de enrutamiento, se puede usar la directiva `FallbackResource`. Está disponible en Apache 2.4.4 y versiones posteriores.

    Dado que la directiva `SetHandler` se aplica tanto si el archivo existe como si no, y `FallbackResource` solo se aplica si aún no se ha definido un manejador, puede ser necesario utilizar la directiva `If` para asegurarse de que el manejador solo se aplique si el archivo existe. Esto permite que `FallbackResource` gestione las rutas que terminan en `.php` pero que no existen, lo que puede resultar útil para el manejo de errores y el enrutamiento.

```php
    <FilesMatch "\.php$">
        <If "-f %{REQUEST_FILENAME}">
            SetHandler application/x-httpd-php
        </If>
    </FilesMatch>
    FallbackResource /index.php

        
    ```

    `mod_rewrite` puede ser utilizado para permitir que cualquier archivo `.php` sea mostrado como código fuente con coloración sintáctica, sin necesidad de renombrarlo o copiarlo con una extensión `.phps`. :

```php
    RewriteEngine On
    RewriteRule (.*\.php)s$ $1 [H=application/x-httpd-php-source]

        
    ```

    El filtro de código fuente PHP no debería estar activo en sistemas de producción, ya que puede exponer código confidencial o información sensible contenida en el código fuente.

9.  Utilice el procedimiento normal para iniciar el servidor Apache, es decir:

        /usr/local/apache2/bin/apachectl start

    O

        service httpd restart

Si se han seguido los pasos anteriores, ahora se tiene un servidor web Apache2 funcional con soporte PHP como módulo `SAPI`. Por supuesto, hay una multitud de otras opciones de configuración disponibles con Apache y PHP. Para más información, introduzca el comando `./configure --help` en el árbol de fuentes correspondiente.

Apache puede ser compilado en modo multithread, seleccionando el MPM `worker`, en lugar del estándar MPM `prefork`. Esto se hace añadiendo la siguiente opción al argumento de `./configure`, en la etapa 3 anterior:

    --with-mpm=worker

Esto no debería emprenderse sin ser consciente de las consecuencias, y teniendo al menos una justa comprensión de lo que implica. La documentación de Apache sobre [MPM-Modules](http://httpd.apache.org/docs/current/mpm.html) proporcionará información importante que permitirá tomar la decisión.

> [!NOTE]
> La [FAQ Apache MultiViews](#faq.installation.apache.multiviews) trata sobre el uso de MultiViews con PHP.

> [!NOTE]
> Para compilar una versión multithread de Apache, el sistema de destino debe soportar threads. En este caso, PHP también debe ser construido con Zend Thread Safety (ZTS). Bajo esta configuración, no todas las extensiones estarán disponibles. Recomendamos compilar Apache con el `prefork` MPM-Module.
