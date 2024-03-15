import chainlit as cl

@cl.step
def parse_support_documents(file):
    return "PDF is parsed"


@cl.step
def parse_questionnaire(file):
    return "questionnaire is parsed"


@cl.step
def fill_survey_from_support_documents_and_questionnaire(support_documents, questionnaire):
    # Fetch questionnaire related information from support documents and pass it to openai along with
    #  parsed questionnaire and ask it to fill the answer in the required format
    #  .
    return "Survey is filled"


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """
    support_documents = None
    questionnaire = None

    # Wait for the user to upload a file
    while support_documents is None:
        support_documents = await cl.AskFileMessage(
            content="Please upload the report file", accept={"application/pdf": [".pdf"]}
        ).send()
    if support_documents:
        await cl.Message(content="support_documents received").send()

    while questionnaire is None:
        questionnaire = await cl.AskFileMessage(
            content="Please upload the questionnaire", accept={"application/pdf": [".pdf"]}
        ).send()
    if questionnaire:
        await cl.Message(content="questionnaire received").send()

    parse_support_documents(support_documents)
    parse_questionnaire(questionnaire)
    survey = fill_survey_from_support_documents_and_questionnaire(support_documents, questionnaire)

    await cl.Message(content="Survey is ready").send()
    await cl.sleep(2)
    # Send the final answer.
    await cl.Message(content="This is the final answer").send()
