import csv
import os
from survey import Survey

# File Paths
DATA_FOLDER = "data"
FAN_DATA_FILE = os.path.join(DATA_FOLDER, "fan_data.csv")
SURVEY_FILE = os.path.join(DATA_FOLDER, "survey_responses.csv")
REPORT_FILE = os.path.join(DATA_FOLDER, "fan_engagement_report.txt")
ENGAGEMENT_FILE = os.path.join(DATA_FOLDER, "engagement_data.csv")

# Ensure the data folder exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Ensure files exist with headers
for file, header in [
    (FAN_DATA_FILE, ["Name", "Email"]),
    (ENGAGEMENT_FILE, ["Type", "Participant", "Details"])
]:
    if not os.path.exists(file):
        with open(file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)


class FanManager:
    @staticmethod
    def add_fan(name, email):
        with open(FAN_DATA_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, email])
        print(f"✅ Fan added: {name} ({email})")


class EngagementManager:
    @staticmethod
    def participate(event_type, participant, details):
        with open(ENGAGEMENT_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([event_type, participant, details])
        print(f"🎉 Participation recorded: {event_type} - {participant}")


def generate_report():
    """Generate a fan engagement report based on survey responses."""
    if not os.path.exists(SURVEY_FILE):
        print("⚠️ No survey responses found.")
        return

    with open(SURVEY_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        responses = list(reader)

    if len(responses) <= 1:
        print("⚠️ No survey responses available for reporting.")
        return

    total_surveys = len(responses) - 1
    positive_count = 0
    negative_count = 0
    neutral_count = 0  # Added to track neutral feedback

    # Basic sentiment analysis
    positive_keywords = ["great", "good", "excellent", "amazing", "love", "fantastic", "wonderful"]
    negative_keywords = ["bad", "poor", "terrible", "worst", "awful", "hate", "disappointed"]

    for row in responses[1:]:
        if len(row) < 3:  # Skip incomplete rows
            continue
        feedback = row[2].lower()
        if any(word in feedback for word in positive_keywords):
            positive_count += 1
        elif any(word in feedback for word in negative_keywords):
            negative_count += 1
        else:
            neutral_count += 1  # Categorizing feedback as neutral

    # Generate report content
    report_content = f"""
    📊 Fan Engagement Report
    ----------------------------
    Total Surveys Submitted: {total_surveys}
    Positive Feedback: {positive_count}
    Negative Feedback: {negative_count}
    Neutral Feedback: {neutral_count}
    ----------------------------
    """

    # Save the report file
    with open(REPORT_FILE, mode="w", encoding="utf-8") as file:
        file.write(report_content)

    print("✅ Report generated successfully!")
    print(report_content)


if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Fan")
        print("2. Submit Survey")
        print("3. Participate in Engagement Event")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("👋 Welcome to the Fan Registration! Join our amazing community today.")
            name = input("Enter fan name: ")
            email = input("Enter fan email: ")
            FanManager.add_fan(name, email)
        elif choice == "2":
            print("📢 Thank you for sharing your feedback! Your voice matters.")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            feedback = input("Enter your feedback: ")
            Survey.submit_survey(name, email, feedback)
        elif choice == "3":
            print("🎉 Get ready to participate in exciting engagement activities!")
            print("1. Voting")
            print("2. Quiz")
            print("3. Prize")
            event_type_choice = input("Select engagement type (1-3): ")
            event_type = "Voting" if event_type_choice == "1" else "Quiz" if event_type_choice == "2" else "Prize" if event_type_choice == "3" else "Unknown"
            participant = input("Enter your name: ")
            if event_type == "Voting":
                print("Select a player to vote for:")
                print("1. Player A")
                print("2. Player B")
                print("3. Player C")
                vote_choice = input("Enter your vote (1-3): ")
                details = "Player A" if vote_choice == "1" else "Player B" if vote_choice == "2" else "Player C" if vote_choice == "3" else "Invalid Choice"
            elif event_type == "Quiz":
                print("🎯 Answer the quiz questions!")
                score = 0
                questions = [
                    ("Who has scored the most runs in international cricket?",
                     ["1. Sachin Tendulkar", "2. Virat Kohli", "3. Ricky Ponting", "4. Jacques Kallis"], "1"),
                    ("Which country won the first-ever Cricket World Cup in 1975?",
                     ["1. Australia", "2. West Indies", "3. England", "4. India"], "2"),
                    ("Who holds the record for the fastest century in ODI cricket?",
                     ["1. AB de Villiers", "2. Chris Gayle", "3. Shahid Afridi", "4. Virender Sehwag"], "1"),
                    ("Which bowler has taken the most wickets in Test cricket?",
                     ["1. Muttiah Muralitharan", "2. Shane Warne", "3. James Anderson", "4. Anil Kumble"], "1"),
                    ("Which Indian cricketer is known as 'Captain Cool'?",
                     ["1. MS Dhoni", "2. Sourav Ganguly", "3. Rahul Dravid", "4. Virat Kohli"], "1")
                ]
                for q, options, correct_option in questions:
                    print(q)
                    for option in options:
                        print(option)
                    ans = input("Enter your choice (1-4): ")
                    if ans.strip() == correct_option:
                        score += 1
                details = f"Quiz Score: {score}/5"
            else:
                details = "Participated in prize event"
            EngagementManager.participate(event_type, participant, details)
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a valid option.")
