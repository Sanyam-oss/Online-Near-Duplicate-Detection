<div id="top"></div>
<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Duplicate Question Finder</h3>
</div>


## About The Project

![ScreenShot](https://github.com/Sanyam-oss/Online-Near-Duplicate-Detection/blob/main/Images/full.png)


Designed binary classification model, which given two questions, predicts whether they are semantically equivalent or not and then tag them as duplicates or non-duplicates respectively. Used Streamlit application to create a minimal ui for the same hosted it on a local server. 

Two questions can be said as duplicates if they can be adequatily answered by the exact same answer. 

### Dataset : `Quora question dataset`

Was able to achieve an accuracy of 82.28% using some featuring engineering(length based features, character based and word based distance measures, fuzzy features), Universal Sentence Encoder(USE) to generate questions embeddings and sklearn Random forest model.

The key feature of Universal Sentence Encoder(USE) is that we can use it for Multi-task learning. And since in quora dataset the questions belonged to a wide range of topic it was a good choice. 

![ScreenShot](https://github.com/Sanyam-oss/Online-Near-Duplicate-Detection/blob/main/Images/flow.png)


### Built With

* [Python](https://www.python.org/)
* [Tensorlfow](https://www.tensorflow.org/)
* [NLTK](https://www.nltk.org/)
* [Streamlit](https://streamlit.io/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Few more examples

![ScreenShot](https://github.com/Sanyam-oss/Online-Near-Duplicate-Detection/blob/main/Images/non-duplicate.png)
![ScreenShot](https://github.com/Sanyam-oss/Online-Near-Duplicate-Detection/blob/main/Images/duplicate.png)


### Future Work Inspirations

* Designing an online model for the same. Given a query of a questions find the sementically similar questions in our existing database.


### Acknowledgment

Kaggle Dataset : https://www.kaggle.com/competitions/quora-question-pairs/
Fuzzy features : https://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
Sentence Embeddings : https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/
Nice Article : https://medium.springboard.com/identifying-duplicate-questions-a-machine-learning-case-study-37117723844
Streamlit Resouce : https://towardsdatascience.com/streamlit-hands-on-from-zero-to-your-first-awesome-web-app-2c28f9f4e214
