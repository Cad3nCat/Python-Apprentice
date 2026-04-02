"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story
"""
import random
words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']
story = []
#story = [words[1], words[3], words[8], words[10], words[8] words[2], words[15], words[8], words[14] words[16]]
print(len(words))
# Create a story using the words in the list
for i in range(100):
    story.append(random.choice(words) )
# Display the story to the user
print(' '.join(story))