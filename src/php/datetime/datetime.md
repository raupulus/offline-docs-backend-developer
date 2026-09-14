---
title: La clase DateTime
source_url: https://www.php.net/manual/es/class.datetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: c9490d424
order: 10560
---

## Introducción

Representación de la fecha y la hora.

Esta clase se comporta igual que `DateTimeImmutable`, excepto que los objetos se modifican cuando se llaman métodos de modificación como `DateTime::modify`.

> [!WARNING]
> Llamando metodos en objetos de la clase `DateTime` cambiará la información encapsulada en ese objeto, si deseas prevenir eso tendrás que usar el operador `clone` para crear un nuevo objeto. Usa `DateTimeImmutable` en lugar de `DateTime` para obtener este comportamiento recomendado por defecto.

## Sinopsis de la clase

DateTime

implements

DateTimeInterface

Constantes heredadas

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 7.2.0 | Las constantes de clase de `DateTime` ahora están definidas en `DateTimeInterface`. |
| 7.1.0 | El constructor de `DateTime` ahora incluye los microsegundos actuales en el valor construido. Antes de esto, siempre inicializaría los microsegundos a `0`. |
