#!/usr/bin/env python
# coding: utf-8

# ## Quiz 1: String Method Playground
# ### Scenario:
# You are working on an NLP project and need to preprocess some text data. Explore different string methods and see how they can be used to manipulate text data.
# 
# ### Task:
# Browse the complete list of string methods at Python String Methods and try them out in the cell below.
# 
# Link:
# https://docs.python.org/3/library/stdtypes.html#string-methods

# In[7]:


## String method playground

# Example usage of some string methods
sample_text = "Hello, World! This is a sample text for NLP tasks."

# Convert the text to lowercase
lower_text = sample_text.lower()
print(f"Lowercase: {lower_text}")

# Replace 'World' with 'Universe'
replaced_text = sample_text.replace('World','Universe')
print("Replaced text:", replaced_text)

# Split the text into words
words = replaced_text.split()
print("Words:", words)

# Try out more string methods from the Python documentation link provided


# ## Quiz 2: Formatting Text for NLP
# ### Scenario:
# You are preparing text data for an NLP task and need to format a sentence with specific values. This is useful for constructing training data or generating output text.
# 
# ### Task:
# Write two lines of code to assign values to two variables. Then, use the format() function to print out a sentence that includes the values of both variables.

# In[15]:


# Write two lines of code below, each assigning a value to a variable
model_name = "BERT"
accuracy = 92.5

# Now write a print statement using .format() to print out a sentence and the values of both of the variables
# TODO

print("My name is {} I am this old {}".format(model_name,accuracy))


# **About BERT**
# 
# BERT (Bidirectional Encoder Representations from Transformers) is a state-of-the-art NLP model developed by Google. It is designed to understand the context of words in a sentence by looking at both the left and right sides of the word. BERT has significantly improved the performance of NLP tasks such as text classification, named entity recognition, and question answering.
