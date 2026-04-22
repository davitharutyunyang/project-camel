from ollama import chat

def ask_model(model_name: str, prompt: str) -> None:
    response = chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
    )
    
    print(response.message.content)

print(
    "Choose a model group: /code, /reasoning, /math, /Mistral "
    "(or press Enter for default llama3.3)"
)

model_choice = input("> ").strip()
print("Powered by Ollama")
prompt = input("Ask your question: ").strip()

if not prompt:
    prompt = "Hello!"

if model_choice == "/code":
    print("Choose your coding model:")
    print("DeepSeek-Coder V2, Qwen2.5-Coder, CodeLlama 34B, Kimi k2.6")
    code_choice = input("> ").strip()

    code_models = {
        "DeepSeek-Coder V2": "deepseek-coder-v2",
        "Qwen2.5-Coder": "qwen2.5-coder",
        "CodeLlama 34B": "codellama:34b",
        "Kimi k2.6": "kimi-k2.6",
    }

    selected = code_models.get(code_choice)
    if selected:
        ask_model(selected, prompt)
    else:
        print("Unknown code model option. Falling back to deepseek-coder-v2.")
        ask_model("deepseek-coder-v2", prompt)

elif model_choice == "/reasoning":
    print("Using reasoning model: qwen2.5")
    ask_model("qwen2.5", prompt)

elif model_choice == "/math":
    print("Choose your math model:")
    print("DeepSeek-R1, Mathstral, Qwen2-Math")
    math_choice = input("> ").strip()

    math_models = {
        "DeepSeek-R1": "deepseek-r1",
        "Mathstral": "mathstral",
        "Qwen2-Math": "qwen2-math",
    }

    selected = math_models.get(math_choice)
    if selected:
        ask_model(selected, prompt)
    else:
        print("Unknown math model option. Falling back to deepseek-r1.")
        ask_model("deepseek-r1", prompt)

elif model_choice == "/Mistral":
    print("Choose your Mistral model:")
    print("Mixtral 8x7b, Mistral-large 3, Mistral-small 3.2, Mistral 7B, Mathstral, Mistral-Nemo, Zephyr 141B")
    mistral_choice = input("> ").strip()

    mistral_models = {
        "Mixtral 8x7b": "mixtral:8x7b",
        "Mistral-large 3": "mistral-large-3:675b-cloud",
        "Mistral-small 3.2": "mistral-small3.2",
        "Mistral 7B": "mistral:7b",
        "Mathstral": "mathstral",
        "MathΣtral": "mathstral",
        "Mistral-Nemo": "mistral-nemo",
        "Zephyr 141B": "zephyr:141b",
        "(Mixtral 8x22b)": "zephyr:141b",
    }

    selected = mistral_models.get(mistral_choice)
    
    if selected:
        ask_model(selected, prompt)
    else:
        print("Unknown Mistral option. Falling back to llama3.3.")
        ask_model("llama3.3", prompt)

else:
    print("Using default model: llama3.3")
    ask_model("llama3.3", prompt)