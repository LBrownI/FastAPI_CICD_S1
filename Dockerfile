# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY pyproject.toml poetry.lock ./
COPY app app/

# Instala dependencias del proyecto
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
