"""
Comprobaciones del normalizador, sin red ni dependencias externas.

Cubre los casos que ya han fallado alguna vez, para que no vuelvan a
colarse en una reconstrucción:

  * prefijos numéricos en directorios, no solo en ficheros
  * enlaces que se resuelven por slug y no por ruta (Docusaurus)
  * URLs externas terminadas en .md que no hay que tocar

    python3 -m scripts.docsync.selftest
"""

from __future__ import annotations

import sys
from pathlib import Path

from .common import Log, Source
from .normalize import (
    extract_title,
    rewrite_links,
    split_front_matter,
    strip_mdx,
    target_path,
)


class Checker:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passed = 0

    def eq(self, label: str, got, want) -> None:
        if got == want:
            self.passed += 1
            Log.ok(label)
        else:
            self.failures.append(label)
            Log.error(label)
            Log.info(f"obtenido: {got!r}")
            Log.info(f"esperado: {want!r}")


def run_checks(c: Checker) -> None:
    filament = Source(
        id="filament",
        raw={"strip_prefix": "packages", "strip_numeric_prefix": True},
    )
    laravel = Source(id="laravel", raw={})

    Log.step("Rutas de destino")
    section, dest = target_path(
        filament, Path("tables/docs/02-columns/01-getting-started.md")
    )
    c.eq(
        "prefijo numérico fuera también en directorios",
        (section, dest.as_posix()),
        ("tables", "tables/columns/getting-started.md"),
    )

    section, dest = target_path(filament, Path("actions/docs/03-modals.md"))
    c.eq(
        "segmento 'docs' descartado",
        (section, dest.as_posix()),
        ("actions", "actions/modals.md"),
    )

    section, dest = target_path(laravel, Path("migrations.md"))
    c.eq(
        "fichero plano sin sección",
        (section, dest.as_posix()),
        ("", "migrations.md"),
    )

    Log.step("Reescritura de enlaces")
    path_map = {
        "tables/docs/02-columns/01-getting-started.md": "tables/columns/getting-started.md",
        "tables/docs/01-installation.md": "tables/installation.md",
        "config-dependencies.md": "config-dependencies.md",
    }
    basename_map: dict[str, list[str]] = {}
    for original, destination in path_map.items():
        basename_map.setdefault(Path(original).name, []).append(destination)

    item = {
        "rel": Path("tables/docs/02-columns/01-getting-started.md"),
        "dest_rel": Path("tables/columns/getting-started.md"),
    }

    c.eq(
        "enlace a hermano renombrado",
        rewrite_links("Ver [inst](../01-installation.md).", item, path_map, basename_map),
        "Ver [inst](../installation.md).",
    )
    c.eq(
        "ancla conservada",
        rewrite_links("[x](../01-installation.md#setup)", item, path_map, basename_map),
        "[x](../installation.md#setup)",
    )
    c.eq(
        "URL externa terminada en .md intacta",
        rewrite_links(
            "[psr](https://github.com/php-fig/x/PSR-11-container.md)",
            item, path_map, basename_map,
        ),
        "[psr](https://github.com/php-fig/x/PSR-11-container.md)",
    )
    c.eq(
        "destino desconocido se deja como está",
        rewrite_links("[x](../99-inexistente.md)", item, path_map, basename_map),
        "[x](../99-inexistente.md)",
    )

    # Docusaurus resuelve por slug: cli/add.md enlaza a un fichero de la raíz
    doc_item = {"rel": Path("cli/add.md"), "dest_rel": Path("cli/add.md")}
    c.eq(
        "enlace por slug resuelto por nombre único",
        rewrite_links(
            "[cfg](config-dependencies.md)", doc_item, path_map, basename_map
        ),
        "[cfg](../config-dependencies.md)",
    )

    # Composer usa enlaces de referencia, que no tienen la forma [x](y)
    c.eq(
        "enlace de referencia con ancla",
        rewrite_links(
            "[1]: ../01-installation.md#type", item, path_map, basename_map
        ),
        "[1]: ../installation.md#type",
    )
    c.eq(
        "enlace de referencia sin ancla",
        rewrite_links("[dos]: ../01-installation.md", item, path_map, basename_map),
        "[dos]: ../installation.md",
    )

    Log.step("Limpieza de MDX")
    c.eq(
        "imports y componentes JSX fuera, texto dentro",
        strip_mdx('import X from "y";\n\n# T\n\n<Callout type="a">texto</Callout>\n').strip(),
        "# T\n\ntexto",
    )

    Log.step("Títulos")
    c.eq(
        "H1 del cuerpo",
        extract_title("# Database: Migrations\n", {}, "migrations"),
        "Database: Migrations",
    )
    c.eq(
        "front-matter propio tiene prioridad",
        extract_title("# Otro\n", {"title": "npm-install"}, "x"),
        "npm-install",
    )
    c.eq(
        "último recurso desde el nombre de fichero",
        extract_title("sin encabezado", {}, "http-client"),
        "Http client",
    )

    Log.step("Front-matter")
    front, body = split_front_matter("---\ntitle: A\n---\n\n# B\n")
    c.eq("cabecera separada del cuerpo", (front.get("title"), body.strip()), ("A", "# B"))

    front, body = split_front_matter("# Sin cabecera\n")
    c.eq("documento sin cabecera", (front, body.strip()), ({}, "# Sin cabecera"))


def main(argv: list[str] | None = None) -> int:
    checker = Checker()
    run_checks(checker)

    Log.step("Resultado")
    if checker.failures:
        Log.error(f"{len(checker.failures)} fallo(s): {', '.join(checker.failures)}")
        return 1

    Log.ok(f"{checker.passed} comprobaciones correctas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
