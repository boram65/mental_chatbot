from flask import Flask
from flask import request
from flask_restx import Api, Resource
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import json
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

def get_dataset():
    df = pd.read_csv('wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()


        
@api.route('/<input>')
class chatbot(Resource):
    def res(self, input):
        embedding = model.encode(input)

        df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
        answer = df.loc[df['distance'].idxmax()]

        return {"res":answer['챗봇']}



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
