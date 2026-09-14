---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/random.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: c4f24e2ee
order: 67830
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

`MT_RAND_MT19937` (`int`)  
Indica que la implementación correcta de [Mt19937](http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/ARTICLES/mt.pdf) (Mersenne Twister) será utilizada por el algoritmo al crear una instancia de `Random\Engine\Mt19937` utilizando `Random\Engine\Mt19937::__construct` o al inicializar el Mersenne Twister global con `mt_srand`.

`MT_RAND_PHP` (`int`)  
Indica que una implementación incorrecta de Mersenne Twister será utilizada por el algoritmo, al crear una instancia de `Random\Engine\Mt19937` utilizando `Random\Engine\Mt19937::__construct` o al inicializar el Mersenne Twister global con `mt_srand`.

La implementación incorrecta está disponible para garantizar la compatibilidad ascendente con `mt_srand` anterior a PHP 7.1.0.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.
