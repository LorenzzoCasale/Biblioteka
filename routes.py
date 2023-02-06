from flask import Flask, jsonify, request
from server import User
from flask_swagger_ui import get_swaggerui_blueprint

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

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My Flask API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
