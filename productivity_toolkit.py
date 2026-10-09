PROMPT_TEMPLATES = {
    "email": """Act as a professional communication assistant.
Write a short email about [TOPIC].
Recipient: [RECIPIENT]
Purpose: [PURPOSE]
Tone: Professional.
Include a subject line.""",

    "resume": """Act as a resume reviewer for a [TARGET_ROLE] role.
Review the resume text below.
Suggest improvements to clarity, relevant skills, and project descriptions.
Do not invent experience or qualifications.
Resume text: [PASTE_RESUME_TEXT]""",

    "coding": """Act as a programming tutor.
Language: [PROGRAMMING_LANGUAGE]
Task: [TASK]
Use beginner-friendly code, explain the logic, show expected output,
and mention possible edge cases.""",

    "research": """Act as a research assistant.
Topic: [TOPIC]
Provide an introduction, key concepts, applications, limitations, and conclusion.
Separate verified facts from uncertain claims and suggest sources to verify.""",

    "summarization": """Summarize the text below in [NUMBER] bullet points.
Keep the main ideas and important facts.
Do not add information that is not present in the text.
Text: [PASTE_TEXT]""",

    "classification": """Classify the text into one of these categories: [CATEGORIES].
Return the category and a one-sentence explanation.
Text: [PASTE_TEXT]"""
}


def show_productivity_toolkit():
    print("\n" + "=" * 60)
    print("REUSABLE AI PRODUCTIVITY TOOLKIT")
    print("=" * 60)
    for name, prompt in PROMPT_TEMPLATES.items():
        print(f"\n[{name.upper()} PROMPT TEMPLATE]")
        print(prompt)


if __name__ == "__main__":
    show_productivity_toolkit()
