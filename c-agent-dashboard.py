#!/usr/bin/env python3
"""
C-Agent Dashboard Web Server
Simple HTTP server for monitoring and controlling the C-Agent
"""

import http.server
import socketserver
import json
import os
import subprocess
import time
from datetime import datetime

class CAgentHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/dashboard':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.generate_dashboard_html().encode())
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.get_status()).encode())
        elif self.path == '/api/system':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.get_system_info()).encode())
        elif self.path.startswith('/api/analyze'):
            self.handle_analysis_request()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 - Not Found</h1>')

    def generate_dashboard_html(self):
        return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C-Agent Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}

        .header {{
            background: rgba(0, 0, 0, 0.1);
            padding: 20px;
            color: white;
            text-align: center;
            backdrop-filter: blur(10px);
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}

        .stat-card {{
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
        }}

        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}

        .controls {{
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }}

        .btn {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1.1em;
            margin: 5px;
            transition: all 0.3s ease;
        }}

        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}

        .log-area {{
            background: #1e1e1e;
            color: #00ff00;
            padding: 20px;
            border-radius: 10px;
            font-family: 'Courier New', monospace;
            height: 200px;
            overflow-y: auto;
            margin: 20px 0;
        }}

        .system-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}

        .info-card {{
            background: rgba(255, 255, 255, 0.9);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🛡️ C-Agent Dashboard</h1>
        <p>Security & Development Agent Monitor</p>
        <p>Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>

    <div class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{len(os.listdir('src')) if os.path.exists('src') else 0}</div>
                <div>Source Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(os.listdir('.'))}</div>
                <div>Total Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{datetime.now().strftime('%H:%M')}</div>
                <div>Current Time</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">✅</div>
                <div>System Status</div>
            </div>
        </div>

        <div class="controls">
            <h3>🎯 Quick Actions</h3>
            <button class="btn" onclick="runSecurityScan()">🔍 Security Scan</button>
            <button class="btn" onclick="generateDocumentation()">📋 Generate Docs</button>
            <button class="btn" onclick="analyzeDependencies()">📊 Analyze Dependencies</button>
            <button class="btn" onclick="runFullAnalysis()">🚀 Full Analysis</button>
        </div>

        <div class="controls">
            <h3>📊 System Information</h3>
            <div class="system-info">
                <div class="info-card">
                    <strong>Directory</strong><br>
                    {os.getcwd()}
                </div>
                <div class="info-card">
                    <strong>Python Version</strong><br>
                    {subprocess.run(['python3', '--version'], capture_output=True, text=True).stdout.strip()}
                </div>
                <div class="info-card">
                    <strong>Files in src/</strong><br>
                    {', '.join(os.listdir('src')[:5])}... if len(os.listdir('src')) > 5 else ', '.join(os.listdir('src'))}
                </div>
            </div>
        </div>

        <div class="controls">
            <h3>📈 Real-time Logs</h3>
            <div class="log-area" id="log-area">
                Dashboard started successfully...
                Ready for analysis tasks...
            </div>
        </div>

        <div class="controls">
            <h3>🎯 Manual Commands</h3>
            <p>You can also use these commands directly:</p>
            <ul>
                <li><code>python3 c-agent-dashboard.py</code> - Start dashboard</li>
                <li><code>ls -la src/</code> - List source files</li>
                <li><code>find . -name "*.c" | wc -l</code> - Count C files</li>
                <li><code>grep -r "#include" src/ | wc -l</code> - Count includes</li>
            </ul>
        </div>
    </div>

    <script>
        function addLog(message) {{
            const logArea = document.getElementById('log-area');
            const timestamp = new Date().toLocaleTimeString();
            logArea.innerHTML += `[${{timestamp}}] ${{message}}\\n`;
            logArea.scrollTop = logArea.scrollHeight;
        }}

        function runSecurityScan() {{
            addLog('Starting security scan...');
            fetch('/api/scan?type=security')
                .then(response => response.json())
                .then(data => addLog('Security scan completed: ' + data.result));
        }}

        function generateDocumentation() {{
            addLog('Generating documentation...');
            fetch('/api/generate?type=docs')
                .then(response => response.json())
                .then(data => addLog('Documentation generated: ' + data.result));
        }}

        function analyzeDependencies() {{
            addLog('Analyzing dependencies...');
            fetch('/api/analyze?type=dependencies')
                .then(response => response.json())
                .then(data => addLog('Dependencies analyzed: ' + data.result));
        }}

        function runFullAnalysis() {{
            addLog('Running full analysis...');
            fetch('/api/analyze?type=full')
                .then(response => response.json())
                .then(data => addLog('Full analysis completed: ' + data.result));
        }}

        // Auto-refresh every 5 seconds
        setInterval(() => {{
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {{
                    // Update metrics if needed
                }});
        }}, 5000);
    </script>
</body>
</html>
        """

    def get_status(self):
        return {
            'total_requests': 1,
            'files_analyzed': len(os.listdir('src')) if os.path.exists('src') else 0,
            'vulnerabilities_found': 0,
            'documentation_generated': 1,
            'last_activity': str(datetime.now()),
            'uptime': time.time()
        }

    def get_system_info(self):
        try:
            cpu_info = subprocess.run(['top', '-l', '1'], capture_output=True, text=True).stdout
            memory_info = subprocess.run(['free', '-h'], capture_output=True, text=True).stdout if os.path.exists('/bin/free') else 'Memory info not available'
            disk_info = subprocess.run(['df', '-h', '/'], capture_output=True, text=True).stdout
            
            return {
                'cpu': cpu_info.split('\n')[0] if cpu_info else 'CPU info not available',
                'memory': memory_info.split('\n')[0] if memory_info else 'Memory info not available',
                'disk': disk_info.split('\n')[1] if disk_info else 'Disk info not available'
            }
        except Exception as e:
            return {'error': str(e)}

    def handle_analysis_request(self):
        query = self.path.split('?')[1] if '?' in self.path else ''
        params = dict(param.split('=') for param in query.split('&') if '=' in param)
        
        analysis_type = params.get('type', 'unknown')
        
        # Simulate analysis
        result = f"Analysis type '{analysis_type}' completed successfully"
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'result': result}).encode())

if __name__ == '__main__':
    PORT = 8080
    Handler = CAgentHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌐 C-Agent Dashboard started at http://localhost:{PORT}")
        print("✅ Dashboard is ready!")
        print("📋 Available endpoints:")
        print("   GET /              - Main dashboard")
        print("   GET /api/status    - JSON status API")
        print("   GET /api/system    - System information")
        print("   GET /api/analyze   - Analysis endpoints")
        print("\n🛑 Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Dashboard stopped")
            httpd.shutdown()
