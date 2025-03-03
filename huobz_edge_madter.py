from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

# Storage for connected devices
devices = {"admin": [], "users": []}

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        if not data or 'device_ip' not in data or 'device_type' not in data:
            return jsonify({"error": "Invalid request. Required: device_ip, device_type"}), 400

        device = {
            "ip": data['device_ip'],
            "type": data['device_type'],
            "cpu": data.get("cpu", "Unknown"),
            "gpu": data.get("gpu", "Unknown"),
            "storage": data.get("storage", "Unknown")
        }

        if data["device_type"] == "admin":
            devices["admin"].append(device)
        elif data["device_type"] == "user":
            devices["users"].append(device)
        else:
            return jsonify({"error": "Invalid device type"}), 400

        print(f"✅ {data['device_type'].capitalize()} Node Registered: {device}")
        return jsonify({"message": "Device registered successfully", "devices": devices}), 200

    except Exception as e:
        print(f"❌ Registration Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
