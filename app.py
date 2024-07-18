# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # Simulating a database with a dictionary
# # bus_data = {
# #     "total_seats": 40,
# #     "booked_seats": {}
# # }
# DATABASE = 'bus_booking.db'  # The name of the SQLite database file

# def init_db():
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS bookings (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 seat_number INTEGER NOT NULL,
#                 name TEXT NOT NULL,
#                 email TEXT NOT NULL
#             )
#         ''')

# # @app.route('/')
# # def index():
# #     available_seats = bus_data["total_seats"] - len(bus_data["booked_seats"])
# #     return render_template('index.html', available_seats=available_seats)
# @app.route('/')
# def index():
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT COUNT(*) FROM bookings')
#         booked_count = cursor.fetchone()[0]
#     available_seats = 40 - booked_count
#     return render_template('index.html', available_seats=available_seats)


# # @app.route('/book', methods=['GET', 'POST'])
# # def book():
# #     if request.method == 'POST':
# #         seat_number = request.form['seat_number']
# #         name = request.form['name']
# #         email = request.form['email']
        
# #         if seat_number not in bus_data["booked_seats"] and int(seat_number) <= bus_data["total_seats"]:
# #             bus_data["booked_seats"][seat_number] = {"name": name, "email": email}
# #             return redirect(url_for('status'))
# #         else:
# #             return render_template('booking.html', error="Seat already booked or invalid seat number.")
    
# #     return render_template('booking.html', booked_seats=bus_data["booked_seats"].keys())

# @app.route('/book', methods=['GET', 'POST'])
# def book():
#     if request.method == 'POST':
#         seat_number = request.form['seat_number']
#         name = request.form['name']
#         email = request.form['email']
        
#         with sqlite3.connect(DATABASE) as conn:
#             cursor = conn.cursor()
#             cursor.execute('SELECT * FROM bookings WHERE seat_number = ?', (seat_number,))
#             if cursor.fetchone() is None:
#                 cursor.execute('INSERT INTO bookings (seat_number, name, email) VALUES (?, ?, ?)', (seat_number, name, email))
#                 conn.commit()
#                 return redirect(url_for('status'))
#             else:
#                 return render_template('booking.html', error="Seat already booked or invalid seat number.")
    
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT seat_number FROM bookings')
#         booked_seats = [row[0] for row in cursor.fetchall()]
    
#     return render_template('booking.html', booked_seats=booked_seats)


# # @app.route('/status')
# # def status():
#     # return render_template('status.html', booked_seats=bus_data["booked_seats"])
# @app.route('/status')
# def status():
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT seat_number, name, email FROM bookings')
#         booked_seats = cursor.fetchall()
    
#     return render_template('status.html', booked_seats=booked_seats)


# # if __name__ == '__main__':
# #     app.run(debug=True)

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'bus_booking.db'  # The name of the SQLite database file

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                seat_number INTEGER NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')

@app.route('/')
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM bookings')
        booked_count = cursor.fetchone()[0]
    available_seats = 40 - booked_count
    return render_template('index.html', available_seats=available_seats)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        seat_number = request.form['seat_number']
        name = request.form['name']
        email = request.form['email']
        
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM bookings WHERE seat_number = ?', (seat_number,))
            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO bookings (seat_number, name, email) VALUES (?, ?, ?)', (seat_number, name, email))
                conn.commit()
                return redirect(url_for('status'))
            else:
                return render_template('booking.html', error="Seat already booked or invalid seat number.")
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT seat_number FROM bookings')
        booked_seats = [row[0] for row in cursor.fetchall()]
    
    return render_template('booking.html', booked_seats=booked_seats)



@app.route('/status')
def status():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT seat_number, name, email FROM bookings')
        booked_seats = cursor.fetchall()
    
    return render_template('status.html', booked_seats=booked_seats)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
