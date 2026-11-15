import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, basedir)

from factory import create_app

app = create_app()

if __name__ == "__main__":
    print("Starting Ifood Copilot Backend on port 5001...")
    app.run(host="127.0.0.1", port=5001, debug=False)
