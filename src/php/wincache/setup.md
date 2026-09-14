---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/wincache.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 48ce43fe7
order: 101830
---

## Instalación/Configuración

## Requisitos

La extensión actualmente solo es compatible con las siguientes configuraciones:

Sistema Operativo Windows:

- Windows XP SP3 con IIS 5.1 y la [Extensión FastCGI](http://www.iis.net/extensions/fastcgi)
- Windows Server 2003 con IIS 6.0 y la [Extensión FastCGI](http://www.iis.net/extensions/fastcgi)
- Windows Vista SP1 con IIS 7.0 y el módulo FastCGI
- Windows Server 2008 con IIS 7.0 y el módulo FastCGI
- Windows 7 con IIS 7.5 y el módulo FastCGI
- Windows Server 2008 R2 con IIS 7.5 y el módulo FastCGI

PHP:

- PHP 5.2.X, compilación no segura para subprocesos
- PHP 5.3 X86, compilación VC9 no segura para subprocesos

> [!NOTE]
> La extensión WinCache solo puede ser utilizada cuando IIS está configurado para ejecutar PHP a través de FastCGI.

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP.

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/wincache>.

Hay dos paquetes para esta extensión: un paquete es para las versiones PHP 5.2.X, y el otro paquete es para PHP 5.3.X. Elija el paquete adecuado para la versión de PHP que esté utilizando.

Para instalar y activar la extensión, siga estos pasos:

1.  Descomprima el paquete en una ubicación temporal.

2.  Copie el archivo `php_wincache.dll` en la carpeta de extensiones PHP. Generalmente, esta carpeta se llama "ext" y está ubicada en el mismo directorio que todos los archivos binarios de PHP. Por ejemplo: `C:\Program Files\PHP\ext`.

3.  Con un editor de texto, abra el archivo php.ini, que generalmente se encuentra en el mismo directorio que todos los archivos binarios de PHP. Por ejemplo: `C:\Program Files\PHP\php.ini`.

4.  Agregue la siguiente línea al final del archivo php.ini: `extension = php_wincache.dll`.

5.  Guarde y cierre el archivo `php.ini`.

6.  Reinicie el grupo de aplicaciones IIS para que PHP recoja los cambios de configuración. Para verificar que la extensión se ha activado, cree un archivo llamado `phpinfo.php` que contenga una llamada a la función [phpinfo](#function.phpinfo).

7.  Guarde el archivo `phpinfo.php` en el directorio raíz de un sitio web IIS que utilice PHP, luego abra un navegador y realice una solicitud a http://localhost/phpinfo.php. Busque una sección llamada `wincache` en la página devuelta. Si la extensión está activada, la salida de [phpinfo](#function.phpinfo) listará los parámetros de configuración proporcionados por WinCache.

> [!NOTE]
> No olvide eliminar el archivo `phpinfo.php` del directorio raíz después de haber verificado que la extensión se ha activado.

## Script de estadísticas WinCache

El paquete de instalación para WinCache incluye un script PHP, `wincache.php`, que puede ser utilizado para obtener información y estadísticas sobre la caché.

Si la extensión WinCache se instaló a través del instalador de Microsoft Web Platform, entonces este script se encuentra en `%SystemDrive%\Program Files\IIS\Windows Cache for PHP\`. En una versión de 64 bits del sistema operativo Windows Server, el script se encuentra en `%SystemDrive%\Program Files (x86)\IIS\Windows Cache for PHP`. Si la extensión se instaló manualmente, entonces el archivo `wincache.php` estará ubicado en el mismo directorio desde el cual se extrajo el contenido del paquete de instalación.

Para usar `wincache.php`, cópielo en el directorio raíz de un sitio web o en cualquier subdirectorio. Para proteger el script, ábralo en cualquier editor y reemplace los valores de las constantes *USERNAME* y *PASSWORD*. Si alguna otra autenticación IIS está habilitada en el servidor, entonces siga las instrucciones en los comentarios:

Configuración de la autenticación para `wincache.php`

```php
<?php
/**
 * ======================== CONFIGURACIÓN DE AJUSTES ==============================
 * Si no desea usar la autenticación para esta página, establezca USE_AUTHENTICATION en 0.
 * Si usa autenticación, reemplace la contraseña predeterminada.
 */
define('USE_AUTHENTICATION', 1);
define('USERNAME', 'wincache');
define('PASSWORD', 'wincache');

/**
 * La autenticación PHP básica solo funcionará cuando IIS esté configurado para admitir
 * 'Autenticación anónima' y nada más. Si IIS está configurado para admitir/usar
 * cualquier otro tipo de autenticación como Básica/Negociar/Digest, etc., esto no funcionará.
 * En ese caso, use la matriz a continuación para definir los nombres de los usuarios en su
 * dominio/red/grupo de trabajo a los que desea otorgar acceso.
 */
$user_allowed = array('DOMAIN\user1', 'DOMAIN\user2', 'DOMAIN\user3');

/**
 * Si la matriz contiene la cadena 'all', entonces todos los usuarios autenticados por IIS
 * tendrán acceso a la página. Descomente la línea a continuación y comente la línea anterior
 * para otorgar acceso a todos los usuarios que sean autenticados por IIS.
 */
/* $user_allowed = array('all'); */

/** ===================== FIN DE CONFIGURACIÓN DE AJUSTES ========================== */
?>

    
```

> [!NOTE]
> Siempre proteja el script `wincache.php` utilizando el mecanismo de autenticación integrado o el mecanismo de autenticación del servidor. Dejar este script sin protección puede comprometer la seguridad de su aplicación web y del servidor.

## Manejador de sesiones WinCache

El manejador de sesiones WinCache (disponible desde WinCache 1.1.0) puede ser utilizado para configurar PHP para almacenar los datos de sesión en la memoria compartida del caché de sesión. El uso de la memoria compartida en lugar de la sesión predeterminada ayuda a mejorar el rendimiento de las aplicaciones PHP que almacenan grandes cantidades de datos en objetos de sesión. El caché de sesión Wincache utiliza archivos basados en memoria compartida, lo que asegura que los datos de sesión no se perderán durante el reciclaje de la cola de aplicaciones IIS.

Para configurar PHP para usar el manejador de sesiones WinCache, establezca el parámetro [session.save_handler](#ini.session.save-handler) del archivo `php.ini` a *wincache*. De forma predeterminada, la ubicación donde se almacenan los archivos temporales en Windows se usa para almacenar los datos de sesión. Para cambiar esta ubicación, use la directiva [session.save_path](#ini.session.save-path).

Activar el manejador de sesiones WinCache

```php
session.save_handler = wincache
session.save_path = C:\inetpub\temp\session\

    
```

## Redirecciones de funciones WinCache

*NOTA:* [wincache.rerouteini](#ini.wincache.rerouteini) fue eliminado con WinCache 1.3.7.0. Esto ha sido reemplazado por el redireccionamiento automático de funciones. Ver: [wincache.reroute_enabled](#ini.wincache.reroute_enabled)

Las funcionalidades de redireccionamiento de funciones de WinCache (disponibles desde WinCache 1.2.0, eliminadas desde WinCache 1.3.7.0) pueden ser utilizadas para reemplazar funciones PHP nativas por sus equivalentes optimizados para casos particulares. La extensión Wincache incluye implementaciones de funciones PHP optimizadas para Windows, especialmente en casos de acceso a red o sistema de archivos. Las siguientes funciones están involucradas:

- [file_exists](#function.file-exists)
- [file_get_contents](#function.file-get-contents)
- [readfile](#function.readfile)
- [is_readable](#function.is-readable)
- [is_writable](#function.is-writable)
- [is_dir](#function.is-dir)
- [realpath](#function.realpath)
- [filesize](#function.filesize)

Para configurar el redireccionamiento de funciones con Wincache, use el archivo `reroute.ini` incluido en el paquete. Cópielo en el directorio donde se encuentra `php.ini`. Luego, agregue wincache.rerouteini en `php.ini` y especifique la ruta absoluta o relativa a `reroute.ini`.

Activación de las funcionalidades de redireccionamiento de funciones de WinCache

```php
wincache.rerouteini = C:\PHP\reroute.ini

    
```

> [!NOTE]
> Si está habilitado, se recomienda aumentar el tamaño del caché de archivos. Esto se puede hacer usando el parámetro [wincache.fcachesize](#ini.wincache.fcachesize).

El archivo `reroute.ini` contiene la correspondencia entre la función PHP nativa y el equivalente de Wincache. Cada línea en el archivo define una correspondencia. Aquí está la sintaxis:

`<Nombre de la función PHP>:[<número de parámetros de la función>]=<nombre de la función wincache>`

A continuación se muestra un ejemplo de archivo. En este ejemplo, las llamadas a las funciones PHP `file_get_contents` serán reemplazadas por `wincache_file_get_contents` solo si el número de parámetros pasados a la función es menor o igual a dos. Es útil especificar el número de parámetros cuando la función de reemplazo no está diseñada para usar todos ellos.

Reroute.ini

```php
 
[FunctionRerouteList]
file_exists=wincache_file_exists
file_get_contents:2=wincache_file_get_contents
readfile:2=wincache_readfile
is_readable=wincache_is_readable
is_writable=wincache_is_writable
is_writeable=wincache_is_writable
is_file=wincache_is_file
is_dir=wincache_is_dir
realpath=wincache_realpath
filesize=wincache_filesize

    
```
