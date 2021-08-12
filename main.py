import importlib
import json

def map_to_step(config):
  transformer = config.get("transformer")
  module = importlib.import_module(f"transformers.{transformer}")
  class_ = getattr(module, transformer)
  return class_(config)

def main():
  with open('config.json') as json_file:
    config = json.load(json_file)

  steps = []
  for step in config.get("steps"):
    step = map_to_step(step)
    steps.append(step)

  for step in steps:
    step.run()

main()