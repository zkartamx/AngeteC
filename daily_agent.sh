#!/bin/bash
# C-Agent Daily Usage Script
# Script optimizado para uso diario

echo "🚀 C-Agent Daily Check - $(date)"
echo "========================================="

# 1. Análisis rápido
echo "📊 Running quick analysis..."
python3 agent_task.py

# 2. Verificar estado actual
echo "📈 Checking current status..."
echo "   Files analyzed: $(find . -name "*.c" | wc -l) C files"
echo "   Dependencies: $(grep -r "#include" src/ | wc -l) includes"

# 3. Actualizar dashboard
echo "🌐 Updating dashboard..."
python3 agent_task.py > /dev/null 2>&1

# 4. Generar resumen diario
echo "📋 Creating daily summary..."
cat > daily_summary.md << EOF
# C-Agent Daily Summary - $(date)

## Quick Stats
- **C Files:** $(find . -name "*.c" | wc -l)
- **Header Files:** $(find . -name "*.h" | wc -l)
- **Python Files:** $(find . -name "*.py" | wc -l)
- **Total Includes:** $(grep -r "#include" src/ | wc -l)

## Action Items
- [ ] Review security analysis
- [ ] Update documentation
- [ ] Check for new dependencies
- [ ] Optimize code structure

## Commands for tomorrow
\`\`\`bash
# Quick analysis
python3 agent_task.py

# Check dependencies
grep -r "#include" src/ | head -10

# Count lines of code
wc -l src/*.c
\`\`\`

## Dashboard Access
Open: file:///Users/carteaga/Projects/Agentes_C/dashboard.html
EOF

echo "✅ Daily check completed!"
echo "📊 Dashboard: file:///Users/carteaga/Projects/Agentes_C/dashboard.html"
echo "📋 Summary: daily_summary.md"
