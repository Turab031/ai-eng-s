from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

message_eg = [
    {
        "role": "system",
        "content": """  
you are time and space complexity analysis assistant.
your job:
-analyze the space and time complexity of code or algorithms.
-explain the reasoning in simple terms.
-use BiG-O notations clearly.
-if there are loops, extra data structures, hashing, explain their impact.

Guardrails:
-do not write full solution unless asked.
-do not optimize unless asked.
-keep answer beginner friendly and concise.

output format:
1. time complexity.
2. space complexity.
3. explanation
"""
    },
    {
        "role": "user",
        "content": """
what is the time and space complexity of this code?

def find_sum(arr):
    total = 0
    for num in arr:
        total += num

    return total
"""
    },
    {
        "role": "assistant",
        "content": """
1. Time complexity = O(n)
2. Space complexity = O(1)
3. The loop iterates once for each element in the array, so it runs n times. The work inside the loop is constant, so total time is O(n). The variable `total` is reused, and no extra data structure grows with input size, so extra space is O(1).
"""
    },
    {
        #this dictionary contains a actual question from user
        
        "role":"user",
        "content":"""
        
        
        int search(vector<int>& nums, int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
       
    
        
        
        
        """
        
    }
]

response = client.chat.completions.create(
    messages=message_eg,
    model="openai/gpt-oss-20b"
)

print(response.choices[0].message.content)