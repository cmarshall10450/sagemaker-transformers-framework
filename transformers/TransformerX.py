from transformers.BaseTransformer import BaseTransformer

class TransformerX(BaseTransformer):
  def transform(self, df):
    df["col_1"] = df["col_1"] * 2
    return df