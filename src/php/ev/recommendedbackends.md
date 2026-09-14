---
title: Ev::recommendedBackends
description: Devuelve una máscara de octetos de backends recomendados para la plataforma
  actual
source_url: https://www.php.net/manual/es/ev.recommendedbackends.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/recommendedbackends.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 17840
---

Ev::recommendedBackends

Devuelve una máscara de octetos de backends recomendados para la plataforma actual

## Descripción

```php
final public static Ev::recommendedBackends(): int
```php

Devuelve un conjunto de todos los backends compilados en este binario de `libev`, y también recomendados para esta plataforma, lo que significa que deberían funcionar para la mayoría de los tipos de descriptor de ficheros. Este conjunto es generalmente más pequeño que el devuelto por la función `ev_supported_backends`, sabiendo que, por ejemplo, `kqueue` está roto en los sistemas `BSD` y no será auto-detectado hasta que no sea requerido explícitamente. Es el conjunto de backends que `libev` utilizará cuando ninguno sea solicitado explícitamente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una máscara de octetos que contiene los [flags de backends](#ev.constants.watcher-backends) combinados utilizando el operador *OR*.

## Ejemplos

Encapsula un bucle en otro

```
<?php
/*
* Intenta recuperar un bucle de evento interno, y encapsularlo en
* el bucle de evento por defecto.
* Si es posible, se utiliza el bucle por defecto.
* El bucle por defecto se almacena en $loop_hi, mientras que el bucle interno
* se almacena en $loop_lo (que es $loop_hi en este caso ya que ningún bucle interno
* puede ser utilizado).
*
* Ejemplo de:
* http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Examples_CONTENT-9
*/
$loop_hi = EvLoop::defaultLoop();
$loop_lo = NULL;
$embed   = NULL;

/*
* Mira si hay posibilidad de recuperar uno que funcione
* (el valor del flag a 0 significa auto-detección)
*/
$loop_lo = Ev::embeddableBackends() & Ev::recommendedBackends()
 ? new EvLoop(Ev::embeddableBackends() & Ev::recommendedBackends())
 : 0;

if ($loop_lo) {
 $embed = new EvEmbed($loop_lo, function () {});
} else {
 $loop_lo = $loop_hi;
}
?>

   
```php

## Véase también

EvEmbed

Ev::embeddableBackends

Ev::supportedBackends

Los flags de Backend

Los ejemplos
