from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__) #tworzenie instancji klasy Flask i przypisanie jej do zmiennej app
#ustawianie konfiguracji serwera poczty
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #ustawienie serwera SMPT Gmail
app.config['MAIL_PORT'] = 465 #ustawienie portu na '465'
app.config['MAIL_USERNAME'] = 'user@gmail.com' #adres mailowy
app.config['MAIL_PASSWORD'] = 'password' #hasło uwierzytelniające przypisane do aplikacji
app.config['MAIL_USE_TLS'] = False #aplikacja nie korzysta z protokołu TLS
app.config['MAIL_USE_SSL'] = True #aplikacja korzysta z protokolu SSL
mail = Mail(app) #tworzenie instancji klasy Mail

@app.route('/home', methods=['GET', 'POST']) #ścieżka obsługuje żadanie GET i POST
@app.route('/', methods=['GET', 'POST']) #ścieżka obsługuje żadanie GET i POST
def home():
    if request.method == 'POST': #warunek po wciśnięciu przycisku
        msg = Message(request.form['title'], sender='noreply@demo.com', #pobranie tytułu maila z interfejsu
                      recipients=['user@gmail.com']) #obiorca maila
        msg.body = request.form['message'] #pobranie treści maila z interfejsu
        mail.send(msg) #wysłanie maila
        return 'Email sent' #wiadomość potwierdzająca wysłanie maila
    return render_template('index.html') #wyświetlanie szablonu index.html

if __name__ == '__main__':
    app.run(debug = True)