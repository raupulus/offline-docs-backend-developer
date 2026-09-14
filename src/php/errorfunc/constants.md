---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/errorfunc.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: true
translation_revision: 4c9b6ff9f
order: 17570
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

Las constantes siguientes (ya sea el valor numérico correspondiente, o su nombre simbólico) se utilizan como una máscara de bits para especificar los errores a reportar. Es posible utilizar [los operadores a nivel de bits](#language.operators.bitwise) para combinar estos valores o enmascarar ciertos tipos de errores.

> [!TIP]
> Los nombres de las constantes pueden ser utilizados en `php.ini` en lugar de los valores numéricos brutos a los que corresponden. Sin embargo, solo los operadores `|`, `~`, `^`, `!`, `&` son comprendidos en `php.ini`.

> [!WARNING]
> No es posible utilizar los nombres simbólicos fuera de PHP. Por ejemplo, en `httpd.conf` el valor calculado de la máscara de bits debe ser utilizado en su lugar.

`E_ERROR` (`int`)  
Errores fatales durante la ejecución Estos indican errores de los cuales no es posible recuperarse, como un problema de asignación de memoria. La ejecución del script es detenida.

Valor de la constante: `1`

`E_WARNING` (`int`)  
Advertencias durante la ejecución (errores no fatales). La ejecución del script no es interrumpida.

Valor de la constante: `2`

`E_PARSE` (`int`)  
Errores de análisis durante la compilación. Los errores de análisis deberían ser generados únicamente por el analizador sintáctico.

Valor de la constante: `4`

`E_NOTICE` (`int`)  
Notificaciones de ejecución. Indican que el script ha encontrado algo que podría señalar un error, pero que también podría ocurrir normalmente durante la ejecución de un script.

Valor de la constante: `8`

`E_CORE_ERROR` (`int`)  
Errores fatales que ocurren durante el inicio inicial de PHP. Es como una `E_ERROR`, excepto que es generada por el núcleo de PHP.

Valor de la constante: `16`

`E_CORE_WARNING` (`int`)  
Advertencias (errores no fatales) que ocurren durante el inicio inicial de PHP. Es como un `E_WARNING`, excepto que es generada por el núcleo de PHP.

Valor de la constante: `32`

`E_COMPILE_ERROR` (`int`)  
Errores fatales de compilación. Es como un `E_ERROR`, excepto que es generado por el motor de script Zend.

Valor de la constante: `64`

`E_COMPILE_WARNING` (`int`)  
Advertencias de compilación (errores no fatales). Es como un `E_WARNING`, excepto que es generado por el motor de script Zend.

Valor de la constante: `128`

`E_DEPRECATED` (`int`)  
Avisos de depreciación durante la ejecución. Actívelo para recibir advertencias sobre código que no funcionará en versiones futuras.

Valor de la constante: `8192`

`E_USER_ERROR` (`int`)  
Mensaje de error generado por el usuario. Esto se asemeja a un `E_ERROR`, excepto que es generado en el código PHP utilizando la función PHP `trigger_error`.

Valor de la constante: `256`

> [!WARNING]
> El uso de esta constante con `trigger_error` está obsoleto a partir de PHP 8.4.0. Se recomienda lanzar una Exception o llamar a `exit` en su lugar.

`E_USER_WARNING` (`int`)  
Mensaje de advertencia generado por el usuario. Esto se asemeja a un `E_NOTICE`, excepto que es generado en el código PHP utilizando la función PHP `trigger_error`.

Valor de la constante: `512`

`E_USER_NOTICE` (`int`)  
Mensaje de notificación generado por el usuario. Esto se asemeja a un `E_NOTICE`, excepto que es generado en el código PHP utilizando la función PHP `trigger_error`.

Valor de la constante: `1024`

`E_USER_DEPRECATED` (`int`)  
Mensaje de depreciación generado por el usuario. Esto se asemeja a un `E_DEPRECATED`, excepto que es generado en el código PHP utilizando la función PHP `trigger_error`.

Valor de la constante: `16384`

`E_STRICT` (`int`)  
Sugerencias de ejecución emitidas por PHP sobre el código ejecutado para garantizar la compatibilidad futura.

Valor de la constante: `2048`

> [!WARNING]
> Este nivel de error no es utilizado, y ha sido depreciado a partir de PHP 8.4.0.

`E_RECOVERABLE_ERROR` (`int`)  
"Excepciones" del motor antiguo correspondientes a un error fatal recuperable. Similar a Error pero debe ser capturado mediante un manejador de errores definido por el usuario (ver `set_error_handler`). Si no es gestionado, se comporta como `E_ERROR`.

Valor de la constante: `4096`

> [!NOTE]
> Este nivel de error está efectivamente inutilizado, el único caso en el que puede ocurrir es cuando la interpretación de un `object` como `bool` falla. Esto solo puede ocurrir para objetos internos.
>
> El ejemplo más común, anterior a PHP 8.4.0, es el uso de una instancia `GMP` en una condición.

`E_ALL` (`int`)  
Máscara de bits que contiene todos los errores, advertencias y notificaciones.

Valor de la constante: `30719`

> [!WARNING]
> Anterior a PHP 8.4, el valor de la constante era `32767`.
