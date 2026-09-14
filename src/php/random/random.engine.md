---
title: La interfaz Random\Engine
source_url: https://www.php.net/manual/es/class.random-engine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random.engine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 68310
---

## Introducción

Un `Random\Engine` constituye una fuente de aleatoriedad de bajo nivel al devolver bytes aleatorios que son consumidos por las API de alto nivel para realizar sus operaciones. La interfaz `Random\Engine` permite intercambiar el algoritmo utilizado para generar aleatoriedad, ya que cada algoritmo realiza compromisos diferentes para responder a casos de uso específicos. Algunos algoritmos son muy rápidos, pero generan aleatoriedad de menor calidad, mientras que otros algoritmos son más lentos, pero generan mejor aleatoriedad, hasta aleatoriedad criptográficamente segura como la proporcionada por el motor `Random\Engine\Secure`.

PHP proporciona varios motores `Random\Engine` para responder a diferentes casos de uso. El motor `Random\Engine\Secure` que está respaldado por un CSPRNG es la opción por omisión recomendada, a menos que la aplicación requiera secuencias reproducibles o un rendimiento muy elevado.

## Sinopsis de la interfaz

Random

Engine

Métodos
