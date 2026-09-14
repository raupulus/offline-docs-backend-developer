---
title: Instalado como CGI binario
source_url: https://www.php.net/manual/es/security.cgi-bin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/cgi-bin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: 330a38c4d
order: 109900
---

## Instalado como CGI binario

## Ataques posibles

Usar PHP como un binario CGI es una opción para configuraciones que por alguna razón no desean integrar PHP como un módulo dentro del software de servidor (como Apache), o usarán PHP con diferentes tipos de envoltorios CGI para crear entornos seguros `chroot` y `setuid` para scripts. Esta configuración usualmente involucra la instalación del binario ejecutable de `php` en el directorio `cgi-bin` del servidor web. La recomendación [CA-96.11](http://www.cert.org/advisories/CA-1996-11.html) del CERT recomienda que está en contra de colocar cualquiera de los intérpretes dentro de `cgi-bin`. Aún si el binario de `php` puede ser usado como un intérprete independiente, PHP está diseñado para prevenir los ataques que esta configuración hace posible:

- Accediendo a los ficheros del sistema: `http://mi.servidor/cgi-bin/php?/etc/passwd`

  La consulta de información en una URL después del signo de interrogación (`?`) es pasado como argumento de la línea de comandos al intérprete por la interfaz del CGI. Usualmente los intérpretes abren y ejecutan el fichero especificado como el primer argumento en la línea de comandos.

  Cuando es invocado como un binario de CGI, `php` se niega a interpretar los argumentos de línea de comandos.

- Accediendo a cualquier documento web en el servidor: `http://mi.servidor/cgi-bin/php/directorio/secreto/doc.html`

  Parte de la ruta de información de la URL después del nombre del binario de PHP, `/directorio/secreto/doc.html` es convencionalmente utilizado para especificar el nombre del fichero a ser abierto e interpretado por el programa CGI. Usualmente las directivas de configuración de algunos servidores web (Apache: `Action`) son utilizados para redirigir peticiones a los documentos como `http://mi.servidor/directorio/secreto/script.php` al intérprete de PHP. Con esta configuración, el servidor web revisa primero los permisos de acceso a los directorios `/directorio/secreto`, y después crea la petición redirigida `http://mi.servidor/cgi-bin/php/directorio/secreto/script.php`. Desafortunadamente, si la petición es proporcionada originalmente en esta forma, no se revisan los accesos a los directorios hechos por el servidor web `/directorio/secreto/script.php`, sino solamente al fichero `/cgi-bin/php`. De esta forma `/cgi-bin/php` cualquier usuario está habilitado a acceder a cualquier documento protegido en el servidor web.

  En PHP, las directivas de configuración en tiempo de ejecución [cgi.force_redirect](#ini.cgi.force-redirect), [doc_root](#ini.doc-root) y [user_dir](#ini.user-dir) pueden ser utilizadas para prevenir este ataque, si el árbol de documentos del servidor tiene cualquiera de estos directorios con restricciones de acceso. Véase más abajo para una explicación completa de las diferentes combinaciones.

## Caso 1: Ficheros públicos servidos solamente

Si su servidor no tiene ningún contenido que no esté restringido por contraseña o control de acceso basado en IP, no hay necesidad de estas opciones de configuración. Si su servidor web no le permite hacer redirecciones, o el servidor no tiene una forma de comunicar al binario de PHP que la petición es una forma segura de petición de redireccionada la solicitud, puedes habilitar la directiva ini [cgi.force_redirect](#ini.cgi.force-redirect). Usted todavía tiene que asegurarse que sus scripts de PHP no confían en una forma o en otra para llamar el script, ni directamente `http://mi.servidor/cgi-bin/php/directorio/script.php` ni por redirección `http://mi.servidor/directorio/script.php`.

La redirección puede ser configurada en Apache utilizando directivas `Action` y `AddHandler` (vea más abajo).

## Caso 2: utilizando `cgi.force_redirect`

La directiva de configuración [cgi.force_redirect](#ini.cgi.force-redirect) previene a cualquiera que llame a PHP directamente por medio de una URL como esta `http://mi.servidor/cgi-bin/php/directoriosecreto/script.php`. En cambio, `php` solamente lo analizará en este modo si éste se ha ido a través de una regla directa del servidor web.

Usualmente la redirección en la configuración de Apache se hace con las siguientes directivas:

```php
Action php-script /cgi-bin/php
AddHandler php-script .php

    
```

Esta opción ha sido probada solamente con el servidor web Apache, y se basa en que en Apache se configure en una variable de entorno no-estándar de CGI `REDIRECT_STATUS` para peticiones de redirección. Si su servidor web no soporta ninguna forma de decirle si la petición es directa o redirigida, usted no puede utilizar esta opción y debe usar una de las otras formas de ejecutar la versión CGI aquí documentadas.

## Caso 3: Configurando doc_root o user_dir

Para incluir contenido activo, como scripts y ejecutables, en los directorios de documentos del servidor web es algunas veces considerado una práctica insegura. Si, por el hecho del algún error de configuración, los scripts no se ejecutan y son mostrados como documentos HTML regulares, esto podría resultar en una fuga de información de propiedad intelectual o de información de seguridad como las contraseñas. Por lo tanto muchos Administradores de Sistemas preferirán configurar otra estructura de directorios para scripts que sean accesibles solamente a través del CGI de PHP, y por lo tanto siempre interpretado y no desplegado como tal.

También si el método para asegurar las peticiones no es redirigido, como se describió en la sección anterior, no está disponible, es necesario configurar un script [doc_root](#ini.doc-root) que sea diferente de la raíz del documento web.

Usted puede configurar el script de la raíz de documento de PHP en la directiva de configuración [doc_root](#ini.doc-root) en el [fichero de configuración](#configuration.file), o puede configurar la variable de entorno `PHP_DOCUMENT_ROOT`. Si éste es configurado, la versión del CGI de PHP siempre construirá el nombre del fichero para abrir con este `doc_root` y la ruta de información en la petición, de tal forma que pueda estar seguro que ningún script será ejecutado fuera de este directorio (excepto por `user_dir` que se encuentra más abajo).

Otra opción utilizable es esta [user_dir](#ini.user-dir). Cuando `user_dir` no está configurado, lo único que controla el fichero abierto es `doc_root`. Al abrir una URL como `http://mi.servidor/~usuario/documento.php` no resulta en la apertura de un fichero bajo el directorio personal de los usuarios, pero si un fichero llamado `~usuario/documento.php` debajo de `doc_root` (si, un nombre de directorio que inicia con una a tilde \[`~`\]).

Si `user_dir` es configurado, por ejemplo `public_php`, una petición como `http://mi.servidor/~usuario/doc.php` abrirá un fichero llamado `doc.php` bajo el directorio llamado `public_php` debajo de el directorio personal del usuario. Si el directorio personal del usuario es `/home/usuario`, el fichero ejecutado será `/home/user/public_php/doc.php`.

La expansión de `user_dir` sucede sin tomar en cuenta la configuración de `doc_root`, así que usted puede controlar el acceso a la raíz de los documentos y el directorio de los usuarios separadamente.

## Caso 4: El analizador de PHP fuera del árbol de la web

Una opción muy segura es poner el binario analizador de PHP en algún lugar fuera del árbol de ficheros de la web. En `/usr/local/bin`, por ejemplo. El único inconveniente real con esta opción es que ahora tendrá que poner una línea similar a:

    #!/usr/local/bin/php

como la primera línea de cualquier fichero que contenga etiquetas de PHP. También necesitará hacer que el fichero sea ejecutable. Eso significa, tratarlo exactamente como trataría cualquier otro script de CGI escrito en Perl, sh, bash, o cualquier otro lenguaje común de script el cual utilice `#!` como mecanismo de ejecución de si mismo.

Para que PHP maneje la información correctamente de `PATH_INFO` y `PATH_TRANSLATED` con esta configuración, La directiva ini [cgi.discard_path](#ini.cgi.discard-path) debe estar habilitada..
