"""This is model modules, conatins all business logic"""
import json

rows = []


class Models:
    """"Models class"""

    def __init__(self):
        pass

    def load_data(self):

        """"Store playlist json data in memeory"""
        global rows

        with open('playlist.json', 'r') as f:

            data = json.load(f)     
            for i in range(0, 100):
                dic = {}
                for key, val in data.items():
                    dic[key] = val[str(i)]
                rows.append(dic)

    def provide_rating(self, id, rating):

        """"Provide rating to any songs via id"""
        global rows
        # rows = self.load_data()

        row = [row for row in rows if row['id'] == id]

        if not row:
            return {"message": "No song list found with provided id"}

        index = rows.index(row[0])

        row[0]['star_rating'] = rating

        rows[index] = row[0]

        return row[0]

    def get_songs_details_via_title(self, title):

        """Get the songs via title"""

        global rows

        songs_detail = [row for row in rows if row['title'] == title]

        if not songs_detail:
            return {"message": "No song list found with provided title"}

        return songs_detail

    def get_songs(self, page_no, page_size):

        """Implementation of pagination"""

        global rows

        if page_no > 1:
            strt_row = (page_no - 1) * page_size
        else:
            strt_row = 0

        rows_val = [row for row in rows[strt_row: page_size + strt_row]]

        return rows_val
