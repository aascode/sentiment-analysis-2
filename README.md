# **Multi-modal Sentiment Analyzer**

Multi-class LSTM neural network model (Long-Short-Term-Memory with softmax output).
Built with Tensorflow 2.x.

---

## Datasets:

Trained with the preprocessed-concatenation of seven datasets

1. Emobank
2. ISEAR
3. Sentiment140 (1.6+ million tweets)
4. NRC Emotion Intensity Lexicon v1
5. NRC Emotion Lexicon Word-level v0.92
6. NRC Hashtag Emotion Lexicon v0.2
7. NRC VAD Lexicon

## NLP tools

- Stanza (lemmatization and polarities)
- SpaCy (training : text categorization)
- Flair (Polarities)
- TextBlob (only Subjectivity)
- NLTK (words, wordnet, stopwords, VADER)

## **Categories distribution**

Words play a central role in language and thought.
There are three main dimensions of word meaning shown by analysis studies:

- **Valence:** postive / negative or pleasure / displesure
- **Arousal:** excited / calm or active / passive
- **Dominance:** powerful / weak or have control / no have control

As represented as dimensions:

- **x** **⟷** **Valence**
- **Y** **⟷** **Arousal**
- **Z** **⟷** **Dominance**

Through these three-dimensional categories was compared the **Wheel of emotions** by Robert Plutchik.
To later be resolved with the categories that were previously deliberated by Sidejar ©.
In this way, a better distribution was achieved at the time of preprocessing the data, where certain categories are merely
redirected to the Speech Recognition stage.

![categories_explaination](https://github.com/Y4rd13/sentiment-analysis/blob/master/categories.png)

---

## **Processing datasets**

![processing_chartflow](https://github.com/Y4rd13/sentiment-analysis/blob/master/processing%20chartflow.png)

---

## Observations

- flair can complement stanza values
- if stanza value == 0, then assign the prediction from flair
- flair should be a different tokens by predicction
- e.g.: does not handles pressure
- stanza == 0
- flair == -1
- flair == 0.98 == > -0.98 --> will mean the label {does not handles pressure}
