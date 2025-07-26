from anthropic import Anthropic

print("Anthropic module installed successfully!")


client = Anthropic(api_key="https://api.anthropic.com/v1/organizations/api_keys/{api_key_id}")


def ask_claude(prompt):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
answer = ask_claude("What is quantum computing?")
print(answer)
