from distutils.log import debug
from flask import Flask, jsonify, request

import numpy as np
from sentence_transformers import SentenceTransformer

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

model = SentenceTransformer('cl-tohoku/bert-base-japanese-v2')

app = Flask(__name__)

@app.route('/get_sim', methods=['GET'])
def get_sim():
    sentence1 = request.args.get("sentence1")
    sentence2 = request.args.get("sentence2")
    sentences = [sentence1, sentence2]
    embeddings = model.encode(sentences)
    sim = cos_sim(embeddings[0], embeddings[1])
    return jsonify({'sim': str(sim)})

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=8080, debug=True)