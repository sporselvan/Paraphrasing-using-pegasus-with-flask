from flask import Flask, request
from flask_restful import Resource, Api
import json

import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

class Paraphrase(Resource):
    def post(self):
        print(request.json)
        input_text = request.json['input_text']
        output_count = request.json['output_count']
        batch = tokenizer.prepare_seq2seq_batch([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
        translated = model.generate(**batch,max_length=60,num_beams=20, num_return_sequences=output_count, temperature=1.5)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return {'result':tgt_text}
        
api.add_resource(Paraphrase, '/paraphrase')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

