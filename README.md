# Paraphrasing-using-pegasus-with-flask
This repository includes information about implementing paraphrasing using pegasus ml pre-trained model.

Framework:
   Flask
Required libraries:
   flask_restful, flask_cors, torch, torchvision, transformers, sentence-splitter, SentencePiece

This POST method takes two params. 1) input_text 2) output_count
  input_text = used to generate paraphrasing.
  output_count = output count . 
     for example 10 : API generates 10 paraphrased output.
     
Sample json payload:
   {
    "input_text":"I wanted to follow-up about your interest in Digital-Art",
    "output_count":10
   }
   
