#!/usr/bin/env python
# coding: utf-8

# <h1>Activity: Functions</h1>

# ## Introduction 
# 
# In this lab, you will practice defining functions and returning values, writing clean code, and using comments to scaffold code.
# 
# As a data professional, you'll often need to reuse the same block of code more than once when you're writing Python code to automate a certain task. This is why functions are important. You can call functions whenever you need the computer to execute those steps. Python has built-in functions that have already been defined and also provides tools for users to define their own functions.
# 
# In this lab, you'll define and call a function that calculates the revenue a theater makes depending on the number of tickets sold, then test the function with a new value.
# 

# ## Tips for completing this lab
# 
# As you navigate this lab, keep the following tips in mind:
# 
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task.
# - To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.
# 

# ## Task 1: Analyze a function
# 
# In your work as a data analyst for a movie theater, you're asked to quickly calculate how much the theater has made in sales so far.
# 
# In the following cell, analyze the function named `total_sales` and make note of your observations.
# 
# You do not need to run this cell, but if you do it will not produce an output.

# In[ ]:


# Define a function named `total_sales`
def total_sales():

    # Return a value
    return
#doesnt return a value


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# You can refer back to what you've learned about functions.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# When analyzing the function definition, make sure to observe the function body, which is the indented block of code after the function header.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Notice that the code comments on each line clearly explain how the function operates.
# 
# Code comments can also be used to scaffold code as you build it, since Python will not interact with the text captured as a comment.
# 
# </details>

# ## Task 2: Add a parameter and calculations to the function
# 
# As you continue refining your code, imagine that the price of tickets is $7.99. Now you will need to add a parameter to the function definition and the calculation to the function body.
# 
# 

# ### 2a: Add a calculation to the function
# 
# In this task, update the `total_sales` function so it returns the value of the number of tickets `n` multiplied by the price `7.99`.

# In[1]:


def total_sales(n):
    return n*7.99


# ### 2b: Call the function
# 
# With the calculations added to the `total_sales` function, test it with a value of `59`.
# 
# *Example:*
# 
# ```
# [IN]  total_sales(59)
# [OUT] 471.41
# ```

# In[2]:


total_sales(59)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# You can refer back to what you learned about functions and arithmetic operators.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To create a function, use the `def` keyword to define the function, then write the name of the function, followed by parentheses and a colon: `():`. This set of parentheses is where a parameter would be added.
# 
# The body of the function begins on the next line and is indented, conventionally by four spaces. This is where to write the function's operations (such as arithmetic calculations) and a `return` statement.
# 
# To call a function, type the function name followed by parentheses, with a parameter in the parentheses.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# After defining the `total_sales` function, add a parameter `n` to the function.
# 
# In the body of the function, multiply the parameter by the ticket price to get total sales.
# 
# To call the function, replace `n` with the number of tickets in the function's parenthesis, then run the cell.
# 
# </details>

# # Task 3: Create a function that accepts two values
# 
# You learn that the price of tickets is more expensive for opening night, and now you need to create a function that will accept two values and return their total value.

# ### 3a: Refine the `total_sales` function
# 
# *  Update your `total_sales` function so it accepts two parameters:
#     * `price` for the price per ticket
#     * `num_tickets` for the total number of tickets.
# 
# * Return the product of the two arguments. Use the Python `round()` function to round the returned value to two decimal places. Refer to the [round() Python documentation](https://docs.python.org/3/library/functions.html#round) for more information regarding this function.

# In[5]:


def total_sales(n, p):
    return round(n*p, ndigits=2)


# ### 3b: Call the function
# 
# Then, call the function with the value of `15.99` for `price` and `1001` for the number of tickets sold (`num_tickets`).
# 
# Example:
# 
# ```
# [IN]  total_sales(15.99, 1001)
# [OUT] 16005.99
# ```

# In[6]:


total_sales(15.99, 1001)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you learned about functions, arithmetic operators, and the `round()` function.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Defining up a function that accepts two parameters is a very similar process to defining a function with just one.
# 
# Begin by defining the function and naming it, but instead of a single parameter within the parentheses, place two parameters separated by a comma (`,`).
# 
# The body of the function is still on a new line and indented four spaces. The `round()` function is included here, and the calculation of the two parameters takes place within the `round()` function's parentheses.
# 
# When calling the new function, type the name of the function followed by a set of parentheses. Then, place the parameters that the function is operating on within the parentheses, separated by a comma.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Define a function called `total_sales` that calculates the total dollar value of the tickets sold based on the per-ticket price (`price`), and the number of tickets sold (`num_tickets`).
# 
# In the body of the function, multiply the parameters to get the total and round the calculation to two decimal places.
# 
# To call the function, write the name of the function on a new line and replace the parameters with the price per ticket and number of tickets sold.
# 
# </details>

# # Task 4: Test the function with different values
# 
# As prices and sales fluctate, your function will need to accept different values and still return the total sales.
# 
# In this task, practice calling your function with different values.
# 
# Example:
# 
# ```
# [IN]  total_sales(16.99, 1232)
# [OUT] 20931.68
# 
# [IN]  total_sales(10.50, 1472)
# [OUT] 15456.0
# 
# [IN]  total_sales(5.00, 349)
# [OUT] 1745.0
# 
# ```

# In[7]:


total_sales(16.99, 1232)


# In[8]:


total_sales(10.50, 1472)#


# In[9]:


total_sales(5.00, 349)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# You can refer to what you've learned about calling functions with multiple parameters.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Call the function by writing the name, followed by parenthesis. Write the two values you want to calculate inside the parenthesis, separated by a comma.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# To run the function and calculate a new total, call `total_sales()` and write `16.99, 1232` inside the parenthesis.
# 
# </details>

# # Conclusion
# 
# **What are your key takeaways from this lab?**

# [Double-click to enter your response.]

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
