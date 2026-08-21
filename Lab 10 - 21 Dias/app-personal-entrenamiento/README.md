# Training Tracker

Aplicación web para tracking de entrenamiento con estética Notion-like.

## 🚀 Características

- ✅ **Interfaz minimalista** estilo Notion (mucho espacio en blanco, tipografía limpia)
- ✅ **Vista de entrenamiento del día** - Filtra automáticamente ejercicios según el día de la semana
- ✅ **Registro de series** - Captura peso real, reps reales y observaciones
- ✅ **Dashboard de progreso** - Visualiza volumen semanal con gráficas
- ✅ **Biblioteca de ejercicios** - Catálogo completo organizado por grupo muscular
- ✅ **Historial** - Revisa entrenamientos anteriores
- ✅ **Exportación de datos** - Descarga tu progreso en formato JSON

## 📁 Estructura del Proyecto

```
app-personal-entrenamiento/
├── index.html      # Estructura principal de la aplicación
├── styles.css      # Estilos Notion-like (minimalista)
├── app.js          # Lógica de la aplicación
├── data.json       # Base de datos con ejercicios y historial
└── README.md       # Este archivo
```

## 🎯 Cómo usar

1. **Abre `index.html` en tu navegador** - No requiere instalación ni servidor

2. **Vista "Hoy"** (predeterminada):
   - Muestra automáticamente los ejercicios programados para el día actual
   - Registra peso, repeticiones y observaciones para cada serie
   - Haz clic en "Guardar" para almacenar tu entrenamiento

3. **Vista "Progreso"**:
   - Visualiza estadísticas de la semana actual
   - Gráfica de volumen por grupo muscular
   - Métricas de entrenamientos completados

4. **Vista "Ejercicios"**:
   - Biblioteca completa de ejercicios
   - Información de series/reps objetivo
   - Organizado por grupo muscular

5. **Vista "Historial"**:
   - Entrenamientos anteriores ordenados por fecha
   - Resumen de volumen y duración

## 📊 Base de Datos (data.json)

El archivo `data.json` contiene:

- **Grupos musculares**: Pecho, Espalda, Piernas, Hombros, Brazos
- **Ejercicios**: 17 ejercicios con objetivos de series/reps/peso
- **Cardio**: Correr y Bicicleta con objetivos de km/tiempo
- **Historial**: Entrenamientos registrados previamente

### Programación Semanal

- **Lunes/Jueves**: Pecho y Hombros
- **Martes/Viernes**: Espalda y Brazos
- **Miércoles/Sábado**: Piernas
- **Domingo**: Descanso (o cardio opcional)

## 🎨 Estética Notion-like

- Paleta de colores neutros y minimalista
- Tipografía Inter (limpia y profesional)
- Espaciado generoso entre elementos
- Bordes suaves y sombras sutiles
- Iconos SVG simples
- Animaciones suaves en interacciones

## 🔧 Personalización

### Agregar nuevos ejercicios

Edita `data.json` y añade objetos en el array `exercises`:

```json
{
  "id": "mi-ejercicio",
  "name": "Nombre del Ejercicio",
  "muscleGroup": "chest",
  "targetSets": 4,
  "targetReps": "8-10",
  "targetWeight": 50,
  "notes": "Instrucciones técnicas"
}
```

### Cambiar días de entrenamiento

Modifica el array `days` en cada grupo muscular:

```json
{
  "id": "chest",
  "name": "Pecho",
  "icon": "💪",
  "days": ["lunes", "jueves"]
}
```

## 📈 Exportar Datos

Haz clic en el botón "Exportar" en la cabecera para descargar tus datos en formato JSON. Útil para:
- Backup de tu progreso
- Análisis en otras herramientas
- Compartir tu rutina

## 🌐 Navegadores Compatibles

- Chrome/Edge (recomendado)
- Firefox
- Safari
- Opera

## 💡 Próximas Mejoras

- [ ] Timer integrado para medir duración de entrenamientos
- [ ] Modo oscuro
- [ ] Gráficas de progreso individual por ejercicio
- [ ] Calculadora de 1RM
- [ ] Almacenamiento en localStorage
- [ ] PWA para uso offline

## 📝 Notas

Esta es una aplicación **cliente-side only** (frontend puro). Los datos se almacenan en memoria durante la sesión. Para persistencia real, considera implementar:
- localStorage para guardar en el navegador
- Backend con API REST
- Base de datos (MongoDB, PostgreSQL, etc.)

---

**¡Feliz entrenamiento! 💪**
