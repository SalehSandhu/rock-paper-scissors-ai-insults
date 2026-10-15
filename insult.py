from openai import OpenAI
#Creating client
client = OpenAI(
    #Reading in the API key
    api_key= open("API_KEY.txt", "r").read()
)
#Creating a def
def insult():
    #Creating the varaible chat_completion
    chat_completion = client.chat.completions.create(
        #Asking chat GBT to send me an insult for losing in rock paper scissors
    messages=[
        {
            "role": "user",
            "content": "insult me for being bad at rock paper scissors\n",
        }
    ],
    #The model which will get the prompt
    model="gpt-3.5-turbo",
    )
    #Returning the insult 
    return(chat_completion.choices[0].message.content)