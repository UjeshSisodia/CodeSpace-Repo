from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace "Your Full Name" with your actual name
    name = "Ujesh"
    username = os.getenv('USER', 'codespace')  # Default to 'codespace' if not found
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %f")
    
    # Capture top command output
    try:
        top_output = subprocess.check_output(['top', '-n', '1', '-b']).decode('utf-8')
    except FileNotFoundError:
        top_output = "Error: 'top' command not found. Install procps."
    
    return f"""
    <pre>
    Name: {name}
    user: {username}
    Server Time (IST): {current_time}
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)