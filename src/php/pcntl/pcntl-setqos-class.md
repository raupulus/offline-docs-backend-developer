---
title: pcntl_setqos_class
description: Establece la clase de calidad de servicio del hilo actual
source_url: https://www.php.net/manual/es/function.pcntl-setqos-class.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-setqos-class.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: 28192e830
order: 61330
---

pcntl_setqos_class

Establece la clase de calidad de servicio del hilo actual

## Descripción

```php
pcntl_setqos_class([Pcntl\QosClass $qos_class]): void
```php

Establece la clase de calidad de servicio (QoS) del hilo actual.

## Parámetros

`qos_class`  
La clase de calidad de servicio a asignar al hilo actual. El sistema operativo la utiliza como una indicación para planificar el tiempo de CPU, la prioridad de E/S y el consumo de energía, donde las clases superiores tienen prioridad sobre las inferiores. Véase Pcntl\QosClass para los casos disponibles.

`Pcntl\QosClass::UserInteractive`  
Prioridad más alta. Destinada al trabajo que controla directamente una interfaz de usuario y debe completarse prácticamente al instante para evitar retrasos perceptibles, como la gestión de eventos o el dibujado.

`Pcntl\QosClass::UserInitiated`  
Prioridad alta, justo por debajo de `UserInteractive`. Destinada al trabajo que el usuario ha iniciado explícitamente y está esperando activamente, que se espera que se complete en unos pocos segundos.

`Pcntl\QosClass::Default`  
Prioridad estándar, utilizada cuando no se aplica ninguna clase más específica. Se ejecuta después del trabajo de mayor prioridad pero antes de `Utility` y `Background`.

`Pcntl\QosClass::Utility`  
Prioridad inferior, destinada al trabajo de larga duración del que el usuario es consciente pero que no está esperando activamente, como descargas, importaciones o cálculos masivos. Se planifica de forma eficiente energéticamente.

`Pcntl\QosClass::Background`  
Prioridad más baja, destinada al trabajo del que el usuario no es consciente, como la precarga, la indexación o el mantenimiento. Muy optimizada para la eficiencia energética y puede aplazarse cuando el sistema está bajo carga.

> [!NOTE]
> Esta función solo está disponible en plataformas Apple.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza un Error si la llamada subyacente a `pthread_set_qos_class_self_np()` falla.

## Véase también

pcntl_getqos_class

Pcntl\QosClass
