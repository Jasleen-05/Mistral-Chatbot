# 🤖 Mistral Chatbot

A locally hosted conversational chatbot powered by the **Mistral-7B** model, fine-tuned for custom tasks. Built using Flask for the backend and vanilla HTML/CSS/JS for the frontend. No API keys or internet required after setup.

---

## 🔧 Features

- 🧠 Runs locally with your fine-tuned **Mistral 7B** model.
- ⚡ Fast, real-time responses (GPU preferred, CPU supported).
- 🌐 Clean web-based interface using Flask + JS.
- 🔐 No internet access required after setup.
- 🎨 Customizable UI with animated CSS effects.

---

## 📁 Project Structure

```
mistral-chatbot/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend HTML UI
├── static/
│ └── styles.css # CSS styling
├── requirements.txt # Dependencies
└── README.md
```

---

## 🖥️ Demo

![Chatbot Demo Screenshot]![image](https://github.com/user-attachments/assets/7cdb3e03-cd13-49f4-b1b6-fc94b063d679)


---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Jasleen-05/mistral-chatbot.git
cd mistral-chatbot
```
2. Create a Virtual Environment (optional but recommended)
```
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Linux/Mac
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Add Your Fine-tuned Model
Place your fine-tuned Mistral model in a folder like:
trained_model_mistral/
Update model_path in app.py accordingly:
```
model_path = "./trained_model_mistral"
```
5. Run the App
```
python app.py
```
Visit: http://localhost:5005

---

💡 **Example Prompt**  
**You**: What are transformers in deep learning?  
**Bot**: Transformers are a type of neural network architecture commonly used in natural language processing (NLP) tasks such as language translation...

---

### ❓ FAQs

**Q: Can I run it on CPU?**  
A: Yes, but response time will be slower. CUDA is preferred.

**Q: Do I need Hugging Face keys or internet access?**  
A: No. The model runs entirely offline after downloading.

**Q: Can I use a different Mistral variant?**  
A: Yes, as long as it's compatible with `AutoModelForCausalLM`.

---

### 🧠 Tech Stack
- **Flask** – Python backend & API  
- **Transformers** – Hugging Face library  
- **PyTorch** – For model inference  
- **HTML + CSS + JS** – Clean frontend interface  

---

📄 **License**: MIT License – free to use, modify, and distribute.

---

✨ **Author**: Made by Jasleen Kaur Matharoo  
📧 Email: [jasleen.matharoo@s.amity.edu](mailto:jasleen.matharoo@s.amity.edu)  
🌐 GitHub: [@Jasleen-05](https://github.com/Jasleen-05)

