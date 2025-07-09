from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# ✅ Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# ✅ Hugging Face token from environment
HF_TOKEN = os.getenv("HF_TOKEN")

# ✅ Model info
model_id = "mistralai/Mistral-7B-Instruct-v0.1"
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🖥️ Using device: {device}")

# ✅ Quantization config for 4-bit
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

# ✅ Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id, token=HF_TOKEN)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    token=HF_TOKEN,
    quantization_config=quant_config,
    device_map="auto"
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    prompt = f"[INST] {user_input} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=500,   # ✅ Up to 500 tokens
            do_sample=False,      # ✅ Faster inference
            top_p=0.95,
            temperature=0.7
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    reply = response.split("[/INST]")[-1].strip()
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5002, debug=True)