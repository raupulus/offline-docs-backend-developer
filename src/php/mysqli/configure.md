---
title: Instalación
source_url: https://www.php.net/manual/es/mysqli.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 050e16021
order: 54790
---

## Instalación

La extensión `mysqli` fue introducida en PHP 5.0.0. El controlador nativo MySQL (MySQL Native Driver) fue introducido en PHP 5.3.0.

## Instalación en Linux

Las distribuciones Linux incluyen versiones binarias de PHP que pueden ser instaladas. Aunque estos binarios están construidos con las extensiones MySQL, las bibliotecas cliente deben ser instaladas a menudo mediante un paquete adicional. Verifique si este es el caso para su distribución.

Por ejemplo, en Ubuntu el paquete `php5-mysql` instala las extensiones PHP ext/mysql, ext/mysqli y pdo_mysql. En CentOS, el paquete `php-mysql` instala también estas tres extensiones PHP.

Alternativamente, es posible compilar esta extensión manualmente. Construir PHP desde las fuentes permite especificar las extensiones MySQL a incluir, así como las bibliotecas cliente de cada extensión.

El controlador nativo MySQL es la biblioteca cliente recomendada, ya que ofrece un aumento de rendimiento y proporciona acceso a características que no están disponibles al utilizar la biblioteca cliente MySQL. Consulte la sección [¿Qué es el controlador nativo MySQL de PHP?](#mysqli.overview.mysqlnd) para una breve descripción de las ventajas del controlador nativo MySQL.

`/path/to/mysql_config` representa la ruta de acceso del programa `mysql_config` proporcionado con MySQL servidor.

| Versión PHP | Por defecto | Opciones de configuración : [mysqlnd](#mysqlnd.overview) | Opciones de configuración : `libmysqlclient` | Historial de cambios |
|----|----|----|----|----|
| 5.4.x y posteriores | mysqlnd | `--with-mysqli` | `--with-mysqli=/path/to/mysql_config` | mysqlnd por omisión |
| 5.3.x | libmysqlclient | `--with-mysqli=mysqlnd` | `--with-mysqli=/path/to/mysql_config` | mysqlnd es soportado |
| 5.0.x, 5.1.x, 5.2.x | libmysqlclient | No Disponible | `--with-mysqli=/path/to/mysql_config` | mysqlnd no es soportado |

Matriz de soporte para la compilación mysqli {#mysqli.installation.time.matrix}

Cabe señalar que es posible mezclar las extensiones MySQL así como las bibliotecas cliente. Por ejemplo, es posible activar la extensión MySQL para utilizar la biblioteca cliente MySQL (libmysqlclient) mientras se configura la extensión `mysqli` para utilizar el controlador nativo MySQL. Todas las combinaciones de extensiones y bibliotecas cliente son posibles.

## Instalación en sistemas Windows

En Windows, la DLL `php_mysqli.dll` debe ser activada en el fichero `php.ini`.

Para activar una extensión PHP (tal como `php_mysqli.dll`), la directiva PHP [extension_dir](#ini.extension-dir) debe apuntar hacia el directorio que contiene las extensiones PHP. Consulte también [Instalación manual en Windows ](#install.windows.manual). Por ejemplo, `extension_dir` podría tener el valor `c:\php\ext`.

> [!NOTE]
> Si al iniciar el servidor web se produce un error como `"Unable to load dynamic library './php_mysqli.dll'"`, es porque `php_mysqli.dll` y/o `libmysql.dll` no pueden ser encontrados en el sistema.
