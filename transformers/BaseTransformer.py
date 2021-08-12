import pandas as pd

class BaseTransformer():
  def __init__(self, config):
    self.config(config)

  def transform(self, df):
    pass

  def config(self, config):
    self.input = config.get("input", {})
    self.output = config.get("output", {})

  def load_input(self):
    return pd.read_csv(self.input.get("filepath"))

  def write_output(self, df):
    df.to_csv(self.output.get("filepath"))
    
  def run(self):
    df = self.load_input()
    transformed_result = self.transform(df)
    self.write_output(transformed_result)