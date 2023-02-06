from flask import Flask, jsonify, request
from model import User

app = Flask(__name__)

@app.route("/user/<cpf>", methods=["GET"])
def get_user_by_cpf(cpf):
    user = User.get(cpf)
    if user:
        return jsonify({"cpf": user.cpf, "name": user.name, "tel": user.tel})
    return jsonify({"message": "User not found"}), 404

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User.create(data["cpf"], data["name"], data["tel"])
    return jsonify({"cpf": user.cpf, "name": user.name, "tel": user.tel})

@app.route("/user/<cpf>", methods=["PUT"])
def update_user_by_cpf(cpf):
    user = User.get(cpf)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    name = data.get("name")
    tel = data.get("tel")
    user.update(name, tel)
    return jsonify({"cpf": user.cpf, "name": user.name, "tel": user.tel})

@app.route("/user/<cpf>", methods=["DELETE"])
def delete_user_by_cpf(cpf):
    user = User.get(cpf)
    if not user:
        return jsonify({"message": "User not found"}), 404
    user.delete()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
