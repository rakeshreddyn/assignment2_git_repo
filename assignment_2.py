import random
import json
from flask import Flask, jsonify, request


server_port=5000
app = Flask(__name__)

random_jokes = ["Why don't eggs tell jokes? Because they might crack up!",
        "What did one wall say to the other wall? I will meet you at the corner!",
        "Why don't scientists trust atoms anymore? Because they make up everything!",
        "How does a vampire start a letter? Tomb it may concern.",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a snowman with a six-pack? An abdominal snowman!",
        "How do you organize a space party? You planet!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "What did the big flower say to the little flower? Hi, bud!",
        "How does a computer catch a cold? It gets a byte!"]

@app.route("/")
def index ():
    return (json.dumps(random_jokes))


@app.route("/random_jokes", methods=['GET'])
def get_jokes():
    jokes_num = request.args.get('num', default=1, type=int)
    jokes= random.sample(random_jokes, jokes_num)
    return jsonify(jokes)


if __name__ == '__main__':
    app.run('0.0.0.0', port=server_port)
