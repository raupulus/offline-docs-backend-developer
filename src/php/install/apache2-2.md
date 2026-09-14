---
title: Apache 2.x en Microsoft Windows
source_url: https://www.php.net/manual/es/install.windows.apache2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/windows/apache2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: 330a38c4d
order: 1900
---

## Apache 2.x en Microsoft Windows

Esta sección contiene notas y sugerencias específicas de Apache 2.x instaladas con PHP en sistemas Microsoft Windows.

> [!NOTE]
> Se debe leer primero el [manual de instalación PHP en Windows](#install.windows.manual)

Se recomienda consultar la [Documentación de Apache](http://httpd.apache.org/docs/current/) para obtener un conocimiento básico del servidor Apache 2.x. También considere leer las [notas específicas para Windows](http://httpd.apache.org/docs/current/platform/windows.html) para Apache 2.x antes de seguir leyendo.

Descargue la versión más reciente de [Apache 2.x](https://www.apachelounge.com/download/) y una versión adecuada de PHP. Siga los pasos del [manual de instalación](#install.windows.manual) y regrese para continuar con la integración de PHP y Apache.

Hay tres formas de configurar PHP para que funcione con Apache 2.x en Windows. PHP se puede ejecutar como controlador, como CGI o bajo FastCGI

> [!NOTE]
> Recuerde que al añadir valores que representan una ruta en la configuración de Apache bajo Windows, todos los backslash, como `c:\directorio\fichero.ext`, deben ser convertidos a slashes, como `c:/directorio/fichero.ext`. Un slash final puede también ser necesario para los directorios.

## Instalación como un controlador de Apache

> [!NOTE]
> Cuando se utiliza apache2handler SAPI, se debe utilizar la versión Thread Safe (TS) de PHP.

Para cargar el módulo PHP en Apache 2.x las siguientes líneas en el fichero de configuración `httpd.conf` de Apache deben ser añadidas:

PHP y Apache 2.x como controlador

```php
## antes de PHP 8.0.0 el nombre del módulo era php7_module
LoadModule php_module "c:/php/php8apache2_4.dll"
<FilesMatch \.php$>
    SetHandler application/x-httpd-php
</FilesMatch>
## configurar la ruta a php.ini
PHPIniDir "C:/php"

    
```

> [!NOTE]
> La ruta real de PHP debe sustituirse por `C:/php/` en los ejemplos anteriores. Asegúrese que el fichero al que hace referencia en la directiva `LoadModule` está en la ubicación especificada, y utilize `php7apache2_4.dll` para PHP 7, o `php8apache2_4.dll` para PHP 8.

## Ejecución de PHP como CGI

Se recomienda consultar la [documentación de Apache CGI](http://httpd.apache.org/docs/current/howto/cgi.html) para una comprensión más completa de la ejecución de CGI en Apache.

Para ejecutar PHP como CGI, deberá colocar los ficheros php-cgi en un directorio designado como directorio CGI utilizando la directiva ScriptAlias.

Será necesario colocar una línea `#!` en los ficheros PHP, que apunte a la ubicación del binario PHP:

PHP y Apache 2.x como CGI

    #!C:/php/php.exe
    <?php
      phpinfo();
    ?>

> [!WARNING]
> Un servidor desplegado en modo CGI se expone a varias vulnerabilidades posibles. Por favor, lea nuestra [sección sobre la seguridad en modo CGI](#security.cgi-bin) para aprender cómo protegerse contra estos ataques.

## Ejecutando PHP bajo FastCGI

Ejecutar PHP bajo FastCGI tiene una serie de ventajas con respecto a ejecutarlo bajo CGI. Configurarlo de esta manera es bastante sencillo:

Descargue `mod_fcgid` desde [https://www.apachelounge.com](https://www.apachelounge.com/download/). Los binarios de Win32 están disponibles para descargar desde ese sitio. Instale el módulo de acuerdo con las instrucciones que lo acompañarán.

Configure su servidor web como se muestra a continuación, teniendo cuidado de ajustar cualquier ruta que reflejen la forma en que ha instalado las cosas en su sistema particular:

Configurar Apache para ejecutar PHP como FastCGI

    LoadModule fcgid_module modules/mod_fcgid.so
    # ¿Dónde está el fichero php.ini?
    FcgidInitialEnv PHPRC        "c:/php"
    <FilesMatch \.php$>
        SetHandler fcgid-script
    </FilesMatch>
    FcgidWrapper "c:/php/php-cgi.exe" .php

Los archivos con una extensión .php ahora serán ejecutados por el contenedor PHP FastCGI.
