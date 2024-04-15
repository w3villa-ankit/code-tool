from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def dockerCommandLineCodeExecutor(item):
    from autogen import ConversableAgent
    from autogen.coding import DockerCommandLineCodeExecutor
    from pathlib import Path

    work_dir = Path("coding")
    work_dir.mkdir(exist_ok=True)

    executor = DockerCommandLineCodeExecutor(work_dir=work_dir)

    code_executor_agent = ConversableAgent(
        name="code_executor_agent",
        llm_config=False,
        code_execution_config={
            "executor": executor,
        },
        human_input_mode="NEVER",
    )

    code_writer_system_message = """
    You have been given coding capability to solve tasks using Python code.
    In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
        1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
        2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
    Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
    When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
    If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
    """

    import os

    code_writer_agent = ConversableAgent(
    "code_writer",
    system_message=code_writer_system_message,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": OPENAI_API_KEY}]},
    code_execution_config=False,  # Turn off code execution for this agent.
    max_consecutive_auto_reply=2,
    human_input_mode="NEVER",
)

    chat_result = code_executor_agent.initiate_chat(
        code_writer_agent, message=item.message
    )

    return chat_result    
