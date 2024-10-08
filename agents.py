from textwrap import dedent
from crewai import Agent

# from crewai_tools import FileReadTool

# file_read_tool = FileReadTool(file_path='path/to/your/file.txt')

from langchain.chat_models import ChatOpenAI

class GameAgents():
	def senior_engineer_agent(self):
		return Agent(
			role='Senior Software Engineer',
			goal='Create software as needed',
			backstory=dedent("""\
				You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in python. and do your best to
				produce perfect code"""),
			allow_delegation=False,
			verbose=True,
			llm =ChatOpenAI(
  temperature=1,
  model_name="gpt-4o-mini",
)
			# tools = [file_read_tool],
		)

	def qa_engineer_agent(self):
		return Agent(
			role='Software Quality Control Engineer',
			goal='Create Perfect code, by analyzing the code that is given for errors',
			backstory=dedent("""\
				You are a software engineer that specializes in checking code
  				for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  				You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  				You also check for security vulnerabilities, and logic errors"""),
			allow_delegation=False,
			verbose=True,
			llm =ChatOpenAI(
  temperature=1,
  model_name="gpt-4o-mini",
)
		)

	def chief_qa_engineer_agent(self):
		return Agent(
			role='Chief Software Quality Control Engineer',
			goal='Ensure that the code does the job that it is supposed to do',
			backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""),
			allow_delegation=True,
			verbose=True,
			llm =ChatOpenAI(
  temperature=1,
  model_name="gpt-4o-mini",
)
		)
