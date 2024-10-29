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

@app.route('/update_contact/<int:user_id>', methods=["PUT"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"Message": "Contact not found"}), 404
    
    data = request.json
    contact.first_name = data('first_name', contact.first_name)
    contact.last_name = data('last_name', contact.last_name)
    contact.email = data('email', contact.email)

    db.session.commit()

    return jsonify({"message": "User updated."}, 200)

@app.route('/delete_contact/<int:user_id>', methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted."}, 200)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
