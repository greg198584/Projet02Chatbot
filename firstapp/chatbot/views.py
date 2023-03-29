from nltk.tokenize import word_tokenize
import numpy as np

from django.shortcuts import render

import fasttext

fasttext_model = fasttext.load_model('fasttext_french.bin')


pairs = [    ['Bonjour', ['Bonjour ! Comment puis-je vous aider ?']],
    ['Comment ça va ?', ['Je suis un programme, je n\'ai pas d\'émotions, mais merci de demander ! Et vous ?']],
    ['Quel est ton nom ?', ['Je m\'appelle Chatbot. Et vous ?']],
    ['Quel est le sens de la vie ?', ['C\'est une question complexe, je ne suis pas sûr d\'avoir la réponse. Mais certains pensent que c\'est 42.']],
    ['Comment vas-tu ?', ['Je vais bien, merci ! Et vous ?']],
    ['Quelle est la météo aujourd\'hui ?', ['Je suis désolé, je ne peux pas vous fournir la météo actuelle.']],
    ['Comment puis-je vous aider ?', ['Je peux répondre à vos questions ou vous donner des informations sur différents sujets.']],
    ['Qui est le président de la France ?', ['Le président de la France est actuellement Emmanuel Macron.']],
    ['Quel est le plus grand pays du monde ?', ['Le plus grand pays du monde est la Russie.']],
]

# chat = Chat(pairs)

def preprocess_sentence(sentence):
    tokens = word_tokenize(sentence.lower())
    return tokens

def find_best_match(input_question, pairs):
    preprocessed_input = preprocess_sentence(input_question)
    similarities = []

    for pair in pairs:
        preprocessed_pair = preprocess_sentence(pair[0])
        similarity = np.dot(fasttext_model.get_sentence_vector(' '.join(preprocessed_input)), fasttext_model.get_sentence_vector(' '.join(preprocessed_pair))) / (np.linalg.norm(fasttext_model.get_sentence_vector(' '.join(preprocessed_input))) * np.linalg.norm(fasttext_model.get_sentence_vector(' '.join(preprocessed_pair))))
        similarities.append(similarity)

    max_index = np.argmax(similarities)
    return pairs[max_index], similarities[max_index]


def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        threshold = 0.5  # Vous pouvez ajuster ce seuil pour contrôler la tolérance aux questions mal comprises

        best_match, similarity = find_best_match(question, pairs)

        if similarity > threshold:
            response = best_match[1][0]
        else:
            response = "Désolé, je ne comprends pas votre question. Pouvez-vous reformuler ?"

        messages = [{'sender': 'user', 'text': question}, {'sender': 'bot', 'text': response}]
        return render(request, 'chatbot.html', {'messages': messages})
    else:
        return render(request, 'chatbot.html')
