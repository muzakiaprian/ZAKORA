from flask import Flask, render_template, abort, redirect, url_for

app = Flask(__name__)

# Username yang sudah terdaftar
TERDAFTAR = ["zaki", "bondan"]

# Data produk
PRODUK = {
    1: {"id": 1, "nama": "Buku Catatan", "harga": 15000, "stok": 10},
    2: {"id": 2, "nama": "Pulpen Gel Hitam", "harga": 8000, "stok": 3},
    3: {"id": 3, "nama": "Tas Kuliah", "harga": 125000, "stok": 0},
    4: {"id": 4, "nama": "Flashdisk 32GB", "harga": 65000, "stok": 8}
}


# BERANDA
@app.route("/")
def beranda():
    return render_template("index.html")


# TENTANG
@app.route("/tentang")
def tentang():
    return render_template("tentang.html")


# PRODUK
@app.route("/produk")
def produk():
    daftar_produk = list(PRODUK.values())
    return render_template("produk.html", produk=daftar_produk)


# KONTAK
@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


# CEK USERNAME
@app.route("/cek/<username>")
def cek_username(username):
    u = username.lower()
    valid = len(u) >= 4
    tersedia = valid and u not in TERDAFTAR

    status = 200 if valid else 400

    return render_template(
        "cek.html",
        username=u,
        valid=valid,
        tersedia=tersedia
    ), status


# PROFIL USER
@app.route("/user/<username>")
def profil_user(username):
    username = username.lower()

    if len(username) < 4:
        return "Username minimal 4 karakter", 400

    return render_template("user.html", username=username)


# DETAIL PRODUK
@app.route("/produk/<int:id>")
def detail_produk(id):
    p = PRODUK.get(id)

    if p is None:
        abort(404)

    return render_template("detail_produk.html", p=p)


# REDIRECT
@app.route("/home")
def home_lama():
    return redirect(url_for("beranda"))


# CUSTOM ERROR 404
@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)