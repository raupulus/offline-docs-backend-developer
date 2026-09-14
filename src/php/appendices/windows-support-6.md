---
title: Soporte para Windows
source_url: https://www.php.net/manual/es/migration84.windows-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/windows-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: d64e811ea
order: 1170
---

## Soporte para Windows

## Núcleo

La compilación con Visual Studio ahora requiere al menos Visual Studio 2019. Sin embargo, se recomienda Visual Studio 2022.

Ahora se detecta correctamente la compatibilidad con CPU AVX(2) en las compilaciones MSVC.

Las compilaciones nativas AVX-512 son ahora compatibles a través de la opción de configuración `--enable-native-intrinsics=avx512`
