# Scenario 10: Summarization with Constraints
# Task: Write a prompt to summarize a news article into 2 sentences. 
# If the summary exceeds 50 words, truncate it to the nearest complete sentence.


import re


summary = input("Enter sentence :\n")


sentences = re.split(r'(?<=[.!?])\s+', summary.strip())


short_summary = ' '.join(sentences[:2])


word_count = len(short_summary.split())


if word_count > 50:
    final_summary = sentences[0]
else:
    final_summary = short_summary

# Output
print("\n Final Summary:")
print(final_summary)
print(f"\n Word Count: {len(final_summary.split())}")
