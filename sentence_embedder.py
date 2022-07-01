import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

print('done')

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" 
embed_model = hub.load(module_url)

print('done')