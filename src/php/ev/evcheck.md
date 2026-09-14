---
title: La clase EvCheck
source_url: https://www.php.net/manual/es/class.evcheck.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evcheck.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17960
---

## Introducción

Los observadores `EvPrepare` y `EvCheck` se utilizan habitualmente juntos. El observador `EvPrepare` será llamado antes de los bloques del proceso, mientras que el observador `EvCheck` será llamado después.

No está permitido llamar al método EvLoop::run o a un método/función similar que entre en el bucle del evento actual desde el observador `EvPrepare`, o desde el observador `EvCheck`. Sin embargo, esto es posible para todos los demás bucles que no sean el actual. La razón es que no es necesario verificar la recursión en estos observadores, es decir, la secuencia siguiente será siempre: `EvPrepare` -\> bloqueo -\> `EvCheck`, por lo tanto, tener un observador para cada uno no es útil, sabiendo que siempre serán llamados juntos al llamar al bloqueo.

El propósito principal es integrar otros mecanismos de eventos en la biblioteca *libev*, con un uso avanzado. Pueden ser utilizados, por ejemplo, para monitorear los cambios de variables, implementar observadores personalizados, integrar net-snmp o una biblioteca adicional, y mucho más. También pueden ser útiles para almacenar en caché datos, y querer mostrarlos después del bloqueo.

Se recomienda proporcionar una prioridad alta a `EvCheck` (`Ev::MAXPRI`) para asegurarse de que se ejecutará antes que cualquier otro observador en la cola (a diferencia de lo que ocurre con el observador `EvPrepare`).

Además, los observadores `EvCheck` no deben activar/alimentar eventos. Aunque *libev* admite esto, pueden ser ejecutados antes de que los otros observadores `EvCheck` terminen sus trabajos.

## Sinopsis de la clase

EvCheck

EvCheck

extends

EvWatcher

Propiedades heredadas

Métodos

Métodos heredados
