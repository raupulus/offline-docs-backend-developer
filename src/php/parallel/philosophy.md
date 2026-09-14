---
title: Filosofía
source_url: https://www.php.net/manual/es/philosophy.parallel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/philosophy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60350
---

## Filosofía

Esta sección contiene filosofías importantes para escribir código paralelo y algunos detalles sobre la implementación interna de parallel.

## No se comunica compartiendo memoria; comparta memoria comunicando.

Esta filosofía, adoptada por parallel, tiene sus orígenes en Go, una de las plataformas más ampliamente admiradas, si no utilizadas, para escribir código paralelo en este momento. Los desarrolladores de Go deben trabajar duro para estar a la altura de este ideal: PHP y parallel hacen todo el trabajo difícil para el programador, y por omisión.

En los modelos de hilos convencionales encontrados en otros lenguajes, generalmente los hilos se comunican entre sí por el simple hecho de que operan en el mismo espacio de direcciones. El desarrollador debe desplegar exclusiones mutuas, variables de condición y otras primitivas de bajo nivel de hilos o sincronización para garantizar una comunicación adecuada del estado y la coherencia.

Cuando el modelo convencional se invierte, significa que los hilos solo comparten memoria mediante la comunicación (una variable se pasa sobre un canal, por ejemplo).

Cuando parallel pasa una variable de un hilo a otro por cualquier medio - argumentos de tarea, retorno a través de Future y Channels - se pasa por valor. En todos los casos, excepto en el caso de los canales no almacenados en búfer, la variable también se almacena en búfer de modo que no pueda cambiar (o ser destruida) antes de ser utilizada en el hilo al que se transmite la variable. Una lectura no almacenada en búfer en un canal es el único caso en el que un hilo lee directamente la memoria asignada por otro hilo, puede hacerlo de manera segura porque el hilo que posee la memoria espera a que la lectura termine antes de poder continuar manipulándola, y el hilo que no posee la memoria lee por valor. Cuando ambos hilos continúan, ya no comparten memoria.

Esto hace que escribir y razonar sobre el código paralelo sea mucho más fácil que el modelo convencional de hilos. Esto significa que el programador no necesita considerar que los hilos pueden manipular datos simultáneamente, ya que esto no es posible.

Esto también convierte a PHP en la plataforma perfecta para implementar una API de concurrencia paralela basada en CSP (paso de mensajes sobre canales), ya que PHP en sí mismo no comparte nada - los hilos de PHP funcionan en su propio espacio de direcciones virtual por omisión, y por lo tanto solo pueden compartir memoria comunicándose.

## Los datos deben tener un propietario único y definitivo

Cuando se aborda el modelo CSP por primera vez, un programador versado en el modelo tradicional de hilos puede encontrarse buscando estructuras de datos concurrentes, ya que es a lo que está acostumbrado: pasa objetos compartidos para manipularlos.

Cuando se aborda el modelo CSP, no es necesario que las estructuras de datos sean compartidas por muchas tareas, y de hecho, es más simple si no lo son. Los datos deben ser propiedad de una sola tarea, las modificaciones (o operaciones) de esta estructura de datos deben ser comunicadas a través de canales y realizadas por el propietario de los datos, el éxito, el fracaso, o el resultado (estado) del cambio (o de la operación) siendo comunicado de vuelta.

Una vez más, la naturaleza de PHP y la naturaleza de copia por valor de parallel ayuda al desarrollador a alcanzar este objetivo, ningún dato será compartido por accidente, solo como resultado de la comunicación.
