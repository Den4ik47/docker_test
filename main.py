from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import GameTasks
from agents import GameAgents

tasks = GameTasks()
agents = GameAgents()

import os
from fastapi.concurrency import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from models.input import Input

app = FastAPI()


@app.post("/")
async def post_question(input: Input):
  game = input.text

	# Create Agents
  senior_engineer_agent = agents.senior_engineer_agent()
  qa_engineer_agent = agents.qa_engineer_agent()
  chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

	# Create Tasks
  code_game = tasks.code_task(senior_engineer_agent, game)
  review_game = tasks.review_task(qa_engineer_agent, game)
  approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

	# Create Crew responsible for Copy
  crew = Crew(
		agents=[
			senior_engineer_agent,
			qa_engineer_agent,
			chief_qa_engineer_agent
		],
		tasks=[
			code_game,
			review_game,
			approve_game
		],
		verbose=True
	)

  game = crew.kickoff()
    
  return game

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

