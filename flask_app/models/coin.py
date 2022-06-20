from flask_app.config.mysqlconnection import connectToMySQL



class Coin:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.cuny_coin = db_data['cuny_coin']