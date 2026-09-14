---
title: La enumeración Pcntl\QosClass
source_url: https://www.php.net/manual/es/enum.pcntl-qosclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/pcntl.qosclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: aeba24a37
order: 61520
---

## Introducción

La enumeración Pcntl\QosClass se utiliza para especificar la prioridad del proceso de usuario con `pcntl_setqos_class`.

## Sinopsis del enum

Pcntl

QosClass

UserInteractive

Inicia el proceso con la prioridad más alta.

UserInitiated

Inicia el proceso con una prioridad alta pero inferior a UserInteractive.

Default

Inicia el proceso después de todos los procesos de alta prioridad pero antes que los procesos de baja prioridad.

Utility

Descripción de Pcntl\QosClass::Utility

Background

Inicia el proceso después de que todos los procesos de alta prioridad hayan terminado.
