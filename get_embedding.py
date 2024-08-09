import pandas as pd
import openai
from openai.embeddings_utils import get_embedding

openai.api_key = "your-api-key"

#function transforms the values of column from text into embeddings
def hashable_column(column_value, column_name):
    if isinstance(column_value, dict):
        hashable_items = []
        
        for key, value in column_value.items():
            if key == column_name:
                # Convert 'Content' value to embedding
                value = get_embedding(value, engine="text-embedding-ada-002")
            elif isinstance(value, dict):
                value = hashable_column(value)
            elif isinstance(value, list):
                print("Unhashable list value at key:", key, "with value:", value)
            elif isinstance(value, str):
                value = value.replace("\n", " ")
            hashable_items.append((key, value))
        return tuple(sorted(hashable_items))
    else:
        if isinstance(column_value, str):
            return get_embedding(column_value, engine="text-embedding-ada-002")
        else:
            return column_value

def get_data():
    faqs = pd.read_csv("FAQs.csv", sep = ";")
    faqs['FAQ_emb'] = faqs['FAQ'].apply(lambda x: hashable_column(x, 'FAQ'))
    faqs.to_csv("faqs_emb.csv", index=False)
    return faqs

if __name__ == '__main__':
    get_data()
    #print(get_answer_from_input(input(), read_data()))