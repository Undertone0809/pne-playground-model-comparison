from dotenv import load_dotenv
from flask import Flask, jsonify, request
from promptulate.llms import ChatOpenAI, ErnieBot

load_dotenv()
app = Flask(__name__)


# Example route
@app.route("/", methods=["GET"])
def hello():
    return jsonify(message="Hello, Flask!")


@app.route("/chat/completions", methods=["POST"])
def api_completion():
    data = request.json
    if data["model"] in ["ernie-bot", "ernie-bot-turbo"]:
        llm = ErnieBot()
    else:
        llm = ChatOpenAI()

    try:
        # COMPLETION CALL
        response = llm(data["messages"][0]["content"])
    except Exception as e:
        # print the error
        print(e)

    return response


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=4000, threads=500)
