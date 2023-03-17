

class OutputSanitizer(Tool):
    def __init__(self, openai_key: str, temperature: float = 0.7, max_tokens: int = 50):
        self.openai_key = openai_key
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.llm = LLMChain(openai_key=self.openai_key, model="text-davinci-002", max_tokens=self.max_tokens, temperature=self.temperature)
        super().__init__()

    def run(self, input: str, *args, **kwargs):
        raw_output = super().run(input, *args, **kwargs)
        sanitized_output = self.sanitize_output(raw_output)
        return sanitized_output

    def sanitize_output(self, output: str) -> str:
        prompt = f"Provide a safe and relevant alternative response for the following AI output: '{output}'"
        response = self.llm.run(prompt)
        sanitized_output = response.strip()

        if not sanitized_output:
            sanitized_output = "I'm sorry, but I cannot generate a safe response for the given output."

        return sanitized_output
