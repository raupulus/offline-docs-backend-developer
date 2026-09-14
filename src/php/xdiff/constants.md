---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/xdiff.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_revision: 86e6094e8
order: 102080
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`XDIFF_PATCH_NORMAL` (`int`)  
Este indicador indica que las funciones `xdiff_string_patch` y `xdiff_file_patch` deben crear el resultado de aplicar el parche al contenido original, creando así una versión más reciente del archivo. Este es el modo por defecto de funcionamiento.

`XDIFF_PATCH_REVERSE` (`int`)  
Este indicador indica que las funciones `xdiff_string_patch` y `xdiff_file_patch` deben crear el resultado de revertir el parche de modificación desde el nuevo contenido, creando así la versión original.
