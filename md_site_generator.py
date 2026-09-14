import os
import sys
import markdown
from jinja2 import Template

# Plantilla base para el HTML
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            background-color: #f5f5f5;
            color: #333;
            display: flex; /* Usar flexbox para layout principal */
            min-height: 100vh; /* Asegura que el body ocupe al menos todo el alto */
        }

        nav {
            background-color: #34495e;
            position: fixed; /* Fijo en la izquierda */
            top: 0;
            left: 0;
            width: 200px;
            height: 100%;
            padding-top: 2rem;
            box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
            overflow-y: auto; /* Scroll si el contenido es muy largo */
            box-sizing: border-box; /* Incluir padding en el ancho */
            flex-shrink: 0; /* Evita que se encoja en flexbox */
            color: white; /* Color por defecto para texto dentro de nav */
        }

        nav h3 {
            color: #bdc3c7; /* Color para títulos de grupo */
            /* Padding aplicado al h3 para que el área clickeable sea grande */
            padding: 10px 20px 5px;
            margin: 0; /* Reset margin */
            margin-top: 15px; /* Espacio encima del grupo */
            border-bottom: 1px solid #4a637a; /* Separador */
            cursor: pointer; /* Indica que es clickeable */
            font-size: 0.9em;
            text-transform: uppercase;
        }
         nav h3:first-of-type { /* Estilo específico para el primer h3 (Navigation) */
            margin-top: 0; /* No hay margen encima del primer h3 */
            margin-bottom: 5px; /* Espacio debajo */
            border-bottom: none; /* Sin separador debajo del título principal */
        }


        /* Estilo para los links dentro de h3 (títulos de grupo clickeables) */
        nav h3 a {
            color: inherit; /* Hereda el color de #bdc3c7 */
            text-decoration: none; /* Sin subrayado */
            display: block; /* Hace que el link ocupe todo el área del h3, incluyendo su padding */
            padding: 0; /* Asegura que el link no tenga padding propio */
        }

        nav h3 a:hover {
            background-color: transparent; /* No queremos el hover de link normal */
            color: #ecf0f1; /* Ligeramente más claro al pasar el ratón */
        }


        nav ul {
            list-style: none; /* Eliminar viñetas */
            padding: 0; /* Eliminar padding por defecto */
            margin: 0;
        }

        /* REFINADO CSS: Ocultar ULs que son hermanos adyacentes de H3 por defecto (las listas de archivos) */
        nav h3 + ul {
             display: none;
        }

        /* Estilo específico para la lista de enlaces principal ('Inicio') - SIEMPRE VISIBLE */
        nav > ul { /* Selecciona el ul directo hijo de nav */
            display: block; /* Siempre visible */
            margin-bottom: 15px; /* Espacio antes del primer grupo */
        }

        /* REFINADO CSS: Mostrar la lista de archivos solo si el grupo es el activo (h3 tiene active-group) */
        nav h3.active-group + ul {
            display: block; /* Muestra solo el UL que sigue a un h3 con active-group */
        }


        nav li {
            margin: 0;
            padding: 0;
        }


        nav a {
            display: block;
            padding: 10px 20px;
            color: white;
            text-decoration: none;
            font-weight: 400;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        nav a:hover {
            background-color: #16a085;
            color: #ecf0f1;
        }

        nav a.active {
            background-color: #1abc9c; /* Color para el enlace activo */
            font-weight: 500;
        }


        .content-wrapper {
            margin-left: 200px; /* Espacio para el nav fijo */
            flex-grow: 1; /* Permitir que ocupe el espacio restante */
            display: flex;
            flex-direction: column;
            width: calc(100% - 200px); /* Ajustar el ancho para pantallas grandes */
            box-sizing: border-box; /* Incluir padding en el ancho */
        }

        header {
            background-color: #2c3e50;
            color: white; /* Asegura el color blanco */
            padding: 1rem 2rem;
            text-align: center;
            flex-shrink: 0;
            box-sizing: border-box;
            width: 100%; /* Ocupa el ancho del content-wrapper */
        }

        header h1 {
            margin: 0;
            color: white !important; /* Asegura que el título del header sea blanco */
        }

        .container {
            padding: 2rem;
            flex-grow: 1; /* Empuja el footer hacia abajo */
            width: 100%; /* Ocupa el ancho del content-wrapper */
            box-sizing: border-box;
        }

        h1, h2 {
            color: #2c3e50;
        }

        .md-card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            padding: 1.5rem;
        }

        .md-card h2 {
            margin-top: 0;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }

        .md-content {
            line-height: 1.6;
            color: #555;
        }

        /* Estilos para elementos markdown dentro de .md-content */
        .md-content pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }

        .md-content code {
             font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        }

        .md-content pre code {
            display: block;
            padding: 0;
            background-color: transparent;
            color: #333;
        }

        .md-content table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1em;
        }

        .md-content th, .md-content td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        .md-content th {
            background-color: #f2f2f2;
            font-weight: bold;
        }

         .md-content img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1em auto;
        }


        footer {
            background-color: #2c3e50;
            color: white; /* Asegura el color blanco */
            padding: 1rem;
            text-align: center;
            flex-shrink: 0;
            box-sizing: border-box;
            width: 100%; /* Ocupa el ancho del content-wrapper */
        }

        /* Responsive design */
        @media (max-width: 768px) {
            body {
                flex-direction: column; /* Apilar nav y contenido en pantallas pequeñas */
            }

            nav {
                position: static; /* Quitar fixed positioning */
                width: 100%;
                height: auto;
                padding-top: 0;
                box-shadow: none;
                overflow-y: visible;
            }

            /* En móvil, queremos que todos los grupos y sus listas se vean */
             nav h3 + ul { /* Dirigido a los ULs de archivos */
                display: flex !important; /* Flex en móvil para inline */
                flex-wrap: wrap;
                justify-content: center;
                padding: 0 10px;
            }
             /* Asegurar que la lista principal también se muestre en móvil */
             nav > ul {
                display: flex !important; /* Flex en móvil para inline */
                flex-wrap: wrap;
                justify-content: center;
                padding: 0 10px;
                margin-bottom: 10px; /* Reducir margen en móvil */
            }


            nav h3 {
                 border-bottom: none; /* Eliminar separador en móvil */
                 text-align: center;
                 padding: 10px 0 0; /* Ajustar padding */
                 margin-top: 10px;
            }

            nav li {
                margin: 0 5px; /* Espacio entre elementos de lista inline */
            }

            nav a {
                 padding: 8px 15px;
            }

            .content-wrapper {
                margin-left: 0; /* Reset margin */
                width: 100%; /* Occupy full width */
            }

             header, footer {
                margin-left: 0; /* Reset margin */
                width: 100%; /* Occupy full width */
            }
        }
    </style>
