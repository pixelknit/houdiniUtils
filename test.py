from mlx_lm import load, generate

model, tokenizer = load("mistralai/Mistral-7B-v0.1")

running = True

while(running):
    usr_input = input("AI how can I help you?: ")
    response = generate(model, tokenizer, max_tokens=80, prompt=usr_input, verbose=True)

    exit_state = input("Would to like to aks me anything else?: y/n: ")

    if exit_state == "n":
        break
