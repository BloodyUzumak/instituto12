import streamlit as st
import base64

# Función para cargar la imagen en formato base64
def load_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo de imagen. Verifica la ruta.")
        return None

# Ruta a la imagen
image_path = r"C:\Users\blood\OneDrive\Escritorio\Bloody\Estudio\Python\prueba\i12logo.png"
image_base64 = load_image(image_path)

# Verificar si se pudo cargar la imagen
if image_base64:
    # Añadir la imagen de fondo y estilos con CSS
    page_bg_img = f'''
    <style>
    .stApp {{
        background-color: white; /* Fondo blanco */
        background-image: url("data:image/png;base64,{image_base64}");
        background-size: contain; /* Ajusta el tamaño de la imagen */
        background-repeat: no-repeat;
        background-position: left top;
    }}

    * {{
        color: black !important; /* Texto negro para todo */
    }}

    a {{
        color: blue !important; /* Color azul para los enlaces */
        text-decoration: none; /* Sin subrayado en los enlaces */
    }}

    a:hover {{
        text-decoration: underline; /* Subrayado al pasar el mouse */
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
else:
    st.error("No se pudo cargar el fondo.")

# Resto del código
st.title('¡Hola! Bienvenido al asistente virtual.')

st.write('''¡Estoy aquí para ayudarte con algunas duda que puedas tener.
Puedo asistirte en los siguientes temas:
''')

# Campo de radio buttons para seleccionar la opción principal
opcion = st.radio(
    "Por favor seleccione una opción",
    ["Información del Instituto", "Información de las Carreras", "Cómo inscribirse", "Test vocacional"]
)

# Validar la opción seleccionada
if opcion == "Información del Instituto":
    st.subheader("Información del Instituto")
    st.write("📍 Estamos ubicados en 7 e 76 y 75")
    st.write("⌚ Nuestro horario de atención es de 9:00 a 17:00")
    st.write("📱 Podrás obtener más información con nuestras redes sociales:")
    st.write("Contamos con una biblioteca y laboratorios donde hay acceso a computadoras.")
    st.markdown("""
    - [Instagram](https://www.instagram.com/isft12/)
    """)

elif opcion == "Información de las Carreras":
    st.subheader("Información de las Carreras")
    subopcion = st.radio(
        "Seleccione una carrera para más detalles:",
        ["Ciencia de datos e inteligencia artificial", "Internet de las cosas", "Administración financiera", 
         "Desarrollo de software", "Análisis y sistemas", "Organización de eventos ceremoniales", 
         "Seguridad e higiene", "Administración contable"]
    )
    
    if subopcion == "Ciencia de datos e inteligencia artificial":
        st.write("""
        **Horarios de Clases:**
        Las clases se organizan en 16 semanas por cuatrimestre, con una carga horaria total de 1408 horas. Las sesiones se distribuyen a lo largo de la semana e incluyen tanto clases teóricas como prácticas, dependiendo de las asignaturas.
        
        **Asignaturas del Plan de Estudio:**
        - Seminario de Actualización
        - Técnicas de Procesamiento Digital de Imágenes
        - Materias relacionadas con inteligencia artificial y análisis de datos.
        
        **Competencias Desarrolladas:**
        Los estudiantes adquieren competencias en:
        - Diseño de sistemas de inteligencia artificial.
        - Procesamiento de imágenes y análisis de datos.
        - Trabajo en equipo y reflexión sobre el rol profesional en contextos interdisciplinarios.
        
        **Estructura del Plan de Estudio:**
        El plan de estudio se organiza en módulos que integran teoría y práctica, con un enfoque en prácticas profesionalizantes desde el inicio de la carrera.
        - Los dos primeros años cuentan con 64 horas de prácticas.
        - En el tercer año, se incrementa a 128 horas.
        
        **Prácticas Profesionalizantes:**
        Se realizan en entornos reales o simulados, donde los estudiantes abordan problemas específicos relacionados con la ciencia de datos y la inteligencia artificial.
        """)

    elif subopcion == "Internet de las cosas":
        st.write("""
        **Materias del Primer Año:**
        - Lógica Computacional – 4 horas semanales.
        - Administración y Gestión de Base de Datos – 4 horas semanales.
        - Elementos de Análisis Matemático – 4 horas semanales.
        - Estadística y Probabilidades para Gestión de Datos – 4 horas semanales.
        - Inglés I – 2 horas semanales.
        - Inglés II – 2 horas semanales.
        - Práctica Profesionalizante I: Aproximación al Campo Laboral – 4 horas semanales.
        - Comunicación – 2 horas semanales.
        
        **Horarios y Total de Horas Anuales:**
        - Total anual de horas cursadas: 512.
        - Horarios: Lunes a viernes de 8:00 a 12:00 hs y de 18:00 a 21:30 hs, además de los sábados de 8:00 a 15:00 hs. Las prácticas profesionalizantes se coordinan en días y horarios específicos.
        
        **Descripción de la Materia:**
        La Tecnicatura Superior en IoT y Sistemas Embebidos está orientada a la modernización de procesos productivos mediante la Internet de las Cosas (IoT).
        
        **Competencias:**
        El egresado estará capacitado para:
        - Diseñar y gestionar proyectos tecnológicos relacionados con IoT y sistemas embebidos.
        - Proyectar y dirigir sistemas embebidos en hardware, firmware y software.
        """)

    elif subopcion == "Administración financiera":
        st.write("""
        **Descripción de la Carrera:**
        La carrera de Administración Financiera está orientada a formar profesionales capaces de gestionar recursos financieros en empresas y organizaciones, con un enfoque en la toma de decisiones estratégicas.
        
        **Competencias:**
        - Análisis financiero.
        - Gestión de presupuestos.
        - Evaluación de inversiones.
        """)

    elif subopcion == "Desarrollo de software":
        st.write("""
        **Descripción de la Carrera:**
        El Desarrollo de Software enseña a los estudiantes a crear y mantener aplicaciones y sistemas informáticos. Es ideal para aquellos interesados en la programación y el diseño de software.
        
        **Competencias:**
        - Desarrollo de aplicaciones web y móviles.
        - Mantenimiento de sistemas informáticos.
        - Trabajo en equipo en proyectos de desarrollo.
        """)

    elif subopcion == "Análisis y sistemas":
        st.write("""
        **Introducción:**
        La carrera de Analista de Sistemas tiene un enfoque integral que combina formación técnica y profesional, abarcando tanto conocimientos teóricos como prácticos.
        
        **Perfil Profesional:**
        El Analista de Sistemas tiene competencias para:
        - Planificar y gestionar proyectos de sistemas de información.
        - Diagnosticar problemas y diseñar soluciones informáticas.
        
        **Estructura Curricular:**
        En el primer año, los estudiantes cursan materias como:
        - Inglés I
        - Análisis Matemático I
        - Álgebra
        - Algoritmos y Estructuras de Datos I
        """)

    elif subopcion == "Organización de eventos ceremoniales":
        st.write("""
        **Descripción de la Carrera:**
        La Organización de Eventos Ceremoniales capacita a los estudiantes en la planificación, gestión y ejecución de eventos, tanto sociales como corporativos.
        
        **Competencias:**
        - Coordinación de eventos.
        - Gestión de recursos.
        - Comunicación efectiva con diferentes públicos.
        """)

    elif subopcion == "Seguridad e higiene":
        st.write("""
        **Descripción de la Carrera:**
        La carrera de Seguridad e Higiene forma profesionales capacitados para gestionar la seguridad en el trabajo, con competencias en diseño, planificación y capacitación.
        
        **Estructura Curricular:**
        La carrera se organiza en tres años con una carga horaria total de 1920 horas.
        
        **Prácticas Profesionalizantes:**
        Obligatorias, integrando teoría y práctica en organizaciones públicas o privadas.
        """)

    elif subopcion == "Administración contable":
        st.write("""
        **Descripción de la Carrera:**
        La Administración Contable forma profesionales en la gestión de la contabilidad de empresas y organizaciones, asegurando un manejo adecuado de los recursos financieros.
        
        **Competencias:**
        - Elaboración de informes financieros.
        - Análisis de costos.
        - Toma de decisiones contables.
        """)

elif opcion == "Cómo inscribirse":
    st.subheader("Cómo inscribirse")
    
    # Opciones de preguntas sobre inscripción
    pregunta = st.radio(
        "Selecciona una pregunta para obtener más información:",
        ["¿Qué requisitos necesito para inscribirme?",
         "¿Hay un examen de ingreso?",
         "¿Cómo es el proceso de admisión?",
         "¿Cómo es el proceso de inscripción? ¿Se puede hacer online?",
         "¿Horario de recepción de documentación?"]
    )

    # Mostrar respuestas basadas en la pregunta seleccionada
    if pregunta == "¿Qué requisitos necesito para inscribirme?":
        st.write("Requisitos para inscribirse: Haber completado los estudios de Nivel Medio/Secundario o tener certificado de título en trámite, no se acepta el de alumno regular.")
        st.write("Pre-inscribirse")
        st.write("Presentar la documentación.")
        st.write("Acreditar el Curso Inicial.")
    elif pregunta == "¿Hay un examen de ingreso?":
        st.write("Examen de ingreso: Antes de comenzar las clases los nuevos ingresantes tendrán que realizar un curso nivelatorio.")
    elif pregunta == "¿Cómo es el proceso de admisión?":
        st.write("Proceso de admisión: PARA FORMALIZAR LA INSCRIPCIÓN AL CURSO INICIAL DEBERÁ PRESENTAR LA SIGUIENTE DOCUMENTACIÓN A PARTIR DEL 1/12/2023 HASTA EL 8/3/2024. Receso de verano desde el 30/12/2023 al 31/01/2024.")
    elif pregunta == "¿Cómo es el proceso de inscripción? ¿Se puede hacer online?":
        st.write("Proceso de inscripción: Primero y obligatorio tendrás que inscribirte en la web. ABAJO ESTÁ EL LINK DONDE PODRÁS INSCRIBIRTE.")
    elif pregunta == "¿Horario de recepción de documentación?":
        st.write("Horario de recepción de documentación:")
        st.write("Turno Mañana: de 9:00 a 12:00 HS.")
        st.write("Turno Tarde: de 14:00 a 17:00 HS.")
        st.write("Turno Noche: de 19:00 a 22:00 HS, clases en abril.")

    st.write("Puedes entrar aquí [link](https://www.dasintranet.com/sigiba/i12/2022/acceso) para llegar a un cuestionario que nos ayudará a saber más de ti.")
    st.write("A través de este [link](http://www.i12.com.ar/i12/?page_id=2056) podrás inscribirte.")

elif opcion == "Test vocacional":
    st.subheader("Test Vocacional")
    st.write("Responde las siguientes preguntas para ayudarte a encontrar la carrera adecuada:")

    pregunta1 = st.checkbox("?")
   

    st.write("### Resultados:")
    if pregunta1:
        st.write("Te interesa una carrera en áreas relacionadas con la ingeniería o matemáticas.")

    st.write("Recuerda que este test es solo una guía inicial. Te recomendamos investigar más sobre las carreras que te interesen.")
