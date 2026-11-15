from flask import Flask,request,render_template,url_for,flash,redirect,session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash,check_password_hash
from config import Config
app=Flask(__name__)
app.config.from_object(Config)
mysql=MySQL(app)
@app.route("/")
def accueil():

    return redirect(url_for('login'))
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form.get("username")
        email=request.form.get("email")
        password=generate_password_hash(request.form.get("password"))
        try:
            cur=mysql.connection.cursor()
            cur.execute("INSERT into users (username,email,password)VALUES(%s,%s,%s)",(username,email,password))
            mysql.connection.commit()
            flash("Inscription réussie","warning")
            return redirect(url_for('login'))
        except Exception as e:
            mysql.connection.rollback()
            flash(f"Email utilisé, veuillez entrer un autre email:{e}","danger")
            return redirect(url_for('register'))
            cur.close()
    return render_template('register.html')
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get("email") 
        password=request.form.get("password") 
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(email,)) 
        user=cur.fetchone()
        cur.close()
        if user and check_password_hash(user[3],password):
            session['username']=user[1]
            return redirect(url_for('etudiant'))
        flash("Votre email ou le mot de pass est incorrert, veuillez contact l'administrateur","danger")
        return redirect(url_for('login'))
    return render_template('login.html')  
@app.route("/etudiant")
def etudiant():
    if 'username' not in session:
        return redirect(url_for('login'))
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM etudiant")
    etudiant=cur.fetchall()
    return render_template('etudiant.html',etudiant=etudiant)
@app.route("/add",methods=['POST'])
def add():
    if 'username' not in session:
        return redirect(url_for('login'))
    try:
        nom=request.form.get("nom")
        prenom=request.form.get("prenom")
        adresse=request.form.get("adresse")
        nationalite=request.form.get("nationalite")
        tel=request.form.get("tel")
        sexe=request.form.get("sexe")
        age=request.form.get("age")
        if not nationalite:
            flash("Vous sélectionnez la nationalité","danger")
            return redirect(url_for('etudiant'))
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO etudiant(nom,prenom,adresse,nationalite,tel,sexe,age)VALUES(%s,%s,%s,%s,%s,%s,%s)",(nom,prenom,adresse,nationalite,tel,sexe,age))
        mysql.connection.commit()
        flash("Enregistrement avec succès","success")
        return redirect(url_for('etudiant'))
        cur.close()
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Echec d'enregistrement:{e}","danger")
        return redirect(url_for('etudiant'))

#Editer
@app.route("/update/<int:id>",methods=['POST'])
def update(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    try:
        nom=request.form.get("nom")
        prenom=request.form.get("prenom")
        adresse=request.form.get("adresse")
        nationalite=request.form.get("nationalite")
        tel=request.form.get("tel")
        sexe=request.form.get("sexe")
        age=request.form.get("age")
        if not nationalite:
            flash("Vous sélectionnez la nationalité","danger")
            return redirect(url_for('etudiant'))
        cur=mysql.connection.cursor()
        cur.execute("UPDATE etudiant SET nom=%s,prenom=%s,adresse=%s,nationalite=%s,tel=%s,sexe=%s,age=%s WHERE id=%s",(nom,prenom,adresse,nationalite,tel,sexe,age,id))
        mysql.connection.commit()
        flash("Modification avec succès","success")
        return redirect(url_for('etudiant'))
        cur.close()
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Echec de la modification:{e}","danger")
        return redirect(url_for('etudiant')) 

@app.route("/delete/<int:id>",methods=['POST'])
def delete(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    try:
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM etudiant WHERE id=%s",(id,))
        mysql.connection.commit()
        flash("Suppression avec succès","success")
        return redirect(url_for('etudiant'))
        cur.close()
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Echec de la suppression:{e}","danger")
        return redirect(url_for('etudiant'))         
@app.route("/logout")
def logout():
   session.clear()
   return redirect(url_for('login'))  
    #return render_template('login.html')                   

if __name__=='__main__':
    app.run(debug=True)

