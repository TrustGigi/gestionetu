import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'ta_cle_secrete_change_moi'

# Base SQLite - fichier créé automatiquement sur Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'gestion.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    # Table users pour register / login
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        email TEXT UNIQUE,
        password TEXT
    )''')
    # Table etudiant pour add / update / delete
    cur.execute('''CREATE TABLE IF NOT EXISTS etudiant (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        adresse TEXT,
        nationalite TEXT,
        tel TEXT,
        sexe TEXT,
        age TEXT
    )''')
    conn.commit()
    conn.close()

# Créer les tables au démarrage
init_db()

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO users(nom,prenom,email,password) VALUES(?,?,?,?)", (nom,prenom,email,password))
            conn.commit()
            conn.close()
            flash("Inscription avec succès", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Echec de l'inscription: {e}", "danger")
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password))
        user = cur.fetchone()
        conn.close()
        if user:
            session['username'] = user['email']
            session['user_id'] = user['id']
            flash("Connexion avec succès", "success")
            return redirect(url_for('etudiant'))
        else:
            flash("Email ou mot de passe incorrect", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/etudiant')
def etudiant():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM etudiant")
    etudiants = cur.fetchall()
    conn.close()
    return render_template('etudiant.html', etudiants=etudiants)

@app.route('/add', methods=['POST'])
def add():
    if 'username' not in session:
        return redirect(url_for('login'))
    try:
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        adresse = request.form.get('adresse')
        nationalite = request.form.get('nationalite')
        tel = request.form.get('tel')
        sexe = request.form.get('sexe')
        age = request.form.get('age')
        if not nationalite:
            flash("Vous selectionner la nationalite", "danger")
            return redirect(url_for('etudiant'))
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO etudiant(nom,prenom,adresse,nationalite,tel,sexe,age) VALUES(?,?,?,?,?,?,?)", (nom,prenom,adresse,nationalite,tel,sexe,age))
        conn.commit()
        conn.close()
        flash("Enregistrement avec succes", "success")
        return redirect(url_for('etudiant'))
    except Exception as e:
        flash(f"Echec d'enregistrement: {e}", "danger")
        return redirect(url_for('etudiant'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    try:
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        adresse = request.form.get('adresse')
        nationalite = request.form.get('nationalite')
        tel = request.form.get('tel')
        sexe = request.form.get('sexe')
        age = request.form.get('age')
        if not nationalite:
            flash("Vous selectionner la nationalite", "danger")
            return redirect(url_for('etudiant'))
        conn = get_db()
        cur = conn.cursor()
        cur.execute("UPDATE etudiant SET nom=?,prenom=?,adresse=?,nationalite=?,tel=?,sexe=?,age=? WHERE id=?", (nom,prenom,adresse,nationalite,tel,sexe,age,id))
        conn.commit()
        conn.close()
        flash("Modification avec succes", "success")
        return redirect(url_for('etudiant'))
    except Exception as e:
        flash(f"Echec de la modification: {e}", "danger")
        return redirect(url_for('etudiant'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM etudiant WHERE id=?", (id,))
        conn.commit()
        conn.close()
        flash("Suppression avec succes", "success")
        return redirect(url_for('etudiant'))
    except Exception as e:
        flash(f"Echec de la suppression: {e}", "danger")
        return redirect(url_for('etudiant'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
