from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

def askChef(recipe_message):
    # SECRET_KEY = config('OPENAI_API_KEY')
    # chat = ChatOpenAI(openai_api_key=SECRET_KEY)
    SECRET_KEY = config("GOOGLE_API_KEY")
    chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=SECRET_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template("Your name is Gusto. You are a master chef in India so First Introduce yourself as Gusto The Master Chef. You are Indian Master Chef so tell answers in Simple English Language. You can write any type of food recipe which can be cooked in 5 minutes or whatever time it takes. You are only allowed to answer food related queries. If you don't know the answer then tell I don't know the answer.")
    humanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_recipe}')
    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])
    formattedChatPrompt = chatPrompt.format_messages(asked_recipe=recipe_message)
    # print("Formatted Chat Prompt: ", formattedChatPrompt)
    response = chat.invoke(formattedChatPrompt)
    return response.content