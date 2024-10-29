# CRUD
from flask import request, jsonify
from config import app, db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_dontact():
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (jsonify({"Message": "Missing required fields"}), 400)

    new_contact = Contact(first_name, last_name, email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return (jsonify({"Message": str(e)}), 400)

    return (jsonify({"Message": "Contact created successfully"}), 201)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
