from langchain.prompt_template import PromptTemplate

template = """
以下の料理のレシピを考えてください。

料理名: {dish}
"""

prompt = PromptTemplate(
    input_variables=["dish"],
    template=template,
)

result = prompt.format(dish="カレー")


print('\n####################################################')
print(result)
print('####################################################\n')

