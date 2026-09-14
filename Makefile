# ═══════════════════════════════════════════════════════════════════
# Documentación offline — interfaz única de uso
#
#   make            muestra esta ayuda
#   make update     reconstrucción completa (lo que se ejecuta cada pocos meses)
#
# Ver AGENTS.md para la arquitectura completa.
# ═══════════════════════════════════════════════════════════════════

PYTHON      ?= $(shell [ -f .venv/bin/python ] && echo .venv/bin/python || echo python3)
DOCSYNC     := $(PYTHON) -m scripts.docsync
SRC_DIR     := src
WORK_DIR    := work
PUBLIC_DIR  := public
DIST_DIR    := dist
PORT        := 8080

# Fuente concreta para los objetivos *-one:  make fetch-one S=laravel
S ?=

.DEFAULT_GOAL := help
.PHONY: help update fetch fetch-one normalize build serve check diff \
        bundles clean clean-work clean-all tidy venv deps status test

# ───────────────────────────────────────────────────────────────────
# Ayuda
# ───────────────────────────────────────────────────────────────────

help:  ## Muestra esta ayuda
	@echo ""
	@echo "  Documentación offline — @raupulus"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "  Ejemplo:  make fetch-one S=laravel"
	@echo ""

# ───────────────────────────────────────────────────────────────────
# Flujo principal
# ───────────────────────────────────────────────────────────────────

update: deps fetch normalize check build tidy  ## Reconstrucción completa desde cero
	@echo ""
	@echo "  ✓ Reconstrucción terminada. Solo quedan src/ y public/."
	@echo "    Revisa qué cambió en la documentación con:  make diff"
	@echo ""

tidy:  ## Borra descargas y caché; deja solo src/ y public/
	@rm -rf $(WORK_DIR) repos
	@find . -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
	@find . -type f \( -name '*.py[cod]' -o -name '.DS_Store' -o -name '*.part' \) \
		-delete 2>/dev/null || true
	@echo "  ✓ Descargas y caché eliminadas"

fetch: | $(WORK_DIR)  ## Descarga todas las fuentes a work/
	$(call require_script,fetch)
	$(DOCSYNC).fetch --config sources.yaml --out $(WORK_DIR)

fetch-one: | $(WORK_DIR)  ## Descarga una sola fuente:  make fetch-one S=php
	@if [ -z "$(S)" ]; then \
		echo "Error: indica la fuente.  Ejemplo: make fetch-one S=laravel"; exit 1; \
	fi
	$(call require_script,fetch)
	$(DOCSYNC).fetch --config sources.yaml --out $(WORK_DIR) --source $(S)

normalize:  ## Convierte work/ a markdown canónico en src/
	$(call require_script,normalize)
	$(DOCSYNC).normalize --config sources.yaml --in $(WORK_DIR) --out $(SRC_DIR)

build:  ## Genera el sitio HTML en public/ a partir de src/
	$(call require_script,build)
	$(DOCSYNC).build --config sources.yaml --in $(SRC_DIR) --out $(PUBLIC_DIR)

# ───────────────────────────────────────────────────────────────────
# Utilidades
# ───────────────────────────────────────────────────────────────────

serve: $(PUBLIC_DIR)  ## Sirve public/ en http://localhost:8080
	@echo "  → http://localhost:$(PORT)   (Ctrl+C para parar)"
	@$(PYTHON) -m http.server $(PORT) --directory $(PUBLIC_DIR)

test:  ## Comprobaciones del normalizador (sin red, instantáneo)
	@$(DOCSYNC).selftest

check:  ## Valida configuración, front-matter y enlaces internos
	@echo "→ Validando sources.yaml…"
	@$(PYTHON) -c "import yaml,sys; yaml.safe_load(open('sources.yaml')); print('  ✓ sources.yaml válido')" \
		|| { echo "  ✗ sources.yaml inválido"; exit 1; }
	@if [ -f versions.lock.json ]; then \
		$(PYTHON) -c "import json; json.load(open('versions.lock.json')); print('  ✓ versions.lock.json válido')" \
			|| { echo "  ✗ versions.lock.json inválido"; exit 1; }; \
	fi
	$(call require_script,check)
	$(DOCSYNC).check --config sources.yaml --src $(SRC_DIR)

diff:  ## Qué cambió en la documentación desde la última actualización
	@git diff --stat $(SRC_DIR) 2>/dev/null || echo "  (todavía no es un repositorio git)"

