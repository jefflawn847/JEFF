
# Internet Research Agent

An AI-powered web research agent built with Hugging Face smolagents and Qwen/Qwen2.5-Coder-32B-Instruct.

## Overview

This agent accepts a research question, searches the web, visits relevant webpages, and uses an AI model to produce a research result.

## Architecture

User → CodeAgent → Web Search → Webpage Reading → AI Reasoning → Answer

## Features

- Web search with DuckDuckGo
- Webpage reading
- Multi-step agent reasoning
- Natural-language research questions
- Hugging Face Inference API

## Tech Stack

- Python
- Hugging Face smolagents
- Qwen/Qwen2.5-Coder-32B-Instruct
- DuckDuckGoSearchTool
- VisitWebpageTool
- Hugging Face Inference Providers

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
