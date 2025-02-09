from llm_api.app.settings import settings

from llm_api.interfaces.llm_interfaces.llm_client_interface import LlmClientInterface
from llm_api.interfaces.llm_interfaces.llm_interface import LlmInterface


class LlmService(LlmInterface):
	def __init__(self, client: LlmClientInterface) -> None:
		self.client = client
		self.response_structure = " Also structure it with the title under 'title:' \
			and the body under 'body:' (exactly like title: and body:, dont add anything):"

	async def create_completion(self, prompt: str) -> str:
		response = await self.client.get_client().chat.completions.create(
			model=settings.llm_model,
			messages=[
				{"role": "user", "content": f"{prompt} {self.response_structure}"}
			],
			store=True,
		)

		return response.choices[0].message.content

	def grab_title_and_body(self, generated_text: str) -> dict:
		"""
		Grabs the title and body from the generated text.
		"""

		if "title:" in generated_text and "body:" in generated_text:
			parts = generated_text.split("body:", 1)
			title = parts[0].replace("title:", "").strip()
			body = parts[1].strip()

			return {"title": title, "body": body}
		else:
			return {"title": "", "body": generated_text}
