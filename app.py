from flask import Flask, render_template, request, redirect, session
import mysql.connector
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, SECRET_KEY
app = Flask(__name__)
app.secret_key = SECRET_KEY


# ------------------ DATABASE CONNECTION ------------------
def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )


# ------------------ HOME ------------------
@app.route('/')
def home():
    return render_template('home.html')


# ------------------ BUTIKK ------------------
@app.route('/butikk')
def butikk():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    conn.close()
    return render_template("butikk.html", categories=categories)


# ------------------ KONTAKT ------------------
@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')


# ------------------ CATEGORY PAGE ------------------
@app.route('/category/<int:category_id>')
def category_page(category_id):

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM categories WHERE id = %s", (category_id,))
    category = cur.fetchone()

    cur.execute("SELECT * FROM boxes WHERE category_id = %s", (category_id,))
    boxes = cur.fetchall()

    conn.close()

    return render_template("category.html", category=category, boxes=boxes)


# ------------------ BOX PAGE ------------------
@app.route("/box/<int:box_id>")
def box_page(box_id):

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM boxes WHERE id = %s", (box_id,))
    box = cur.fetchone()

    if not box:
        return "Boks ikke funnet", 404

    cur.execute("SELECT * FROM products WHERE box_id = %s", (box_id,))
    products = cur.fetchall()

    conn.close()

    return render_template("box.html", box=box, products=products)


# ------------------ ADD TO CART ------------------
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    box_id = request.form.get("box_id")

    if not box_id:
        return "Feil: ingen boks valgt", 400

    cart = session.get("cart", {})
    cart[box_id] = cart.get(box_id, 0) + 1
    session["cart"] = cart

    return redirect("/cart")


# ------------------ CART PAGE ------------------
@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    for box_id, qty in cart.items():
        cur.execute("SELECT * FROM boxes WHERE id = %s", (box_id,))
        box = cur.fetchone()
        if box:
            items.append({"box": box, "qty": qty})

    conn.close()

    return render_template("cart.html", items=items)


# ------------------ REMOVE ITEM FROM CART ------------------
@app.route("/remove_item", methods=["POST"])
def remove_item():
    box_id = request.form.get("box_id")

    cart = session.get("cart", {})

    if box_id in cart:
        del cart[box_id]

    session["cart"] = cart
    return redirect("/cart")


# ------------------ CLEAR CART ------------------
@app.route("/cart/clear")
def clear_cart():
    session["cart"] = {}
    return redirect("/cart")


# ------------------ CHECKOUT PAGE ------------------
@app.route("/checkout")
def checkout_page():
    if "user_id" not in session:
        session["login_error"] = "Du må logge inn for å bestille."
        return redirect("/")

    cart = session.get("cart", {})
    if not cart:
        return redirect("/cart")

    items = []
    total_price = 0

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    for box_id, qty in cart.items():
        cur.execute("SELECT * FROM boxes WHERE id = %s", (box_id,))
        box = cur.fetchone()
        if box:
            price = 299  # fixed price for now
            total_price += price * qty
            items.append({"box": box, "qty": qty, "price": price})

    conn.close()

    return render_template("checkout.html", items=items, total=total_price)


# ------------------ CHECKOUT SUBMIT ------------------
@app.route("/checkout/submit", methods=["POST"])
def checkout_submit():

    if "user_id" not in session:
        return redirect("/")

    bruker_id = session["user_id"]
    address = request.form["address"]
    phone = request.form["phone"]
    note = request.form.get("note", "")

    cart = session.get("cart", {})

    if not cart:
        return redirect("/cart")

    conn = get_db_connection()
    cur = conn.cursor()

    # Генеруємо унікальний ID замовлення
    bestilling_id = datetime.now().strftime("ORD%Y%m%d%H%M%S")

    # Додаємо рядки замовлення
    for box_id, qty in cart.items():
        cur.execute("""
            INSERT INTO bestillinger 
            (bestilling_id, bruker_id, dato, status, boks_id, antall)
            VALUES (%s, %s, NOW(), %s, %s, %s)
        """, (bestilling_id, bruker_id, "Mottatt", box_id, qty))

    conn.commit()
    conn.close()

    session["cart"] = {}  # Очистити корзину

    return render_template("thanks.html", order_id=bestilling_id)



# ------------------ REGISTER ------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        passord = request.form["passord"]

        hashed = generate_password_hash(passord)

        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO brukere (navn, epost, passord_hash) VALUES (%s, %s, %s)",
                (navn, epost, hashed)
            )

            conn.commit()
            conn.close()

            return redirect("/")

        except mysql.connector.errors.IntegrityError:
            session["register_error"] = "Denne e-posten er allerede registrert."
            return redirect("/register")

    return render_template("register.html")


# ------------------ LOGIN ------------------
@app.route("/login", methods=["POST"])
def login():
    epost = request.form["epost"]
    passord = request.form["passord"]

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM brukere WHERE epost = %s", (epost,))
    user = cur.fetchone()
    conn.close()

    if user and check_password_hash(user["passord_hash"], passord):
        session["user_id"] = user["id"]
        session["user_name"] = user["navn"]
        session["login_error"] = None
        return redirect("/account")

    session["login_error"] = "Feil e-post eller passord"
    return redirect("/")


# ------------------ LOGOUT ------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ------------------ ACCOUNT PAGE ------------------
@app.route("/account")
def account():
    if "user_id" not in session:
        return redirect("/")

    bruker_id = session["user_id"]

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    # Перевірка що користувач існує
    cur.execute("SELECT * FROM brukere WHERE id = %s", (bruker_id,))
    bruker = cur.fetchone()

    if not bruker:
        session.clear()
        return redirect("/")

    # Завантажити замовлення
    cur.execute("""
        SELECT bestilling_id, dato, status, SUM(antall) AS total_items
        FROM bestillinger
        WHERE bruker_id = %s
        GROUP BY bestilling_id, dato, status
        ORDER BY dato DESC
    """, (bruker_id,))
    orders = cur.fetchall()

    conn.close()

    return render_template("account.html", bruker=bruker, orders=orders)



# ------------------ RUN ------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
