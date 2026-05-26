from flask import Flask, jsonify, request
import TimelineRepository as timelineRepo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# GET endpoint to retrieve all items
@app.route('/api/timeline/<login>', methods=['GET'])
def get_timeline(login):
    posts = timelineRepo.readTimeline(login) 
    return jsonify(posts)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
