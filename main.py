import pandas as pd
import openai
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import distances_from_embeddings

openai.api_key = "your-api-key"

def read_data():
    faqs_emb = pd.read_csv("faqs_emb.csv")
    faqs_dict = {}
    for index, row in faqs_emb.iterrows():
        FAQ = row['FAQ']
        embeddings = row['FAQ_emb']
        faqs_dict[FAQ] = ('Embeddings', embeddings)
    
    for FAQ, (embeddings, embeddings_str) in faqs_dict.items():
        # Check for empty string before converting to float
        embeddings_list = [float(value) if value.strip() else 0.0 for value in embeddings_str.strip('[]').split(',')]
        faqs_dict[FAQ] = (embeddings, embeddings_list)
    return faqs_dict

def distances_based_on_content(input_string, faqs_dict):
    input_embedding = get_embedding(input_string, engine="text-embedding-ada-002")  # Get the embedding of the user
    faq_ids = list(faqs_dict.keys()) #list of news articles
    faq_embeddings = [faqs_dict[FAQ][1] for FAQ in faq_ids]# Get the embedding of each news article

    # Calculate distances from the user to each news article
    distances = distances_from_embeddings(input_embedding, faq_embeddings, distance_metric="cosine")

    # Create a DataFrame with news IDs and corresponding distances
    df = pd.DataFrame({'FAQ': faq_ids, 'Distance': distances})
    sorted_distances = df.sort_values(by='Distance', ascending=True)
    
    return sorted_distances

def get_answer(faq_value):
    faqs_emb = pd.read_csv("faqs_emb.csv")
    result = faqs_emb[faqs_emb['FAQ'] == faq_value]['Answer']
    if not result.empty:
        return result.iloc[0]
    else:
        return "FAQ not found."

def get_answer_from_input(input_string, faqs_dict):
    df = distances_based_on_content(input_string, faqs_dict)
    faq_value = df['FAQ'].iloc[0]
    answer = get_answer(faq_value)
    print(f"Initial FAQ: {faq_value}")
    print(f"Answer: {answer}")
    return faq_value, answer

if __name__ == '__main__':
    print("Your FAQ📝:")
    get_answer_from_input(input(), read_data())