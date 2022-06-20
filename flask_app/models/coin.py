from flask_app.config.mysqlconnection import connectToMySQL



class Coin:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.cuny_coin = db_data['cuny_coin']

    @classmethod
    def add_specific(cls, data):
        query = "INSERT INTO `hackathon`.`cuny_coin` (`balance`, `user_id`) VALUES ('%(balance)s', '%(user_id)s');" 
        return connectToMySQL('hackathon').query_db(query, data)