</head>
<body>

    <nav>
        <h3>Navigation</h3> {# Título general de la navegación #}
        <ul> {# Lista principal (contiene link a Inicio) - siempre visible #}
           <li><a href="{{ rel_prefix }}/index.html">Inicio</a></li>
        </ul>
        {% for group, files_list in nav %}
            {# Añadir clase 'active-group' si este es el grupo de la página actual #}
            {# El h3 siempre es visible y contiene el link al primer archivo #}
            <h3 {% if current_group_name and group == current_group_name %}class="active-group"{% endif %}>
                {# Enlazar el título del grupo al primer archivo de ese grupo #}
                {% if files_list %} {# Asegurarse de que hay archivos en el grupo antes de intentar enlazar #}
                    <a href="{{ rel_prefix }}/{{ files_list[0][1] }}">{{ group.capitalize() }}</a>
                {% else %}
                    {{ group.capitalize() }} {# Si no hay archivos, mostrar solo el título sin enlace #}
                {% endif %}
            </h3>
            {# Mostrar la lista de archivos SOLO si este es el grupo activo usando CSS h3.active-group + ul { display: block; } #}
            {# Por defecto, nav h3 + ul { display: none; } #}
            <ul>
            {% for file_title, file_relative_path_within_output in files_list %}
                <li><a href="{{ rel_prefix }}/{{ file_relative_path_within_output }}">{{ file_title }}</a></li>
            {% endfor %}
            </ul>
        {% endfor %}
    </nav>

    <div class="content-wrapper">
        <header>
            <h1>{{ title }}</h1>
        </header>

        <div class="container">
            <div class="md-card"> {# Contenido principal de la página #}
                 <div class="md-content">
                    {{ content | safe }}
                </div>
            </div>
        </div>

        <footer>
            <p>&copy; 2025 Documentos generados desde Markdown</p>
        </footer>
    </div>

</body>
</html>
"""

def convert_md_to_html(md_path):
    """Convierte un archivo .md a HTML usando Markdown"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            text = f.read()
        # Usar extensiones comunes
        return markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc', 'sane_lists'])
    except Exception as e:
        print(f"Error leyendo o convirtiendo {md_path}: {e}", file=sys.stderr)
        return f"<p>Error al cargar contenido: {e}</p>"

# ESTA FUNCIÓN YA PROCESA ARCHIVOS TANTO EN LA RAÍZ COMO EN SUBDIRECTORIOS
def scan_directories_and_generate_structure(root_dir, root_group_name):
    """
    Escanea recursivamente el directorio raíz y organiza los archivos .md.
    Archivos directamente en root_dir se agrupan bajo root_group_name.
    Archivos en subdirectorios se agrupan por el nombre del primer nivel de subdirectorio.
    Retorna: {'group_name': [('path/in/group/file_without_ext', 'full/path/to/file.md'), ...]}
    """
    md_structure = {}
    print(f"Escaneando directorios en: {root_dir}")

    # Asegurarse de que root_dir es una ruta absoluta para os.path.relpath fiable
    root_dir_abs = os.path.abspath(root_dir)

    if not os.path.isdir(root_dir_abs):
        print(f"Error: Directorio de entrada no encontrado: {root_dir_abs}", file=sys.stderr)
        return md_structure

    # Recorrer recursivamente todo el directorio raíz
    for root, dirs, files in os.walk(root_dir_abs):
        for file in files:
            if file.endswith('.md'):
                full_md_path = os.path.join(root, file)
                # Obtener la ruta relativa del archivo desde el directorio raíz de entrada
                relative_to_root_dir = os.path.relpath(full_md_path, root_dir_abs)

                # Dividir la ruta relativa en componentes
                parts = relative_to_root_dir.split(os.sep)

                # === LÓGICA CLAVE: DISTINGUIR ARCHIVOS DE LA RAÍZ VS SUBDIRECTORIOS ===
                if len(parts) == 1: # El archivo está directamente en root_dir (ej: README.md, parts = ['README.md'])
                    group = root_group_name
                    # La ruta dentro del grupo es solo el nombre del archivo sin extensión
                    path_in_group_without_ext = os.path.splitext(parts[0])[0]

                else: # El archivo está en un subdirectorio (ej: forms/docs/intro.md, parts = ['forms', 'docs', 'intro.md'])
                    # El grupo es el nombre del primer subdirectorio
                    group = parts[0]
                    # La ruta dentro del grupo es el resto de los componentes unidos
                    # parts[1:] da ['docs', 'intro.md']
                    # os.path.join(*parts[1:]) da 'docs/intro.md'
                    # os.path.splitext(...) da ('docs/intro', '.md')
                    path_in_group = os.path.join(*parts[1:])
                    path_in_group_without_ext = os.path.splitext(path_in_group)[0]

                # Añadir la tupla (path_in_group_without_ext, full_md_path) bajo el grupo determinado
                # Asegurarse de que el path_in_group_without_ext no sea vacío (ej. si el archivo es solo la extensión)
                # y que el nombre del grupo no sea una cadena vacía (caso borde de root_dir ser '/' y archivo en '/')
                if group and path_in_group_without_ext:
                     md_structure.setdefault(group, []).append((path_in_group_without_ext, full_md_path))


    # Ordenar grupos y archivos alfabéticamente para la navegación consistente
    # Solo incluimos grupos que realmente tienen archivos MD después del escaneo
    sorted_md_structure = {group: sorted(files_list, key=lambda x: x[0])
                           for group, files_list in sorted(md_structure.items()) if files_list}

    return sorted_md_structure


def generate_html_pages(md_structure, output_dir, root_input_dir_name):
    """
    Genera las páginas HTML en el directorio de salida.
    md_structure: {'group_name': [('path/in/group/file_without_ext', 'full/path/to/file.md'), ...]}
    output_dir: Directorio donde se generará el sitio.
    root_input_dir_name: Nombre del directorio raíz de entrada (para el título).
    """
    print(f"Generando archivos HTML en: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)

    # Preparar los datos de navegación una vez
    # nav_data: [(group_name, [(file_title, file_relative_path_within_output), ...]), ...]
    nav_data = []
    for group, files_list in md_structure.items():
        group_nav_files = []
        for path_in_group_without_ext, _ in files_list:
            # Generar título para el link (basename sin extensión, capitalizado)
            file_basename = os.path.basename(path_in_group_without_ext)
            file_title = file_basename.replace('-', ' ').replace('_', ' ').capitalize()
            # La ruta relativa DENTRO del directorio de salida es group/path/in/group/file.html
            file_relative_path_within_output = os.path.join(group, path_in_group_without_ext + '.html')
            group_nav_files.append((file_title, file_relative_path_within_output))
        nav_data.append((group, group_nav_files))

    # Generar cada página HTML individualmente
    for group, files_list in md_structure.items():
        # El nombre del grupo actual para pasar a la plantilla
        current_group_name = group
        for path_in_group_without_ext, full_md_path in files_list:
            # Construir la ruta de salida para este archivo HTML
            # EJ: output_dir/GroupName/path/in/group/file.html
            output_html_path = os.path.join(output_dir, group, path_in_group_without_ext + '.html')

            # Asegurarse de que los directorios de salida existan
            os.makedirs(os.path.dirname(output_html_path), exist_ok=True)

            print(f"Generando archivo: {output_html_path}")

            # Calcular el prefijo de ruta relativa para volver al output_dir desde la ubicación actual
            rel_prefix = os.path.relpath(output_dir, os.path.dirname(output_html_path))

            # Convertir Markdown a HTML
            html_content = convert_md_to_html(full_md_path)

            # Derivar el título de la página del nombre del archivo (o del primer encabezado MD si existiera)
            page_title_basename = os.path.basename(path_in_group_without_ext)
            page_title = page_title_basename.replace('-', ' ').replace('_', ' ').capitalize()


            # Renderizar la plantilla con los datos
            rendered_html = Template(BASE_TEMPLATE).render(
                title=f"{page_title} - {root_input_dir_name.capitalize()}", # Título de la página
                nav=nav_data, # Estructura de navegación completa
                content=html_content, # Contenido HTML del archivo MD
                rel_prefix=rel_prefix, # Prefijo de ruta relativa para los enlaces
                current_group_name=current_group_name # Pasar el nombre del grupo actual
            )

            # Guardar el archivo HTML
            with open(output_html_path, "w", encoding="utf-8") as f:
                f.write(rendered_html)

    # Generar el archivo de índice (index.html)
    index_output_path = os.path.join(output_dir, "index.html")
    print(f"Generando archivo de índice: {index_output_path}")

    # El prefijo relativo para el índice es '.' (el propio directorio de salida)
    index_rel_prefix = "."

    # Contenido para el índice: Lista de grupos con enlaces a la primera página de cada grupo
    index_content_html = f"<h2>Índice de Documentos de {root_input_dir_name.capitalize()}</h2>"
    if nav_data:
        index_content_html += "<p>Selecciona una sección del menú lateral o haz clic en los enlaces de abajo para ir a la primera página de cada sección.</p>"
        index_content_html += "<ul>"
        for group, files_list in nav_data:
             if files_list: # Asegurarse de que el grupo tenga al menos un archivo
                 # Enlazar al primer archivo de este grupo
                 # files_list[0][1] ya es la ruta relativa DENTRO del directorio de salida (ej: GroupName/path/file.html)
                 first_file_relative_path = files_list[0][1]
                 group_title = group.capitalize()
                 # Enlace desde el índice (en root_dir) a GroupName/path/file.html es ./GroupName/path/file.html
                 index_content_html += f'<li><a href="{index_rel_prefix}/{first_file_relative_path}">{group_title}</a></li>'
             # Grupos sin archivos no se añaden a esta lista en el contenido principal
        index_content_html += "</ul>"
    else:
         index_content_html += "<p>No se encontraron grupos de documentos.</p>"


    # Para el índice, no hay un grupo "activo" en el sentido de contenido mostrado.
    # current_group_name=None asegura que ninguna lista de archivos esté desplegada por defecto en el nav.
    rendered_index_html = Template(BASE_TEMPLATE).render(
        title=f"Índice - {root_input_dir_name.capitalize()}",
        nav=nav_data,
        content=index_content_html,
        rel_prefix=index_rel_prefix,
        current_group_name=None # No hay grupo activo en el índice
    )

    with open(index_output_path, "w", encoding="utf-8") as f:
        f.write(rendered_index_html)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 md_site_generator.py <directorio_entrada> <directorio_salida>", file=sys.stderr)
        sys.exit(1)

    root_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # Obtener el nombre del directorio de entrada para usarlo en los títulos
    # y como nombre de grupo para archivos en el nivel raíz
    root_input_dir_abs = os.path.abspath(root_dir)
    root_input_dir_name = os.path.basename(root_input_dir_abs)

    # Si la ruta es '.', basename puede ser vacío, usar el nombre del padre o un default
    if not root_input_dir_name or root_input_dir_name == '.':
         # Usar el nombre del directorio padre si el input es '.' o '/'
         root_input_dir_name = os.path.basename(os.path.dirname(root_input_dir_abs)) or 'Documents' # Fallback a 'Documents'


    # Escanear y obtener la estructura de directorios, pasando el nombre del grupo raíz.
    # La función scan_directories_and_generate_structure ahora maneja:
    # 1. Archivos en root_dir -> Agrupados bajo root_input_dir_name
    # 2. Archivos en subdirectorios -> Agrupados bajo el nombre del primer subdirectorio
    md_structure = scan_directories_and_generate_structure(root_dir, root_input_dir_name)

    if not md_structure:
        print(f"No se encontraron archivos .md con estructura válida en '{root_dir}'.", file=sys.stderr)
        print("Asegúrate de que tus archivos markdown estén en subdirectorios (ej: ./entrada/mi-grupo/archivo.md) O directamente en el directorio de entrada (ej: ./entrada/README.md).", file=sys.stderr)
    else:
        # Generar las páginas HTML
        generate_html_pages(md_structure, output_dir, root_input_dir_name)

    print("Proceso finalizado.")