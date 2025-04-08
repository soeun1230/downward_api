from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    pod_name = os.getenv("POD_NAME", "testPod")
    node_name = os.getenv("NODE_NAME", "testNode")
    namespace = os.getenv("POD_NAMESPACE", "testNS")
    return f"Container EDU | POD Working : {pod_name} | nodename : {node_name} | namespace : {namespace}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
