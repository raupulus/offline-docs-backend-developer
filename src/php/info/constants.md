---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/info.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_revision: 3f1dbc451
order: 38710
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

`CREDITS_GROUP` (`int`)  
Una lista de los desarrolladores principales

`CREDITS_GENERAL` (`int`)  
Créditos generales. Diseño del lenguaje, conceptos, autores de PHP y módulo SAPI.

`CREDITS_SAPI` (`int`)  
Una lista de las API de servidores, y sus autores.

`CREDITS_MODULES` (`int`)  
Una lista de las extensiones de PHP, y sus autores

`CREDITS_DOCS` (`int`)  
Los créditos del equipo de documentación

`CREDITS_FULLPAGE` (`int`)  
Generalmente utilizado combinado con otras opciones. Esta opción indica que debe generarse una página HTML completa.

`CREDITS_QA` (`int`)  
Los créditos para el grupo de aseguramiento de calidad.

`CREDITS_ALL` (`int`)  
Todos los créditos. Es el equivalente a: `CREDITS_DOCS | CREDITS_GENERAL | CREDITS_GROUP | CREDITS_MODULES | CREDITS_QA | CREDITS_FULLPAGE`. Genera una página HTML completa y autónoma. Es el valor por omisión.

`INFO_GENERAL` (`int`)  
La línea de configuración, la ruta del `php.ini`, la fecha de compilación, el sistema y más.

`INFO_CREDITS` (`int`)  
Créditos de PHP. Véase también `phpcredits`.

`INFO_CONFIGURATION` (`int`)  
Valores locales y de servidor de las directivas PHP. Véase también `ini_get`.

`INFO_MODULES` (`int`)  
Los módulos cargados y sus configuraciones respectivas.

`INFO_ENVIRONMENT` (`int`)  
Las variables de entorno, que también están disponibles en `$_ENV`.

