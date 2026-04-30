from fastapi import FastAPI

app = FastAPI(
    title="Escape Room API",
    description="API para gestión de escape rooms",
    version="1.0.0"
)

# ============================================
# ENDPOINT RAÍZ
# ============================================

@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "Escape Room API",
        "version": "1.0.0",
        "domain": "escape-room"
    }

# ============================================
# BIENVENIDA PERSONALIZADA
# ============================================

@app.get("/team/{name}")
async def welcome(
    name: str,
    language: str = "es"
) -> dict[str, str]:

    messages = {
        "es": f"¡Bienvenido al escape room, {name}!",
        "en": f"Welcome to the escape room, {name}!",
        "fr": f"Bienvenue dans l'escape room, {name}!"
    }

    message = messages.get(language, messages["es"])

    return {
        "message": message
    }

# ============================================
# INFORMACIÓN DE BOOKINGS
# ============================================

@app.get("/bookings/{booking_id}/info")
async def booking_info(
    booking_id: str,
    detail_level: str = "basic"
) -> dict:

    if detail_level == "full":
        return {
            "id": booking_id,
            "team": "Team Alpha",
            "room": "Horror Room",
            "time": "20:00",
            "status": "confirmed"
        }

    return {
        "id": booking_id,
        "team": "Team Alpha",
        "room": "Horror Room"
    }

# ============================================
# SERVICIO SEGÚN HORA
# ============================================

@app.get("/service/schedule")
async def schedule(hour: int) -> dict:

    if 6 <= hour <= 11:
        return {
            "message": "Turno de mañana - Salas abiertas",
            "available": ["rooms", "clues"]
        }

    elif 12 <= hour <= 17:
        return {
            "message": "Turno de tarde - Máxima actividad",
            "available": ["rooms", "teams", "bookings"]
        }

    else:
        return {
            "message": "Turno nocturno - Modo terror activo",
            "available": ["horror rooms", "special clues"]
        }

# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "domain": "escape-room"
    }