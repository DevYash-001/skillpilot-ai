import json 
from pathlib import Path


def load_skills():
    file_path = Path(__file__).parent.parent / "data" / "skills.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_all_skills(skill_data):
    all_skills = []

    for category in skill_data:
        all_skills.extend(skill_data[category])
    return all_skills

def calculate_skill_gap(user_skills,required_skills):
    user_skills = {skill.lower() for skill in user_skills}

    have_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in user_skills:
            have_skills.append(skill)
        else:
            missing_skills.append(skill)
    return have_skills,missing_skills

def get_category_scores(skill_data,user_skills):
    for category, skills in skill_data.items():
        print(f"{category} {skills}")

def main():
    skill_data = load_skills()

    required_skills = get_all_skills(skill_data)

    print("=" *45)
    print("             SKILLPILOT AI")
    print("          AI Engineer Skill Analyzer")
    print("=" * 45)

    user_input = input(
        "\nEnter your skills seprated by commas:\n>"

    )

    user_skills = [
        skill.strip()
        for skill in user_input.split(",")
        if skill.strip()
    ]
    have_skills,missing_skills = calculate_skill_gap(
        user_skills,
        required_skills
    )

    total_skills = len(required_skills)
    learned_skills = len(have_skills)

    readliness = (learned_skills / total_skills)*100

    print("\n" + "=" * 45)
    print("              RESULTS")
    print("=" * 45)

    print(f"\nAI Engineer Readiness Score: {readliness:.1f}%")

    print("\n✓ SKILLS YOU HAVE:")
    for skill in have_skills:
        print(f"  ✓ {skill}")

    print("\n✗ SKILLS YOU NEED:")
    for skill in missing_skills:
        print(f"  ✗ {skill}")
    if missing_skills:
        print(f"\n NEXT SKILL TO LEARN: {missing_skills[0]}")
if __name__ == "__main__":
    main()