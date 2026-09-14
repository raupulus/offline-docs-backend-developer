---
title: La clase DateTimeImmutable
source_url: https://www.php.net/manual/es/class.datetimeimmutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 576c7c43f
order: 10730
---

## Introducción

Representación de fecha y hora.

Esta clase se comporta igual que `DateTime` con la excepción de que devuelve nuevos objetos cuando se llaman a métodos de modificación como `DateTime::modify`.

## Sinopsis de la clase

DateTimeImmutable

implements

DateTimeInterface

Constantes heredadas

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 7.1.0 | El constructor de `DateTimeImmutable` ahora incluye los microsegundos actuales en el valor construido. Antes de esto, siempre inicializaría los microsegundos a `0`. |
