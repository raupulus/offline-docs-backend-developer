---
title: Instalación
source_url: https://www.php.net/manual/es/mongodb.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 838c897fc
order: 48720
---

## Instalación

## Instalación de la extensión MongoDB PHP con PIE

> [!NOTE]
> El instalador de Extensiones para PHP (PHP Installer for Extensions - PIE) es una nueva herramienta que reemplazará PECL. Recomendamos usar PIE para instalar extensiones. Más información en <https://github.com/php/pie>

Para instalar la extensión MongoDB usando PIE, ejecute el siguiente comando:

```php
pie install mongodb/mongodb-extension

    
```

## Instalación de la extensión MongoDB PHP con PECL

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/mongodb>

Los usuarios de Linux, Unix y macOS pueden ejecutar el siguiente comando para instalar la extensión:

```php
$ sudo pecl install mongodb

   
```

En sistemas con múltiples versiones de PHP instaladas (por ejemplo, la versión predeterminada de macOS, Homebrew), cada versión de PHP tendrá su propio comando [pecl](#install.pecl) y archivo(s) `php.ini`. Además, cada entorno de PHP (por ejemplo, CLI, web) puede usar archivos `php.ini` separados.

A partir de la versión 1.17.0 de la extensión, PECL solicitará varias opciones de `configure`. Para instalar la extensión con las opciones predeterminadas en un script no interactivo, se puede enviar una entrada de cadena vacía a `pecl install` usando el comando `yes`:

```php
$ yes '' | sudo pecl install mongodb

   
```

Se puede encontrar una lista completa de las opciones de `configure` admitidas en el archivo `package.xml` incluido en el paquete PECL. Para instalar la extensión con opciones específicas de `configure` en un script no interactivo, se puede usar la opción `--configureoptions` para `pecl install`:

```php
$ sudo pecl install --configureoptions='with-mongodb-system-libs="yes" enable-mongodb-developer-flags="no"' mongodb

   
```

Por omisión, instalar la extensión mediante PECL usará versiones integradas de [libbson](https://github.com/mongodb/mongo-c-driver/tree/master/src/libbson), [libmongoc](https://github.com/mongodb/mongo-c-driver) y [libmongocrypt](https://github.com/mongodb/libmongocrypt) e intentará configurarlas automáticamente.

> [!NOTE]
> Si el proceso de compilación no logra encontrar una biblioteca SSL, verifique que los paquetes de desarrollo (por ejemplo, `libssl-dev`) y [pkg-config](https://en.wikipedia.org/wiki/Pkg-config) estén ambos instalados. Si esto no resuelve el problema, considere usar el [proceso de instalación manual](#mongodb.installation.manual).

Finalmente, agregue la siguiente línea al archivo `php.ini` para cada entorno que necesite usar la extensión:

```php
extension=mongodb.so

   
```

## Instalación de la extensión MongoDB PHP en macOS con Homebrew

[Homebrew 1.5.0](https://brew.sh/2018/01/19/homebrew-1.5.0/) dejó de dar soporte al [Homebrew/php tap](https://github.com/Homebrew/brew) y eliminó las fórmulas para extensiones individuales de PHP. A partir de ahora, los usuarios de macOS deben instalar la fórmula [php](https://formulae.brew.sh/formula/php) y seguir las instrucciones estándar de [instalación con PECL](#mongodb.installation.pecl) usando el comando [pecl](#install.pecl) proporcionado por la instalación de PHP de Homebrew.

Alternativamente, el [repositorio shivammathur/extensions](https://github.com/shivammathur/homebrew-extensions) proporciona fórmulas para extensiones individuales de PHP. Por ejemplo, para instalar la extensión para PHP 8.4, ejecute:

```php
$ brew install shivammathur/extensions/mongodb@8.4

   
```

Tenga en cuenta que solo está disponible la versión más reciente de la extensión en brew.

> [!NOTE]
> Para garantizar que el soporte SSL pueda configurarse correctamente, asegúrese de que las fórmulas `openssl` y `pkgconf` estén instaladas. Si falta alguno de estos paquetes, la extensión se compilará con Secure Transport, lo que puede generar problemas de compatibilidad.

## Instalación de la extensión MongoDB PHP en Windows

Se adjuntan binarios precompilados a los [lanzamientos del proyecto en Github](https://github.com/mongodb/mongo-php-driver/releases/). Se publican archivos para varias combinaciones de versión de PHP, seguridad de subprocesos (TS o NTS) y arquitectura (x86 o x64). Determine el archivo correcto para el entorno de PHP y extraiga el archivo `php_mongodb.dll` al directorio de extensiones ("ext" por omisión).

Agregue la siguiente línea al archivo `php.ini` para cada entorno que necesite usar la extensión:

```php
extension=php_mongodb.dll

   
```

Si no selecciona el binario correcto, se producirá un error al intentar cargar la DLL de la extensión en tiempo de ejecución:

```php
PHP Warning:  PHP Startup: Unable to load dynamic library 'mongodb'

   
```

Asegúrese de que la DLL descargada corresponda a las siguientes propiedades del entorno de ejecución de PHP: Versión de PHP (`PHP_VERSION`), Seguridad de subprocesos (`PHP_ZTS`), Arquitectura (`PHP_INT_SIZE`)

Además de las constantes mencionadas anteriormente, estas propiedades también pueden inferirse desde la función `phpinfo`. Si un sistema tiene múltiples entornos de ejecución de PHP instalados, verifique que la salida de `phpinfo` corresponda al entorno correcto.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `libsasl.dll`

## Compilación del controlador MongoDB PHP desde el código fuente

Para desarrolladores y usuarios interesados en las correcciones más recientes de errores, la extensión puede compilarse desde el código fuente más reciente en [Github](https://github.com/mongodb/mongo-php-driver). Ejecute los siguientes comandos para clonar y compilar el proyecto:

```php
$ git clone https://github.com/mongodb/mongo-php-driver.git
$ cd mongo-php-driver
$ git submodule update --init
$ phpize
$ ./configure
$ make all
$ sudo make install

   
```

En sistemas con múltiples versiones de PHP instaladas (por ejemplo, la versión predeterminada de macOS, Homebrew), cada versión de PHP tendrá su propio comando [phpize](#install.pecl.phpize) y archivo(s) `php.ini`. Además, cada entorno de PHP (por ejemplo, CLI, web) puede usar archivos `php.ini` separados.

Por omisión, la extensión usará versiones integradas de [libbson](https://github.com/mongodb/mongo-c-driver/tree/master/src/libbson), [libmongoc](https://github.com/mongodb/mongo-c-driver) y [libmongocrypt](https://github.com/mongodb/libmongocrypt) e intentará configurarlas automáticamente. Si estas bibliotecas ya están instaladas como bibliotecas del sistema, la extensión puede utilizarlas especificando `--with-mongodb-system-libs=yes` como opción para `configure`.

Para obtener una lista completa de las opciones de `configure`, ejecute `configure --help`.

Al usar versiones integradas de libmongoc y libmongocrypt, la extensión también intentará seleccionar una biblioteca SSL según la opción `--with-mongodb-ssl` de `configure`. A partir de la versión 1.17.0 de la extensión, OpenSSL siempre se prefiere por omisión. Anteriormente, Secure Transport era la opción predeterminada en macOS y OpenSSL era la opción predeterminada en todas las demás plataformas.

> [!NOTE]
> Si el proceso de compilación no logra encontrar una biblioteca SSL, verifique que los paquetes de desarrollo (por ejemplo, `libssl-dev`) y [pkg-config](https://en.wikipedia.org/wiki/Pkg-config) estén ambos instalados.
>
> Al usar Homebrew en macOS, es común que un sistema tenga instaladas múltiples versiones de OpenSSL. Para garantizar que se seleccione la versión deseada de OpenSSL, se puede usar la variable de entorno `PKG_CONFIG_PATH` para controlar la ruta de búsqueda de `pkg-config`.

El paso final de compilación, `make install`, informará dónde se ha instalado `mongodb.so`, similar a:

```php
Installing shared extensions:     /usr/lib/php/extensions/debug-non-zts-20220829/

   
```

Asegúrese de que la opción [extension_dir](#ini.extension-dir) en `php.ini` apunte al directorio donde se instaló `mongodb.so`. La opción puede consultarse ejecutando:

```php
$ php -i | grep extension_dir
  extension_dir => /usr/lib/php/extensions/debug-non-zts-20220829 =>
                   /usr/lib/php/extensions/debug-non-zts-20220829

   
```

Si los directorios difieren, cambie [extension_dir](#ini.extension-dir) en `php.ini` o mueva manualmente `mongodb.so` al directorio correcto.

Finalmente, agregue la siguiente línea al archivo `php.ini` para cada entorno que necesite usar la extensión:

```php
extension=mongodb.so

   
```
