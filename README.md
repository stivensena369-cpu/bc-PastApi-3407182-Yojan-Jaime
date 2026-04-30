# bc-PastApi-3407182-Yojan-Jaime


# 🎯 Escape Room API

Esta es una API básica creada con FastAPI para el proyecto de la semana 01.
Simula un sistema de Escape Room donde se pueden manejar saludos, equipos y salas.

---

## 📋 Descripción

Esta API permite:

* Ver información general del proyecto
* Enviar saludos personalizados en diferentes idiomas
* Generar saludos formales para equipos
* Mostrar mensajes según la hora del día
* Verificar si la API está funcionando correctamente

Todo el proyecto se ejecuta usando Docker.

---

## 🚀 Tecnologías usadas

* Python
* FastAPI
* Docker
* Docker Compose

---

## ▶️ Cómo ejecutar el proyecto

1. Abrir la terminal en la carpeta del proyecto
2. Ejecutar el siguiente comando:

```bash
docker compose up --build
```

3. Abrir el navegador y entrar a:

```
http://localhost:8000/docs
```

Ahí puedes ver y probar todos los endpoints.

---

## 🔗 Endpoints principales

### 🟢 Información de la API

```
GET /
```

---

### 🟢 Saludo personalizado

```
GET /player/{name}?language=es
```

Ejemplo:

```
/player/Juan?language=en
```

---

### 🟢 Saludo formal

```
GET /team/{name}/formal?title=Pro
```

---

### 🟢 Saludo según la hora

```
GET /room/{name}/time-based?hour=10
```

---

### 🟢 Estado de la API

```
GET /health
```

---

## 🧠 Notas

* Los idiomas soportados son: es, en, fr
* Si el idioma no existe, usa español por defecto
* La API responde diferente según la hora del día

---

## ✅ Estado

Proyecto funcional para el bootcamp de FastAPI 🚀
