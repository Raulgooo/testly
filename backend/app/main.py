import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client()
nombre_del_archivo = "files/roeqq5tzltyn"
myfile = client.files.get(name=nombre_del_archivo)



response = client.models.generate_content(
    model="gemini-2.5-flash", contents=["""ROLE:
You are Testly's Head Curriculum Architect. Your goal is to design a high-performance, "Sports Science" based study macro-cycle. You do not generate the content text; you generate the SCHEDULE (The Strategy).

INPUT DATA:

1. BOOK METADATA (Source of Truth):
   {{BOOK_STRUCTURE_JSON}}: {
 "ABOUT THE BOOK": {
  "book_title": "GEOMETRÍA ANALÍTICA",
  "total_difficulty": 7,
  "chapter_amount": 17
 },
 "CHAPTERS": [
  {
   "chapter_name": "SISTEMAS DE COORDENADAS",
   "chapter_number": 1,
   "content_density": 7,
   "difficulty": 6,
   "page_range": [19, 49],
   "reading_time_minutes": 120,
   "core_concepts": [
    "Segmento rectilíneo dirigido",
    "Sistema coordenado lineal",
    "Sistema coordenado en el plano",
    "Distancia entre dos puntos",
    "División de un segmento en una razón dada",
    "Pendiente de una recta",
    "Ángulo de dos rectas",
    "Demostración de teoremas geométricos por el método analítico"
   ],
   "prerequirement_chapters": [],
   "pedagogic_objetive_brief_summary": "Introduces fundamental concepts of plane analytic geometry, generalizing elemental geometry notions. Covers coordinate systems (linear and planar), directed line segments, distance, division of segments, slope, angle between lines, and analytical proofs of geometric theorems."   
  },
  {
   "chapter_name": "GRÁFICA DE UNA ECUACIÓN Y LUGARES GEOMÉTRICOS",
   "chapter_number": 2,
   "content_density": 8,
   "difficulty": 7,
   "page_range": [50, 73],
   "reading_time_minutes": 110,
   "core_concepts": [
    "Gráfica de una ecuación",
    "Intercepciones con los ejes",
    "Simetría",
    "Extensión de una curva",
    "Asíntotas",
    "Construcción de curvas",
    "Ecuaciones factorizables",
    "Intersecciones de curvas",
    "Ecuación de un lugar geométrico"
   ],
   "prerequirement_chapters": [1],
   "pedagogic_objetive_brief_summary": "Explores the relationship between equations and their geometric representations (graphs). Covers plotting curves, identifying intercepts, symmetries, asymptotes, and deriving equations for given geometric conditions."
  },
  {
   "chapter_name": "LA LÍNEA RECTA",
   "chapter_number": 3,
   "content_density": 7,
   "difficulty": 6,
   "page_range": [74, 116],
   "reading_time_minutes": 190,
   "core_concepts": [
    "Definición de línea recta",
    "Ecuación de una recta (punto-pendiente, pendiente-ordenada, dos puntos, simétrica)",
    "Forma general de la ecuación de una recta",
    "Posiciones relativas de dos rectas",
    "Forma normal de la ecuación de la recta",
    "Aplicaciones de la forma normal",
    "Área de un triángulo",
    "Familias de líneas rectas"
   ],
   "prerequirement_chapters": [1, 2],
   "pedagogic_objetive_brief_summary": "Provides a detailed study of the straight line in analytic geometry. Covers various forms of linear equations, their properties, relative positions of lines, normal form, and applications like calculating area. Introduces families of lines."
  },
  {
   "chapter_name": "ECUACIÓN DE LA CIRCUNFERENCIA",
   "chapter_number": 4,
   "content_density": 8,
   "difficulty": 7,
   "page_range": [117, 149],
   "reading_time_minutes": 150,
   "core_concepts": [
    "Ecuación de la circunferencia (forma ordinaria, general)",
    "Determinación de una circunferencia sujeta a tres condiciones",
    "Familias de circunferencias",
    "Eje radical",
    "Tangente a una circunferencia",
    "Teoremas y problemas de lugares geométricos relativos a la circunferencia" 
   ],
   "prerequirement_chapters": [1, 2, 3],
   "pedagogic_objetive_brief_summary": "Focuses on the analytical representation and properties of the circle. Covers standard and general equations, finding circles from given conditions, radical axis, tangents, and related locus problems."
  },
  {
   "chapter_name": "TRANSFORMACIÓN DE COORDENADAS",
   "chapter_number": 5,
   "content_density": 8,
   "difficulty": 8,
   "page_range": [151, 166],
   "reading_time_minutes": 90,
   "core_concepts": [
    "Traslación de los ejes coordenados",
    "Rotación de los ejes coordenados",
    "Simplificación de ecuaciones por transformación de coordenadas"
   ],
   "prerequirement_chapters": [1, 2, 3, 4],
   "pedagogic_objetive_brief_summary": "Introduces techniques to simplify equations by changing the coordinate system through translation and rotation of axes. 
This is a crucial tool for analyzing conic sections in simpler forms."
  },
  {
   "chapter_name": "LA PARÁBOLA",
   "chapter_number": 6,
   "content_density": 8,
   "difficulty": 7,
   "page_range": [167, 190],
   "reading_time_minutes": 110,
   "core_concepts": [
    "Definiciones de parábola (foco, directriz, vértice, eje, lado recto)",     
    "Ecuación de la parábola (vértice en el origen, eje coordenado)",
    "Ecuación de una parábola (vértice (h,k), eje paralelo a un eje coordenado)",
    "Ecuación de la tangente a una parábola",
    "La función cuadrática",
    "Aplicaciones de la parábola (arco parabólico, propiedad focal)"
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5],
   "pedagogic_objetive_brief_summary": "Provides a comprehensive study of the parabola, its definitions, standard equations (at origin and shifted), tangents, and applications, including its relation to quadratic functions."
  },
  {
   "chapter_name": "LA ELIPSE",
   "chapter_number": 7,
   "content_density": 8,
   "difficulty": 7,
   "page_range": [191, 208],
   "reading_time_minutes": 85,
   "core_concepts": [
    "Definiciones de elipse (focos, vértices, eje mayor, eje menor, centro, lado recto, excentricidad)",
    "Ecuación de la elipse (centro en el origen, ejes coordenados como ejes)",  
    "Ecuación de la elipse (centro (h,k), ejes paralelos a los coordenados)",   
    "Propiedades de la elipse"
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5, 6],
   "pedagogic_objetive_brief_summary": "Details the ellipse, covering its definitions, standard and general equations, properties (e.g., eccentricity, latus rectum), and methods for finding tangents."
  },
  {
   "chapter_name": "LA HIPÉRBOLA",
   "chapter_number": 8,
   "content_density": 8,
   "difficulty": 8,
   "page_range": [209, 228],
   "reading_time_minutes": 100,
   "core_concepts": [
    "Definiciones de hipérbola (focos, vértices, eje transverso, eje conjugado, 
centro, lado recto, radios vectores)",
    "Primera ecuación ordinaria de la hipérbola",
    "Asíntotas de la hipérbola",
    "Hipérbola equilátera o rectangular",
    "Hipérbolas conjugadas",
    "Segunda ecuación ordinaria de la hipérbola",
    "Propiedades de la hipérbola",
    "Resumen relativo a las secciones cónicas"
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5, 6, 7],
   "pedagogic_objetive_brief_summary": "Covers the hyperbola in detail, including definitions, standard equations (at origin and shifted), asymptotes, equilateral/rectangular hyperbolas, conjugate hyperbolas, and properties. Includes a summary of all conic sections."
  },
  {
   "chapter_name": "ECUACIÓN GENERAL DE SEGUNDO GRADO",
   "chapter_number": 9,
   "content_density": 9,
   "difficulty": 9,
   "page_range": [230, 254],
   "reading_time_minutes": 120,
   "core_concepts": [
    "Ecuación general de segundo grado",
    "Transformación por rotación de los ejes coordenados",
    "El indicador I = B² - 4AC (clasificación de cónicas)",
    "Definición general de cónica",
    "Tangente a la cónica general",
    "Sistemas de cónicas",
    "Secciones planas de un cono circular recto"
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5, 6, 7, 8],
   "pedagogic_objetive_brief_summary": "Unifies the study of conic sections by analyzing the general second-degree equation. Introduces axis rotation to eliminate the xy-term, the discriminant (indicator I) to classify conics, and covers general conic definitions, tangents, systems of conics, and how they arise as sections of a cone."
  },
  {
   "chapter_name": "COORDENADAS POLARES",
   "chapter_number": 10,
   "content_density": 8,
   "difficulty": 8,
   "page_range": [255, 282],
   "reading_time_minutes": 140,
   "core_concepts": [
    "Sistema de coordenadas polares (polo, eje polar, radio vector, ángulo polar)",
    "Paso de coordenadas polares a rectangulares y viceversa",
    "Trazado de curvas en coordenadas polares",
    "Intersecciones de curvas dadas en coordenadas polares",
    "Fórmula de la distancia entre dos puntos en coordenadas polares",
    "Ecuación de la recta en coordenadas polares",
    "Ecuación de la circunferencia en coordenadas polares",
    "Ecuación general de las cónicas en coordenadas polares",
    "Problemas relativos a lugares geométricos en coordenadas polares"
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5, 6, 7, 8, 9],
   "pedagogic_objetive_brief_summary": "Introduces the polar coordinate system, 
covering conversion between polar and rectangular coordinates, plotting curves (lines, circles, conics) in polar form, distance formula, and solving locus problems using polar coordinates."
  },
  {
   "chapter_name": "ECUACIONES PARAMÉTRICAS",
   "chapter_number": 11,
   "content_density": 8,
   "difficulty": 8,
   "page_range": [283, 302],
   "reading_time_minutes": 100,
   "core_concepts": [
    "Obtención de la ecuación rectangular a partir de la representación paramétrica",
    "Gráfica de una curva a partir de su representación paramétrica",
    "Representación paramétrica de las cónicas",
    "La cicloide",
    "Epicicloide e hipocicloide",
    "Resolución de problemas de lugares geométricos por el método paramétrico"  
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
   "pedagogic_objetive_brief_summary": "Introduces parametric equations as another way to represent curves. Covers conversion to rectangular form, graphing parametric curves, parametric representations of conics, and specific curves like cycloids, epicycloids, and hypocycloids, and solving locus problems using this method."
  },
  {
   "chapter_name": "CURVAS PLANAS DE GRADO SUPERIOR",
   "chapter_number": 12,
   "content_density": 9,
   "difficulty": 9,
   "page_range": [303, 332],
   "reading_time_minutes": 150,
   "core_concepts": [
    "Clasificación de funciones (algebraicas, trascendentes)",
    "Clasificación de las curvas planas",
    "Curvas planas algebraicas de grado superior (polinomias, potenciales, curva de Agnesi)",
    "Tres famosos problemas de la antigüedad (duplicación del cubo, trisección del ángulo, cuadratura del círculo)",
    "La sinusoide",
    "Curvas trigonométricas (tangentoide, secantoide, cosecantoide)",
    "Gráficas de las funciones trigonométricas inversas",
    "Curva logarítmica",
    "Curva exponencial",
    "Curvas compuestas (adición de ordenadas)"
   ],
   "prerequirement_chapters": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
   "pedagogic_objetive_brief_summary": "Explores advanced planar curves beyond conics, classifying functions and curves. Covers higher-degree algebraic curves (polynomial, power functions, Witch of Agnesi) and their relation to classical geometric problems, as well as transcendental curves (sinusoidal, trigonometric inverses, logarithmic, exponential) and composite curves."
  },
  {
   "chapter_name": "EL PUNTO EN EL ESPACIO",
   "chapter_number": 13,
   "content_density": 7,
   "difficulty": 7,
   "page_range": [335, 354],
   "reading_time_minutes": 100,
   "core_concepts": [
    "Sistemas de coordenadas rectangulares en el espacio (octantes, terna ordenada)",
    "Distancia entre dos puntos en el espacio",
    "División de un segmento en el espacio en una razón dada",
    "Cosenos directores de una recta en el espacio",
    "Números directores de una recta en el espacio",
    "Ángulo formado por dos rectas dirigidas en el espacio",
    "Números directores de una recta perpendicular a dos dadas"
   ],
   "prerequirement_chapters": [1],
   "pedagogic_objetive_brief_summary": "Shifts focus to 3D analytic geometry, introducing rectangular coordinate systems in space, distance formula, segment division, direction cosines, direction numbers, and angles between directed lines in 3D."
  },
  {
   "chapter_name": "EL PLANO",
   "chapter_number": 14,
   "content_density": 8,
   "difficulty": 7,
   "page_range": [359, 370],
   "reading_time_minutes": 70,
   "core_concepts": [
    "Forma general de la ecuación del plano",
    "Intercepciones con los ejes coordenados",
    "Trazas sobre los planos coordenados",
    "Simetría de una superficie",
    "Otras formas de la ecuación del plano (forma simétrica, de las intercepciones)",
    "Posiciones relativas de dos planos",
    "Forma normal de la ecuación del plano",
    "Aplicaciones de la forma normal",
    "Familias de planos"
   ],
   "prerequirement_chapters": [13],
   "pedagogic_objetive_brief_summary": "Dedicated to the study of planes in 3D space. Covers various forms of plane equations (general, intercept, normal), their properties, relative positions of planes, and families of planes."
  },
  {
   "chapter_name": "LA RECTA EN EL ESPACIO",
   "chapter_number": 15,
   "content_density": 8,
   "difficulty": 8,
   "page_range": [371, 406],
   "reading_time_minutes": 170,
   "core_concepts": [
    "Forma general de las ecuaciones de la recta",
    "Forma simétrica de las ecuaciones de la recta",
    "Ecuación de la recta que pasa por dos puntos",
    "Ecuaciones paramétricas de la recta",
    "Planos proyectantes de una recta",
    "Reducción de la forma general a la forma simétrica",
    "Posiciones de una recta y un plano"
   ],
   "prerequirement_chapters": [13, 14],
   "pedagogic_objetive_brief_summary": "Focuses on lines in 3D space, defined as intersections of planes. Covers general, symmetric, and parametric forms of line equations, projecting planes, reducing general form to symmetric, and analyzing relative positions of lines and planes."
  },
  {
   "chapter_name": "SUPERFICIES",
   "chapter_number": 16,
   "content_density": 9,
   "difficulty": 9,
   "page_range": [407, 439],
   "reading_time_minutes": 190,
   "core_concepts": [
    "Ecuación rectangular en tres variables",
    "Discusión de la ecuación de una superficie (intercepciones, trazas, simetría, secciones, extensión)",
    "Construcción de una superficie",
    "Ecuación de la superficie esférica",
    "Coordenadas esféricas",
    "Ecuación de una superficie cilíndrica",
    "Coordenadas cilíndricas",
    "Ecuación de una superficie cónica",
    "Superficies de revolución",
    "Superficies regladas",
    "Ecuación general de segundo grado con tres variables (cuádricas)",
    "Cuádricas con centro (elipsoides, hiperboloides)",
    "Cuádricas sin centro (paraboloides)"
   ],
   "prerequirement_chapters": [13, 14, 15],
   "pedagogic_objetive_brief_summary": "Introduces the general concept of surfaces in 3D space and methods for analyzing their equations. Covers specific surfaces like spheres, cylinders, cones, surfaces of revolution, ruled surfaces, and a detailed classification and study of quadric surfaces (ellipsoids, hyperboloids, paraboloids)."
  },
  {
   "chapter_name": "CURVAS EN EL ESPACIO",
   "chapter_number": 17,
   "content_density": 9,
   "difficulty": 9,
   "page_range": [440, 455],
   "reading_time_minutes": 90,
   "core_concepts": [
    "Representación de curvas en el espacio (intersección de dos superficies)", 
    "Curvas planas en el espacio",
    "Curva de intersección de las superficies de dos cilindros rectos",
    "Cilindros proyectantes de una curva del espacio",
    "Construcción de las curvas del espacio",
    "Ecuaciones paramétricas de una curva del espacio",
   ],
   "prerequirement_chapters": [13, 14, 15, 16],
   "pedagogic_objetive_brief_summary": "Explores curves in 3D space, which are defined by the intersection of two surfaces. Covers plane curves in space, intersections of cylinders, projecting cylinders, general construction methods, parametric equations for space curves, and calculating volumes."
  }
 ]
}
   (Use 'reading_time_minutes', 'difficulty', and 'prerequirement_chapters' to determine pacing and order). FOR THIS TEST YOU MUST ONLY USE UP UNTIL CHAPTER 9

2. USER CONSTRAINTS (The Athlete's Profile):
   {{USER_CONSTRAINTS_JSON}}: {
  "course_duration_weeks": 15,
  "study_days_per_week": 3,
  "daily_study_time_min": 60,
  "exams": [
    {
      "name": "Primer Parcial (La Recta)",
      "type": "partial",
      "week_scheduled": 4,
      "scope_chapters": [1, 2, 3] 
    },
    {
      "name": "Examen Final",
      "type": "global",
      "week_scheduled": 10,
      "scope_chapters": "ALL"
    }
  ]
}
   (Contains: 
    - 'course_duration_weeks': Total weeks available.
    - 'study_days_per_week': Integer (e.g., 5).
    - 'daily_study_time_min': Integer (e.g., 60).
    - 'exams': List of objects with {week, type: 'partial'/'global', scope: [chapters]}.
   )

------------------------------------------------------------------
ALGORITHMIC RULES (Sports Science Application):

1. CAPACITY MANAGEMENT (Load Calculation):
   - Compare `reading_time_minutes` vs `daily_study_time_min`. 
   - Rule: If a chapter's reading time > daily time, SPLIT the chapter across multiple days. Never overload a day.
   - Example: If Chap 3 takes 190 mins and user has 60 mins/day -> Schedule it over 3-4 days.

2. PERIODIZATION (Macro-Rhythm):
   - **Base Phase:** Early weeks. Low difficulty chapters. Focus on volume.
   - **Build Phase:** Middle weeks. High density/difficulty chapters.
   - **Deload Weeks:** - IF course > 4 weeks: Every 4th week is a "Deload".
     - Logic: Reduce 'New Content' by 50%. Fill days with "Active Recall" and "Consolidation" of previous topics.
   - **Tapering (Pre-Exam):**
     - The week immediately before a Major Exam (Global) is a Taper week.
     - Logic: Volume = Low, Intensity = High (Mock Tests). NO new reading in the last 3 days before exam.

3. INTERLEAVED PRACTICE (Anti-Monotony):
   - Do NOT schedule linear blocks (e.g., Week 1 is ONLY Chapter 1).
   - **The Mix Rule:** A study week should contain ~70% Current Topic and ~30% Review of previous topics (Spaced Repetition).
   - "Rest Days" must be respected as defined in `study_days_per_week`.

4. EXAM LOGIC:
   - **Partial Exams:** The days leading up to it must review ONLY the specific scope defined.
   - **Global Exams:** The days leading up to it must mix topics from the entire history of the course.

5. PREREQUISITES:
   - Strictly respect `prerequirement_chapters`. You cannot schedule Chapter 7 if Chapter 6 hasn't been covered in a previous or current week.

------------------------------------------------------------------
TASK:
Generate the MACRO CALENDAR JSON.

OUTPUT STRUCTURE REQUIREMENTS:
- Returns a single JSON object.
- **CRITICAL:** The "activity_type" field must map to the inputs required by Pass 3 (Lecture, Practice, Quiz, Rest).
- **CRITICAL:** The "pages" field must be accurate based on the book metadata.

JSON TEMPLATE:
{
  "plan_overview": {
    "total_weeks": Integer,
    "pacing_strategy": "String (e.g., 'Aggressive Build with Tapering')",
    "predicted_completion": "String (e.g., 'All chapters covered' or 'Chapters 1-12 only')"
  },
  "weeks": [
    {
      "week_number": 1,
      "phase": "Base / Build / Deload / Peak / Taper",
      "weekly_goal": "String",
      "days": [
        {
          "day_number": 1,
          "topic": "String (e.g., 'Sistemas de Coordenadas Part 1')",
          "target_chapter_id": 1,
          "pages": [19, 30], 
          "activity_type": "Theory + Practice / Practice Only / Active Recall / Mock Exam / Rest",
          "reasoning": "Split chapter due to length (120min > 60min daily limit)"
        },
        ... (Repeat for all days in the week)
      ]
    }
    ... (Repeat for all weeks)
  ]
}""", myfile]
)

print(response.text)