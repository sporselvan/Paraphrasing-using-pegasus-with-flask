# Paraphrasing-using-pegasus-with-flask
This repository includes information about implementing paraphrasing using pegasus ml pre-trained model.

Framework:
   Flask
Required libraries:
   torch, torchvision, transformers, sentence-splitter,SentencePiece

This POST method takes two params. 1) input_text 2) output_count
  input_text = used to generate paraphrasing.
  output_count = output count . 
     for example 10 : API generates 10 paraphrased output.
     
Sample json payload:
   {
    "input_text":"you know it's cheating",
    "output_count":10,
    "beam_count":20
   }
   
