from flask import Flask, render_template, request, redirect, url_for
import persistence


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_list():
    if request.method == 'GET':
        list_of_dict = persistence.import_from_file()
        headers = persistence.import_headers()

        return render_template("q_list.html", list_of_dict=list_of_dict, headers=headers)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
