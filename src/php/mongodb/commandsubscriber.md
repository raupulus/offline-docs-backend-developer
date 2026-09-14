---
title: La interfaz MongoDB\Driver\Monitoring\CommandSubscriber
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-commandsubscriber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsubscriber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50150
---

## Introducción

Las clases pueden implementar esta interfaz para registrar un observador de eventos que es notificado para cada evento de comando iniciado, [???](#mongodb.tutorial.apm) para más información.

## Sinopsis de la interfaz

MongoDB\Driver\Monitoring\CommandSubscriber

MongoDB\Driver\Monitoring\CommandSubscriber

MongoDB\Driver\Monitoring\Subscriber

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Los tipos de retorno previamente declarados como provisionales ahora son aplicados. |
| PECL mongodb 1.15.0 | Los tipos de retorno de los métodos son declarados como provisionales en PHP 8.0 y posteriores, lo que desencadena avisos de depreciación en el código que implementa esta interfaz sin declarar los tipos de retorno apropiados. El atributo `#[ReturnTypeWillChange]` puede ser añadido para ignorar la notificación de depreciación. |
