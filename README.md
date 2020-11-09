# Install
pip install -r requirements.txt

## Referencia del regex horrible: 

https://embed.ihateregex.io/make/JTVCJTVFJTQwJTIwJTVDJTVDdCU1QyU1Q3IlNUMlNUNuJTVEJTJCJTVDJTVDcyU1QiU1RSU0MCUyMCU1QyU1Q3QlNUMlNUNyJTVDJTVDbiU1RCUyQiU1QyU1Q3MlNUIlNUUlNDAlMjAlNUMlNUN0JTVDJTVDciU1QyU1Q24lNUQlMkIlMkMlMjBSdXQlNUMlNUNzJTJCJTVDJTVDZCU3QjElMkMyJTdEJTVDJTVDLiU1QyU1Q2QlN0IzJTdEJTVDJTVDLiU1QyU1Q2QlN0IzJTdEJTVCLSU1RCU1QjAtOWtLJTVEJTVDJTVDbg

# Scrapping

## Web Scraping

En la página del Diario Oficial (https://www.diariooficial.interior.gob.cl/) se encuentran todas las publicaciones digitalizadas de los últimos años. Estas publicaciones corresponden a extractos de publicaciones de leyes, normas y constitución de empresas entre otras. Para este ejercicio nos enfocaremos solo en la parte de empresas.

Si navegas a la sección de "EDICIÓN ELECTRÓNICA" y luego a la sub-sección de "EMPRESAS Y COOPERATIVAS" verás un detalle de todas las Constituciones, Modificaciones y Disoluciones del día actual.

1.- Función que descarga en una carpeta todos los PDFs (CVE-157XXXX) del tipo CONSTITUCIÓN del día actual.

```python
"""
path:string > path a la carpeta donde bajar los archivos
"""
def download_todays_constituciones(path):
   ...
   ...
```

2.- Función que descarga todas las constituciones del año 2019.

```python
"""
path:string > path a la carpeta donde bajar los archivos
year:number > año a descargar (ej: 2019)
"""
def download_constituciones_from_year(year, path):
   ...
   ...
```

## Extracción de información

1.- En la carpeta "sociedades-pdf" hay 5 archivos PDF con constituciones de sociedad.

```python
"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path):
   ...
   ...
   return text
```

2.- ¿Se puede extraer con la misma función de la parte (1) los textos de los PDF en la carpeta "sociedades-b-pdf"? ¿Qué es lo distinto?

## Procesamiento de Lenguaje

En la carpeta "sociedades-texto" hay una lista de +400 textos de sociedades ya extraídas.

1.- Función que imprime en consola el nombre y RUT de quienes comparecen(\*) en la escritura.

(\*) Puedes ver quienes comparecen generalmente en el tercer párrafo, bajo el RUT de la sociedad. Ejemplo:

> En RECOLETA, Región METROPOLITANA DE SANTIAGO, Chile, a 18 de mayo del 2018, ante el Registro Electrónico de Empresas y Sociedades, **comparecen: ANDREA PAULINA NÚÑEZ ESPINOZA, Rut 15.602.114-8, domiciliada en El Marco N°1020 villa Augusto Zamorano, comuna de RECOLETA, Región METROPOLITANA DE SANTIAGO;** y expone/n: Por el presente acto...

```python
def print_owners():
   ...
   ...
   for...
      ...
      print(...)
   ...
   ...
```

Output esperado

```
-- AC0AV8Q7cIeH.txt --
ANDREA PAULINA NÚÑEZ ESPINOZA, 15.602.114-8

-- AC0b5mWFT80k.txt --
MAURICIO ANDRÉS CAROCA LARA, 15.630.469-7
SANDRA ELIZABETH CORTÉS-MONROY ARAOS, 15.044.523-K

....+400
```
.-
