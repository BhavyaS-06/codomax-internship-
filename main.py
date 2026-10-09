from prompt_examples import show_prompt_examples
from structured_output import create_sample_json
from productivity_toolkit import show_productivity_toolkit


def main():
    print("=" * 60)
    print("CODOMAX MODULE 2: PROMPT ENGINEERING & AI PRODUCTIVITY")
    print("=" * 60)

    show_prompt_examples()

    print("\n" + "=" * 60)
    print("STRUCTURED JSON OUTPUT EXAMPLE")
    print("=" * 60)
    print(create_sample_json())

    show_productivity_toolkit()


if __name__ == "__main__":
    main()
