---
title: El atributo ReturnTypeWillChange
source_url: https://www.php.net/manual/es/class.returntypewillchange.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/returntypewillchange.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 0019a7e20
order: 2970
---

## Introducción

La mayoría de los métodos internos no finales requieren ahora que los métodos sobrescritos declaren un tipo de retorno compatible, de lo contrario se emite un aviso de deprecación durante la validación de herencia. Esto introduce una fase de tipo de retorno tentativo: el motor emite un aviso de deprecación en lugar de un error fatal cuando los tipos de retorno son incompatibles, antes de que se vuelvan obligatorios en una versión futura. En caso de que el tipo de retorno no pueda declararse para un método sobrescrito debido a preocupaciones de compatibilidad entre versiones de PHP, se puede añadir un atributo `#[\ReturnTypeWillChange]` para silenciar el aviso de deprecación.

> [!WARNING]
> El atributo `ReturnTypeWillChange` suprime los avisos de deprecación *únicamente* durante la fase de tipo de retorno tentativo. No tiene efecto al sobrescribir métodos definidos en clases definidas por el usuario. Una vez que los métodos internos adopten tipos estrictos, las discrepancias en las firmas de los métodos sobrescritos provocarán un error fatal y este atributo dejará de tener efecto.

## Sinopsis de la clase

\#\[\Attribute\]

final

ReturnTypeWillChange

Métodos

## Véase también

[Visión general de los atributos](#language.attributes)
