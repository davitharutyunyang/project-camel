import sys
try:
    from ollama import chat, ResponseError
except ImportError:
    print("Error: The 'ollama' library is not installed. Run 'pip install ollama'.")
    sys.exit(1)

def ask_model(model_name: str, prompt: str) -> None:
    try:
        response = chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        print(f"\n[{model_name}]: {response.message.content}")
    except ResponseError as e:
        print(f"Error: Model '{model_name}' not found. Did you run 'ollama run {model_name}'?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_selection(options_dict, category_name, fallback):
    print(f"\nChoose your {category_name} model:")
    for display_name in options_dict.keys():
        print(f"- {display_name}")
    
    choice = input("> ").strip().lower()
    # Match against display name (lowercase) or the actual model value
    for display, model_id in options_dict.items():
        if choice == display.lower() or choice == model_id.lower():
            return model_id
    
    print(f"Unknown option. Falling back to {fallback}.")
    return fallback

print(
    "Choose a model group: /code, /reasoning, /math, /Mistral "
    "(or press Enter for default llama3)"
)

model_choice = input("> ").strip().lower()
prompt = input("Ask your question: ").strip()

if not prompt:
    prompt = "Hello!"

print("\n--- Powered by Ollama ---")

if model_choice == "/code":
    code_models = {
        "DeepSeek-Coder V2": "deepseek-coder-v2",
        "Qwen2.5-Coder": "qwen2.5-coder",
        "CodeLlama 34B": "codellama:34b",
        "Kimi k2.6": "kimi-k2.6",
    }
    selected = get_selection(code_models, "coding", "deepseek-coder-v2")
    ask_model(selected, prompt)

elif model_choice == "/reasoning":
    print("Using reasoning model: qwen2.5")
    ask_model("qwen2.5", prompt)

elif model_choice == "/math":
    math_models = {
        "DeepSeek-R1": "deepseek-r1",
        "Mathstral": "mathstral",
        "Qwen2-Math": "qwen2-math",
    }
    selected = get_selection(math_models, "math", "deepseek-r1")
    ask_model(selected, prompt)

elif model_choice == "/mistral":
    mistral_models = {
        "Mixtral 8x7b": "mixtral:8x7b",
        "Mistral-large 3": "mistral-large",
        "Mistral-small 3.2": "mistral-small3.2",
        "Mistral 7B": "mistral:7b",
        "Mathstral": "mathstral",
        "Mistral-Nemo": "mistral-nemo",
        "Zephyr 141B": "zephyr:141b",
    }
    selected = get_selection(mistral_models, "Mistral", "llama3")
    ask_model(selected, prompt)

else:
    print("Using default model: llama3")
    ask_model("llama3", prompt)