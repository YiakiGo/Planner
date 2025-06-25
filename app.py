from flask import Flask, jsonify, request

app = Flask(__name__)

# Example in-memory NGO data
NGOS = [
    {
        'id': 1,
        'name': 'Helping Hands',
        'status': 'pending_review'
    },
    {
        'id': 2,
        'name': 'Green Earth',
        'status': 'approved'
    },
    {
        'id': 3,
        'name': 'Relief Aid',
        'status': 'rejected'
    }
]

@app.route('/api/admin/ngos', methods=['GET'])
def get_ngos():
    """Return NGO applications filtered by status."""
    status = request.args.get('status')
    if status:
        filtered = [ngo for ngo in NGOS if ngo['status'] == status]
    else:
        filtered = NGOS
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
