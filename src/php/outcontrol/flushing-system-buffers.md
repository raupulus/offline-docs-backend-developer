---
title: Vaciar los búferes del sistema
source_url: https://www.php.net/manual/es/outcontrol.flushing-system-buffers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/flushing-system-buffers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 7ad99aeaf
order: 59720
---

## Vaciar los búferes del sistema

PHP ofrece dos formas de vaciar (enviar y eliminar el contenido) los búferes del sistema: mediante la llamada a `flush` y activando el vaciado de búfer implícito con `ob_implicit_flush` o el parámetro [implicit_flush](#ini.implicit-flush) de `php.ini`.

## Comportamiento de vaciado del búfer de salida

Con el vaciado de búfer implícito desactivado, PHP solo vacía la salida cuando se llama a `flush` o cuando finaliza el script.

Con el vaciado de búfer implícito activado, PHP intentará vaciar después de cada bloque de código que produzca salida. La salida en este contexto son datos de longitud no nula que son:

- fuera de las etiquetas `<?php ?>`

- mostrados por construcciones del lenguaje y funciones cuyo propósito explícito es mostrar variables o strings proporcionados por el usuario tales como `echo`, `print`, `printf`, `var_dump`, `var_export`, `vprintf`

- mostrados por funciones cuyo propósito es recolectar y producir datos/información sobre el script en ejecución o PHP tales como `debug_print_backtrace`, `phpcredits`, `phpinfo`, ReflectionExtension::info

- mostrados por PHP en una excepción no capturada o un error no manejado (sujeto a los parámetros de [display_errors](#ini.display-errors) y [error_reporting](#ini.error-reporting))

- todo lo que se escribe en `php://output`

> [!NOTE]
> Mostrar strings vacíos o enviar encabezados no se considera salida y no desencadenará una operación de vaciado de búfer.

> [!WARNING]
> Si el vaciado de búfer implícito está activado, los caracteres de control (por ejemplo `"\n"`, `"\r"`, `"\0"`) también desencadenarán un vaciado de búfer.

## Limitaciones

Esta funcionalidad no puede vaciar los búferes de salida a nivel de usuario. Para usarlos juntos, los búferes de salida a nivel de usuario deben ser vaciados antes de vaciar los búferes del sistema para que PHP produzca una salida.

> [!WARNING]
> Llamar a `flush` o activar el vaciado de búfer implícito puede interferir con los manejadores de salida de los búferes de salida a nivel de usuario que definen y envían encabezados en un contexto web (por ejemplo `ob_gzhandler`) al enviar encabezados antes de que estos manejadores lo hagan.

El almacenamiento en búfer implementado por el software/hardware subyacente no puede ser reemplazado por PHP y debe ser tenido en cuenta al utilizar las funciones de control de búferes de PHP. Verificar los parámetros de almacenamiento en búfer de los servidores web/navegadores/consolas y trabajar con ellos puede mitigar los problemas potenciales. Trabajando en un contexto web, ya sea los parámetros de almacenamiento en búfer del servidor web o el almacenamiento en búfer del script podrían ser ajustados para funcionar en conjunto mientras que trabajar con las estrategias de almacenamiento en búfer de varios navegadores puede lograrse ajustando el almacenamiento en búfer en el script PHP. En las consolas que implementan el almacenamiento en búfer por línea, los caracteres de nueva línea podrían ser insertados en los lugares apropiados antes de vaciar la salida.

## Diferencias en el vaciado entre SAPI

Aunque el vaciado de búfer es implementado por cada SAPI de manera ligeramente diferente, estas implementaciones caen en una de dos categorías:

- Los SAPIs usados en un contexto web vaciarán primero los encabezados seguidos de la salida. `Apache2Handler`, `CGI`, `FastCGI` y `FPM` son tales SAPIs

- otros SAPIs tales como `CLI` y `embed` vaciarán solo la salida
