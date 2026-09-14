---
title: Bufferización de salida
source_url: https://www.php.net/manual/es/outcontrol.output-buffering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/output-buffering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 7ad99aeaf
order: 59900
---

## Bufferización de salida

La bufferización de salida es el almacenamiento en búfer (temporal) de la salida antes de que sea volcada (enviada y eliminada) al navegador (en un contexto web) o al shell (en línea de comandos). Mientras la bufferización de salida esté activa, ninguna salida es enviada por el script, en su lugar, la salida es almacenada en un búfer interno.

## Efectos de la bufferización en PHP

PHP depende de la infraestructura lógica/material subyacente al vaciar el búfer de la salida. La bufferización implementada por las consolas en línea de comandos (por ejemplo, en modo línea) o los servidores web y los navegadores en un contexto web (por ejemplo, completamente bufferizado) afectan cuándo se muestra la salida al usuario final. Algunos de estos efectos pueden ser eliminados ajustando finamente los parámetros del servidor y/o alineando los tamaños de los búferes de las diferentes capas.

## Control de la bufferización de salida en PHP

PHP proporciona un búfer de salida de usuario completamente bufferizado con funciones para iniciar, manipular y desactivar el búfer (la mayoría de las funciones [ob\_\<\*\>](#ref.outcontrol)), y dos funciones para vaciar los búferes del sistema subyacentes (`flush` y `ob_implicit_flush`). Algunas de estas funcionalidades pueden ser definidas y/o configuradas utilizando los parámetros `php.ini` apropiados.

## Casos de uso

La bufferización de salida es generalmente útil en situaciones donde la salida bufferizada es modificada o inspeccionada, o es utilizada más de una vez en una petición; o cuando se desea el vaciado controlado del búfer de la salida. Los casos de uso específicos incluyen:

- almacenar en caché el resultado de scripts de cálculo/tiempo intensivos por ejemplo generando páginas `HTML` estáticas

- reutilizar la salida generada al mostrarla, guardarla en un fichero y/o enviarla por correo electrónico

- vaciar la `head` de una página `HTML` separada del `body` permite a los navegadores cargar recursos externos mientras el script ejecuta procesos potencialmente más largos (por ejemplo, acceso a una base de datos/fichero, conexión de red externa). Esto es útil únicamente si el código de estado `HTTP` no puede cambiar después del envío de las cabeceras

- extraer información de funciones que producirían de otro modo una salida (por ejemplo `phpinfo`)

- controlar la salida de código de terceros al modificar/utilizar partes (por ejemplo, extraer datos, reemplazar palabras/frases, añadir etiquetas `HTML` faltantes), o al eliminarla completamente bajo ciertas condiciones (por ejemplo, errores)

- Polyfiller ciertas funcionalidades de servidor web no disponibles (por ejemplo, comprimir o codificar la salida)
