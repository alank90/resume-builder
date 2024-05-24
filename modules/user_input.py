from Classes import resume__builder


def get():
    # Gather user input for creating the resume
    name = input("Enter your name: ")
    email = input("Ënter your email: ")
    mobile = input("Enter your mobile number: ")

    print("\nEducation:")
    education = []
    while True:
        # Prompt user to add education details
        edu_input = input(
            "Do you want to add education details? (yes/no)").lower()
        if edu_input != 'yes':
            break

        level = input(
            "Enter education level (e.g., Graduation(UG/PG), High School): ")
        institution = input(f"Enter the name of the {level} institution: ")
        field = input(f"Enter the field of study at {institution}: ")
        duration = input(f"Enter passing year of {
            level} at {institution}: ")
        score = input(
            f"Enter your score (e.g., GPA/Percentage) of {level} at {institution}: ")
        education.append({"level": level, "institution": institution,
                          "field": field, "duration": duration, "score": score, })

    skills = input("\nEnter your skills (comma-seperated): ")

    print("\nExperience:")
    experience = []
    while True:
        # Prompt user to add work experience details
        job_role = input(
            "Enter your job role (or type 'done' to finish): ")
        if job_role.lower() == 'done':
            break
        exp_company_name = input("Enter the company name: ")
        exp_description = input(
            f"Enter the description for '{job_role}': ")
        experience.append(
            {"job_role": job_role, "company_name": exp_company_name,
                "description": exp_description})

    print("\nProjects:")
    projects = []
    while True:
        # Prompt user to add project details
        proj_heading = input(
            "Enter the project Title (or type 'done' to finish): ")
        if proj_heading.lower() == 'done':
            break
        proj_description = input(
            f"Enter the description for '{proj_heading}': ")
        projects.append(
            {"name": proj_heading, "description": proj_description})

    print("\nAchievements:")
    achievements = []
    while True:
        # Prompt user to add achievement details
        ach_input = input(
            "Enter an achievement detail (or type 'done' to finish): ")
        if ach_input.lower() == 'done':
            break
        achievements.append(ach_input)

    print("\nOther Activities like hobbies:")
    # Prompt user to add other activities or hobbies
    activities = input("Enter your other activities: ")

    return resume__builder.Resume(name, email, mobile, education, skills, experience, projects, achievements, activities)
