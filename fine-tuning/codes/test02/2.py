import os
import openai

openai.api_key = '****'

file_id = openai.File.create(
  file = open("training_examples.jsonl", "rb"),
  purpose = 'fine-tune'
).id

job = openai.FineTuningJob.create(training_file = file_id, model = "gpt-3.5-turbo", suffix = "test02")
job_id = job.id

openai.FineTuningJob.list_events(id = job_id, limit = 10)