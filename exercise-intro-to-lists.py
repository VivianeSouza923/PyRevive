{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dfbfefc9",
   "metadata": {
    "papermill": {
     "duration": 0.00556,
     "end_time": "2023-07-01T17:49:23.429299",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.423739",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**This notebook is an exercise in the [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/intro-to-lists).**\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffaf5304",
   "metadata": {
    "papermill": {
     "duration": 0.004901,
     "end_time": "2023-07-01T17:49:23.439323",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.434422",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "In the tutorial, you learned how to define and modify Python lists.  In this exercise, you will use your new knowledge to solve several problems.\n",
    "\n",
    "# Set up the notebook\n",
    "\n",
    "Run the next code cell without changes to set up the notebook."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d5f2763a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.451524Z",
     "iopub.status.busy": "2023-07-01T17:49:23.450801Z",
     "iopub.status.idle": "2023-07-01T17:49:23.493560Z",
     "shell.execute_reply": "2023-07-01T17:49:23.492698Z"
    },
    "papermill": {
     "duration": 0.051324,
     "end_time": "2023-07-01T17:49:23.495644",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.444320",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Setup complete.\n"
     ]
    }
   ],
   "source": [
    "from learntools.core import binder\n",
    "binder.bind(globals())\n",
    "from learntools.intro_to_programming.ex5 import *\n",
    "print('Setup complete.')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdcdb500",
   "metadata": {
    "papermill": {
     "duration": 0.00472,
     "end_time": "2023-07-01T17:49:23.505616",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.500896",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Question 1\n",
    "\n",
    "You own a restaurant with five food dishes, organized in the Python list `menu` below.  One day, you decide to:\n",
    "- remove bean soup (`'bean soup'`) from the menu, and\n",
    "- add roasted beet salad (`'roasted beet salad'`) to the menu.\n",
    "\n",
    "Implement this change to the list below.  While completing this task, \n",
    "- do not change the line that creates the `menu` list.  \n",
    "- your answer should use `.remove()` and `.append()`.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "07d05400",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.518377Z",
     "iopub.status.busy": "2023-07-01T17:49:23.517800Z",
     "iopub.status.idle": "2023-07-01T17:49:23.528470Z",
     "shell.execute_reply": "2023-07-01T17:49:23.527864Z"
    },
    "papermill": {
     "duration": 0.019526,
     "end_time": "2023-07-01T17:49:23.530013",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.510487",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['stewed meat with onions', 'risotto with trout and shrimp', 'fish soup with cream and onion', 'gyro', 'roasted beet salad']\n"
     ]
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"1_FoodMenu\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Do not change: Initial menu for your restaurant\n",
    "menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',\n",
    "       'fish soup with cream and onion', 'gyro']\n",
    "\n",
    "# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu\n",
    "menu.remove('bean soup')\n",
    "menu.append('roasted beet salad')\n",
    "\n",
    "print(menu)\n",
    "\n",
    "# Do not change: Check your answer\n",
    "q1.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "50a66141",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.541913Z",
     "iopub.status.busy": "2023-07-01T17:49:23.541568Z",
     "iopub.status.idle": "2023-07-01T17:49:23.551695Z",
     "shell.execute_reply": "2023-07-01T17:49:23.550872Z"
    },
    "papermill": {
     "duration": 0.018465,
     "end_time": "2023-07-01T17:49:23.553801",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.535336",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 2, \"questionId\": \"1_FoodMenu\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> Here is the original line of code that created the menu: `menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp', 'fish soup with cream and onion', 'gyro']`.  Use `.append()` to add an item, and use `.remove()` to remove an item."
      ],
      "text/plain": [
       "Hint: Here is the original line of code that created the menu: `menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp', 'fish soup with cream and onion', 'gyro']`.  Use `.append()` to add an item, and use `.remove()` to remove an item."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 2, \"questionId\": \"1_FoodMenu\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "# Do not change: Initial menu for your restaurant\n",
       "menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',\n",
       "       'fish soup with cream and onion', 'gyro']\n",
       "\n",
       "# Remove 'bean soup', and add 'roasted beet salad' to the end of the menu\n",
       "menu.remove('bean soup')\n",
       "menu.append('roasted beet salad')\n",
       "\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "# Do not change: Initial menu for your restaurant\n",
       "menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',\n",
       "       'fish soup with cream and onion', 'gyro']\n",
       "\n",
       "# Remove 'bean soup', and add 'roasted beet salad' to the end of the menu\n",
       "menu.remove('bean soup')\n",
       "menu.append('roasted beet salad')\n",
       "\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Uncomment to see a hint\n",
    "q1.hint()\n",
    "\n",
    "# Uncomment to see the solution\n",
    "q1.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bc7c721",
   "metadata": {
    "papermill": {
     "duration": 0.005483,
     "end_time": "2023-07-01T17:49:23.565621",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.560138",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Question 2\n",
    "\n",
    "The list `num_customers` contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days).  Fill in values for each of the following:\n",
    "- `avg_first_seven` - average number of customers who visited in the first seven days\n",
    "- `avg_last_seven` - average number of customers who visited in the last seven days\n",
    "- `max_month` - number of customers on the day that got the most customers in the last month\n",
    "- `min_month` - number of customers on the day that got the least customers in the last month\n",
    "\n",
    "Answer this question by writing code.  For instance, if you have to find the minimum value in a list, use `min()` instead of scanning for the smallest value and directly filling in a number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6740e32b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.578258Z",
     "iopub.status.busy": "2023-07-01T17:49:23.577793Z",
     "iopub.status.idle": "2023-07-01T17:49:23.585288Z",
     "shell.execute_reply": "2023-07-01T17:49:23.584751Z"
    },
    "papermill": {
     "duration": 0.015495,
     "end_time": "2023-07-01T17:49:23.586720",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.571225",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"2_NumCustomers\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Do not change: Number of customers each day for the last month\n",
    "num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,\n",
    "                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,\n",
    "                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]\n",
    "\n",
    "# TODO: Fill in values for the variables below\n",
    "avg_first_seven = (num_customers[0]+num_customers[1]+num_customers[2]+num_customers[3]+num_customers[4]+num_customers[5]+num_customers[6])/7 \n",
    "avg_last_seven = (num_customers[23]+num_customers[24]+num_customers[25]+num_customers[26]+num_customers[27]+num_customers[28]+num_customers[29])/7 \n",
    "max_month = max(num_customers)\n",
    "min_month = min(num_customers)\n",
    "\n",
    "# Do not change: Check your answer\n",
    "q2.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f3fc6987",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.600269Z",
     "iopub.status.busy": "2023-07-01T17:49:23.599787Z",
     "iopub.status.idle": "2023-07-01T17:49:23.610859Z",
     "shell.execute_reply": "2023-07-01T17:49:23.610240Z"
    },
    "papermill": {
     "duration": 0.019519,
     "end_time": "2023-07-01T17:49:23.612484",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.592965",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 1, \"questionId\": \"2_NumCustomers\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> To take the average of a list of numbers, you can calculate the sum and then divide by the length. And, to pull the last `y` entries of a list `my_list`, use `my_list[-y:]`."
      ],
      "text/plain": [
       "Hint: To take the average of a list of numbers, you can calculate the sum and then divide by the length. And, to pull the last `y` entries of a list `my_list`, use `my_list[-y:]`."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 1, \"questionId\": \"2_NumCustomers\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "# Fill in values for the variables below\n",
       "avg_first_seven = sum(num_customers[:7])/7 \n",
       "avg_last_seven = sum(num_customers[-7:])/7\n",
       "max_month = max(num_customers)\n",
       "min_month = min(num_customers)\n",
       "\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "# Fill in values for the variables below\n",
       "avg_first_seven = sum(num_customers[:7])/7 \n",
       "avg_last_seven = sum(num_customers[-7:])/7\n",
       "max_month = max(num_customers)\n",
       "min_month = min(num_customers)\n",
       "\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Uncomment to see a hint\n",
    "q2.hint()\n",
    "\n",
    "# Uncomment to see the solution\n",
    "q2.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "983e103d",
   "metadata": {
    "papermill": {
     "duration": 0.006053,
     "end_time": "2023-07-01T17:49:23.625368",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.619315",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Question 3\n",
    "\n",
    "In the tutorial, we gave an example of a Python string with information that was better as a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2c5014f2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.639526Z",
     "iopub.status.busy": "2023-07-01T17:49:23.639082Z",
     "iopub.status.idle": "2023-07-01T17:49:23.642552Z",
     "shell.execute_reply": "2023-07-01T17:49:23.641984Z"
    },
    "papermill": {
     "duration": 0.012459,
     "end_time": "2023-07-01T17:49:23.644061",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.631602",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "flowers = \"pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "619f5787",
   "metadata": {
    "papermill": {
     "duration": 0.00602,
     "end_time": "2023-07-01T17:49:23.656340",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.650320",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "You can actually use Python to quickly turn this string into a list with `.split()`.  In the parentheses, we need to provide the character should be used to mark the end of one list item and the beginning of another, and enclose it in quotation marks.  In this case, that character is a comma."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "355c521c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.670038Z",
     "iopub.status.busy": "2023-07-01T17:49:23.669631Z",
     "iopub.status.idle": "2023-07-01T17:49:23.673637Z",
     "shell.execute_reply": "2023-07-01T17:49:23.672624Z"
    },
    "papermill": {
     "duration": 0.01257,
     "end_time": "2023-07-01T17:49:23.675124",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.662554",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle']\n"
     ]
    }
   ],
   "source": [
    " print(flowers.split(\",\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5f06c82",
   "metadata": {
    "papermill": {
     "duration": 0.006216,
     "end_time": "2023-07-01T17:49:23.687668",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.681452",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Now it is your turn to try this out!  Create two Python lists:\n",
    "- `letters` should be a Python list where each entry is an uppercase letter of the English alphabet.  For instance, the first two entries should be `\"A\"` and `\"B\"`, and the final two entries should be `\"Y\"` and `\"Z\"`.  Use the string `alphabet` to create this list.\n",
    "- `address` should be a Python list where each row in `address` is a different item in the list.  Currently, each row in `address` is separated by a comma. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8af49419",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.702982Z",
     "iopub.status.busy": "2023-07-01T17:49:23.702332Z",
     "iopub.status.idle": "2023-07-01T17:49:23.708576Z",
     "shell.execute_reply": "2023-07-01T17:49:23.707985Z"
    },
    "papermill": {
     "duration": 0.016536,
     "end_time": "2023-07-01T17:49:23.710601",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.694065",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"3_SplitString\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# DO not change: Define two Python strings\n",
    "alphabet = \"A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z\"\n",
    "address = \"Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey\"\n",
    "\n",
    "# TODO: Convert strings into Python lists\n",
    "letters = alphabet.split(\".\")\n",
    "formatted_address = address.split(\",\")\n",
    "\n",
    "# Do not change: Check your answer\n",
    "q3.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5bcce8c5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.726613Z",
     "iopub.status.busy": "2023-07-01T17:49:23.726075Z",
     "iopub.status.idle": "2023-07-01T17:49:23.735745Z",
     "shell.execute_reply": "2023-07-01T17:49:23.735068Z"
    },
    "papermill": {
     "duration": 0.019157,
     "end_time": "2023-07-01T17:49:23.737327",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.718170",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 1, \"questionId\": \"3_SplitString\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> In each case, you need to use `.split()`."
      ],
      "text/plain": [
       "Hint: In each case, you need to use `.split()`."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 1, \"questionId\": \"3_SplitString\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "letters = alphabet.split(\".\")\n",
       "formatted_address = address.split(\",\")\n",
       "\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "letters = alphabet.split(\".\")\n",
       "formatted_address = address.split(\",\")\n",
       "\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Uncomment to see a hint\n",
    "q3.hint()\n",
    "\n",
    "# Uncomment to see the solution\n",
    "q3.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bed914c",
   "metadata": {
    "papermill": {
     "duration": 0.007,
     "end_time": "2023-07-01T17:49:23.751496",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.744496",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Question 4\n",
    "\n",
    "In the Python course, you'll learn all about **list comprehensions**, which allow you to create a list based on the values in another list.  In this question, you'll get a brief preview of how they work.\n",
    "\n",
    "Say we're working with the list below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "efd33f1a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.767054Z",
     "iopub.status.busy": "2023-07-01T17:49:23.766519Z",
     "iopub.status.idle": "2023-07-01T17:49:23.770214Z",
     "shell.execute_reply": "2023-07-01T17:49:23.769649Z"
    },
    "papermill": {
     "duration": 0.013398,
     "end_time": "2023-07-01T17:49:23.771768",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.758370",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "test_ratings = [1, 2, 3, 4, 5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc279214",
   "metadata": {
    "papermill": {
     "duration": 0.006639,
     "end_time": "2023-07-01T17:49:23.785508",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.778869",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Then we can use this list (`test_ratings`) to create a new list (`test_liked`) where each item has been turned into a boolean, depending on whether or not the item is greater than or equal to four."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1d3a255b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.801150Z",
     "iopub.status.busy": "2023-07-01T17:49:23.800638Z",
     "iopub.status.idle": "2023-07-01T17:49:23.805315Z",
     "shell.execute_reply": "2023-07-01T17:49:23.804649Z"
    },
    "papermill": {
     "duration": 0.014427,
     "end_time": "2023-07-01T17:49:23.806872",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.792445",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False, False, False, True, True]\n"
     ]
    }
   ],
   "source": [
    "test_liked = [i>=4 for i in test_ratings]\n",
    "print(test_liked)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc133fea",
   "metadata": {
    "papermill": {
     "duration": 0.006856,
     "end_time": "2023-07-01T17:49:23.820745",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.813889",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "In this question, you'll use this list comprehension to define a function `percentage_liked()` that takes one argument as input:\n",
    "- `ratings`: list of ratings that people gave to a movie, where each rating is a number between 1-5, inclusive\n",
    "\n",
    "We say someone liked the movie, if they gave a rating of either 4 or 5.  Your function should return the percentage of people who liked the movie.\n",
    "\n",
    "For instance, if we supply a value of `[1, 2, 3, 4, 5, 4, 5, 1]`, then 50% (4/8) of the people liked the movie, and the function should return `0.5`.\n",
    "\n",
    "Part of the function has already been completed for you.  You need only use `list_liked` to calculate `percentage_liked`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1484c8f3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.836610Z",
     "iopub.status.busy": "2023-07-01T17:49:23.836055Z",
     "iopub.status.idle": "2023-07-01T17:49:23.843910Z",
     "shell.execute_reply": "2023-07-01T17:49:23.843287Z"
    },
    "papermill": {
     "duration": 0.017686,
     "end_time": "2023-07-01T17:49:23.845533",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.827847",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"4_PercentageLiked\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def percentage_liked(ratings):\n",
    "    list_liked = [rating for rating in ratings if rating >= 4]\n",
    "    percentage = len(list_liked) / len(ratings)\n",
    "    return percentage\n",
    "\n",
    "# Do not change: should return 0.5\n",
    "percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])\n",
    "\n",
    "# Do not change: Check your answer\n",
    "q4.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0c557a95",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.862023Z",
     "iopub.status.busy": "2023-07-01T17:49:23.861637Z",
     "iopub.status.idle": "2023-07-01T17:49:23.872138Z",
     "shell.execute_reply": "2023-07-01T17:49:23.871226Z"
    },
    "papermill": {
     "duration": 0.020656,
     "end_time": "2023-07-01T17:49:23.873805",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.853149",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 2, \"questionId\": \"4_PercentageLiked\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> Remember that when we add booleans, it returns the total number of entries in the sum that are `True`."
      ],
      "text/plain": [
       "Hint: Remember that when we add booleans, it returns the total number of entries in the sum that are `True`."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 2, \"questionId\": \"4_PercentageLiked\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "\n",
       "# Complete the function\n",
       "def percentage_liked(ratings):\n",
       "    list_liked = [i >= 4 for i in ratings]\n",
       "    percentage_liked = sum(list_liked)/len(list_liked)\n",
       "    return percentage_liked\n",
       "\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "\n",
       "# Complete the function\n",
       "def percentage_liked(ratings):\n",
       "    list_liked = [i >= 4 for i in ratings]\n",
       "    percentage_liked = sum(list_liked)/len(list_liked)\n",
       "    return percentage_liked\n",
       "\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Uncomment to see a hint\n",
    "q4.hint()\n",
    "\n",
    "# Uncomment to see the solution\n",
    "q4.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a96cce8",
   "metadata": {
    "papermill": {
     "duration": 0.007602,
     "end_time": "2023-07-01T17:49:23.889621",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.882019",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 🌶️ Question 5\n",
    " \n",
    "Say you're doing analytics for a website.  You need to write a function that returns the percentage growth in the total number of users relative to a specified number of years ago.\n",
    "\n",
    "Your function `percentage_growth()` should take two arguments as input:\n",
    "- `num_users` = Python list with the total number of users each year.  So `num_users[0]` is the total number of users in the first year, `num_users[1]` is the total number of users in the second year, and so on.  The final entry in the list gives the total number of users in the most recently completed year.\n",
    "- `yrs_ago` = number of years to go back in time when calculating the growth percentage\n",
    "\n",
    "For instance, say `num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]`.\n",
    "- if `yrs_ago = 1`, we want the function to return a value of about `0.036`. This corresponds to a percentage growth of approximately 3.6%, calculated as (2001078 - 1930992)/1930992.\n",
    "- if `years_ago = 7`, we would want to return approximately `0.66`.  This corresponds to a percentage growth of approximately 66%, calculated as (2001078 - 1204334)/1204334.\n",
    "\n",
    "Your coworker sent you a draft of a function, but it doesn't seem to be doing the correct calculation.  Can you figure out what has gone wrong and make the needed changes?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1bfc7451",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.906689Z",
     "iopub.status.busy": "2023-07-01T17:49:23.906346Z",
     "iopub.status.idle": "2023-07-01T17:49:23.916882Z",
     "shell.execute_reply": "2023-07-01T17:49:23.915986Z"
    },
    "papermill": {
     "duration": 0.021361,
     "end_time": "2023-07-01T17:49:23.918752",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.897391",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.03629533421163837\n",
      "0.6615639847417742\n"
     ]
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"5_WebsiteAnalytics\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# TODO: Edit the function\n",
    "def percentage_growth(num_users, yrs_ago):\n",
    "    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]\n",
    "    return growth\n",
    "\n",
    "# Do not change: Variable for calculating some test examples\n",
    "num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]\n",
    "\n",
    "# Do not change: Should return .036\n",
    "print(percentage_growth(num_users_test, 1))\n",
    "\n",
    "# Do not change: Should return 0.66\n",
    "print(percentage_growth(num_users_test, 7))\n",
    "\n",
    "# Do not change: Check your answer\n",
    "q5.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "fc86d78b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-01T17:49:23.936445Z",
     "iopub.status.busy": "2023-07-01T17:49:23.936062Z",
     "iopub.status.idle": "2023-07-01T17:49:23.947496Z",
     "shell.execute_reply": "2023-07-01T17:49:23.946627Z"
    },
    "papermill": {
     "duration": 0.02219,
     "end_time": "2023-07-01T17:49:23.949032",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.926842",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 2, \"questionId\": \"5_WebsiteAnalytics\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> It's already correct that you need to subtract two numbers from the list, before dividing by an item in the list. You only need to modify the positions for the items that are pulled from the list. \n",
       "\n",
       "In order to pull the final entry in the `num_users` list, you would need to use `num_users[len(num_users)-1]`.  This corresponds to the number of users in the most recently completed year.  \n",
       "\n",
       "Then, to get the number of users from one year prior, you should use `num_users[len(num_users)-2]`.  \n",
       "\n",
       "To get the number of users from `yrs_ago` years ago, use `num_users[len(num_users)-yrs_ago-1]`."
      ],
      "text/plain": [
       "Hint: It's already correct that you need to subtract two numbers from the list, before dividing by an item in the list. You only need to modify the positions for the items that are pulled from the list. \n",
       "\n",
       "In order to pull the final entry in the `num_users` list, you would need to use `num_users[len(num_users)-1]`.  This corresponds to the number of users in the most recently completed year.  \n",
       "\n",
       "Then, to get the number of users from one year prior, you should use `num_users[len(num_users)-2]`.  \n",
       "\n",
       "To get the number of users from `yrs_ago` years ago, use `num_users[len(num_users)-yrs_ago-1]`."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 2, \"questionId\": \"5_WebsiteAnalytics\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "def percentage_growth(num_users, yrs_ago):\n",
       "    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]\n",
       "    return growth\n",
       "\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "def percentage_growth(num_users, yrs_ago):\n",
       "    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]\n",
       "    return growth\n",
       "\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Uncomment to see a hint\n",
    "q5.hint()\n",
    "\n",
    "# Uncomment to see the solution\n",
    "q5.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "621c52e4",
   "metadata": {
    "papermill": {
     "duration": 0.008172,
     "end_time": "2023-07-01T17:49:23.965759",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.957587",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Congratulations!\n",
    "\n",
    "Congratulations for finishing the Intro to Programming course!  You should be proud of your very first steps with learning programming.  As next steps, we recommend taking:\n",
    "- the **[Python course](http://www.kaggle.com/learn/python)**, and \n",
    "- the **[Intro to Machine Learning course](https://www.kaggle.com/learn/intro-to-machine-learning)**."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2fdf5e5f",
   "metadata": {
    "papermill": {
     "duration": 0.008233,
     "end_time": "2023-07-01T17:49:23.982245",
     "exception": false,
     "start_time": "2023-07-01T17:49:23.974012",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "---\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "*Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 9.608608,
   "end_time": "2023-07-01T17:49:24.609619",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2023-07-01T17:49:15.001011",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
