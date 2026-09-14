---
title: La clase EvStat
source_url: https://www.php.net/manual/es/class.evstat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18590
---

## Introducción

La clase `EvStat` supervisa un fichero del sistema de ficheros para detectar cualquier modificación de sus atributos. Invoca el comando *stat()* en esta ruta, a intervalos regulares (o cuando el sistema operativo notifica una modificación) y verifica si ha sido modificado desde la última vez, llamando a la función de retrollamada si es el caso.

La ruta no necesita existir: el cambio de "la ruta existe" a "la ruta no existe" es una modificación de estado como cualquier otra. La condición "la ruta no existe" está indicada por el valor 0 del elemento `'nlink'` (devolvido por el método EvStat::attr).

La ruta no debe terminar con un slash, ni contener componentes especiales como `'.'` o `..`. La ruta debe ser absoluta: si es relativa, y el directorio de trabajo cambia, entonces el comportamiento será indefinido.

Dado que no hay una interfaz de notificación de cambios portable, la implementación portable simplemente invoca el comando *stat()* en la ruta para verificar las modificaciones. Para este caso, un intervalo regular puede ser especificado. Si se especifica, un intervalo de `0.0` (altamente recomendado) entonces un valor predeterminado no especificado será utilizado (alrededor de 5 segundos, y puede ser modificado dinámicamente). *libev* también impondrá un intervalo mínimo que actualmente está alrededor de `0.1`, lo cual es ampliamente suficiente.

Este tipo de observador no está previsto para un gran número de observadores `EvStat`, dado que incluso con las notificaciones del sistema sobre modificaciones soportadas por el sistema operativo, esto consume muchos recursos.

## Sinopsis de la clase

EvStat

EvStat

extends

EvWatcher

Propiedades

public

path

public

interval

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`interval`  
*Solo lectura*. La rapidez con la que una modificación debe ser detectada; normalmente, debe valer `0.0` para dejar que *libev* elija un buen valor.

`path`  
*Solo lectura*. La ruta hacia el fichero del cual se desean supervisar las modificaciones de estado.
