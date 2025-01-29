from flask import Flask, render_template, request, jsonify
from network_scanner import scan_network
from vulnerability_assessor import assess_vulnerabilities
from exploit_deployer import deploy_exploit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan_network', methods=['POST'])
def scan_network_endpoint():
    devices = scan_network()
    vulnerabilities = assess_vulnerabilities(devices)
    return jsonify(vulnerabilities)

@app.route('/deploy_exploit', methods=['POST'])
def deploy_exploit_endpoint():
    target = request.json.get('target')
    result = deploy_exploit(target)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
