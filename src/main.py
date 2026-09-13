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


def calculate_skill_gap(user_skills, required_skills):
    user_skills = {skill.lower() for skill in user_skills}

    have_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in user_skills:
            have_skills.append(skill)
        else:
            missing_skills.append(skill)

    return have_skills, missing_skills


def get_category_scores(skill_data, user_skills):
    user_skills = {skill.lower() for skill in user_skills}

    category_scores = {}

    for category, skills in skill_data.items():
        learned = 0

        for skill in skills:
            if skill.lower() in user_skills:
                learned += 1

        total = len(skills)
        score = (learned / total) * 100

        category_scores[category] = score

    return category_scores

def load_skill_dependencies():
    file_path = (
        Path(__file__).parent.parent
        / "data"
        / "skill_dependencies.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
def recommend_next_skill(
    skill_data,
    user_skills,
    category_scores
):
    user_skills = {skill.lower() for skill in user_skills}

    weakest_category = min(
        category_scores,
        key=category_scores.get
    )

    for skill in skill_data[weakest_category]:
        if skill.lower() not in user_skills:
            return skill

    return None
def recommend_next_skill(
    skill_data,
    user_skills,
    category_scores
):
    user_skills = {skill.lower() for skill in user_skills}

    weakest_category = min(
        category_scores,
        key=category_scores.get
    )

    category_skills = skill_data[weakest_category]

    for skill in category_skills:
        if skill.lower() not in user_skills:
            return skill

    return None
def main():
    skill_data = load_skills()

    required_skills = get_all_skills(skill_data)

    print("=" * 45)
    print("             SKILLPILOT AI")
    print("          AI Engineer Skill Analyzer")
    print("=" * 45)

    user_input = input(
        "\nEnter your skills separated by commas:\n> "
    )

    user_skills = [
        skill.strip()
        for skill in user_input.split(",")
        if skill.strip()
    ]

    have_skills, missing_skills = calculate_skill_gap(
        user_skills,
        required_skills
    )

    category_scores = get_category_scores(
        skill_data,
        user_skills
    )
    next_skill = recommend_next_skill(
    skill_data,
    user_skills,
    category_scores
    )
    total_skills = len(required_skills)
    learned_skills = len(have_skills)

    readiness = (learned_skills / total_skills) * 100

    print("\n" + "=" * 45)
    print("              RESULTS")
    print("=" * 45)

    print(f"\nAI Engineer Readiness Score: {readiness:.1f}%")

    print("\n📊 SKILL CATEGORY SCORES:")

    for category, score in category_scores.items():
        display_name = category.replace("_", " ").title()
        print(f"  {display_name:<20}: {score:.1f}%")
    if next_skill:
        print(f"\n🎯 RECOMMENDED NEXT SKILL: {next_skill}")
    best_category = max(
        category_scores,
        key=category_scores.get
    )

    weakest_category = min(
        category_scores,
        key=category_scores.get
    )

    print(
        f"\n🏆 STRONGEST CATEGORY: "
        f"{best_category.replace('_', ' ').title()}"
    )

    print(
        f"⚠️ WEAKEST CATEGORY: "
        f"{weakest_category.replace('_', ' ').title()}"
    )

    print("\n✓ SKILLS YOU HAVE:")

    for skill in have_skills:
        print(f"  ✓ {skill}")

    print("\n✗ SKILLS YOU NEED:")

    for skill in missing_skills:
        print(f"  ✗ {skill}")

    if missing_skills:
        print(
            f"\n🎯 NEXT SKILL TO LEARN: "
            f"{missing_skills[0]}"
        )


if __name__ == "__main__":
    main()