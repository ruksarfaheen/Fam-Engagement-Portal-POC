import matplotlib.pyplot as plt
import csv
import os

SURVEY_FILE = "data/survey_responses.csv"

def plot_survey_report():
    """Read survey responses and plot a bar graph of the report."""

    if not os.path.exists(SURVEY_FILE):
        print("⚠️ No survey responses found.")
        return

    with open(SURVEY_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        responses = list(reader)

    if len(responses) <= 1:
        print("⚠️ No survey responses available for plotting.")
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

    # Data for plotting
    labels = ["Total Surveys", "Positive Feedback", "Negative Feedback", "Neutral Feedback"]
    values = [total_surveys, positive_count, negative_count, neutral_count]

    # Plot the bar graph
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=["blue", "green", "red", "gray"])
    plt.xlabel("Survey Metrics")
    plt.ylabel("Count")
    plt.title("Survey Report Analysis")
    plt.ylim(0, max(values) + 5)  # Adjust y-axis for better visibility

    # Display the count on top of each bar
    for i, v in enumerate(values):
        plt.text(i, v + 0.5, str(v), ha='center', fontsize=12)

    plt.show()


# Call the function to plot the graph
plot_survey_report()
