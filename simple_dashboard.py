#!/usr/bin/env python3
"""
Ultra-simple C-Agent Dashboard
Minimal HTTP server for demonstration
"""

import http.server
import socketserver
import os
import json
from datetime import datetime

class SimpleDashboard(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>C-Agent Dashboard</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }}
                    .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; text-align: center; border-radius: 10px; margin-bottom: 20px; }}
                    .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
                    .stat-card {{ background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; }}
                    .btn {{ background: #667eea; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin: 5px; }}
                    .btn:hover {{ background: #5a6fd8; }}
                    .log {{ background: #1e1e1e; color: #00ff00; padding: 10px; border-radius: 5px; font-family: monospace; height: 150px; overflow-y: auto; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🛡️ C-Agent Dashboard</h1>
                        <p>Security & Development Monitor</p>
                        <p>Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    </div>
                    
                    <div class="stats">
                        <div class="stat-card">
                            <h3>📁 Files</h3>
                            <p>{len(os.listdir('.'))} total files</p>
                        </div>
                        <div class="stat-card">
                            <h3>📝 Source Files</h3>
                            <p>{len([f for f in os.listdir('.') if f.endswith('.c')])} .c files</p>
                        </div>
                        <div class="stat-card">
                            <h3>🔧 Status</h3>
                            <p>✅ Active</p>
                        </div>
                    </div>
                    
                    <h3>🎯 Quick Actions</h3>
                    <button class="btn" onclick="alert('Security scan started')">🔍 Security Scan</button>
                    <button class="btn" onclick="alert('Documentation generation started')">📋 Generate Docs</button>
                    <button class="btn" onclick="alert('Dependency analysis started')">📊 Analyze Dependencies</button>
                    <button class="btn" onclick="alert('Full analysis started')">🚀 Full Analysis</button>
                    
                    <h3>📊 Project Information</h3>
                    <p><strong>Current Directory:</strong> {os.getcwd()}</p>
                    <p><strong>Files in src/:</strong> {', '.join(os.listdir('src')[:5])}... if len(os.listdir('src')) > 5 else ', '.join(os.listdir('src'))}</p>
                    
                    <h3>📈 Real-time Logs</h3>
                    <div class="log">
                        Dashboard started successfully...<br>
                        Security monitoring active...<br>
                        Ready for analysis tasks...<br>
                        {datetime.now().strftime('%H:%M:%S')} - System ready
                    </div>
                    
                    <h3>💻 Manual Commands</h3>
                    <ul>
                        <li><code>ls -la src/</code> - List source files</li>
                        <li><code>find . -name "*.c" | wc -l</code> - Count C files</li>
                        <li><code>grep -r "#include" src/ | wc -l</code> - Count includes</li>
                        <li><code>wc -l src/*.c</code> - Count lines of code</li>
                    </ul>
                </div>
            </body>
            </html>
            """
            
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'<h1>404 - Not Found</h1>')

if __name__ == '__main__':
    PORT = 8080
    Handler = SimpleDashboard
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌐 C-Agent Dashboard started at http://localhost:{PORT}")
        print("✅ Dashboard is ready!")
        print("📋 Available endpoints:")
        print("   GET /              - Main dashboard")
        print("\n🛑 Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Dashboard stopped")
