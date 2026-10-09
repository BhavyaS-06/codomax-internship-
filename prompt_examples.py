def show_prompt_examples():
    zero_shot_prompt = (
        "Classify this review as Positive, Negative, or Neutral: "
        "'The application is useful and easy to use.'"
    )

    few_shot_prompt = """Classify each review as Positive or Negative.
Review: The product is excellent.
Answer: Positive
Review: The service was terrible.
Answer: Negative
Review: The application is useful.
Answer:"""

    role_context_prompt = """Role: You are a beginner-friendly Python tutor.
Context: The learner is preparing for a technical interview.
Task: Explain Python lists in simple English.
Constraints: Use three bullet points and one short code example."""

    print("\n--- ZERO-SHOT PROMPT ---")
    print(zero_shot_prompt)
    print("\n--- FEW-SHOT PROMPT ---")
    print(few_shot_prompt)
    print("\n--- ROLE, CONTEXT, INSTRUCTIONS, AND CONSTRAINTS ---")
    print(role_context_prompt)
    print("\nNote: These are prompt examples; no live AI model is called.")
