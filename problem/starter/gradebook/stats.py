"""gradebook.stats — aggregate statistics over grade records."""


#def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


#def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


#def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


#def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass

def average_per_student(records: list[dict]) -> dict[str, float]:
    student_scores = {}
    for record in records:
        student_name = record["name"]
        score = record["score"]
        if student_name not in student_scores:
            student_scores[student_name] = []
        student_scores[student_name].append(score)
    average_scores = {}
    for student_name, scores in student_scores.items():
        average = sum(scores) / len(scores)
        average_scores[student_name] = round(average, 2)
    return average_scores
def subjects_offered(records: list[dict]) -> set[str]:
    unique_subjects = set()
    for record in records:
        if "subject" in record:
            unique_subjects.add(record["subject"])
    return unique_subjects
def top_scorer(records: list[dict]) -> tuple[str, float]:
    average_scores = average_per_student(records)
    if not average_scores:
        return "", 0.0
    top_name = ""
    top_score = -1.0
    for name, score in average_scores.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name, top_score
def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    average_scores = average_per_student(records)
    passing = []
    for name, avg in average_scores.items():
        if avg >= threshold:
            passing.append(name)
    passing.sort()
    return passing
    