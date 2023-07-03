import openai
from pydantic import BaseModel



class Document(BaseModel):
  prompt: str = ''

def inference(prompt: str) -> list:
  openai.organization = 'org-DYRwCOZ92Bsf4lIsYceu2SVQ'
  openai.api_key = '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'
  print('[PROCESANDO]'.center, '_')

  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """Eres un profeso de programacion para ninios de 5 anios, geneera un ecplicacion para el tema que te proporcioens
          E.G: Programacion
           -Es como armar un rompecabeza donde cada pieza forma el sistema completo"""},
    {"role": "user", "content": prompt}
  ]
  )

  content = completion.choices[0].message.content
  total_tokens = completion.usage.total_tokens
  print('[SE TERMINO DE PROCESAR]'.center, '_')
  return [content, total_tokens]
