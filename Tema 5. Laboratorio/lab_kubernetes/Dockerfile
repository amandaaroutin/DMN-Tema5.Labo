# Imagen base ligera con Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de la app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Puerto expuesto
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
