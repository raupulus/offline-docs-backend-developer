---
title: Ejecución de PHP en línea de comandos en sistemas Windows
source_url: https://www.php.net/manual/es/install.windows.commandline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/windows/commandline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: 10e6a2b04
order: 1920
---

## Ejecución de PHP en línea de comandos en sistemas Windows

Esta sección contiene notas y consejos específicos para la ejecución de PHP en línea de comandos en Windows.

> [!NOTE]
> ¡Leer primero los [pasos de instalación manual](#install.windows.manual)!

Tener PHP ejecutándose desde la línea de comandos puede realizarse sin hacer modificaciones en Windows.

    C:\php\php.exe -f "C:\PHP Scripts\script.php" -- -arg1 -arg2 -arg3

      

Pero hay algunos pasos fáciles de seguir para simplificar esto. Algunos de estos pasos ya deberían haberse tomado, pero se repiten aquí para proporcionar una secuencia completa paso a paso.

- Añadir la ubicación del ejecutable PHP (`php.exe`, `php-win.exe` o `php-cli.exe` según la versión de PHP y las preferencias de visualización) a la variable de entorno `PATH`. Leer más sobre cómo añadir el directorio PHP apropiado a la variable de entorno `PATH` en la [entrada FAQ correspondiente](#faq.installation.addtopath).

- Añadir la extensión `.PHP` a la variable de entorno `PATHEXT`. Esto puede hacerse al mismo tiempo que se añade la variable de entorno `PATH`. Siga los mismos pasos descritos en la [FAQ](#faq.installation.addtopath) pero modifique la variable de entorno `PATHEXT` en lugar de la variable de entorno `PATH`.

  > [!NOTE]
  > La posición en la que se coloca `.PHP` determinará qué script o programa se ejecuta cuando hay nombres de ficheros correspondientes. Por ejemplo, colocar `.PHP` antes de `.BAT` hará que se ejecute el script, en lugar del fichero batch, si hay un fichero batch con el mismo nombre.

- Asociar la extensión `.PHP` con un tipo de fichero. Esto se hace ejecutando el siguiente comando:

      assoc .php=phpfile

           

- Asociar el tipo de fichero `phpfile` con el ejecutable PHP apropiado. Esto se hace ejecutando el siguiente comando:

      ftype phpfile="C:\php\php.exe" -f "%1" -- %~2

           

Siguiendo estos pasos, los scripts PHP podrán ser ejecutados desde cualquier directorio sin necesidad de escribir el ejecutable PHP o la extensión `.PHP` y todos los argumentos serán proporcionados al script para su procesamiento.

El ejemplo a continuación detalla algunos de los cambios de registro que pueden hacerse manualmente.

Cambios de registro

    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\.php]
    @="phpfile"
    "Content Type"="application/php"

    [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\phpfile]
    @="PHP Script"
    "EditFlags"=dword:00000000
    "BrowserFlags"=dword:00000008
    "AlwaysShowExt"=""

    [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\phpfile\DefaultIcon]
    @="C:\\php\\php-win.exe,0"

    [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\phpfile\shell]
    @="Open"

    [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\phpfile\shell\Open]
    @="&Open"

    [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\phpfile\shell\Open\command]
    @="\"C:\\php\\php.exe\" -f \"%1\" -- %~2"

Con estos cambios, el mismo comando puede escribirse como sigue:

    "C:\PHP Scripts\script" -arg1 -arg2 -arg3

      

o, si la ruta `"C:\PHP Scripts"` está en la variable de entorno `PATH`:

    script -arg1 -arg2 -arg3

      

> [!NOTE]
> Hay un pequeño problema si la intención es utilizar esta técnica y utilizar los scripts PHP como filtro en línea de comandos, como en el ejemplo a continuación:
>
>     dir | "C:\PHP Scripts\script" -arg1 -arg2 -arg3
>
>        
>
> o
>
>     dir | script -arg1 -arg2 -arg3
>
>        
>
> El script puede simplemente bloquearse y no mostrar nada. Para que esto funcione, se debe realizar otro cambio de registro:
>
>     Windows Registry Editor Version 5.00
>
>     [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer]
>     "InheritConsoleHandles"=dword:00000001
>
>        
>
> Más información sobre este problema puede encontrarse en el artículo de la base de conocimientos de Microsoft: 321788. A partir de Windows 10, este ajuste parece estar invertido, haciendo que la instalación por defecto de Windows 10 soporte automáticamente los manejadores de consola heredados.