`INFO_VARIABLES` (`int`)  
Todas las [ variables predefinidas](#language.variables.predefined) : `EGPCS` (Entorno, GET, POST, Cookie, Servidor).

`INFO_LICENSE` (`int`)  
La licencia de PHP. Véase también la [FAQ de la licencia](https://www.php.net/license/).

`INFO_ALL` (`int`)  
Muestra todos los valores citados anteriormente. Es el valor por omisión.

`INI_USER` (`int`)  
Esta entrada puede ser definida en los scripts de usuario (como con `ini_set`) o en el [registro de Windows](#configuration.changes.windows). La entrada puede ser definida en el fichero `.user.ini`.

`INI_PERDIR` (`int`)  
Esta entrada puede ser definida en el fichero `php.ini`, `.htaccess`, `httpd.conf` o `.user.ini`.

`INI_SYSTEM` (`int`)  
Esta entrada puede ser definida en el fichero `php.ini` o `httpd.conf`.

`INI_ALL` (`int`)  
Esta entrada puede ser definida en cualquier lugar.

Las constantes de aserciones sirven con la función `assert_options`.

`ASSERT_ACTIVE` (`int`)  
Activa la evaluación `assert`.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`ASSERT_CALLBACK` (`int`)  
Función de retrollamada de aserciones fallidas.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`ASSERT_BAIL` (`int`)  
Termina la ejecución de aserciones fallidas.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`ASSERT_EXCEPTION` (`int`)  
Lanza una `AssertionError` para cada aserción fallida.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`ASSERT_WARNING` (`int`)  
Emite una alerta PHP para cada aserción fallida.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

`ASSERT_QUIET_EVAL` (`int`)  
Desactiva el `error_reporting` durante la evaluación de las expresiones de aserción.

> [!WARNING]
> Esta característica ha sido *ELIMINADA* a partir de PHP 8.0.0.

Las constantes siguientes solo están disponibles si el sistema de alojamiento es Windows, y pueden proporcionar información sobre las versiones, lo que permite detectar la presencia de funcionalidades. Están disponibles desde PHP 5.3.0.

`PHP_WINDOWS_VERSION_MAJOR` (`int`)  
La versión mayor de Windows, que puede ser `4` (NT4/Me/98/95), `5` (XP/2003 R2/2003/2000) o `6` (Vista/2008/7/8/8.1).

`PHP_WINDOWS_VERSION_MINOR` (`int`)  
La versión menor de Windows, que puede ser `0` (Vista/2008/2000/NT4/95), `1` (XP), `2` (2003 R2/2003/XP x64), `10` (98) o `90` (ME).

`PHP_WINDOWS_VERSION_BUILD` (`int`)  
El número de compilación de Windows (por ejemplo, Windows Vista con SP1 tiene el número 6001)

`PHP_WINDOWS_VERSION_PLATFORM` (`int`)  
La plataforma que PHP utiliza actualmente: este valor puede ser `2` en Windows Vista/XP/2000/NT4, Server 2008/2003 y en Windows ME/98/95 este valor es `1`.

`PHP_WINDOWS_VERSION_SP_MAJOR` (`int`)  
La versión mayor del paquete de servicio instalado: este valor es `0` si ningún paquete de servicio está disponible. Por ejemplo, Windows XP con el paquete de servicio 3 da el valor `3` a esta constante.

`PHP_WINDOWS_VERSION_SP_MINOR` (`int`)  
La versión menor del paquete de servicio instalado. Este valor es `0` si ningún paquete de servicio está instalado.

`PHP_WINDOWS_VERSION_SUITEMASK` (`int`)  
La máscara es un campo de bits que permite conocer la presencia de diferentes funcionalidades de Windows. Vea la tabla a continuación para conocer los diferentes campos.

`PHP_WINDOWS_VERSION_PRODUCTTYPE` (`int`)  
Esta constante contiene el valor utilizado para determinar el valor de las constantes `PHP_WINDOWS_NT_*`. Este valor puede ser una de las constantes `PHP_WINDOWS_NT_*`, indicando el tipo de plataforma.

`PHP_WINDOWS_NT_DOMAIN_CONTROLLER` (`int`)  
El controlador de dominio.

`PHP_WINDOWS_NT_SERVER` (`int`)  
Un servidor de sistema (ej. `Server 2008/2003/2000`). Tenga en cuenta que si es un controlador de dominio, se indica en `PHP_WINDOWS_NT_DOMAIN_CONTROLLER`.

`PHP_WINDOWS_NT_WORKSTATION` (`int`)  
Un puesto de trabajo (ej. `Vista/XP/2000/NT4`)

La tabla a continuación presenta las funcionalidades que pueden ser verificadas en el campo de bits de la constante `PHP_WINDOWS_VERSION_SUITEMASK`.

| Bits | Descripción |
|----|----|
| `0x00000004` | Los componentes Microsoft BackOffice están instalados. |
| `0x00000400` | Windows Server 2003, Web Edition está instalado. |
| `0x00004000` | Windows Server 2003, Compute Cluster Edition está instalado. |
| `0x00000080` | Windows Server 2008 Datacenter, Windows Server 2003, Datacenter Edition o Windows 2000 Datacenter Server está instalado. |
| `0x00000002` | Windows Server 2008 Enterprise, Windows Server 2003, Enterprise Edition, Windows 2000 Advanced Server, o Windows NT Server 4.0 Enterprise Edition está instalado. |
| `0x00000040` | Windows XP Embedded está instalado. |
| `0x00000200` | Windows Vista Home Premium, Windows Vista Home Basic, o Windows XP Home Edition está instalado. |
| `0x00000100` | Remote Desktop es soportado, pero solo una sesión interactiva es soportada. Este valor está presente, a menos que el sistema no funcione en modo servidor de aplicación. |
| `0x00000001` | Microsoft Small Business Server fue instalado en el sistema, pero fue actualizado a una nueva versión de Windows. |
| `0x00000020` | Microsoft Small Business Server está instalado con la licencia cliente restringida. |
| `0x00002000` | Windows Storage Server 2003 R2 o Windows Storage Server 2003 está instalado. |
| `0x00000010` | Terminal Services está instalado. Este valor siempre está activado. Si este valor está activado, pero `0x00000100` no lo está, entonces el sistema funciona en modo de servidor de aplicación. |
| `0x00008000` | Windows Home Server está instalado. |

Campos de la máscara Windows
