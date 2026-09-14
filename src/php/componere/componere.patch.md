---
title: La clase Componere\Patch
source_url: https://www.php.net/manual/es/class.componere-patch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere.patch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8380
---

## Introducción

La clase Patch permite al programador cambiar el tipo de una instancia en tiempo de ejecución sin registrar una nueva Definition

Cuando se destruye un parche se revierte, de modo que los casos que fueron parcheados durante la vida del Parche son restaurados a su tipo formal.

## Sinopsis de la clase

Componere\Patch

final

Componere\Patch

extends

Componere\Abstract\Definition

Constructores

Métodos

Métodos heredados
