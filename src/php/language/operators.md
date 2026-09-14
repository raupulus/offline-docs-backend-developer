---
title: Los operadores
source_url: https://www.php.net/manual/es/language.operators.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 6043cd254
order: 2780
---

## Los operadores

Un operador es algo que toma uno o más valores (o expresiones, en la jerga de la programación) y que produce otro valor (por lo tanto, la construcción misma se convierte en una expresión).

Los operadores pueden ser agrupados según el número de valores que aceptan. El operador unario opera solo sobre un valor, por ejemplo `!` (el [operador de negación](#language.operators.logical)) o `++` (el [operador de incremento](#language.operators.increment)). Los operadores binarios toman dos valores, como los tan conocidos [operadores aritméticos](#language.operators.arithmetic) `+` (más) y `-` (menos), y la mayoría de los operadores PHP entran en esta categoría. Finalmente, hay un único [operador ternario](#language.operators.comparison.ternary), `? :`, que acepta tres valores; Esto se suele denominar simplemente "operador ternario" (aunque quizá podría llamarse más apropiadamente "operador condicional").

Una lista completa de los operadores de PHP se encuentra en la sección [precedencia de los operadores](#language.operators.precedence). Esta sección también explica la precedencia de los operadores y la asociatividad, que indican exactamente cómo se evalúan las expresiones que contienen varios operadores diferentes.

Existe una extensión PECL que permite la sobrecarga de algunos operadores para objetos. Para más información, véase la sección de [Sobrecarga de operadores para objetos](#book.operator).
