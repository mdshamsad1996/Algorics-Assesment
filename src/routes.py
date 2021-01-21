"""contains all endpoint"""

from flask import jsonify, request
from src import app
from src.models import Models

mod = Models()


# provide page_no and row_size via query string
# example http://127.0.0.1:5000/record?page_no=2&row_size=3
@app.route('/record', methods=['GET'])
def get_songs_via_pagination():

    """Get songs via page no and page size(implementation of server side pagination)"""

    page_no = request.args.get('page_no')

    row_size = request.args.get('row_size')

    songs_details = mod.get_songs(int(page_no), int(row_size))

    return jsonify(songs_details)


# provide title of song via query string
# example http://127.0.0.1:5000/songs?title=3AM
@app.route('/songs', methods= ['GET'])
def get_songs_via_title():

    """Retrieve song via title"""

    title = request.args.get('title')

    songs_detail = mod.get_songs_details_via_title(title)

    return jsonify(songs_detail)


# Provide id of song and rating via query string using POST method
# end point url example http://127.0.0.1:5000/rating?id=14p5EKgbPx4U3P1j5JNHeh&rating=3
@app.route('/rating', methods=['POST'])
def post_rating():

    """provide rating to a particular song"""

    id = request.args.get('id')

    rating = request.args.get('rating')

    record = mod.provide_rating(id, int(rating))

    return jsonify(record)
