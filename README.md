# Instagram-Spam-Detection-
This project aims to build an AI model capable of detecting spam comments on Instagram using advanced Natural Language Processing (NLP) techniques. Due to the lack of labeled Instagram spam datasets, data is scraped using the Instagram API to gather unlabelled comments. For training, Kaggle’s YouTube Spam Collection Dataset is used, as it contains a variety of labeled spam comments. The project incorporates methods like keyword identification, N-Grams for word weightage, and distance-based algorithms such as cosine similarity to match spam patterns. Additionally, pre-trained models like ALBERT and BERT are employed to capture sentence context, improving the accuracy of spam detection. The goal is to create a robust system that differentiates spam comments from legitimate ones, enhancing social media authenticity and user experience.

Key Data:

- YouTube Spam Collection Dataset (Kaggle): Used to train the model for spam detection.
- Instagram API: Utilized to scrape unlabelled comments from Instagram for testing.
- Techniques: N-Grams, Cosine Similarity, BERT, and ALBERT models for context-aware spam classification.
