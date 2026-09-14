---
title: Lighttpd 1.4 en sistemas Unix
source_url: https://www.php.net/manual/es/install.unix.lighttpd-14.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/lighttpd-14.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 1840
---

## Lighttpd 1.4 en sistemas Unix

Esta sección contiene información específica sobre la instalación de PHP con Lighttpd 1.4 en sistemas Unix.

Consulte [Lighttpd](http://trac.lighttpd.net/trac/) para una instalación correcta de Lighttpd antes de continuar.

FastCGI es el SAPI preferido para conectar PHP y Lighttpd. FastCGI activa automáticamente php-cgi.

## Llamada de PHP por Lighttpd

Para configurar Lighttpd para que se conecte a PHP y llame al proceso FastCGI, se debe editar el fichero `lighttpd.conf`. Una conexión por sockets es la solución preferida para sistemas locales.

Porción del fichero lighttpd.conf

    server.modules += ( "mod_fastcgi" )

    fastcgi.server = ( ".php" =>
      ((
        "socket" => "/tmp/php.socket",
        "bin-path" => "/usr/local/bin/php-cgi",
        "bin-environment" => (
          "PHP_FCGI_CHILDREN" => "16",
          "PHP_FCGI_MAX_REQUESTS" => "10000"
        ),
        "min-procs" => 1,
        "max-procs" => 1,
        "idle-timeout" => 20
      ))
    )

La directiva `bin-path` permite a lighttpd llamar al proceso FastCGI dinámicamente. PHP llamará a los hijos según la variable de entorno `PHP_FCGI_CHILDREN`. La directiva `bin-environment` define el entorno para los procesos llamados. PHP terminará un proceso hijo cuando el número de solicitudes especificado por `PHP_FCGI_MAX_REQUESTS` haya sido alcanzado. Las directivas `min-procs` y `max-procs` pueden generalmente ser ignoradas con PHP. PHP gestiona sus propios hijos y caches opcode como APC que comparte únicamente los hijos gestionados por PHP. Si `min-procs` se establece en algo superior a 1, el número total de respuestas PHP será multiplicado por `PHP_FCGI_CHILDREN` (2 min-procs \* 16 hijos, da 32 respuestas).

## Llamada con spawn-fcgi

Lighttpd proporciona un programa llamado spawn-fcgi para facilitar las llamadas a los procesos FastCGI.

## Llamada de php-cgi

Es posible llamar a los procesos sin spawn-fcgi, con un mínimo de configuración. La variable de entorno `PHP_FCGI_CHILDREN` controla el número de hijos que PHP llama para gestionar las solicitudes. La variable de entorno `PHP_FCGI_MAX_REQUESTS` determina la duración de vida, en número de solicitudes, de cada hijo. A continuación se muestra un script bash simple que ayuda a las llamadas a los gestores PHP.

Llamada a los gestores FastCGI

    #!/bin/sh

    # Ubicación del binario php-cgi
    PHP=/usr/local/bin/php-cgi

    # Ubicación del fichero PID
    PHP_PID=/tmp/php.pid

    # Enlace a una dirección
    #FCGI_BIND_ADDRESS=10.0.1.1:10000
    # Enlace a un socket de dominio
    FCGI_BIND_ADDRESS=/tmp/php.sock

    PHP_FCGI_CHILDREN=16
    PHP_FCGI_MAX_REQUESTS=10000

    env -i PHP_FCGI_CHILDREN=$PHP_FCGI_CHILDREN \
           PHP_FCGI_MAX_REQUESTS=$PHP_FCGI_MAX_REQUESTS \
           $PHP -b $FCGI_BIND_ADDRESS &

    echo $! > "$PHP_PID"

## Conexión a instancias FCGI remotas

Las instancias FastCGI pueden ser llamadas en múltiples máquinas remotas para distribuir las aplicaciones.

Conexión a instancias remotas de php-fastcgi

    fastcgi.server = ( ".php" =>
       (( "host" => "10.0.0.2", "port" => 1030 ),
        ( "host" => "10.0.0.3", "port" => 1030 ))
    )
