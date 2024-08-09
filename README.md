# FAQ-answer-with-embeddings

## Project Description

**FAQ-answer-with-embeddings** is a tool that transforms Frequently Asked Questions (FAQs) into embeddings using the `get_embedding.py` script. By leveraging embedding algorithms, the tool processes user input, converts it into embeddings, calculates the embedding distances, and returns the most appropriate response using the `main.py` script. This project is particularly useful for automating the process of finding relevant answers to user queries by utilizing the power of embeddings.

## Installation

To install and set up the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/FAQ-answer-with-embeddings.git
   cd FAQ-answer-with-embeddings
2. **Install Dependencies**:

    The project includes a requirements.txt file. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
## Turning your FAQs into embeddings

1. **Prepare your FAQs**:

    Ensure your FAQs are stored in a CSV file (e.g., FAQs.csv).

2. **Generate Embeddings**:

    Run the get_embedding.py script to convert your FAQs into embeddings:
    ```bash
    python get_embedding.py
This will output a file (e.g., faqs_emb.csv) containing the embeddings for your FAQs.
## Finding the Most Appropriate Response
1. **Run the Main Script**:
Use the main.py script to input a question and receive the most relevant FAQ and answer based on embedding distance:
    ```bash
    python main.py
After running the script, input your question, and the script will output the corresponding FAQ and its answer.
## Example
Your FAQ📝:
I have Celiac, do you have anything for me?

Initial FAQ: Do you have any gluten-free options?

Answer: Yes, several flavors are gluten-free, and we also offer gluten-free cones and toppings.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to submit pull requests or open issues on the GitHub repository.

## Contact Information
If you have any questions, suggestions, or feedback, please feel free to reach out:

Email: kristina.barabashova1@gmail.com

GitHub: krisbara
