from flask import Flask, make_response, request
import io
import csv

app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>APi for showing crossing and not crossing with the help of trained model's csv file</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/transform', methods=["POST"])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    print(csv_input)
    for label in csv_input:
        
        if label == '0':
            print("not crossing")
        else :
            print("crossing")

    return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000, debug=True)