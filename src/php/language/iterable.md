---
title: Iterables
source_url: https://www.php.net/manual/es/language.types.iterable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/iterable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: e587d0655
order: 4450
---

## Iterables

Un `Iterable` es un alias de tipo integrado durante la compilación para `array|Traversable`. Desde su introducción en PHP 7.1.0 y antes de PHP 8.2.0, `iterable` era un pseudo-tipo integrado que actuaba como el alias de tipo mencionado anteriormente y puede ser utilizado como una declaración de tipo. Un tipo iterable puede ser utilizado en un ciclo [`foreach`](#control-structures.foreach) y con `yield from` en un [generador](#language.generators).

> [!NOTE]
> Las funciones que declaran un tipo de retorno iterable también pueden ser [generadores](#language.generators).
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo de tipo de retorno iterable de un generador
>
> </div>
>
> ```
> <?php
>
> function gen(): iterable {
>     yield 1;
>     yield 2;
>     yield 3;
> }
>
> foreach(gen() as $value) {
>     echo $value, "\n";
> }
> ?>
>
>     
> ```
>
> </div>
