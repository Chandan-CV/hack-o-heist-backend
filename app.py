import psycopg2
from flask import Flask, jsonify, request

# conn = psycopg2.connect(database="dccvhrhdhdemh6", user='schfljfffwlbft', password='768b83bf3aa28222ec0afc2ac937282e9976669aec1305c73b7666ec14a0c16f', host='ec2-54-76-43-89.eu-west-1.compute.amazonaws.com', port= '5432')
# cursor = conn.cursor()
#establishing the database connection
# data = cursor.execute("select version()")
# data = cursor.fetchone()
# print("Connection established to: ", data)

def setup():
    # cursor.execute("DROP TABLE IF EXISTS food")
    # conn.commit()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS food(
                id SERIAL PRIMARY KEY,
                name VARCHAR (20),
                location VARCHAR (2000),
                quantity INTEGER
                )
                """
    )
    conn.commit()

# setup()



def get_row(id):
    cursor.execute("SELECT * FROM food WHERE id = $1",id)
    data = cursor.fetchall()
    return data

def get_all():
    cursor.execute("SELECT * FROM food")
    data = cursor.fetchall()
    print(data)
    return data


def new_entry(name,quantity,location):
    cursor.execute("INSERT INTO food(name,quantity,location) VALUES(%s,%s,%s)",(name,quantity,location))
    conn.commit()

# new_entry("test",1,"Bangalore")

  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
#         data =  get_all()
        return jsonify({'data': "lmaoo"})
  
  
# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num**2})
  
  
# driver function
if __name__ == '__main__':
    #app.run(debug = True)
    app.run(debug = True)