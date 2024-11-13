#!/usr/bin/env python
# coding: utf-8

# ## Type Playground
# Use this programming space below to experiment with types of objects. Don't forget to use `print` to see the output of your code. Click `Run` from the top bar to run the code.

# In[ ]:


# This is the type play ground



# **Understanding Loss in Machine Learning**
# 
# **Loss** is a measure of how well or poorly a model's predictions match the actual target values. It quantifies the difference between the predicted values and the actual values. The goal of training a machine learning model is to minimize this loss. Lower loss values indicate better model performance. Monitoring loss over time helps in understanding how well the model is learning and adjusting during the training process.
# 

# ## Quiz: Total Sales
# In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.
# 
# Calculate the total sales for the week from the data provided. Assign the result to a string variable with the form `"This week's total sales: xxx"`, where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total.
# 
# **Note**: While assigning `"This week's total sales: xxx"`, you need to take care of the spaces to get the correct answer. Don't forget to include a space after the colon `": "`.

# In[9]:


mon_loss = "0.15"
tues_loss = "0.12"
wed_loss = "0.13"
thurs_loss = "0.10"
fri_loss = "0.11"
sat_loss = "0.09"
sun_loss = "0.08"

# TODO: assign the total loss to a string with this format: This week's total loss: xxx
# You will probably need to write some lines of code before the assigning statement.

# Convert string loss values to float and calculate the total loss
total_loss = (float(mon_loss) + float(tues_loss) +float(wed_loss) +float(thurs_loss) +float(fri_loss)+ float(sat_loss) +float(sun_loss))

# Format the result string
result_string = "This week's total loss: {:.2f}".format(total_loss)
print(result_string)

### Notebook grading
if result_string == "This week's total loss: 0.78":
    print("You calculated the correct sum and formatted the string correctly. Nice work!")
else:
    print("That doesn't match the solution. The total loss should be 0.78. If that's what you got, check that your string is formatted correctly.")


# In[ ]:




