---
title: Directivas INI eliminadas
source_url: https://www.php.net/manual/es/migration70.incompatible.removed-ini-directives.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/removed-ini-directives.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 3e08a8aae
order: 340
---

## Directivas INI eliminadas

### Funcionalidades eliminadas

Las siguientes directivas INI se han eliminado porque sus funcionalidades asociadas también se han eliminado:

- `always_populate_raw_post_data`

- `asp_tags`

### `xsl.security_prefs`

La directiva `xsl.security_prefs` se ha eliminado. En su lugar, se debe llamar al método XsltProcessor::setSecurityPrefs para controlar las preferencias de seguridad de forma individual para cada procesador.
