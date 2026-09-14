---
title: Nginx 1.4.x en sistemas Unix
source_url: https://www.php.net/manual/es/install.unix.nginx.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/nginx.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: false
translation_revision: f0261e36d
order: 1860
---

## Nginx 1.4.x en sistemas Unix

Esta documentación cubre la instalación y configuración de PHP con PHP-FPM para el servidor HTTP Nginx 1.4.x.

Este guía asume que se ha compilado Nginx a partir de las fuentes y por lo tanto todos los binarios y ficheros de configuración se encuentran en `/usr/local/nginx`. Si no es el caso y se ha obtenido Nginx por otros medios, por favor refiérase al [Wiki de Nginx](https://www.nginx.com/resources/wiki/) para adaptar este manual a su configuración.

Este guía cubre las bases de la configuración del servidor Nginx para servir una aplicación PHP en el puerto 80. Se recomienda estudiar las documentaciones de Nginx y PHP-FPM para optimizar su instalación.

Tenga en cuenta que a lo largo de esta documentación, los números de versión han sido reemplazados por una "x" para asegurar que esta última permanezca correcta en el futuro. Recuerde reemplazarlos por su número de versión.

1.  Se recomienda consultar la [documentación de Nginx](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/) para instalarla en su sistema.

2.  Recuperar y descomprimir las fuentes de PHP:

        tar zxf php-x.x.x

3.  Configurar y compilar PHP. Este será el momento en el que se podrá personalizar PHP con diversas opciones, como las extensiones a activar. Ejecutar ./configure --help para obtener una lista de las opciones disponibles. En nuestro ejemplo, se realizará una configuración simple con soporte PHP-FPM y MySQLi.

        cd ../php-x.x.x
        ./configure --enable-fpm --with-mysqli
        make
        sudo make install

4.  Recuperar y mover los ficheros de configuración en los directorios correctos

        cp php.ini-development /usr/local/php/php.ini
        cp /usr/local/etc/php-fpm.d/www.conf.default /usr/local/etc/php-fpm.d/www.conf
        cp sapi/fpm/php-fpm /usr/local/bin

5.  Es importante que se impida que Nginx pase las peticiones al backend PHP-FPM si el fichero no existe, evitando así las vulnerabilidades por inyecciones arbitrarias de scripts.

    Esto se puede realizar definiendo la directiva de configuración [cgi.fix_pathinfo](#ini.cgi.fix-pathinfo) al valor `0` en su php.ini.

    Editar php.ini:

        vim /usr/local/php/php.ini

    Encontrar la directiva `cgi.fix_pathinfo=` y modificarla como sigue:

        cgi.fix_pathinfo=0

6.  El fichero php-fpm.conf debe ser modificado para especificar que php-fpm debe ser ejecutado con el usuario www-data y el grupo www-data antes de iniciar el servicio:

        vim /usr/local/etc/php-fpm.d/www.conf

    Encontrar y modificar lo siguiente:

        ; Usuario/grupo Unix de los procesos
        ; Nota: el usuario es obligatorio. Si no se define el grupo, se usará el grupo
        ;       por defecto del usuario.
        user = www-data
        group = www-data

    El servicio php-fpm puede ahora ser iniciado:

        /usr/local/bin/php-fpm

    Este guía no va a configurar php-fpm más allá de esto; si está interesado en la configuración avanzada de php-fpm, por favor consulte la documentación.

7.  Nginx debe ahora ser configurado para soportar el análisis de las aplicaciones PHP:

        vim /usr/local/nginx/conf/nginx.conf

    Modificar el bloque por defecto para que pueda servir ficheros .php:

```php
    location / {
        root   html;
        index  index.php index.html index.htm;
    }

        
    ```

    La siguiente etapa asegura que los ficheros .php sean pasados al backend PHP-FPM; Bajo el bloque comentado por defecto y entre:

```php
    location ~* \.php$ {
        fastcgi_index   index.php;
        fastcgi_pass    127.0.0.1:9000;
        include         fastcgi_params;
        fastcgi_param   SCRIPT_FILENAME    $document_root$fastcgi_script_name;
        fastcgi_param   SCRIPT_NAME        $fastcgi_script_name;
    }

        
    ```

    Reiniciar Nginx.

        sudo /usr/local/nginx/sbin/nginx -s stop
        sudo /usr/local/nginx/sbin/nginx

8.  Crear un fichero de prueba

        rm /usr/local/nginx/html/index.html
        echo "<?php phpinfo(); ?>" >> /usr/local/nginx/html/index.php

    Ahora, navegue a http://localhost. El phpinfo() debería ser mostrado.

Siguiendo estos diferentes pasos, se debería ejecutar un servidor web Nginx con soporte de PHP como módulo `FPM` `SAPI`. Por supuesto, hay muchas más opciones de configuración disponibles para Nginx y PHP. Para más información, escriba `./configure --help` en la fuente correspondiente.
