from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "kdkldjkjfkldjfkljdskl;jioerut68589dhfk"


@app.route('/')
def home():

    if 'num_of_visits' in session:
        print('key exists!')
        session['num_of_visits'] += 1
        print(session['num_of_visits'])
    else:
        print("key 'num_of_visits' does NOT exist")
        session['num_of_visits'] = 1

    if session['num_of_visits'] == 1:
        word = "time"
    else:
        word = "times"
    return render_template('index.html', word=word)


@app.route('/destroy_session')
def reset():
    if 'num_of_visits' in session:
        session.clear()
    else:
        print("yo")

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
