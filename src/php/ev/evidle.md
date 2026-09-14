---
title: La clase EvIdle
source_url: https://www.php.net/manual/es/class.evidle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evidle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18110
---

## Introducción

Los observadores `EvIdle` lanzan los eventos cuando ningún otro evento con la misma (o superior) prioridad está pendiente (`EvPrepare`, `EvCheck` y otros observadores `EvIdle` no cuentan como *eventos*).

Asimismo, mientras el proceso está gestionando sockets o tiempos de espera máximos (o incluso señales) de la misma prioridad (o de prioridad superior), no se lanzará. Pero cuando el proceso está inactivo (o solo hay observadores con prioridad baja pendientes), los observadores `EvIdle` serán llamados una vez por iteración del bucle de eventos - y esto, mientras no se detengan, o el proceso no reciba más eventos y se ocupe así de gestionar trabajos con prioridad superior.

Además de mantener el proceso no bloqueante (lo cual es útil a veces), los observadores `EvIdle` son un buen lugar para realizar *"trabajos en pseudo-segundo plano"*, o reprogramar trabajos después de que el bucle de eventos haya gestionado los eventos excepcionales.

El efecto más notable es que, mientras los observadores *idle* estén activos, el proceso *no* se bloqueará al esperar nuevos eventos.

## Sinopsis de la clase

EvIdle

EvIdle

extends

EvWatcher

Propiedades heredadas

Métodos

Métodos heredados
