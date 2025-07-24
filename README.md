# 🛡️ C-Agent - Security & Development Agent

## 🚀 Descripción

**C-Agent** es un agente inteligente de seguridad y desarrollo para proyectos C/C++, que proporciona análisis automático, generación de documentación, escaneo de dependencias y monitoreo en tiempo real a través de un dashboard web moderno.

## ✨ Características Principales

### 📊 Dashboard Web Interactivo
- **Interfaz moderna** con diseño responsivo
- **Monitoreo en tiempo real** de métricas del proyecto
- **Análisis visual** de archivos y dependencias
- **Controles interactivos** para ejecutar tareas

### 🔍 Análisis Automático
- **Análisis de archivos** C/C++
- **Detección de dependencias** y vulnerabilidades
- **Generación automática** de documentación
- **Reportes detallados** en JSON y Markdown

### 🛡️ Seguridad
- **Validación de rutas** seguras
- **Escaneo de vulnerabilidades** conocidas
- **Análisis de dependencias** inseguras
- **Reportes de seguridad** detallados

### 📈 Monitoreo
- **Métricas en tiempo real**
- **Estado del proyecto** actualizado
- **Logs de actividad** automatizados
- **Alertas y notificaciones**

## 🚀 Instalación y Uso

### Requisitos previos
- Python 3.x
- GCC (para proyectos C)
- Navegador web moderno

### Instalación rápida
```bash
# Clonar repositorio
git clone https://github.com/zkartamx/AngeteC.git
cd AngeteC

# Hacer ejecutables los scripts
chmod +x daily_agent.sh
chmod +x *.py

# Ejecutar análisis inicial
./daily_agent.sh
```

### Uso diario
```bash
# Análisis completo
python3 agent_task.py

# Dashboard web
open dashboard.html

# Monitoreo diario
./daily_agent.sh
```

## 📋 Scripts disponibles

### `agent_task.py`
Análisis completo del proyecto con métricas y reportes.

### `daily_agent.sh`
Script diario para análisis y mantenimiento.

### `dashboard.html`
Dashboard web interactivo para monitoreo visual.

### `demo_simple`
Programa de demostración de las capacidades del agente.

## 📊 Estructura del proyecto

```
AngeteC/
├── 📁 src/                    # Código fuente C/C++
├── 📁 reports/                # Reportes generados
├── 📁 docs/                   # Documentación
├── 📁 dashboard.html          # Dashboard web
├── 📁 agent_task.py          # Análisis principal
├── 📁 daily_agent.sh         # Script diario
├── 📁 README.md             # Este archivo
└── 📁 ...
```

## 🎯 Comandos útiles

### Análisis básico
```bash
# Contar archivos C
find . -name "*.c" | wc -l

# Ver dependencias
grep -r "#include" src/

# Análisis de líneas
cat reports/task_summary.md
```

### Dashboard
```bash
# Abrir dashboard
open dashboard.html

# O en navegador
file:///ruta/al/proyecto/dashboard.html
```

## 🔧 Configuración avanzada

### Alias útiles
```bash
# Agregar a ~/.zshrc
alias agent="cd /ruta/al/proyecto && ./daily_agent.sh"
alias dashboard="open /ruta/al/proyecto/dashboard.html"
alias analyze="python3 /ruta/al/proyecto/agent_task.py"
```

### Monitoreo automático
```bash
# Ejecutar cada hora
./monitor.sh &

# Ver logs en tiempo real
tail -f reports/*.log
```

## 📈 Métricas y reportes

### Reportes generados
- `reports/agent_analysis.json` - Análisis detallado
- `reports/task_summary.md` - Resumen ejecutivo
- `reports/dependency_report.md` - Análisis de dependencias

### Métricas disponibles
- Número de archivos por tipo
- Dependencias encontradas
- Includes del sistema vs locales
- Vulnerabilidades detectadas

## 🛡️ Seguridad

### Validaciones implementadas
- Validación de rutas seguras
- Escaneo de funciones inseguras
- Análisis de dependencias vulnerables
- Reportes de seguridad detallados

## 🤝 Contribución

1. Fork el proyecto
2. Crear feature branch
3. Commit cambios
4. Push a la rama
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo LICENSE para más detalles.

## 📞 Soporte

Para soporte o preguntas, abrir un issue en GitHub o contactar al equipo de desarrollo.

---

**🚀 C-Agent - Desarrollo seguro y eficiente para proyectos C/C++**
