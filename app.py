from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/english')
def english_index():
  conn = sqlite3.connect("dictionary.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM english")
  words = cursor.fetchall()
  conn.close()
  return render_template("english/index.html", words=words)

@app.route("/english/add", methods=["GET", "POST"])
def add_english_word():
  if request.method == "POST":
    word = request.form['word']
    definition = request.form['definition']
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO english (word, definition) VALUES (?, ?)", (word, definition))
    conn.commit()
    conn.close()
    return redirect(url_for("english_index"))
  return render_template('english/add.html')

@app.route('/english/delete/<int:word_id>', methods=["POST"])
def delete_english_word(word_id):
  conn = sqlite3.connect("dictionary.db")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM english WHERE id = ? ", (word_id, ))
  conn.commit()
  conn.close()
  return redirect(url_for('english_index'))



@app.route('/terms')
def terms_index():
  conn = sqlite3.connect("dictionary.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM terms")
  terms = cursor.fetchall()
  conn.close()
  return render_template("terms/index.html", terms=terms)

@app.route("/terms/add", methods=["GET", "POST"])
def add_term():
  if request.method == "POST":
    word = request.form['word']
    definition = request.form['definition']
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO terms (word, definition) VALUES (?, ?)", (word, definition))
    conn.commit()
    conn.close()
    return redirect(url_for("terms_index"))
  return render_template('terms/add.html')

@app.route('/terms/delete/<int:term_id>', methods=["POST"])
def delete_term(term_id):
  conn = sqlite3.connect("dictionary.db")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM terms WHERE id = ? ", (term_id, ))
  conn.commit()
  conn.close()
  return redirect(url_for('terms_index'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=5000)
