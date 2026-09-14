---
title: La clase parallel\Channel
source_url: https://www.php.net/manual/es/class.parallel-channel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel.channel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60270
---

## canales no tamponados

Un canal no tamponado bloqueará las llamadas a parallel\Channel::send hasta que haya un receptor, y bloqueará las llamadas a parallel\Channel::recv hasta que haya un emisor. Esto significa que un canal no tamponado no es solo un medio para compartir datos entre las tareas sino también un método simple de sincronización.

Un canal no tamponado es la forma más rápida de compartir datos entre las tareas, requiriendo la menor cantidad de copias.

## canales tamponados

Un canal tamponado no bloqueará las llamadas a parallel\Channel::send hasta que se alcance la capacidad, las llamadas a parallel\Channel::recv bloquearán hasta que haya datos en el búfer.

## Cierres en los canales

Una funcionalidad poderosa de los canales paralelos es que permiten el intercambio de cierres entre las tareas (y los entornos de ejecución).

Cuando un cierre es enviado a través de un canal, el cierre es tamponado, esto no cambia el búfer del canal que transmite el cierre, pero afecta el ámbito estático dentro del cierre: el mismo cierre enviado a diferentes ejecuciones, o a la misma ejecución, no compartirá su ámbito estático.

Esto significa que cada vez que un cierre es ejecutado y ha sido transmitido por un canal, el estado estático será el mismo que cuando el cierre fue tamponado.

## canales anónimos

La construcción de canales anónimos permite al desarrollador evitar asignar nombres a cada canal: parallel generará un nombre único para los canales anónimos.

## Sinopsis de la clase

parallel\Channel

final

parallel\Channel

Constructores anónimos

Acceso

Compartir

Cerrar

Constantes para el tamponamiento infinito

const

Infinite
