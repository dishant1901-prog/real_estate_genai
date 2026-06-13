# 🏠 Real Estate Research Tool using RAG

An AI-powered real estate research assistant that allows users to analyze information from web URLs and ask natural language questions based on the extracted content. The application leverages Retrieval-Augmented Generation (RAG) to provide accurate, source-backed answers using modern LLM technologies.



## 🚀 Features

* 🌐 Extract information from user-provided URLs
* 📄 Automatically load and process webpage content
* ✂️ Split documents into semantic chunks for efficient retrieval
* 🧠 Generate embeddings using Hugging Face Sentence Transformers
* 🗂️ Store embeddings in ChromaDB vector database
* 🔍 Retrieve relevant context based on user queries
* 🤖 Generate answers using Groq's Llama 3.3 model
* 📌 Display the original sources used to answer the question
* 💻 Interactive Streamlit-based user interface


## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **ChromaDB**
* **Groq (Llama 3.3 70B)**
* **Hugging Face Embeddings**
* **Sentence Transformers**
* **Unstructured URL Loader**


## ⚙️ How It Works

1. Enter one or more URLs containing relevant information.
2. Click **Process URLs**.
3. The application:

   * Loads webpage content
   * Splits the content into chunks
   * Generates embeddings
   * Stores them in ChromaDB
4. Ask questions related to the processed URLs.
5. Receive accurate answers along with the supporting sources.


## 📂 Project Structure


real_estate_genai/
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/


## 📥 Installation

### Clone the Repository


git clone https://github.com/dishant1901-prog/real_estate_genai.git
cd real_estate_genai


### Install Dependencies


pip install -r requirements.txt


### Configure Environment Variables

Create a `.env` file in the project root:


GROQ_API_KEY=your_groq_api_key


### Run the Application


streamlit run app.py


The application will be available at:


http://localhost:8501



## 💡 Example Usage

### Input URLs


https://www.freddiemac.com/pmms
https://www.freddiemac.com/pmms/pmms-archives


### Example Question

Tell me what was the 30-year fixed mortgage rate along with the date?


### Example Response


The 30-year fixed-rate mortgage rate was 6.48% as of June 4, 2026.


### Sources


https://www.freddiemac.com/pmms
https://www.freddiemac.com/pmms/pmms-archives




## 🔒 Security

API keys and sensitive credentials are not included in this repository.

Please use environment variables (`.env`) to securely manage secrets.



## 📚 Key Learnings

Through this project, I gained hands-on experience with:

* Retrieval-Augmented Generation (RAG)
* Vector databases and semantic search
* LangChain's modern architecture
* Streamlit application development
* Integrating Groq-hosted LLMs
* Building end-to-end Generative AI applications


## 🔮 Future Improvements

* Support PDF and document uploads
* Add conversational memory
* Deploy using Streamlit Cloud, Render, or Hugging Face Spaces
* Integrate additional LLM providers
* Improve UI/UX and error handling



## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.



## ⭐ If you found this project interesting, please consider giving it a star!

### Connect with Me

If you'd like to discuss this project or collaborate on AI projects, feel free to connect with me on LinkedIn.

Happy Coding! 🚀
