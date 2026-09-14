---
title: La clase Random\Engine\Secure
source_url: https://www.php.net/manual/es/class.random-engine-secure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random.engine.secure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: c8e3b2cca
order: 68300
---

## Introducción

Genera un valor aleatorio criptográficamente seguro utilizando el CSPRNG del sistema operativo.

El valor aleatorio generado por esta `Random\Engine` es adecuado para todas las aplicaciones, incluyendo la generación de secretos a largo plazo, tales como las claves de cifrado.

El motor `Random\Engine\Secure` es la opción predeterminada recomendada y segura, a menos que la aplicación requiera secuencias reproducibles o un rendimiento muy elevado.

## Sinopsis de la clase

Random\Engine

final

Secure

implements

Random\CryptoSafeEngine

Métodos
