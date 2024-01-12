import os
import openai
import json
from pprint import pprint

# APIキーの設定
with open("apikey.txt") as f:
    key = f.read()
    os.environ["OPENAI_API_KEY"] = str(key)
    openai.api_key = os.environ["OPENAI_API_KEY"]

# 任意の関数を定義
def get_current_weather(location, unit="celsius"):
    weather_info = {
        "location": location,
        "temperature": "25",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

# LLMが使用できる関数一覧を定義
functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. Tokyo",
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"]
                },
            },
            "required": ["location"],
        },
    }
]

# ChatCompletionAPIの呼び出し１
messages = [
    {"role": "user", "content": "What's the weather like in Tokyo?"}
]

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,

)


print('\n####################################################\n')
print(type(response))
pprint(vars(response))
print()
print(response.choices[0].message)
print()
pprint(response.choices[0].message.content)
pprint(response.choices[0].message.function_call)
pprint(response.choices[0].message.function_call.name)
print('\n####################################################\n')


# 関数の実行
response_message = response.choices[0].message

available_functions = {
    "get_current_weather": get_current_weather,
}

function_name = response_message.function_call.name
function_to_call = available_functions[function_name]
function_args = json.loads(response_message.function_call.arguments)
print()
pprint(function_args)
print()

function_response = function_to_call(
    location=function_args.get("location"),
    unit=function_args.get("unit"),
)

print(function_response)
print()

# メッセージに追加
response_message_pop = response_message.model_dump()
response_message_pop.pop('tool_calls')
messages.append(response_message_pop)
messages.append(
    {
        "role": "function",
        "name": function_name,
        "content": function_response,
    }
)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# pprint(messages)
for m in messages:
    pprint(m)
    print()
print()

# ChatCompletionAPIの呼び出し２
second_response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

print('\n####################################################\n')
pprint(vars(second_response))
print()
print(second_response.choices[0].message)
print()
pprint(second_response.choices[0].message.content)
pprint(second_response.choices[0].message.function_call)
print('\n####################################################\n')