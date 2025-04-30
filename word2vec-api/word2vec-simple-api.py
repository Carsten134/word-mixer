from flask import Flask, request
from flask_restful import Resource, Api
import gensim.models.keyedvectors as word2vec
from flask_cors import CORS

print("loading model")
model = word2vec.load_word2vec_format("./glove.twitter.27B.100d.txt", no_header = True)

def perfect_match(left:str, right:str, percent:float):
    vec = model.get_mean_vector([left, right], [(1-percent), percent], pre_normalize=False, post_normalize=False)
    return model.most_similar([vec], [("none", 0)], topn = 10)[1:]

class PerfectMatch(Resource):
    def get(self):
        left = request.args.get("left")
        right = request.args.get("right")
        percent = request.args.get("percent")
        return perfect_match(left, right, float(percent))
    

if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    path = "/word2vec"
    api.add_resource(PerfectMatch, path + "/perfect-match")
    app.run("localhost", 5000)

    