status:  ## Resumen de lo que hay descargado ahora mismo
	@echo ""
	@printf "  %-14s %8s  %s\n" "TECNOLOGÍA" "FICHEROS" "VERSIÓN"
	@printf "  %-14s %8s  %s\n" "──────────────" "────────" "───────"
	@for d in $(SRC_DIR)/*/; do \
		[ -d "$$d" ] || continue; \
		name=$$(basename $$d); \
		n=$$(find "$$d" -name '*.md' 2>/dev/null | wc -l | tr -d ' '); \
		v=$$($(PYTHON) -c "import json;print(json.load(open('$$d/_meta.json')).get('version','?'))" 2>/dev/null || echo "-"); \
		printf "  %-14s %8s  %s\n" "$$name" "$$n" "$$v"; \
	done
	@echo ""

bundles: | $(DIST_DIR)  ## Concatena cada tecnología en un .md para modelos de IA
	$(call require_script,bundle)
	$(DOCSYNC).bundle --src $(SRC_DIR) --out $(DIST_DIR)

venv:  ## Crea .venv e instala las dependencias Python
	@test -d .venv || $(PYTHON) -m venv .venv
	@./.venv/bin/pip install --quiet --upgrade pip
	@./.venv/bin/pip install --quiet -r requirements.txt
	@echo "  ✓ Entorno listo. Actívalo con:  source .venv/bin/activate"

deps:  ## Comprueba que están las herramientas necesarias
	@echo "  Python:  $$($(PYTHON) -c 'import sys; print(sys.executable)')"
	@$(PYTHON) -c "import sys; sys.exit(0 if sys.prefix != sys.base_prefix else 1)" \
		&& echo "  Entorno: virtual (correcto)" \
		|| echo "  Entorno: sistema — se recomienda un venv, ver info/dependencias.md"
	@sys_missing=""; \
	for c in git $(PYTHON); do \
		command -v $$c >/dev/null 2>&1 || sys_missing="$$sys_missing $$c"; \
	done; \
	command -v pandoc >/dev/null 2>&1 || echo "  ! pandoc no está: hace falta para PHP y Bash"; \
	command -v texi2any >/dev/null 2>&1 || echo "  ! texi2any no está: hace falta para Bash"; \
	py_missing=""; \
	for m in yaml markdown jinja2 pygments; do \
		$(PYTHON) -c "import $$m" 2>/dev/null || py_missing="$$py_missing $$m"; \
	done; \
	if [ -n "$$sys_missing" ]; then \
		echo "  ✗ Faltan herramientas:$$sys_missing"; \
		echo "      Debian/Ubuntu:  sudo apt install git python3 python3-venv pandoc texinfo"; \
		echo "      macOS:          brew install git python3 pandoc texinfo"; \
	fi; \
	if [ -n "$$py_missing" ]; then \
		echo "  ✗ Faltan paquetes Python:$$py_missing"; \
		echo "      pip install -r requirements.txt"; \
	fi; \
	if [ -n "$$sys_missing" ] || [ -n "$$py_missing" ]; then exit 1; fi; \
	echo "  ✓ Dependencias correctas"

# ───────────────────────────────────────────────────────────────────
# Limpieza
# ───────────────────────────────────────────────────────────────────

clean-work:  ## Borra work/ (clones y tarballs descargados)
	@rm -rf $(WORK_DIR)
	@echo "  ✓ work/ eliminado"

clean: clean-work  ## Borra todo lo generado (work/, public/, dist/)
	@rm -rf $(PUBLIC_DIR) $(DIST_DIR)
	@echo "  ✓ public/ y dist/ eliminados"

clean-all: clean  ## Además elimina la carpeta repos/ de la estructura antigua
	@if [ -d repos ]; then \
		echo "  Eliminando repos/ (estructura antigua, decenas de miles de ficheros)…"; \
		rm -rf repos; \
		echo "  ✓ repos/ eliminado"; \
	else \
		echo "  repos/ no existe, nada que hacer"; \
	fi

# ───────────────────────────────────────────────────────────────────
# Interno
# ───────────────────────────────────────────────────────────────────

$(WORK_DIR) $(DIST_DIR) $(PUBLIC_DIR):
	@mkdir -p $@

# Mensaje claro mientras los scripts de la fase 2 no existan todavía.
# Definido en una sola línea a propósito: un `define` multilínea expandido
# dentro de una receta rompe el prefijo de tabulación de make.
require_script = @if [ ! -f scripts/docsync/$(1).py ]; then echo ""; echo "  scripts/docsync/$(1).py aún no está implementado."; echo "  Corresponde a la fase 2 del plan (ver ANALISIS-Y-PLAN.md)."; echo ""; exit 1; fi
